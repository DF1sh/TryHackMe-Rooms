# mKingdom

### It's-a-me!

Initial nmap scan shows port 85 open:

    nmap -sC -sV -p85 10.10.137.9                 
    Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-04 12:58 EDT
    Nmap scan report for 10.10.137.9
    Host is up (0.054s latency).
    
    PORT   STATE SERVICE VERSION
    85/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
    |_http-title: 0H N0! PWN3D 4G4IN
    |_http-server-header: Apache/2.4.7 (Ubuntu)
Gobuster directory enumeration shows /app directory, which eventually leads me to `http://10.10.137.9:85/app/castle/`<br />
![image](https://github.com/user-attachments/assets/5b5eae1c-9472-4d91-8070-0edacb0a1249)<br />
As you can see from the image above, Wappalyzer shows that this server is running `Concrete CMS 8.5.2`. After some online search and website enumeration, I found the following page `http://10.10.137.9:85/app/castle/index.php/login`:<br />
![image](https://github.com/user-attachments/assets/994cb771-e08d-42af-9f77-93b6ce5159ef)<br />
I saw online that the default username for the admin is `admin.` So I tried with `admin:password`, and it worked, lol. Now I can exploit a vulnerability that i found [here](https://hackerone.com/reports/768322). Follow the steps provided in this guide:<br />
Add .php in the allowed file types: <br />
![image](https://github.com/user-attachments/assets/76e8c642-45ab-4bfe-96d1-62cfbf2efb84)<br />
Now generate a php revershe shell. Personally I used the one from PentestMonkey, provided in the `rev.php` file of this repo.<br />
Now upload it:<br />
![image](https://github.com/user-attachments/assets/6cdf3097-1912-47c2-b9fc-abd5deb962e4)<br />
Now open a netcat listener and click on the created link: <br />
![image](https://github.com/user-attachments/assets/7b301926-ee80-436e-87b7-0b8199e01bc6)<br />
Nice(flags are at the end of this writeup): <br />
![image](https://github.com/user-attachments/assets/6a12bc38-e10b-4c66-8dd5-59d161122344)<br />
Now [stabilize the shell](https://maxat-akbanov.com/how-to-stabilize-a-simple-reverse-shell-to-a-fully-interactive-terminal) so that you can keep you mental sanity. 
Next, I run linpeas.sh on the target system to check any privesc paths. First thing I noticed is that /bin/cat has the SUID bit set, but I wasn't able to exploit it. Next, I found credentials for a mysql DB running on the target machine: <br />
![image](https://github.com/user-attachments/assets/c8c7a145-edeb-4acd-afe7-3cf3baec3c5a)<br />
To log inside the DB, the command is `mysql -u toad -p -h localhost`, and then input the discovered password. However, before logging in the DB, I wanted to try if that password also worked for toad's accout, so I run `su toad`, provided the password, and it worked. However I wasn't able to find anything from toad's account besides one thing: the .mysql_history file showed me a hint: <br />
![image](https://github.com/user-attachments/assets/03679186-b90b-47d0-a07c-3bcf08de7a60)<br />
There must be a `user` table with some data in it. Inside the mKingdom database I was able to find a `Users` table, only to find that the password of the admin account is `password`, which I already knew. What I'm looking for is a way to access root. Instead I found a `user` table inside the `mysql` database. <br />
![image](https://github.com/user-attachments/assets/3370c5f4-0cb0-4f07-ad3d-8e3f132d96b7)<br />
I already know toad's password.  Let's try to break debian-sys-maint password. Nope, nothing. I can't do it. Whatching again linpeas output I found a weird environment variable: <br />
![image](https://github.com/user-attachments/assets/42f38c36-b3fc-455b-9616-b7e7b43e0c38)<br />
This base64 encoded value is `ikaTeNTANtES`, and it turns out to be the password for Mario. Thus I finally got the first flag(with nano, cat doens't work). <br />
Running `sudo -l` on mario, this is what we find: <br />
![image](https://github.com/user-attachments/assets/e10985e1-2b31-4e6b-a960-c80797e58921)<br />


To be continued

- What is user.txt? `thm{030a769febb1b3291da1375234b84283}`
- What is root.txt? 

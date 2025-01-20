# Gallery

### Gallery
Nmap scan shows ports 80 and 8080 open. Port 80 is a default apache webpage, while port 8080 directs me to a login page. After some enumeration I tried to see if this form is vulnerable to SQLinjection with `sqlmap`, and it seems it is.<br />
First, I capture a login request with burpsuite and put copy it into a file named `request`, then I run `sqlmap -r request -p username --risk 3 --level 5 --batch --dbms=mysql --dbs`:<br />
![image](https://github.com/user-attachments/assets/8595f446-9cbc-444f-a056-e25a093ef10e)<br />
Now I run `sqlmap -r request -p username --risk 3 --level 5 --batch --dbms=mysql -D gallery_db --tables`:<br />
![image](https://github.com/user-attachments/assets/9179acd1-9299-45a4-bf96-87745f94d25b)<br />
To dump the users table, I run `sqlmap -r request -p username --risk 3 --level 5 --batch --dbms=mysql -D gallery_db -T users --dump`:<br />
![image](https://github.com/user-attachments/assets/3f7db589-5919-4d08-89d1-1932c3182362)<br />
This gets me the admin's hash. To log in as admin, I can just type `admin'--`. Next, I found a working exploit for this CMS [here](https://www.exploit-db.com/exploits/50214). <br />
Now for privesc, I used linpeas and found mike's password: <br />
![image](https://github.com/user-attachments/assets/fc5992b0-edc8-4bfe-ad5d-53661077c642)<br />
As mike, if I run `sudo -l` I get: <br />
![image](https://github.com/user-attachments/assets/329169e9-7502-48e5-91f2-05c8e04d2325)<br />
This is the code: <br />
![image](https://github.com/user-attachments/assets/cf124075-05d4-4822-8296-39ee8d715267)<br />
The exploit for this is because it uses nano, which is vulnerable to privesc. Just run the file with `read` option and then do the follwing steps provided by [gtfobins](https://gtfobins.github.io/gtfobins/nano/#sudo): <br />
![image](https://github.com/user-attachments/assets/3a81946e-2469-4f3b-9809-e31c9c8af3a0)<br />




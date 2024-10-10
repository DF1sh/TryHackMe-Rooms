# Breakme

### Break the system
(Flags can be found at the end of this writeup)<br />
Initial nmap scan only shows port 22 and 80 open. The webserver seems just an empty apache webserver, however, a gobuster directory enumeration shows other resources:<br />
![image](https://github.com/user-attachments/assets/1862c187-c3be-4bfc-91f8-f10a88751816)<br />
Movin around on the webserver, I found a login page at `/wordpress/wp-login`. If I try to login with `admin`, I get back a response that the password for that user is wrong. This means that the `admin` user actually exists:<br  />
![image](https://github.com/user-attachments/assets/e8d5dad4-61b2-4bba-ab34-094940f871d0)<br/>
I tried bruteforcing admin account with `wpscan --url http://10.10.75.11/wordpress/wp-login.php -U admin -P /usr/share/wordlists/rockyou.txt`, but it didn't work.
Next, the following command ` wpscan --url http://10.10.75.11/wordpress/ -e u,p,t` enumerates users, plugins and templates. This time wpscan found another user, bob: <br />
![image](https://github.com/user-attachments/assets/f0e43a3a-36df-478b-909e-cc0009e989f0)<br />
So now try bruteforce bob: `wpscan --url http://10.10.122.80/wordpress/wp-login.php -U bob -P /usr/share/wordlists/rockyou.txt`. <br />
![image](https://github.com/user-attachments/assets/1e20d13e-626c-495e-a5e1-dbe040bd3060)<br />
His credentials are `bob:soccer`


- What is the first flag?
- What is the second flag?
- What is the root flag?

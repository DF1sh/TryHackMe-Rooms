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
His credentials are `bob:soccer`. 
The previous wpscan showed that the website is using an older version of `WP data access`, which is 5.3.8. Searching online, I found [here](https://www.wordfence.com/blog/2023/04/privilege-escalation-vulnerability-patched-promptly-in-wp-data-access-wordpress-plugin/) that this version is vulnerable to privilege escalation from subscriber+ to administrator. There's no explicit POC, but the exploit works as follows: 
1) On bob's account, click on `Update Profile`, and intercept the request with Burp Suite
2) Add a parameter to the request: `wpda_role[]=administrator`
3) Forward the request and become admin!
![image](https://github.com/user-attachments/assets/7f6f9ea6-e2b3-447e-8ae7-4b05392e9664)<br />
Now, to upload a reverse shell, we need to upload it in the theme's code, which is found inside `Tools->Themes File Editor`, upload the php reverse shell(I used the [PentestMonkey](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) one), open a netcat listener on the attackers machine and update the theme: <br />
![image](https://github.com/user-attachments/assets/e2598068-7ab7-4573-a0cb-ae4e2905ead2)<br />
Next, I [stabilized the shell](https://maxat-akbanov.com/how-to-stabilize-a-simple-reverse-shell-to-a-fully-interactive-terminal) so that i could maintain my mental integrity.<br />
Running linpaeas, it founds a set of credentials inside wordpress configuration file:<br />
![image](https://github.com/user-attachments/assets/f8e6b88d-9549-4d6b-bf3f-bd73830d8f1f)
So use the given credentials(`econor:SuP3rS3cR37#DB#P@55wd`) to log into the database `mysql -u econor -p`. In the database there are a couple of hashed passwords: <br />
![image](https://github.com/user-attachments/assets/a7d76b78-4539-4024-a637-343439d24388)<br />
We already know bob's password, let's try to crack the admin's password. The hash starts with `$P$`, this means that it is a `Phpass` hash format. I doesn't work, there must be something else. <br />
TO BE CONTINUED


- What is the first flag?
- What is the second flag?
- What is the root flag?

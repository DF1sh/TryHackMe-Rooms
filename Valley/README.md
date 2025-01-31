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
So I used these credentials to access valley's account with the `su` command.











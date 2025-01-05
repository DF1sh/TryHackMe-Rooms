# Agent Sudo

### Agent Sudo
Nmap scan shows ports 21,22 and 80 open: 

    PORT   STATE SERVICE VERSION
    21/tcp open  ftp     vsftpd 3.0.3
    22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 ef:1f:5d:04:d4:77:95:06:60:72:ec:f0:58:f2:cc:07 (RSA)
    |   256 5e:02:d1:9a:c4:e7:43:06:62:c1:9e:25:84:8a:e7:ea (ECDSA)
    |_  256 2d:00:5c:b9:fd:a8:c8:d8:80:e3:92:4f:8b:4f:18:e2 (ED25519)
    80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
    |_http-server-header: Apache/2.4.29 (Ubuntu)
    |_http-title: Annoucement
This is the webpage: <br />
![image](https://github.com/user-attachments/assets/44d18336-dc9e-4a84-8c5f-4a205e77dbe9)<br />
So I try to intercept the request and change the useragent to `R`, and I get this: <br />
![image](https://github.com/user-attachments/assets/f52b1e8c-77a0-4010-8da4-2cddae02885c)<br />
I believe this is hinting me that every agent has a codename that is a letter. After some enumeration, here's what I discovered: if I set the useragent, for example, as `A`: <br />
![image](https://github.com/user-attachments/assets/68ef855a-c3b3-4012-a807-a0d9a649a761)<br />
I get a response of 446 bytes. I tried with `B` and it's the same. But with `C` it's different: <br />
![image](https://github.com/user-attachments/assets/16273a18-699d-4994-9568-c50b921b5b30)<br />
I get 459 bytes and an additional header: `Location: agent_C_attention.php`. So I access `/agent_C_attention.php` and it shows me this message: <br />
![image](https://github.com/user-attachments/assets/aa0dec93-9808-485a-8168-179a551efb9b)<br />
Given this information, I try to bruteforce FTP with `hydra -l chris -P /usr/share/wordlists/rockyou.txt 10.10.252.204 ftp`. It works! The FTP server contains a text file and two images (one jpg and one png). The text file has the following content: <br />
![image](https://github.com/user-attachments/assets/49be5bda-9996-4a32-a4f9-97c0003edd27)<br />
So I have to do some steganography. I used `stegseek` to find the passphrase to see what's hidden under this image: <br />
![image](https://github.com/user-attachments/assets/15d71473-0b0b-4235-80e1-84006f14f370)<br />
The hidden message contains the ssh password for the user `james`:<br />
![image](https://github.com/user-attachments/assets/c60385f1-5a54-4d32-8861-444c6a7ee57a)<br />
Now for privesc, if I run `sudo -l`:<br />
![image](https://github.com/user-attachments/assets/8fc101a7-a6ae-4112-a06f-ac75717381d6)<br />
This means that I can spawn a shell with the privileges of any users with a shell, except root. That's not really helpful, but searching online, I found [this CVE](https://www.exploit-db.com/exploits/47502) that allows me to bypass this setting. <br />
Just run `sudo -u#-1 /bin/bash` and become root. 





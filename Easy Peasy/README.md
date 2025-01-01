# Easy Peasy

### Compromising the machine
Nmap scan shows ports 80,6498 and 65524 open: 

    PORT      STATE SERVICE VERSION
    80/tcp    open  http    nginx 1.16.1
    |_http-title: Welcome to nginx!
    | http-robots.txt: 1 disallowed entry 
    |_/
    |_http-server-header: nginx/1.16.1
    6498/tcp  open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 30:4a:2b:22:ac:d9:56:09:f2:da:12:20:57:f4:6c:d4 (RSA)
    |   256 bf:86:c9:c7:b7:ef:8c:8b:b9:94:ae:01:88:c0:85:4d (ECDSA)
    |_  256 a1:72:ef:6c:81:29:13:ef:5a:6c:24:03:4c:fe:3d:0b (ED25519)
    65524/tcp open  http    Apache httpd 2.4.43 ((Ubuntu))
    |_http-title: Apache2 Debian Default Page: It works
    | http-robots.txt: 1 disallowed entry 
    |_/
    |_http-server-header: Apache/2.4.43 (Ubuntu)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Port 65524 hosts a default apache2 server. But it has something hidden. If I look at the source code: <br />
![image](https://github.com/user-attachments/assets/6086a47b-c9ed-4cdb-a04c-0561be1289e1)<br />
This string is encoded in base62: <br />
![image](https://github.com/user-attachments/assets/6b2296b7-f261-4ca2-90ea-1b05739d4be5)<br />
So now if I vist `http://10.10.57.215:65524/n0th1ng3ls3m4tt3r/` I get an empty webpage containing a hash value. At this point I have some trouble understanding what type of hash is this, so I looked at the hint, and it's `GOST`.<br />
`john firstHash --format=GOST --wordlist=easypeasy_1596838725703.txt` is able to crack the password. I use this password to check for any embedded data inside the image `binarycodepixabay.jpg`(the one above the hash in the webpage) with the command `steghide --extract -sf binarycodepixabay.jpg`. It contains a file with username and password in binary words: <br />
![image](https://github.com/user-attachments/assets/fca3275a-9389-40a5-87fb-f6dc7924764d)<br />
So I can now log into `boring`'s ssh account, and get user.txt (You have to apply ROT13 to get it).  For privesc, if I run `cat /etc/crontab`: <br />
![image](https://github.com/user-attachments/assets/4947d63d-de50-486f-b099-6f499050e34b)<br />
![image](https://github.com/user-attachments/assets/e452fe38-2a0c-4d2c-8e7d-bee6e1bfa883)<br />
Since the file is owned by me, and can change it and execute whatever I want as root every minute. So I just added a reverse shell in bash and that's it, I got root. 



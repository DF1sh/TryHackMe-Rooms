# Dreaming
(Flags are at the end of the writeup)
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
TO BE CONTINUED..


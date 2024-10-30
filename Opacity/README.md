# Opacity
(flags are at the end of the writeup)

### Opacity
Initial scan shows ports 22,80,139 and 445 open, and ports 9485, 11972 and 15370 filtered:

    # Nmap 7.94SVN scan initiated Wed Oct 30 06:32:33 2024 as: nmap -p22,80,139,445,9485,11972,15370 -sV -sC -oN scan 10.10.40.162
    Nmap scan report for 10.10.40.162
    Host is up (0.067s latency).
    
    PORT      STATE  SERVICE     VERSION
    22/tcp    open   ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 0f:ee:29:10:d9:8e:8c:53:e6:4d:e3:67:0c:6e:be:e3 (RSA)
    |   256 95:42:cd:fc:71:27:99:39:2d:00:49:ad:1b:e4:cf:0e (ECDSA)
    |_  256 ed:fe:9c:94:ca:9c:08:6f:f2:5c:a6:cf:4d:3c:8e:5b (ED25519)
    80/tcp    open   http        Apache httpd 2.4.41 ((Ubuntu))
    | http-title: Login
    |_Requested resource was login.php
    | http-cookie-flags: 
    |   /: 
    |     PHPSESSID: 
    |_      httponly flag not set
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    139/tcp   open   netbios-ssn Samba smbd 4.6.2
    445/tcp   open   netbios-ssn Samba smbd 4.6.2
    9485/tcp  closed unknown
    11972/tcp closed unknown
    15370/tcp closed unknown
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
    
    Host script results:
    |_clock-skew: -1h00m52s
    |_nbstat: NetBIOS name: OPACITY, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
    | smb2-time: 
    |   date: 2024-10-30T09:32:00
    |_  start_date: N/A
    | smb2-security-mode: 
    |   3:1:1: 
    |_    Message signing enabled but not required

Gobuster finds `/cloud` directory on the webserver: `gobuster dir -u http://10.10.40.162 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-directories-lowercase.txt`<br />
![image](https://github.com/user-attachments/assets/bbd215c0-4ffa-4411-a220-61147005a489)<br />
http://10.10.40.162/cloud/storage.php

![image](https://github.com/user-attachments/assets/2c9685a7-0197-46c1-93f4-b7abfee80f0e)





- What is the  local.txt flag?
- What is the proof.txt flag?

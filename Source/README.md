# Source

### Source
Nmap scan shows ports 22 and 10000 open. 

    PORT      STATE SERVICE VERSION
    22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 b7:4c:d0:bd:e2:7b:1b:15:72:27:64:56:29:15:ea:23 (RSA)
    |   256 b7:85:23:11:4f:44:fa:22:00:8e:40:77:5e:cf:28:7c (ECDSA)
    |_  256 a9:fe:4b:82:bf:89:34:59:36:5b:ec:da:c2:d3:95:ce (ED25519)
    10000/tcp open  http    MiniServ 1.890 (Webmin httpd)
    |_http-server-header: MiniServ/1.890
    |_http-title: Login to Webmin

Looking online, I found that this version is vulnerable to unauthorized RCE, and I found [this](https://github.com/foxsin34/WebMin-1.890-Exploit-unauthorized-RCE/blob/master/webmin-1.890_exploit.py) exploit.<br />
![image](https://github.com/user-attachments/assets/ea805b39-d1b6-46ec-b76a-48bdfcfa0baa)<br />
So I use this to get a reverse shell:<br />
![image](https://github.com/user-attachments/assets/07292ec3-cc69-4b7f-a814-51706827d32c)<br />
At this point I'm already root and got both the flags.

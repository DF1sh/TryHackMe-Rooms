# IDE

### IDE
Nmap scan shows ports 21,22, 80 and 62337 open.

    21/tcp    open  ftp     vsftpd 3.0.3
    |_ftp-anon: Anonymous FTP login allowed (FTP code 230)
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
    |      At session startup, client count was 3
    |      vsFTPd 3.0.3 - secure, fast, stable
    |_End of status
    22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 e2:be:d3:3c:e8:76:81:ef:47:7e:d0:43:d4:28:14:28 (RSA)
    |   256 a8:82:e9:61:e4:bb:61:af:9f:3a:19:3b:64:bc:de:87 (ECDSA)
    |_  256 24:46:75:a7:63:39:b6:3c:e9:f1:fc:a4:13:51:63:20 (ED25519)
    80/tcp    open  http    Apache httpd 2.4.29 ((Ubuntu))
    |_http-server-header: Apache/2.4.29 (Ubuntu)
    |_http-title: Apache2 Ubuntu Default Page: It works
    62337/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
    |_http-title: Codiad 2.8.4
    |_http-server-header: Apache/2.4.29 (Ubuntu)
Port 62337 contains a login page:<br />
![image](https://github.com/user-attachments/assets/229f6538-351f-4b07-bea8-4daef2ddc3d1)<br />
Searching online for codiad 2.8.4, I found [this exploit](https://github.com/WangYihang/Codiad-Remote-Code-Execute-Exploit) which is an authenticated RCE. So I need to first find a valid set of credentials to log in. After some enumeration, I find the github project at [this link](https://github.com/Codiad/Codiad).<br />
Next, I log into the ftp server with the anonymous login and saw a directory named `...`:<br />
![image](https://github.com/user-attachments/assets/8d83a6cb-92d2-4fb7-9c64-5690c0ee0355)<br />
Inside of it, there's a file named `-`:
![image](https://github.com/user-attachments/assets/797f409e-6db6-4790-84f0-dd0c56e45038)<br />
Download it with the `get` command, then read it with `cat ./-`:<br />
![image](https://github.com/user-attachments/assets/12ddeea7-6add-4f8e-ab2e-60ee06af1388)<br />
So I know that there's probably a username `john`, but I can't find the default password online. But then I simply tried to log in with john:password and it worked, lol. So I executed the exploit that I found earlier:
![image](https://github.com/user-attachments/assets/b5d3d596-c660-4dac-95bf-2d7e0959553d)<br />
Inside `drac`'s home directory I found a set of mysql credentials:<br />
![image](https://github.com/user-attachments/assets/fec201eb-346f-4398-ab05-7c72290e6661)<br />
I used that password to log into drac's account with `su drac`. Now, as drac, if I run `sudo -l`, after prompting the password, I get:<br />
![image](https://github.com/user-attachments/assets/ed658269-c74d-4dbe-9420-8b85019690d4)<br />
I found [this website](https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/sudo-service-privilege-escalation/) that explains how to excalate to root with this privilege. <br />
![image](https://github.com/user-attachments/assets/992c9d63-f1ac-4ff2-93a9-c16a29fed7aa)<br />
Since I have write access to the configuration file, I'm going to insert a reverse shell into it:<br />
![image](https://github.com/user-attachments/assets/a81ec46a-ebc1-47a3-9880-4e80000259d1)<br />
Next, run 

    systemctl daemon-reload
    sudo /usr/sbin/service vsftpd restart
And become root!











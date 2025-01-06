# Smag Grotto

### Smag Grotto
Nmap scan shows ports 22 and 80 open. 

    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 74:e0:e1:b4:05:85:6a:15:68:7e:16:da:f2:c7:6b:ee (RSA)
    |   256 bd:43:62:b9:a1:86:51:36:f8:c7:df:f9:0f:63:8f:a3 (ECDSA)
    |_  256 f9:e7:da:07:8f:10:af:97:0b:32:87:c9:32:d7:1b:76 (ED25519)
    80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    |_http-title: Smag

Gobuster finds `/mail` directory with the following content: <br />
![image](https://github.com/user-attachments/assets/71a60ed9-b2eb-4c32-8e8a-22ca14bc6fdf)<br />
If I open the .pcap file, there's an unencrypted(HTTP) login request with credentials: <br />
![image](https://github.com/user-attachments/assets/77c4fce6-4ec2-4386-9e72-f5908eb43266)<br />
Interestingly, it's sent to `development.smag.thm`. To access this page, add the following line `10.10.245.49 smag.thm development.smag.thm` to the file `/etc/hosts`. If I access the subdomain I get this: <br />
![image](https://github.com/user-attachments/assets/8b965d44-0ef1-4f1c-be73-2a8c19b57706)<br />
But admin.php redirects me to login.php so it's the same thing. I use the previously found credentials to log in, and it shows me a panel in which I can insert commands:<br />
![image](https://github.com/user-attachments/assets/3986108d-b4d1-44d1-bf74-57fd12d81976)<br />
I tried some basic commands like `whoami` or `env` but nothing is shown on the website. My next try is to send me a netcat connection just to see if the commands get actually executed, but it just doesn't print the results back. And it actually works. This means that I can spawn a shell: <br />
![image](https://github.com/user-attachments/assets/31828de2-bbeb-4458-b511-815cfe84aea1)<br />
Now for privesc, moving around the filesystem I found a cronjob: <br />
![image](https://github.com/user-attachments/assets/b1af803a-bfa1-4307-afdd-0c7977076b04)<br />
I have write access to `/opt/.backups/jake_id_rsa.pub.backup`, so I will generate a set of rsa keys and let this cronjob do it's job. First, run `ssh-keygen -t rsa -b 4096` to generate a set of keys and save it on your directory. Next modify the `jake_id_rsa.pub.backup` with the newly generated public key. Now wait. <br />
Finally, log into jake's account with `ssh jake@10.10.245.49 -i id_rsa` and get the user flag. If I run `sudo -l` I get: <br />
![image](https://github.com/user-attachments/assets/7c7ac7ec-8ab4-431b-afb5-eb92634face2)<br />
The exploit for this can be easily found on [gtfobins](https://gtfobins.github.io/gtfobins/apt-get/#sudo). Just run `sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh` and become root. 










# Grep

### Grep
Initial nmap scan shows ports 22,80,443,51337 open.

      PORT      STATE SERVICE  VERSION
      22/tcp    open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
      | ssh-hostkey: 
      |   3072 d7:c8:b7:cd:f6:96:1c:00:f4:2f:b0:54:fa:9f:eb:00 (RSA)
      |   256 4a:1b:9a:11:dd:77:70:a2:bd:e9:5c:8b:0b:0b:d2:7a (ECDSA)
      |_  256 64:99:78:e9:f7:da:57:4b:8b:4b:d4:fe:57:b2:96:1e (ED25519)
      80/tcp    open  http     Apache httpd 2.4.41 ((Ubuntu))
      |_http-server-header: Apache/2.4.41 (Ubuntu)
      |_http-title: Apache2 Ubuntu Default Page: It works
      443/tcp   open  ssl/http Apache httpd 2.4.41
      |_ssl-date: TLS randomness does not represent time
      | ssl-cert: Subject: commonName=grep.thm/organizationName=SearchME/stateOrProvinceName=Some-State/countryName=US
      | Not valid before: 2023-06-14T13:03:09
      |_Not valid after:  2024-06-13T13:03:09
      | tls-alpn: 
      |_  http/1.1
      |_http-title: 403 Forbidden
      |_http-server-header: Apache/2.4.41 (Ubuntu)
      51337/tcp open  http     Apache httpd 2.4.41
      |_http-title: 400 Bad Request
      |_http-server-header: Apache/2.4.41 (Ubuntu)
      Service Info: Host: ip-10-10-22-127.eu-west-1.compute.internal; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Looking at the certificate on port 51337, there's a subdomain. <br />
![image](https://github.com/user-attachments/assets/304b9725-dbf9-4ff6-a6dd-8317a7e2b8a8)<br />
I add it to /etc/hosts to access the webpage. 
Directory enumeration of `https://grep.thm/public/html/`:<br />
![image](https://github.com/user-attachments/assets/a366860e-c272-4c16-845a-881361ba7361)<br />
Directory enumeration of `https://grep.thm/api/`:<br />
![image](https://github.com/user-attachments/assets/c3807f2e-696a-4341-8fdf-61d812562cbd)<br />
If I capture a request at `/register.php` with burpsuit this is what i get: <br />
![image](https://github.com/user-attachments/assets/31111f1d-d974-4d7c-8a06-152f7c83145f)<br />
I submit the API key on crackstation, and it the MD5 hash of `johncena`
Next, searching online I found the [repository](https://github.com/supersecuredeveloper/searchmecms) containing the code of this webserver. I found here the correct API to register, in the file `/api/register.php`:<br />
![image](https://github.com/user-attachments/assets/de7fba2b-165c-414f-86db-64659a035912)<br />
The API key I need is inside the initial commit and it's the MD5 hash of `youcantseeme`. This allowed me to register and also to get the first flag. <br />
![image](https://github.com/user-attachments/assets/571521da-5bd8-431e-ad3f-af182399d372)<br />
The name "chuck", which is my user, get's displayed in the web page. If I try to register with a username of `<script>alert(1);</script>`, when I log in, it actually shows an alert. So I can perform XSS, but this is not the right path. <br />
There's page in which we can upload files after being logged in at `/public/html/upload.php`. Here we can upload images. Looking at the code in the repository, the only checks performed by the `upload.php` script is on the magic number of the file. 
The idea is to create a php reverse shell (I used the one from pentest monkey), but before uploading, adding the magic number of jpg files at the beginning of the php reverse shell. I did it using `hexeditor` tool, by adding `FF D8 FF E0` at the begigging of the file. The result is a reverse shell:<br />
![image](https://github.com/user-attachments/assets/763bd17f-1389-425a-82a2-7ad260dba91e)<br />
Found the email inside `/var/www/backup`:<br />
![image](https://github.com/user-attachments/assets/8f884204-3085-4de1-89ca-40de5b6fe9a0)<br />
To find the password, just move to `https://leakchecker.grep.thm:51337/` and submit the admin email. 

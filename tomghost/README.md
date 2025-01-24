# tomghost

### tomghost
Nmap scan shows ports 22,53,8009 and 8080 open. <br />
8080 is running a tomcat server, while 8009 is running the AJP protocol, which is a protocol used by tomcat to comunicate with backend servlet engines. Enumerating a bit the versions, I found out that there's a vulnerability called **ghostcat**. <br />
There's a very well written explanation [here](https://www.trendmicro.com/en_us/research/20/c/busting-ghostcat-an-analysis-of-the-apache-tomcat-vulnerability-cve-2020-1938-and-cnvd-2020-10487.html), and a working POC [here](https://github.com/3ndG4me/ghostcat/blob/main/README.md). Basically it allows the attacker to read files included in the root folder of the web server. If certain conditions are met, it might even lead to RCE, but it's not the case of this machine. <br />
One of the most common directories in the root folder of tomcat web server is `WEB-INF`. This directory contains all things related to the application that aren’t in the document root of the application. Some information is stored in a file called `web.xml`. Let's exploit this vulnerability to read this file: <br />
Download the POC code, and run `python3 tomghost.py -p 8009 -f /WEB-INF/web.xml target_IP`. Inside this files there are a set of ssh credentials.<br />
![image](https://github.com/user-attachments/assets/4b4e7fb9-c55c-44c6-b3e1-eb91f1e1f183)<br />
I'll use them to access to the machine and get the first flag. <br />
Inside the user home directory there are these two files: <br />
![image](https://github.com/user-attachments/assets/3957cfde-8923-4a43-b4b8-643d79db3367)<br />
One is an BGB encrypted file, the other one contains a private key, which I suppose it's used to decrypt the credentials.pgp file. So run `gpg --import tryhackme.asc` and then `gpg --decrypt credential.pgp`. The problem is that if I try to decrypt it I get asked for a passphrase: <br />
![image](https://github.com/user-attachments/assets/e33981b6-39ea-44d2-acf2-6429253adac1)<br />
To crack it, I'll use john the ripper. First I copy the private file in my local machine inside `priv.key`, then run `gpg2john priv.key > hash.txt` and finally `john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt`. This immediately finds the passphrase. <br />
I'm able to use the decrypted credentials to log into `merlin`'s account. Now, if I run `sudo -l` I get: <br />
![image](https://github.com/user-attachments/assets/2926f46f-7ab3-4318-b6c2-81fa501b0ecb)<br />
The exploit for sudo on `zip` can be easily found on [gtfobins](https://gtfobins.github.io/gtfobins/zip/#sudo). Just run the following commands and become root! <br />
![image](https://github.com/user-attachments/assets/cf0cb38f-7699-4d95-8d6e-83a0fc7d7453)<br />



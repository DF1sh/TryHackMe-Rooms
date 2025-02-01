# NerdHerd

### NerdHerd
Nmap scan shows ports 21,22,139,445 and 1337. Port 1337 is a default apache web server: <br />
![image](https://github.com/user-attachments/assets/5cbbd909-02f2-4ecd-98c1-f6a350d20816)<br />
![image](https://github.com/user-attachments/assets/35a131a9-b94b-47f9-bf07-752aad75fdb1)<br />
Gobuster finds `/admin`: <br />
![image](https://github.com/user-attachments/assets/ee951fe8-b80c-464e-99f6-9e3d6961fe79)<br />
Found an interesting comment in the source code: <br />
![image](https://github.com/user-attachments/assets/444e3d4b-84ff-4152-80b8-699661c03090)<br />
`Y2liYXJ0b3dza2k=` is the base64 encoding of `cibartowski`. <br />
Inside FTP server I find two files, `hellon3rd.txt` and `youfoundme.png`. The txt file contains this: <br />
![image](https://github.com/user-attachments/assets/66e5b8dc-0700-4f30-9531-14a0875ecb1b)<br />
And if I run `exiftool`  on the image, I get an owner name, which seems to be encrypted: <br />
![image](https://github.com/user-attachments/assets/eb989020-f82f-4ac4-9684-c0bc0837a02c)<br />
This is encrypted with vigenere cipher (I understood it using [this website](https://www.boxentriq.com/code-breaking/cipher-identifier)) and the key is `birdistheword`(For this I had to look at an external writeup). I decoded it with cyberchef and got a password. <br />
After further enumeration, `enum4linux` reveals a valid username in the SMB share, called `chuck`. I use username `chuck` and the decrypted password to log in. The SMB share contains the following .txt file: <br />
![image](https://github.com/user-attachments/assets/80bece0b-c4df-480e-94b9-5ab59662fcf4)<br />
![image](https://github.com/user-attachments/assets/5bb850f9-4740-4b69-9b44-65a7ae48ebbc)<br />
I use these credentials to access `chuck`'s ssh and get the user flag. Enumerating the system with linpeas, I found that this machine is vulnerable to privilege escalation with [this exploit](https://github.com/rlarabee/exploits/blob/master/cve-2017-16995/cve-2017-16995.c). <br />
I donwload it on my local machine and compile it statically with `gcc pwn.c -o pwn -static` and then transfer it to the target machine. When I run it: <br />
![image](https://github.com/user-attachments/assets/7f67decb-55cb-4ff2-96d8-eb82a7029a25)<br /> 
I become root and got the second flag. The third flag is in root bash history. 


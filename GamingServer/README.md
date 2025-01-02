# GamingServer

### Boot2Root
Nmap scan shows ports 22 and 80 open. Source code of the web page contains a comment with a username: <br />
![image](https://github.com/user-attachments/assets/d1f5fd74-284d-4c98-bd83-5a6b445f6026)<br />
`/uploads` contains the following files: <br />
![image](https://github.com/user-attachments/assets/a2518d77-b5c1-41cf-b6cc-d7c5cbde12f4)<br />
First, there's the beautiful hacker manifesto from The Mentor. Then `dict.lst` is a wordlist of passwords, and the jpg image is the following, lol: <br />
![image](https://github.com/user-attachments/assets/cc43efc9-2b83-475a-bfa2-7386df257483)<br />
Gobuster directory enumeration also reveals `/about.php`. If I visit it, the webpage stays the same as for `about.html`, with a little difference: <br />
![image](https://github.com/user-attachments/assets/fb0bf6df-0381-4584-be33-58438248c093)<br />
There's an upload feature. I spent some time on it and I'm not sure what to do with it, maybe I'll come back to it later. Gobuster enumeration also shows a `/secret` directory: <br />
![image](https://github.com/user-attachments/assets/bd0263c6-9dae-4201-a57d-2ddb90368bdc)<br />
This is a private rsa key but it's encrypted with AES. To decrypt it, my idea is to use the provided wordlist `dict.lst` to try and crack it using john: 

    ssh2john secretKey > hash
    john hash --wordlist=dict.lst
It works! I have the passphrase. So I log on john's account with `ssh john@10.10.193.66 -i secretKey` and get the user flag. <br />
For privesc, linpeas shows me, among other things, the sudo version: <br />
![image](https://github.com/user-attachments/assets/7158b262-45d6-4bce-b9cd-de956309f908)<br />
Searching online, this version might be vulnerable to CVE-2021-3156. I also checked [this script](https://github.com/lypd0/CVE-2021-3156-checker/blob/main/CVE-2021-3156-checker.py) and it confirms it: <br />
![image](https://github.com/user-attachments/assets/006fbaf6-117b-4c82-a14c-546a3593c01a)<br />
So I found this exploit on github and it worked correctly and spawned me a root shell. 




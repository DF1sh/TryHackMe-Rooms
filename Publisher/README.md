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
But really nothing interesting.

- What is the user flag?
- What is the root flag?


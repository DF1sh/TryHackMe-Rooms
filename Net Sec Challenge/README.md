# Net Sec Challenge

### Challenge Questions
- What is the highest port number being open less than 10,000?<br />

       nmap 10.10.161.99 -p- --min-rate=1000 -n -Pn 
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-08 13:57 CEST
      Nmap scan report for 10.10.161.99
      Host is up (0.050s latency).
      Not shown: 65529 closed tcp ports (conn-refused)
      PORT      STATE SERVICE
      22/tcp    open  ssh
      80/tcp    open  http
      139/tcp   open  netbios-ssn
      445/tcp   open  microsoft-ds
      8080/tcp  open  http-proxy
      10021/tcp open  unknown
      
      Nmap done: 1 IP address (1 host up) scanned in 26.94 seconds

  `8080`

- There is an open port outside the common 1000 ports; it is above 10,000. What is it?<br />
`10021`
- How many TCP ports are open?<br />
`6`
- What is the flag hidden in the HTTP server header?<br />
Connect to port 80 through telnet: <br />
![image](https://github.com/user-attachments/assets/8193c940-7307-476c-8c61-7014dd867ba9)<br />
Alternatively, you could run nmap with the `-sC` flag: <br />
![image](https://github.com/user-attachments/assets/801ea3e1-ecbf-48a9-9ce3-89a37ee3370f)<br />
`THM{web_server_25352}`
- What is the flag hidden in the SSH server header?<br />
Do the same thing but with port 22: <br />
![image](https://github.com/user-attachments/assets/60315908-a9b8-40a5-ba06-f55159025408)<br />
`THM{946219583339}`
- We have an FTP server listening on a nonstandard port. What is the version of the FTP server?<br />

      nmap -sV 10.10.161.99 -p 10021 -sC
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-08 14:11 CEST
      Nmap scan report for 10.10.161.99
      Host is up (0.054s latency).
      
      PORT      STATE SERVICE VERSION
      10021/tcp open  ftp     vsftpd 3.0.5
      Service Info: OS: Unix
      
      Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
      Nmap done: 1 IP address (1 host up) scanned in 3.73 seconds

  `vsftpd 3.0.5`

- We learned two usernames using social engineering: eddie and quinn. What is the flag hidden in one of these two account files and accessible via FTP?<br />
Let's try to bruteforce the passwords: run `hydra -l eddie -P /usr/share/wordlists/rockyou.txt ftp://10.10.161.99:10021`: <br />
![image](https://github.com/user-attachments/assets/71961d25-a559-44f4-80a0-426c2b8fa8c2)<br />
Logging into eddie's account, I didn't find any file, let's try to brute force quinn's account: <br />
![image](https://github.com/user-attachments/assets/9b121e70-7f03-47b1-88ec-8347ac3bfe95)<br />
The flag is in quinn's account, download it using the `get` command: `THM{321452667098}`
- Browsing to http://10.10.161.99:8080 displays a small challenge that will give you a flag once you solve it. What is the flag?<br />
![image](https://github.com/user-attachments/assets/71fbe315-5143-4fba-b1b2-c697baff6e5c)<br />
We need to scan the target without getting noticed.  The solution to this challenge is using the `-sN` flag, which is a NULL scan. The null scan does not set any flag; all six flag bits are set to zero.
A TCP packet with no flags set will not trigger any response when it reaches an open port, as shown in the figure below. Therefore, from Nmap’s perspective, a lack of reply in a null scan indicates that either the port is open or a firewall is blocking the packet.
However, we expect the target server to respond with an RST packet if the port is closed.<br />
Run `sudo nmap -sN target_IP` to get the flag: <br />
![image](https://github.com/user-attachments/assets/32c4cf1a-c337-431a-b4a3-5bd496763006)<br />
`THM{f7443f99}`



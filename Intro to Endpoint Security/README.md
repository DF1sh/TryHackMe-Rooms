# Intro to Endpoint Security

### Endpoint Security Fundamentals
- What is the normal parent process of services.exe? `wininit.exe`
- What is the name of the network utility tool introduced in this task? `TCPView`

### Endpoint Logging and Monitoring
- Where do the Windows Event logs (.evtx files) typically reside? `C:\Windows\System32\winevt\Logs`
- Provide the command used to enter OSQuery CLI. `osqueryi`
- What does EDR mean? Provide the answer in lowercase. `endpoint detection and response`

### Endpoint Log Analysis
Provide the flag for the simulated investigation activity.<br />
The picture below shows the legit processes: <br/>
![image](https://github.com/user-attachments/assets/563d3415-b3a9-42a4-969a-70ef88ffc4ea)<br />
There's a process called `beacon.exe` which is not in the list: <be />
![image](https://github.com/user-attachments/assets/44939ea1-2215-4b19-a494-f485c1599bfe)<br />
Remediate to get the flag<br />
![image](https://github.com/user-attachments/assets/2096ce70-deff-408e-8503-a76c093cfee0)<br />
`THM{3ndp01nt_s3cur1ty!}`

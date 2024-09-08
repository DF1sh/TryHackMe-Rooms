# Core Windows Processes
For this task we're going to need to connect to the target machine over RDP(Remote Desktop Protocl). I'm using `xfreerdp` from my kali machine, the full command is `xfreerdp /u:Administrator /p:letmein123! /v:10.10.142.13`
![image](https://github.com/user-attachments/assets/6a459257-27d2-4dc6-95ae-3fffa46e7aa0)

### System
- What PID should System always be? `4`

### System > smss.exe
- Aside from csrss.exe, what process does smss.exe spawn in Session 1? `winlogon.exe`

### csrss.exe
- What was the process which had PID 384 and PID 488? `smss.exe`

### wininit.exe
- Which process might you not see running if Credential Guard is not enabled? `lsaiso.exe`

### wininit.exe > services.exe
- How many instances of services.exe should be running on a Windows system? `1`

### wininit.exe > services.exe > svchost.exe
- What single letter parameter should always be visible in the Command line or Binary path? `k`

### lsass.exe
- What is the parent process for LSASS? `wininit.exe`

### winlogon.exe
- What is the non-existent parent process for winlogon.exe? `smss.exe`

### explorer.exe
-  What is the non-existent process for explorer.exe? `userinit.exe`

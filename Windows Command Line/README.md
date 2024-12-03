# Windows Command Line

### Introduction
- What is the default command line interpreter in the Windows environment? `cmd.exe`

### Basic System Information
- What is the OS version of the Windows VM?<br />
![image](https://github.com/user-attachments/assets/7b04d6f8-2487-4ea1-8164-657ed32fedb9)<br />
`10.0.20348.2655`
- What is the hostname of the Windows VM?<br />
`WINSRV2022-CORE`

### Network Troubleshooting
- Which command can we use to look up the server’s physical address (MAC address)? `ipconfig /all`
- What is the name of the process listening on port 3389?<br />
Run `netstat -abon` to get the answer: `TermService`
- What is the IP address of your gateway?<br />
![image](https://github.com/user-attachments/assets/ebfdd429-bc50-4768-97c7-040f5e015012)<br />
`10.10.0.1`

### File and Disk Management
- What are the file’s contents in C:\Treasure\Hunt?<br />
Run `more C:\Treasure\Hunt\flag.txt` to get the answer: `THM{CLI_POWER}`

### Task and Process Management
- What command would you use to find the running processes related to notepad.exe? `tasklist /FI "imagename eq notepad.exe"`
- What command can you use to kill the process with PID 1516? `taskkill /PID 1516`

### Conclusion
- The command shutdown /s can shut down a system. What is the command you can use to restart a system? `shutdown /r`
- What command can you use to abort a scheduled system shutdown? `shutdown /a`

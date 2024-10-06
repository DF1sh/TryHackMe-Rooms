# Critical

### Memory Forensics
- What type of memory is analyzed during a forensic memory task? `RAM`
- In which phase will you create a memory dump of the target system? `Memory Acquisition`

### Environment & Setup
- Which plugin can help us to get information about the OS running on the target machine? `Windows.info`
- Which tool referenced above can help us take a memory dump on a Linux OS? `LIME`
- Which command will display the help menu using Volatility on the target machine? `vol -h`

### Gathering Target Information
![image](https://github.com/user-attachments/assets/29e2de9b-6687-4de9-a6e0-4e443fab7705)<br/>
- Is the architecture of the machine x64 (64bit) Y/N? `Y`
- What is the Verison of the Windows OS `10`
- What is the base address of the kernel? `0xf8066161b000`

### Searching for Suspicious Activity
- Using the plugin "windows.netscan" can you identify the IP address that establish a connection on port 80?<br />
Run `vol -f memdump.mem windows.netscan`:<br />
![image](https://github.com/user-attachments/assets/eae09bc5-9786-4991-9155-bccc8f62b1b7)<br />
`192.168.182.128`
- Using the plugin "windows.netscan," can you identify the program (owner) used to access through port 80? `msedge.exe`
- Analyzing the process present on the dump, what is the PID of the child process of critical_updat?<br />
![image](https://github.com/user-attachments/assets/24f21ab2-4501-4a34-b7d9-d2916b0c36e1)<br />
From the image above, we can see that `critical_updat` has PID of 1648, and `updater.exe` has PPID of 1684, so the answer is its PID: `1612`
- What is the time stamp time for the process with the truncated name critical_updat? `2024-02-24 22:51:50.000000`

### Finding Interesting Data
- Analyzing the "windows.filescan" output, what is the full path and name for critical_updat?<br />
Run `vol -f memdump.mem windows.filescan > filescan_out`. <br />
![image](https://github.com/user-attachments/assets/f8840ca0-3446-4c77-b1d0-727418baab51)<br />
`C:\Users\user01\Documents\critical_update.exe`
- Analyzing the "windows.mftscan.MFTScan" what is the Timestamp for the created date of important_document.pdf?<br />
Run `vol -f memdump.mem windows.mftscan.MFTScan > mftscan_out`:<br />
![image](https://github.com/user-attachments/assets/1b473661-d04e-44e6-af9e-ac83a704a384)<br />
`2024-02-24 20:39:42.000000`
- Analyzing the updater.exe memory output, can you observe the HTTP request and determine the server used by the attacker?<br />
Run `vol -f memdump.mem -o . windows.memmap --dump --pid 1612`, and then `strings pid.1612.dmp |grep -B 10 -A 10 "http://key.critical-update.com/encKEY.txt"`:<br />
`SimpleHTTP/0.6 Python/3.10.4`

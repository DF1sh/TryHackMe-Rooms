# Sysinternals

### Introduction
- When did Microsoft acquire the Sysinternals tools? `2006`

### Install the Sysinternals Suite
- What is the last tool listed within the Sysinternals Suite? <br />
![image](https://github.com/user-attachments/assets/79376aa1-23b6-4120-8da2-62bbc380df63)<br />
`ZoomIt`

### Using Sysinternals Live
- What service needs to be enabled on the local host to interact with live.sysinternals.com? `WebClient`

### File and Disk Utilities
- There is a txt file on the desktop named file.txt. Using one of the three discussed tools in this task, what is the text within the ADS? <br />
By running the stream command we can see the name of the ADS: <br />
![image](https://github.com/user-attachments/assets/966a6707-524e-474d-a606-f4d5864e24a7)<br />
Now to see the contents of it, run `more < file.txt:ads.txt`:<br />
![image](https://github.com/user-attachments/assets/0e1b0a7b-fe3b-4995-83da-3af2c41154c3)<br />
`I am hiding in the stream.`

### Networking Utilities
- Using WHOIS tools, what is the ISP/Organization for the remote address in the screenshots above? <br />
We want to query the following IP address: <br />
![image](https://github.com/user-attachments/assets/b21bdae3-961b-4ef3-8842-72a1125d7003)<br />
Found the answer [here](https://who.is/whois-ip/ip-address/):<br />
![image](https://github.com/user-attachments/assets/c41b6e0c-a153-4441-9547-667765a2128c)<br />
`Microsoft Corporation`

### Process Utilities
- Run Autoruns and inspect what are the new entries in the Image Hijacks tab compared to the screenshots above.  What entry was updated?<br />
Open powershell and run `autoruns` and click on `Image Hijacks`: <br />
![image](https://github.com/user-attachments/assets/f8103d74-c566-49a4-a63d-742542063219)<br />
If we compare it with the given screenshot:<br />
![image](https://github.com/user-attachments/assets/5e164945-b2a7-43d0-b5f5-b8fbef27985b)<br />
We can see that the task manages has been updated once. So the answer is `taskmgr.exe`. 
- What is the updated value?<br />
![image](https://github.com/user-attachments/assets/3db2a16a-17b2-4617-ad87-a6af6603abd7)<br />
`c:\tools\sysint\procexp.exe`

### Miscellaneous
- Run the Strings tool on ZoomIt.exe. What is the full path to the .pdb file?<br />
Move to the directory containing ZoomIt.exe, `C:\Tools\sysint`. Now run `strings .\ZoomIt.exe | findstr /i .pdb`: <br />
![image](https://github.com/user-attachments/assets/31fce12f-791a-4944-b00e-4ea964e02644)<br />
`C:\agent\_work\112\s\Win32\Release\ZoomIt.pdb`

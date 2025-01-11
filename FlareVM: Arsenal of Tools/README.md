# FlareVM: Arsenal of Tools

### Arsenal of Tools
- Which tool is an Open-source debugger for binaries in x64 and x32 formats? `x64dbg`
- What tool is designed to analyze and edit Portable Executable (PE) files? `CFF Explorer`
- Which tool is considered a sophisticated memory editor and process watcher? `Process Hacker`
- Which tool is used for Disc image acquisition and analysis for forensic use? `FTK Imager`
- What tool can be used to view and edit a binary file? `HxD`

### Commonly Used Tools for Investigation: Overview
- Which tool was formerly known as FLARE Obfuscated String Solver? `FLOSS`
- Which tool offers in-depth insights into the active processes running on your computer? `Process Explorer`
- By using the Process Explorer (procexp) tool, under what process can we find smss.exe?<br />
![image](https://github.com/user-attachments/assets/284d5ec1-ec65-4ca7-84fc-ca7fa5ae1a76)<br />
`System`
- Which powerful Windows tool is designed to help you record issues with your system's apps? `Procmon`
- Which tool can be used for Static analysis or studying executable file properties without running the files? `PEStudio`
- Using the tool PEStudio to open the file cryptominer.bin in the Desktop\Sample folder, what is the sha256 value of the file? <br />
![image](https://github.com/user-attachments/assets/2bf4cbf7-05c4-4faf-a579-d1dac5001eb8)<br />
`E9627EBAAC562067759681DCEBA8DDE8D83B1D813AF8181948C549E342F67C0E`
- Using the tool PEStudio to open the file cryptominer.bin in the Desktop\Sample folder, how many functions does it have? `102`
- What tool can generate file hashes for integrity verification, authenticate the source of system files, and validate their validity? `CFF Explorer`
-  Using the tool CFF Explorer to open the file possible_medusa.txt in the Desktop\Sample folder, what is the MD5 of the file?<br />
![image](https://github.com/user-attachments/assets/bdc95ca8-2270-4c58-a435-4eba64c6b8cd)<br />
`646698572AFBBF24F50EC5681FEB2DB7`
-  Use the CFF Explorer tool to open the file possible_medusa.txt in the Desktop\Sample folder. Then, go to the DOS Header Section. What is the e_magic value of the file?<br />
![image](https://github.com/user-attachments/assets/f469c97f-17ed-45df-86a7-fa2783a75d5f)<br />
`5A4D`

### Analyzing Malicious Files!
- Using PEStudio, open the file windows.exe. What is the entropy value of the file windows.exe?<br />
![image](https://github.com/user-attachments/assets/ffe3b8e1-0772-4f85-ac85-7dc66c8c876f)<br />
`7.999`
- Using PEStudio, open the file windows.exe, then go to manifest (administrator section). What is the value under requestedExecutionLevel?<br />
![image](https://github.com/user-attachments/assets/ce5a8de3-d563-4b4f-9aed-883f84c0951c)<br />
`requireAdministrator`
- Which function allows the process to use the operating system's shell to execute other processes?
![image](https://github.com/user-attachments/assets/8017651d-f25a-4e00-b953-af9564056c5f)<br />
`set_UseShellExecute`
- Which API starts with R and indicates that the executable uses cryptographic functions? `RijndaelManaged`
- What is the Imphash of cobaltstrike.exe? `92EEF189FB188C541CBD83AC8BA4ACF5`
- What is the defanged IP address to which the process cobaltstrike.exe is connecting? <br />
Use procmon for this, and filter by name="cobaltstrike.exe": <br />
![image](https://github.com/user-attachments/assets/210af304-9b2f-4700-8f55-a1b9d6f59be7)<br />
`47[.]120[.]46[.]210`
- What is the destination port number used by cobaltstrike.exe when connecting to its C2 IP Address?<br />
![image](https://github.com/user-attachments/assets/5508e865-a40d-4bb5-9bfc-34cd55891c40)<br />
`81`
- During our analysis, we found a process called cobaltstrike.exe. What is the parent process of cobaltstrike.exe? 
![image](https://github.com/user-attachments/assets/1cc370a5-065a-46b7-a654-b701e7b7361d)<br />
`explorer.exe`

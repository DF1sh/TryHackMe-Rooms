# REMnux: Getting Started

### File Analysis
- What Python tool analyzes OLE2 files, commonly called Structured Storage or Compound File Binary Format? `oledump.py`
- What tool parameter we used in this task allows you to select a particular data stream of the file we are using it with? `-s`
- During our analysis, we were able to decode a PowerShell script. What command is commonly used for downloading files from the internet? `Invoke-WebRequest`
- What file was being downloaded using the PowerShell script? `Doc-3737122pdf.exe`
- During our analysis of the PowerShell script, we noted that a file would be downloaded. Where will the file being downloaded be stored? `$TempFile`
- Using the tool, scan another file named possible_malicious.docx located in the /home/ubuntu/Desktop/tasks/agenttesla/ directory. How many data streams were presented for this file?<br />
![image](https://github.com/user-attachments/assets/e07b20d4-54eb-4099-a4b7-0c4c96694ddb)<br />
`16`
- Using the tool, scan another file named possible_malicious.docx located in the /home/ubuntu/Desktop/tasks/agenttesla/ directory. At what data stream number does the tool indicate a macro present? `8`

### Fake Network to Aid Analysis
- Download and scan the file named flag.txt from the terminal using the command sudo wget https://MACHINE_IP/flag.txt --no-check-certificate. What is the flag?<br />
![image](https://github.com/user-attachments/assets/8c722c4d-5778-4929-9a79-08d97ecc88e7)<br />
`Tryhackme{remnux_edition}`
- After stopping the inetsim, read the generated report. Based on the report, what URL Method was used to get the file flag.txt? `GET`

### Memory Investigation: Evidence Preprocessing
- What plugin lists processes in a tree based on their parent process ID? `PsTree`
- What plugin is used to list all currently active processes in the machine? `PsList`
- What Linux utility tool can extract the ASCII, 16-bit little-endian, and 16-bit big-endian strings? `strings`
- By running vol3 with the Malfind parameter, what is the first (1st) process identified suspected of having an injected code? <br />
![image](https://github.com/user-attachments/assets/2f99f922-ac7f-4c0a-a461-affcff3294c6)<br />
`csrss.exe`
- Continuing from the previous question (Question 6), what is the second (2nd) process identified suspected of having an injected code? `winlogon.exe`
- By running vol3 with the DllList parameter, what is the file path or directory of the binary @WanaDecryptor@.exe? <br />
![image](https://github.com/user-attachments/assets/4f4d6cb2-9273-4751-b587-46bb4d314788)<br />
`C:\Intel\ivecuqmanpnirkt615`


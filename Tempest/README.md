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
`2022-30190`

### Initial Access - Stage 2 execution

### Initial Access - Malicious Document Traffic

### Discovery - Internal Reconnaissance

### Privilege Escalation - Exploiting Privileges

### Actions on Objective - Fully-owned Machine


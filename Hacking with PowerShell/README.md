# Hacking with PowerShell

### What is Powershell?
- What is the command to get a new object? `Get-New`

### Basic Powershell Commands
- What is the location of the file "interesting-file.txt"? <br />
The command that worked for me is: `Get-ChildItem "*interesting-file*"  -Path C:\ -Recurse`. which is somewhat the equivalent of `find / -name *interesting-file*`. <br />
![image](https://github.com/user-attachments/assets/d0d1e8bc-0cbe-4870-8e50-73a1d4db056e)<br />
`C:\Program Files`
- Specify the contents of this file<br />
![image](https://github.com/user-attachments/assets/84adbac7-b01f-43f0-aa3d-a59ac166b880)<br />
`notsointerestingcontent`
- How many cmdlets are installed on the system(only cmdlets, not functions and aliases)?

       Get-Command | Where-Object -Property CommandType -eq Cmdlet | Measure-Object
  `6638`
- Get the MD5 hash of interesting-file.txt<br />
![image](https://github.com/user-attachments/assets/305c6823-d61b-44f0-99c8-893d786f23ac)<br />
`49A586A2A9456226F8A1B4CEC6FAB329`
- What is the command to get the current working directory? `Get-Location`
- Does the path "C:\Users\Administrator\Documents\Passwords" Exist (Y/N)?<br />
![image](https://github.com/user-attachments/assets/45a5f30f-18a1-4718-9d96-b78dc880a1a6)<br />
`N`
- What command would you use to make a request to a web server?<br />
![image](https://github.com/user-attachments/assets/a62f8e7b-1d55-4881-acf0-f6dbab56c1c8)<br />
`Invoke-WebRequest`
- Base64 decode the file b64.txt on Windows. <br />
You can use any online tool you like: <br />
![image](https://github.com/user-attachments/assets/e5a7bd8f-1057-4423-b4b7-363aa7f961a9)<br />
`ihopeyoudidthisonwindows` I didn't do this on windows D:


### Enumeration
- How many users are there on the machine?<br />
![image](https://github.com/user-attachments/assets/07e2ab1a-fdb1-4b51-957b-25dd2554b6f1)<br />
`5`
- Which local user does this SID(S-1-5-21-1394777289-3961777894-1791813945-501) belong to?<br />
![image](https://github.com/user-attachments/assets/a11f7b09-2f54-4586-844e-dcbaaec532f9)<br />
`Guest`
- How many users have their password required values set to False?<br />
I personally had some troubles here, I just used `Get-LocalUser | Select-Object *` and counted manually: `4`
- How many local groups exist?<br />
![image](https://github.com/user-attachments/assets/3f0225c4-8e1c-4b30-b448-1b647f7376dc)<br />
`24`
- What command did you use to get the IP address info? `Get-NetIPAddress`
- How many ports are listed as listening?<br />
The command that worked for me is ` Get-NetTCPConnection | Where-Object -Property State -eq Listen | Measure-Object`: `20`
- What is the remote address of the local port listening on port 445? `::`
- How many patches have been applied?<br />
I used `(Get-HotFix).Count`: `20`
- When was the patch with ID KB4023834 installed?<br />
![image](https://github.com/user-attachments/assets/df4e263e-9b6a-40cd-9dad-51a2a0f773ce)<br />
`6/15/2017 12:00:00 AM`
- Find the contents of a backup file.<br />
![image](https://github.com/user-attachments/assets/734988f1-7821-449d-8716-e077f43ef422)<br />
`backpassflag`
- Search for all files containing API_KEY<br />
![image](https://github.com/user-attachments/assets/58f6530b-c46e-4ea1-ba8a-54214a3113dd)<br />
`fakekey123`
- What command do you do to list all the running processes? `Get-Process`
- What is the path of the scheduled task called new-sched-task? `/` (Don't ask me why)
- Who is the owner of the C:\?<br />
![image](https://github.com/user-attachments/assets/99f7fd6e-b0d7-453b-93e4-1c4fcf0e0e8b)<br />
`NT SERVICE\TrustedInstaller`

### Basic Scripting Challenge
- What file contains the password? <br />
I'm sorry, I'm not going to write powershell scripts. <br />
![image](https://github.com/user-attachments/assets/9668219f-e33a-4ea4-9a57-5c187cd6b0f0)<br />
`Doc3M`
- What is the password? `johnisalegend99`
- What files contains an HTTPS link?<br />
![image](https://github.com/user-attachments/assets/ce5600c0-6231-44af-8d8d-8c0a7f77cb10)<br />
`Doc2Mary`

### Intermediate Scripting
- How many open ports did you find between 130 and 140(inclusive of those two)? `11`

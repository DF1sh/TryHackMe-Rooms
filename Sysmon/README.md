# Sysmon

### Cutting out the Noise
- How many event ID 3 events are in C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Filtering.evtx?<br />
Run the following command: `(Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Filtering.evtx -FilterXPath '*/System/EventID=3').Count`: <br />
![image](https://github.com/user-attachments/assets/c8ef9e43-7bed-4cd8-981a-1563406cbba7)<br />
`73,591`
- What is the UTC time created of the first network event in C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Filtering.evtx? `2021-01-06 01:35:50.464`

### Practical Investigations
- What is the full registry key of the USB device calling svchost.exe in Investigation 1?  <br />
Run `Get-WinEvent -Path .\\Investigation-1.evtx -FilterXPath ‘*/System/EventID=12 or */System/EventID=13 or */System/EventID=14’ -Oldest | Select-Object -Property *`: <br />
![image](https://github.com/user-attachments/assets/b7050336-750d-43fa-a8e7-42069d2e78cb)<br />
Run `HKLM\System\CurrentControlSet\Enum\WpdBusEnumRoot\UMB\2&37c186b&0&STORAGE#VOLUME#_??_USBSTOR#DISK&VEN_SANDISK&PROD_U3_CRUZER_MICRO&REV_8.01#4054910EF19005B3&0#\FriendlyName`
- What is the device name when being called by RawAccessRead in Investigation 1? <br />
![image](https://github.com/user-attachments/assets/8e0089e0-f86b-47c8-8e53-fe3b35ca64d1)<br />
`\Device\HarddiskVolume3`
- What is the first exe the process executes in Investigation 1? `rundll32.exe`
- What is the full path of the payload in Investigation 2? <br />
![image](https://github.com/user-attachments/assets/4204d125-3943-437a-bad5-17b9a345e796)<br />
`C:\Users\IEUser\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5\S97WTYG7\update.hta`<br />
- What is the full path of the file the payload masked itself as in Investigation 2? `C:\Users\IEUser\Downloads\update.html`
- What signed binary executed the payload in Investigation 2?<br />
![image](https://github.com/user-attachments/assets/8e56b812-c710-428e-bedc-912dfb58e89f)<br />
`C:\Users\IEUser\Downloads\update.html`
- What is the IP of the adversary in Investigation 2? <br />
![image](https://github.com/user-attachments/assets/cfd233a8-b486-4730-beb1-cac6b2c742f6)<br />
`10.0.2.18`
- What back connect port is used in Investigation 2? `4443`
- What is the IP of the suspected adversary in Investigation 3.1? <br />
Select the last network connection event: <br />
![image](https://github.com/user-attachments/assets/60981e4b-dc72-4bdf-a8ae-ece71838d769)<br />
`172.30.1.253`
- What is the hostname of the affected endpoint in Investigation 3.1? `DESKTOP-O153T4R` 
- What is the hostname of the C2 server connecting to the endpoint in Investigation 3.1? `empirec2`
- Where in the registry was the payload stored in Investigation 3.1? `HKLM\SOFTWARE\Microsoft\Network\debug`
- What PowerShell launch code was used to launch the payload in Investigation 3.1?<br />
![image](https://github.com/user-attachments/assets/f6f2a3e3-f530-448c-ad86-9c9f282a502b)<br />
`"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -c "$x=$((gp HKLM:Software\Microsoft\Network debug).debug);start -Win Hidden -A \"-enc $x\" powershell";exit;`
- What is the IP of the adversary in Investigation 3.2? <br />
Filter for network connections (ID = 3) to find the answer: <br />
![image](https://github.com/user-attachments/assets/69a20710-d7cc-45cd-9c5f-8dd2c0e7f98c)<br />
`172.168.103.167`
- What is the full path of the payload location in Investigation 3.2?<br />
![image](https://github.com/user-attachments/assets/a8cccc48-32d3-4ea4-b857-f707c2d0cf13)<br /> 
`c:\users\q\AppData:blah.txt`
- What was the full command used to create the scheduled task in Investigation 3.2? `"C:\WINDOWS\system32\schtasks.exe" /Create /F /SC DAILY /ST 09:00 /TN Updater /TR "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NonI -W hidden -c \"IEX ([Text.Encoding]::UNICODE.GetString([Convert]::FromBase64String($(cmd /c ''more < c:\users\q\AppData:blah.txt'''))))\""`
- What process was accessed by schtasks.exe that would be considered suspicious behavior in Investigation 3.2? `lsass.exe`
- What is the IP of the adversary in Investigation 4? <br />
![image](https://github.com/user-attachments/assets/7ede9c0c-df78-4ef0-985d-31af9c048904)<br />
`172.30.1.253`
- What port is the adversary operating on in Investigation 4? `80`
- What C2 is the adversary utilizing in Investigation 4? `empire`

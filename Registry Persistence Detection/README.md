### Registry Persistence Detection

### Intro to Malware Persistence Mechanisms
- What is the value "Name" of the suspicious registry entry that runs during startup? Include the parenthesis.<br />
![image](https://github.com/user-attachments/assets/51852bac-40d4-4443-a2d1-0bb193d35a97)<br />
`(default)`
- What is the value "Data" of the suspicious registry entry that runs during startup? `C:\Users\Administrator\AppData\Local\bd84\24d9.bat`
- What string is displayed on the console when the suspicious file runs?<br />
![image](https://github.com/user-attachments/assets/1656a9bc-3b1f-411b-a113-86cc08b36f62)<br />
`pleaseletmepersist`

### Intro to the AutoRuns PowerShell Module
- What AutoRun function is used for getting and displaying the auto-run entries? `Get-PSAutorun`
- What AutoRun function is used for creating a baseline file from Autoruns artifact(s)? `New-AutoRunsBaseLine`
- What AutoRun function is used for comparing two baseline files of Autoruns artifact(s)? `Compare-AutoRunsBaseLine`

### Filtering AutoRuns Entries
- What parameter switch is used for filtering for artifacts related to boot execution of images?  `BootExecute`
- How many entries are outputted using the parameter switch from the previous question?<br />
![image](https://github.com/user-attachments/assets/1ffcc235-f927-47e6-8434-09225cfeec18)<br />
`1`
- What parameter switch is used for filtering for artifacts related to printer driver and status monitors? `PrintMonitorDLLs`
- How many entries are listed in the output using the parameter switch from the previous question?<br />
![image](https://github.com/user-attachments/assets/ff81af7e-7d2f-4546-bbc5-47d5953900d4)<br />
`5`
- What parameter is used to add a new column to show whether a file is digitally signed? `VerifyDigitalSignature`
- Searching all categories, how many entries have the "Signed" column set to "false"?<br />
![image](https://github.com/user-attachments/assets/1adc196f-dc34-4b50-a1fa-feeb088c9b5d)<br />
`3`


### Comparing to a Baseline
Perform the steps provided in the task:
- There is another suspicious logon Registry entry. What is the full path of this key?<br />
![image](https://github.com/user-attachments/assets/189e108d-9750-486d-b0ea-3d664c7a2152)<br />
`HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`
- What is the value item name of the suspicious Registry entry from question #1?<br /> `Userinit`
- What is the value data of the suspicious Registry entry from question #1?<br /> `C:\Windows\system32\userinit.exe,C:\Users\Administrator\AppData\Local\THM\789a.bat`
- What is the category that AutoRuns assigned to the entry from question #1?<br /> `Logon`
- What string is displayed on the console when the suspicious file ran?<br />
![image](https://github.com/user-attachments/assets/c40d5fce-27c9-48b2-b1fc-42e541719682)<br />
`letmestaymyfriend`

# Windows Event Logs

### Event Viewer
For the questions below, use Event Viewer to analyze Microsoft-Windows-PowerShell/Operational log. 
- What is the Event ID for the earliest recorded event?<br />
Open the Event Viewer at `Microsoft-Windows-PowerShell/Operational`. <br />
From the overview panel(the middle panel) scroll down to the last event logged:<br />
![image](https://github.com/user-attachments/assets/6d0231ab-842e-4fb7-8524-28e65b84c7d2)<br />
`40961`
- Filter on Event ID 4104. What was the 2nd command executed in the PowerShell session? <br />
From the action panel(the panel on the right), select "Filter Current Log", and filter by ID=4104. Now as before, scoll down to the penultimate log: <br />
![image](https://github.com/user-attachments/assets/112ae2a0-7c1c-467d-917b-ef9fabc8ed82)<br />
`whoami`
- What is the Task Category for Event ID 4104?<br />
![image](https://github.com/user-attachments/assets/eb5e7b0f-bf9e-49e6-9297-4538cd403486)<br />
`Execute a Remote Command`
- Analyze the Windows PowerShell log. What is the Task Category for Event ID 800? <br />
To analyze the windows powershell logs, on the left panel click on "Windows Powershell": <br />
![image](https://github.com/user-attachments/assets/d9833a51-d30c-43cf-a869-fd0d50df419d)<br />
Now filter by ID=800:<br />
![image](https://github.com/user-attachments/assets/dcde41bd-3130-471e-8200-273532c64859)<br />
`Pipeline Execution Details`

### wevtutil.exe
- How many log names are in the machine? <br />
Open powershell and run ` wevtutil.exe el | Measure-Object -Line`: <br />
![image](https://github.com/user-attachments/assets/36487e6b-50b6-47d4-9f74-67d093fe1948)<br />
`1071`
- What event files would be read when using the query-events command? <br />
![image](https://github.com/user-attachments/assets/6b0b101f-481f-4a4f-921c-41cef4838146)<br />
`event log, log file, structured query`
- What option would you use to provide a path to a log file?<br />
Run `wevtutil qe /?` to get the answer:<br />
![image](https://github.com/user-attachments/assets/f2ed45e0-14d0-429b-92be-206a53078937)<br />
`/lf:true`

- What is the VALUE for /q?<br />
![image](https://github.com/user-attachments/assets/51690462-20d4-4aec-9607-cdb36b77e284)<br />
`Xpath query`<br />
The questions below are based on this command: `wevtutil qe Application /c:3 /rd:true /f:text`
- What is the log name?<br />
Run the command to get the answer: `Application`
- What is the /rd option for? <br />
![image](https://github.com/user-attachments/assets/30d2f82a-52e8-4452-992b-bc52e0200ed9)<br />
`Event read direction`
- What is the /c option for?<br />
![image](https://github.com/user-attachments/assets/13d5a107-7af9-44a2-8554-0fd70e92b6b6)<br />
`Maximum number of events to read`

### Get-WinEvent
- Execute the command from Example 1 (as is). What are the names of the logs related to OpenSSH?<br />
Run `Get-WinEvent -ListLog *`:<br />
![image](https://github.com/user-attachments/assets/1898fa66-403e-409a-8797-4b0188f2986d)<br />
`OpenSSH/Admin,OpenSSH/Operational`
- Execute the command from Example 8. Instead of the string *Policy* search for *PowerShell*. What is the name of the 3rd log provider?<br />
Run `Get-WinEvent -ListProvider *PowerShell*`: <br />
![image](https://github.com/user-attachments/assets/3a5aea2e-b3db-4699-addf-c74785991a87)<br />
`Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager`
- Execute the command from Example 9. Use Microsoft-Windows-PowerShell as the log provider. How many event ids are displayed for this event provider?<br />
Run `(Get-WinEvent -ListProvider Microsoft-Windows-PowerShell).Events | Format-Table Id, Description | Measure-Object` to get the answer: `192`
- How do you specify the number of events to display?<br />
Found the answer [here](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-7.4&viewFallbackFrom=powershell-7.1):<br />
![image](https://github.com/user-attachments/assets/16c70afa-3a75-4bb6-be17-3f8ebbfda3ce)<br />
`-MaxEvents`
- When using the FilterHashtable parameter and filtering by level, what is the value for Informational?<br />
![image](https://github.com/user-attachments/assets/ccf43790-5fd5-41f1-9022-825c89f7b82e)<br />
`4`


### XPath Queries
- Using the knowledge gained on Get-WinEvent and XPath, what is the query to find WLMS events with a System Time of 2020-12-15T01:09:08.940277500Z?<br />
The command is `Get-WinEvent -LogName Application -FilterXPath '*/System/Provider[@Name="WLMS"] and */System/TimeCreated[@SystemTime="2020-12-15T01:09:08.940277500Z"]'`
- Using Get-WinEvent and XPath, what is the query to find a user named Sam with an Logon Event ID of 4720?<br />
The command is `Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="Sam" and */System/EventID=4720'`
- Based on the previous query, how many results are returned?<br />
![image](https://github.com/user-attachments/assets/61f2a630-d5d3-4499-bd8f-c7db31bc292a)<br />
`2`
- Based on the output from the question #2, what is Message? `A user account was created`
- Still working with Sam as the user, what time was Event ID 4724 recorded? (MM/DD/YYYY H:MM:SS [AM/PM]) `12/17/2020 1:57:14 PM`
- What is the Provider Name? `Microsoft-Windows-Security-Auditing`

### Putting theory into practice
- What event ID is to detect a PowerShell downgrade attack?<br />
Google to find the answer: `400`
- What is the Date and Time this attack took place? (MM/DD/YYYY H:MM:SS [AM/PM]) `12/18/2020 7:50:33 AM`
- A Log clear event was recorded. What is the 'Event Record ID'? `27736`
- What is the name of the computer? `PC01.example.corp`
- What is the name of the first variable within the PowerShell command? `$Va5w3n8`
- What is the Date and Time this attack took place? (MM/DD/YYYY H:MM:SS [AM/PM]) `8/25/2020 10:09:28 PM`
- What is the Execution Process ID? `6620`
- What is the Group Security ID of the group she enumerated? `S-1-5-32-544`
- What is the event ID? `4799`

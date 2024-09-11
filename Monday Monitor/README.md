# Monday Monitor

### Navigate Through the Endpoint Logs
- Initial access was established using a downloaded file. What is the file name saved on the host?<br />
Remember: The tests were run on Apr 29, 2024, between 12:00:00 and 20:00:00. So we first need to filter the logs by this date and time: <br />
![image](https://github.com/user-attachments/assets/99a8c48d-12ad-4fbd-a5f9-cb43179901e0)<br />
Now filter for 'localhost': <br />
![image](https://github.com/user-attachments/assets/40715cc4-d7ae-4756-bfd8-22b68db4faab)<br />
`SwiftSpend_Financial_Expenses.xlsm`
- What is the full command run to create a scheduled task? <br />
For this to work, just search for "scheduler" and filter the results by `data.win.eventdata.parentCommandLine`, (since the scheduled task is created by a parent process) to find the answer: <br />
![image](https://github.com/user-attachments/assets/2a2265da-f3fa-4b0c-84eb-494f1b1301bc)<br />
`\"cmd.exe\" /c \"reg add HKCU\\SOFTWARE\\ATOMIC-T1053.005 /v test /t REG_SZ /d cGluZyB3d3cueW91YXJldnVsbmVyYWJsZS50aG0= /f & schtasks.exe /Create /F /TN \"ATOMIC-T1053.005\" /TR \"cmd /c start /min \\\"\\\" powershell.exe -Command IEX([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String((Get-ItemProperty -Path HKCU:\\\\SOFTWARE\\\\ATOMIC-T1053.005).test)))\" /sc daily /st 12:34\"`
- What time is the scheduled task meant to run? `12:34`
- What was encoded?<br />
Take the encoded text in the command and decode it: <br />
![image](https://github.com/user-attachments/assets/f701591d-0210-42ce-8a20-f77888b6e57a)<br />
`ping www.youarevulnerable.thm`
- What password was set for the new user account? `I_AM_M0NIT0R1NG`
- What is the name of the .exe that was used to dump credentials? `memotech.exe`
- Data was exfiltrated from the host. What was the flag that was part of the data? `THM{M0N1T0R_1$_1N_3FF3CT}`

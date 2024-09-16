# Investigating with Splunk

### Investigating with Splunk
- How many events were collected and Ingested in the index main?<br />
The filter is `index=main`:<br />
![image](https://github.com/user-attachments/assets/12e41d13-c11a-4a99-8eac-248eb74224e6)<br />
`12256`
- On one of the infected hosts, the adversary was successful in creating a backdoor user. What is the new username?<br />
After some reaserch, I found [here](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4720) that the event of user creation has ID=4720.<br />
So the filter I used is: `index=main EventID="4720"`<br />
![image](https://github.com/user-attachments/assets/a6632311-df7c-4394-b9c5-5a5cf3e5b46e)<br />
`A1berto`
- On the same host, a registry key was also updated regarding the new backdoor user. What is the full path of that registry key?<br />
The filter I used is `index=main *A1berto* `. Then click on category and select the category describing a registry value being set.<br />
![image](https://github.com/user-attachments/assets/a381cf30-22ca-46d4-b766-6ec41dac5b3b)<br />
`HKLM\SAM\SAM\Domains\Account\Users\Names\A1berto`
- Examine the logs and identify the user that the adversary was trying to impersonate.<br />
`Alberto` lol
- What is the command used to add a backdoor user from a remote computer?<br />
![image](https://github.com/user-attachments/assets/f47cb94a-8550-4b39-9739-ea7c38dbcd89)<br />
`C:\windows\System32\Wbem\WMIC.exe" /node:WORKSTATION6 process call create "net user /add A1berto paw0rd1`
- How many times was the login attempt from the backdoor user observed during the investigation?<br />
There are no logon events from the user A1berto: `0`
- What is the name of the infected host on which suspicious Powershell commands were executed?<br />
The filter that got me the answer is `index=main powershell`
`James.browne`
- PowerShell logging is enabled on this device. How many events were logged for the malicious PowerShell execution?<br />
![image](https://github.com/user-attachments/assets/754dcd1f-a987-4956-9fbb-84934f2874ee)<br />
`79`
-  An encoded Powershell script from the infected host initiated a web request. What is the full URL?<br />
The last filter is enough to get the encoded string. Apparently the code was not only base64 encoded, but it also has a different unicode format.<br />
![image](https://github.com/user-attachments/assets/5169c0a0-4ebf-42e8-8018-7e7a6dc4a4c8)<br />
`hxxp[://]10[.]10[.]10[.]5/news[.]php`

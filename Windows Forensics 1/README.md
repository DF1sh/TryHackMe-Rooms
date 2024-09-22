# Windows Forensics 1

### Introduction to Windows Forensics
- What is the most used Desktop Operating System right now? `Microsoft Windows`

### Windows Registry and Forensics
- What is the short form for HKEY_LOCAL_MACHINE? `HKLM`

### Accessing registry hives offline
- What is the path for the five main registry hives, DEFAULT, SAM, SECURITY, SOFTWARE, and SYSTEM? `C:\Windows\System32\Config`
- What is the path for the AmCache hive? `C:\Windows\AppCompat\Programs\Amcache.hve`

### System Information and System Accounts
- What is the Current Build Number of the machine whose data is being investigated?<br />
![image](https://github.com/user-attachments/assets/289ed649-be32-47ff-9fdd-1641c702d277)<br />
`19044`
- Which ControlSet contains the last known good configuration?<br />
![image](https://github.com/user-attachments/assets/4fff8acf-f8e3-44a8-b6ed-f3bbc54d994f)<br />
`1`
- What is the Computer Name of the computer?<br />
![image](https://github.com/user-attachments/assets/56d83a5f-fa8c-4305-862b-71adb5911ab0)<br />
`THM-4n6`
- What is the value of the TimeZoneKeyName? <br />
![image](https://github.com/user-attachments/assets/4ce5a2ed-fb3f-4156-af49-05d440dcad8f)<br />
`Pakistan Standard Time`
- What is the DHCP IP address<br />
![image](https://github.com/user-attachments/assets/743efe8f-330a-404c-83f5-6012b8dd5683)<br />
`192.168.100.58`
- What is the RID of the Guest User account?<br />
![image](https://github.com/user-attachments/assets/166183e0-6c23-45e4-8c82-6cfaf2372dff)<br />
`501`

### Usage or knowledge of files/folders
- When was EZtools opened? <br />
![image](https://github.com/user-attachments/assets/a72459ba-1c9d-44b3-a938-f0411555f4bb)<br />
`2021-12-01 13:00:34`
- At what time was My Computer last interacted with? <br />
![image](https://github.com/user-attachments/assets/6394f621-07c9-4d12-9863-737278a8a80f)<br />
`2021-12-01 13:06:47`
- What is the Absolute Path of the file opened using notepad.exe?<br />
![image](https://github.com/user-attachments/assets/51fbf9d7-7e66-4abf-99d2-33333ef995c1)<br />
`C:\Program Files\Amazon\Ec2ConfigService\Settings`
- When was this file opened?<br /> `2021-11-30 10:56:19`

### Evidence of Execution
- How many times was the File Explorer launched? `26`
- What is another name for ShimCache? `AppCompatCache`
- Which of the artifacts also saves SHA1 hashes of the executed programs? `AmCache`
- Which of the artifacts saves the full path of the executed programs? `BAM/DAM`

### External Devices/USB device forensics
- What is the serial number of the device from the manufacturer 'Kingston'? `1C6f654E59A3B0C179D366AE&0`
- What is the name of this device? `Kingston Data Traveler 2.0 USB Device`
- What is the friendly name of the device from the manufacturer 'Kingston'? `USB`

### Hands-on Challenge
First of all we want to access the registry files. To do that, open the Registry Explorer application provided in the machine. Then click on files -> load hive, and select triage -> C -> Windows -> System 32 -> config to access the registry files. <br />
Load the following files(one at a time): <br />
![image](https://github.com/user-attachments/assets/8baf5409-0626-4f42-bf4b-2ad1739d0e95)<br />
A warning should pop up about sequence numbers not matching. Do not worry. Just press Yes. Next, it says select transaction logs. For the DEFAULT hive, select both DEFAULT.LOG1 and DEFAULT.LOG2 files. To select more than one file, you can click on the first file, then hold CTRL and click on the second file. You should get a pop up saying to select a location for our new and updated hive. I just saved it at the default location, which should be our Desktop. Also load NTUSER.DAT at triage -> C -> Users -> THM-4n6 -> NTUSER.DAT. In the end you should end up with something like this: <br />
![image](https://github.com/user-attachments/assets/e959564c-bc1e-4d61-b3df-f57e8fcc20e1)<br />
- How many user created accounts are present on the system?<br />
Check the SAM: <br />
![image](https://github.com/user-attachments/assets/a9fc67df-227d-44ca-9f52-930ac144ec17)<br />
Users with RID 50X are system accounts, users with RID 10XX are user accounts, therefore the answer is `3`
- What is the username of the account that has never been logged in?<br /> 
We can see that one of these users never logged in: <br />
![image](https://github.com/user-attachments/assets/7939ddb1-85be-41bd-94f8-b458f535cbb2)<br />
`thm-user2`
- What's the password hint for the user THM-4n6? Check the picture above: `count`
- When was the file 'Changelog.txt' accessed? <br />
Recently accessed files can be found at `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`: <br />
![image](https://github.com/user-attachments/assets/bd096424-dc9f-4c8a-b880-b9bb49d1f13e)<br /
`2021-11-21 18:18:48`
- What is the complete path from where the python 3.8.2 installer was run?<br />
Evidence of execution can be found at `NTUSER.DAT\Software\Microsoft\Windows\Currentversion\Explorer\UserAssist\{GUID}\Count`. I found the answer by looking at every GUID, luckily there weren't too many: <br />
![image](https://github.com/user-attachments/assets/f521cf77-c9ec-43b9-a97d-d6729724891c)<br />
`Z:\setups\python-3.8.2.exe`
- When was the USB device with the friendly name 'USB' last connected?<br />
Under `SOFTWARE\Microsoft\Windows Portable Devices\Devices` there's a device with friendly name "USB". I took not of the Disk-ID of that device: <br />
![image](https://github.com/user-attachments/assets/7f9a822f-d385-49c7-8f18-a12e1d879bff)<br />
Then I moved on `SYSTEM\CurrentControlSet\Enum\USBSTOR` and found the data I needed: <br />
![image](https://github.com/user-attachments/assets/e326dd09-77d6-4c1b-8b9d-d514bb4c60d9)<br />
`2021-11-24 18:40:06`

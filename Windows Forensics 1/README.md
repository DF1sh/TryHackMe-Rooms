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
- How many times was the File Explorer launched?
- What is another name for ShimCache?
- Which of the artifacts also saves SHA1 hashes of the executed programs?
- Which of the artifacts saves the full path of the executed programs?

### External Devices/USB device forensics
- What is the serial number of the device from the manufacturer 'Kingston'?
- What is the name of this device?
- What is the friendly name of the device from the manufacturer 'Kingston'?

### Hands-on Challenge
- How many user created accounts are present on the system? 
- What is the username of the account that has never been logged in?
- What's the password hint for the user THM-4n6?
- When was the file 'Changelog.txt' accessed?
- What is the complete path from where the python 3.8.2 installer was run?
- When was the USB device with the friendly name 'USB' last connected?

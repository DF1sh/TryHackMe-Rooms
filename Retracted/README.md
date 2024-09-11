# Retracted

### The Message
- What is the full path of the text file containing the "message"?<br />
![image](https://github.com/user-attachments/assets/bb468989-e6a8-44d8-9977-50a7044aa18b)<br />
`C:\Users\Sophie\Desktop\SOPHIE.txt`
- What program was used to create the text file?<br />
Let's use sysmon to find out. Open the event viewer and go to Application and services-->Microsoft-->Windows-->Sysmon-->Operational. Now filter for ID=1 (File creation) and search for "SOPHIE.txt" using the 'find' option on the right:<br />
![image](https://github.com/user-attachments/assets/2e8c751c-514b-4941-a92f-e793cdc90d4d)<br />
![image](https://github.com/user-attachments/assets/031046dd-43a8-4b13-b582-7f94a8cfbf8a)<br />
`notepad.exe`

- What is the time of execution of the process that created the text file? Timezone UTC (Format YYYY-MM-DD hh:mm:ss) `2024-01-08 14:25:30`

### Something Wrong
- What is the filename of this "installer"? (Including the file extension)
Filter for ID=3 (Network connections). All the connections we find are using the RDP protocol, except one: <br />
![image](https://github.com/user-attachments/assets/39d1cec9-cc27-48d4-bd5e-f7760848a859)<br />
`antivirus.exe`. Another way was to look inside the dowload section of microsoft edge. 
- What is the download location of this installer? `C:\Users\Sophie\download\`
- The installer encrypts files and then adds a file extension to the end of the file name. What is this file extension?<br />
Search for "antivirus.exe" from the event viewer, and scroll until you find the answer: <br />
![image](https://github.com/user-attachments/assets/3a4de876-f284-49d1-80f9-2ece7529ed55)<br />
`.dmp`
- The installer reached out to an IP. What is this IP?<br />
Again, filtering by "antivirus.exe", we find an event with ID=3, a network connection. If we inspect it we can find the destination IP address: <br />
![image](https://github.com/user-attachments/assets/55e49b9a-e6d5-4a20-b032-7e136312fb0a)<br />
`10.10.8.111`

### Back to Normal
- The threat actor logged in via RDP right after the “installer” was downloaded. What is the source IP?
- This other person downloaded a file and ran it. When was this file run? Timezone UTC (Format YYYY-MM-DD hh:mm:ss)

### Doesn't Make Sense
- Sophie ran out and reached out to you for help.
- Sophie downloaded the malware and ran it.
- A note was created on the desktop telling Sophie to check her Bitcoin.
- The intruder downloaded a decryptor and decrypted all the files.
- The malware encrypted the files on the computer and showed a ransomware note.
- Someone else logged into Sophie's machine via RDP and started looking around.
- We arrive on the scene to investigate.

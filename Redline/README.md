# Redline

### Introduction
- Who created Redline? `FireEye `

### Data Collection
- What data collection method takes the least amount of time? `Standard Collector`
- You are reading a research paper on a new strain of ransomware. You want to run the data collection on your computer based on the patterns provided, such as domains, hashes, IP addresses, filenames, etc. What method would you choose to run a granular data collection against the known indicators? `IOC Search Collector`
- What script would you run to initiate the data collection process? Please include the file extension. `RunRedlineAudit.bat`
- If you want to collect the data on Disks and Volumes, under which option can you find it?<br />
![image](https://github.com/user-attachments/assets/e00e77ff-0ee0-4160-96e6-ae2f6967cdc5)<br />
`Disk Enumeration`
- What cache does Windows use to maintain a preference for recently executed code? <br />
Found the answer in the Redline user guide :<br />
![image](https://github.com/user-attachments/assets/98bd0bf6-3d72-45fd-9237-1c795bcce8ae)<br />
`Prefetch`

### The Redline Interface
- Where in the Redline UI can you view information about the Logged in User? `System Information`

### Standard Collector Analysis
- Provide the Operating System detected for the workstation.
- What is the suspicious scheduled task that got created on the victim's computer?
- Find the message that the intruder left for you in the task.
- There is a new System Event ID created by an intruder with the source name "THM-Redline-User" and the Type "ERROR". Find the Event ID #.
- Provide the message for the Event ID.
- It looks like the intruder downloaded a file containing the flag for Question 8. Provide the full URL of the website.
- Provide the full path to where the file was downloaded to including the filename.
- Provide the message the intruder left for you in the file.

### IOC Search Collector
- What is the actual filename of the Keylogger?
- What filename is the file masquerading as?
- Who is the owner of the file?
- What is the file size in bytes?
- Provide the full path of where the .ioc file was placed after the Redline analysis, include the .ioc filename as well

### IOC Search Collector Analysis
- Provide the path of the file that matched all the artifacts along with the filename.
- Provide the path where the file is located without including the filename.
- Who is the owner of the file?
- Provide the subsystem for the file.
- Provide the Device Path where the file is located.
- Provide the hash (SHA-256) for the file.
- The attacker managed to masquerade the real filename. Can you find it having the hash in your arsenal?

### Endpoint Investigation
- Can you identify the product name of the machine?
- Can you find the name of the note left on the Desktop for the "Charles"?
- Find the Windows Defender service; what is the name of its service DLL?
- The user manually downloaded a zip file from the web. Can you find the filename?
- Provide the filename of the malicious executable that got dropped on the user's Desktop.
- Provide the MD5 hash for the dropped malicious executable.
- What is the name of the ransomware? 

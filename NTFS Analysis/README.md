# NTFS Analysis

### NTFS Overview
- Which feature does NTFS use to keep track of the changes within the file system? `journaling`

### NTFS Components
- Double-click on the $UsnJrnl file in the $Extend folder; what is the first evidence file you find?<br />
![image](https://github.com/user-attachments/assets/f6a1a9a1-14d0-4ab7-8eca-5acf6c425820)<br />
`$J`

### MFT Record Analysis
![image](https://github.com/user-attachments/assets/66dc59ec-3d59-4090-9e00-728673d59e1c)<br />
- Which column indicates that the file is no longer present on the disk? `In Use`
- Examine the MFT record; what is the network sniffer installed on this system in the \Program Files\ directory?<br />
![image](https://github.com/user-attachments/assets/c7deb98f-8be2-4ad1-a686-3bdc6136a74a)<br />
I filtered for `Program Files exe` and found `wireshark`.
- An anti-forensics tool responsible for wiping out an attacker’s traces was installed in the \Downloads\Tools folder. What is the name of the tool?<br />
![image](https://github.com/user-attachments/assets/1b3550e4-4ead-4dc9-a149-d2f748c0a1cd)<br />
`DiskWipe.exe`
- According to the MFT record, is the anti-forensics tool currently present on the disk? (yay or nay) `nay`
- Examining the MFT record, it seems there is a record of a flag.txt file. What is the parent path of the file?<br />
I was only able to find it using FTK imager:<br />
![image](https://github.com/user-attachments/assets/9e6b0abc-799c-42d8-8d89-965275ee8da5)<br />
`.\tmp\secret_directory`
- What is the content of the flag.txt file? `WelDone_You_F0und_M3`
- What is the file name associated with the MFT entry number "584574"?<br />
Just search for `584574` and you'll get this:<br />
![image](https://github.com/user-attachments/assets/d4dc7715-2609-4899-8a9f-b3744d20ff90)<br />
`SharpHound.ps1`

### NTFS Journaling
![image](https://github.com/user-attachments/assets/4ea1b085-580b-4c7e-a2e2-5eb08ef66168)<br />
- What is the text file name associated with entry number 95071 before renaming it?<br />
Filter for `95071` and find the rename event:<br />
![image](https://github.com/user-attachments/assets/93607383-91a8-4bd2-818c-8f9f3937b15e)<br />
`New Text Document.txt`
- According to the record, what is the first operation performed on the file in the question above? `FileCreate`
- According to the record in $J, what is the count of the rename operation found against secret_code.txt?<br />
Just search for `secret_code.txt` and find the parent sequence number: `2`
- According to the record, when was the secret_code.txt file deleted? <br />
Take the last log (deleted event) and get the timestamp (3rd field): `2025-01-15 08:10:04`

### Index Allocation Attribute ($I30) Overview
![image](https://github.com/user-attachments/assets/3ffa729c-3dc2-4df7-be6a-ddc75ef076ba)<br />
- How many deleted files or folders are present in the $I30 attribute file that was extracted in this task?<br />
`52`
- What is the parent MFT entry of the nmap directory?<br />
![image](https://github.com/user-attachments/assets/4cda6b2f-badd-48ff-8973-6d2f65ae7cc2)<br />
`512386`

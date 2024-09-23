# Windows Forensics 2

### The FAT file systems
- How many addressable bits are there in the FAT32 file system? `28 bits`
- What is the maximum file size supported by the FAT32 file system? `4GB`
- Which file system is used by digital cameras and SD cards? `exFAT`

### The NTFS File System
- Parse the $MFT file placed in C:\users\THM-4n6\Desktop\triage\C\ and analyze it. What is the Size of the file located at .\Windows\Security\logs\SceSetupLog.etl <br />
Move to `C:\Users\THM-4n6\Desktop\Eztools` and run the following command `MFTECmd.exe -f C:\users\THM-4n6\Desktop\triage\C\$MFT --csv C:\Users\THM-4n6\Desktop`. You should have something like this: <br />
![image](https://github.com/user-attachments/assets/48ad839c-7f47-445a-b620-5aeab0afa4db)<br />
To open the csv file, we are going to use EzViewer in the EzTools folder. Open EzViewer, click on "file" -> "open" and select the .csv file we've just parsed. You should have something like this: <br />
![image](https://github.com/user-attachments/assets/fabf246b-e1a5-4367-b2ad-6c1dcf9e657e)<br />
Now press CTRL+F and search for the file: <br />
![image](https://github.com/user-attachments/assets/f7093149-e82c-4b7e-aea1-cbe7022fafad)<br />
The answer is `49152`.
- What is the size of the cluster for the volume from which this triage was taken?<br />
Do the same thing for the $Boot file.<br />
![image](https://github.com/user-attachments/assets/491cc37a-6fe9-4e1c-92d5-b6de31d8d4dc)<br />
`4096`

### Recovering deleted files
- There is another xlsx file that was deleted. What is the full name of that file?<br />
Follow the steps provided in the task to open Autopsy: <br />
![image](https://github.com/user-attachments/assets/4e5d752d-a56b-48d1-b7e0-fe373e311242)<br />
`Tryhackme.xlsx`
- What is the name of the TXT file that was deleted from the disk? `TryHackMe2.txt`
- Recover the TXT file from Question #2. What was written in this txt file? <br />
Extract the file and open it: <br />
![image](https://github.com/user-attachments/assets/1dfb7c59-c4c5-4716-bc37-7e3c8bab4471)<br />
`THM-4n6-2-4`

### Evidence of Execution
- How many times was gkape.exe executed?<br />
Open cmd as administrator, move to the directory `C:\Users\THM-4n6\Desktop\EZtools`, and run the following command: `PECmd.exe -d C:\Users\THM-4n6\Desktop\triage\C\Windows\prefetch --csv C:\Users\THM-4n6\Desktop`. Now in the desktop you should have the following file: <br />
![image](https://github.com/user-attachments/assets/77eeb29b-db57-4516-b4e1-2e6563452e40)<br />
To open it, use the EzViewer tool inside the EzTools folder. Press CTRL+F and filter by `gkape.exe`<br />
![image](https://github.com/user-attachments/assets/956c244a-e5bd-4803-94ed-f6d33aeb1b58)<br />
The execution we are looking for is at line 64: <br />
![image](https://github.com/user-attachments/assets/fa7e6a12-9cfe-4c28-9299-76a16e1ed9c1)<br />
`2`
- What is the last execution time of gkape.exe `12/01/2021 13:04`
- When Notepad.exe was opened on 11/30/2021 at 10:56, how long did it remain in focus?<br />
Again, filter for `notepad.exe` to find the answer: <br />
![image](https://github.com/user-attachments/assets/388daf0f-bbe1-415b-869b-3ec4bd420e11)<br />
To see how long an executable was on focus, Windows 10 Timeline needs to be used. Run `WxTCmd.exe -f C:\Users\THM-4n6\Desktop\triage\C\Users\THM-4n6\AppData\Local\ConnectedDevicesPlatform\L.THM-4n6\ActivitiesCache.db --csv C:\Users\THM-4n6\Desktop`, open the .csv file and do the same as the previous tasks to find the answer: `00:00:41`
- What program was used to open C:\Users\THM-4n6\Desktop\KAPE\KAPE\ChangeLog.txt?<br />
Now we'll parse JumpList. Run `JLECmd.exe -d C:\Users\THM-4n6\Desktop\triage\C\Users\THM-4n6\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations — csv C:\Users\THM-4n6\Desktop` and get the answer: `Notepad.exe`

### File/folder knowledge
- When was the folder C:\Users\THM-4n6\Desktop\regripper last opened? <br />
Run `LECmd.exe -d C:\Users\THM-4n6\Desktop\triage\C\Users\THM-4n6\AppData\Roaming\Microsoft\Windows\Recent\ — csv C:\Users\THM-4n6\Desktop` to find the answer: <br />
`12/1/2021 13:01`
- When was the above-mentioned folder first opened? `12/1/2021 12:31`

### External Devices/USB device forensics
- Which artifact will tell us the first and last connection times of a removable drive? `Setupapi.dev.log`

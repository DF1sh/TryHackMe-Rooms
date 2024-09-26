# Disk Analysis & Autopsy

### Windows 10 Disk Image
- What is the MD5 hash of the E01 image?<br />
![image](https://github.com/user-attachments/assets/8281d6f8-3417-4364-884d-8662495f189e)<br />
`3f08c518adb3b5c1359849657a9b2079`
- What is the computer account name?<br />
![image](https://github.com/user-attachments/assets/f90b2535-6983-4a01-a86a-daef81f07bbd)<br />
`DESKTOP-0R59DJ3`
- List all the user accounts. (alphabetical order)<br />
Select `Operating System User Account` to find the answer: <br />
![image](https://github.com/user-attachments/assets/6ee4d06a-2a43-4429-8460-e6756089854f)<br />
`H4S4N,joshwa,keshav,sandhya,shreya,sivapriya,srini,suba`
- Who was the last user to log into the computer?<br />
Click on `Date Accessed` to order by accessed date: <br />
![image](https://github.com/user-attachments/assets/b2876879-4639-4ed5-a937-34b25c098587)<br />
`sivapriya`
- What was the IP address of the computer?<br />
There is no registry containing the IP address here, so one must get creative. Searching for "LAN", I found that there's a program called `Look@Lan`, which is a network monitoring tool. Checking it's folder inside `Program files (x86)` gave me the answer: <br />
![image](https://github.com/user-attachments/assets/a5dcae85-777e-4c84-b509-1a14a101da9e)<br />
  `192.168.130.216`
- What was the MAC address of the computer? (XX-XX-XX-XX-XX-XX)<br />
The answer can be found inside the same file<br />
![image](https://github.com/user-attachments/assets/9a390eec-f491-4fa6-99f0-89fae1acbb23)<br />
  `08-00-27-2c-c4-b9`
- What is the name of the network card on this computer?<br />
`Intel(R) PRO/1000 MT Desktop Adapter`
- What is the name of the network monitoring tool?<br /> `Look@LAN`
- A user bookmarked a Google Maps location. What are the coordinates of the location?<br />
![image](https://github.com/user-attachments/assets/4a828d22-2c82-453a-9c8f-5ffafe03c3e2)<br />
- A user has his full name printed on his desktop wallpaper. What is the user's full name?<br />`Anto Joshwa`
- A user had a file on her desktop. It had a flag but she changed the flag using PowerShell. What was the first flag?<br />
After a minute of manual search, the user containing the flag is shireya. We can check the powershell history to find the answer: <br />
![image](https://github.com/user-attachments/assets/855267b4-db99-4f29-9a6d-74e9cf602ebd)<br />
`flag{HarleyQuinnForQueen}`
- The same user found an exploit to escalate privileges on the computer. What was the message to the device owner?<br />
![image](https://github.com/user-attachments/assets/dba8cee3-50e9-4031-8687-b48b020e6941)<br />
`flag{I-hacked-you}`
- 2 hack tools focused on passwords were found in the system. What are the names of these tools? (alphabetical order)<br />
I found them under the "Run programs" section: <br />
![image](https://github.com/user-attachments/assets/e71ab156-36dc-4030-b8a0-d1e1d2606189)<br />
`Lazagne,Mimikatz`
- There is a YARA file on the computer. Inspect the file. What is the name of the author?<br />
From the menu on the top, selet "Tools" -> "Search by attribute", search by name = ".yar": <br />
![image](https://github.com/user-attachments/assets/537d1208-77ef-42c2-bde1-46e8a6fc4872)<br />
`Benjamin DELPY (gentilkiwi)`
- One of the users wanted to exploit a domain controller with an MS-NRPC based exploit. What is the filename of the archive that you found? (include the spaces in your answer) <br />
If we look up MS-NRPC exploits, there are many results for the exploit known as Zerologon, therefore try to search for "zerologon":<br />
![image](https://github.com/user-attachments/assets/87d2d584-447b-443c-a05d-6c2d8db7c4cd)<br />
`2.2.0 20200918 Zerologon encrypted.zip`

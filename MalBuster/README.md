# MalBuster

### Challenge Questions
- Based on the ARCHITECTURE of the binary, is malbuster_1 a 32-bit or a 64-bit application? (32-bit/64-bit)<br />
Open malbuster_1 using PEstudio:<br />
![image](https://github.com/user-attachments/assets/23afd562-e381-4dd2-87d3-368dd04a2b28)<br />
`32-bit`
- What is the MD5 hash of malbuster_1?<br />
Do the same thing as before: `4348DA65E4AEAE6472C7F97D6DD8AD8F`
- Using the hash, what is the number of detections of malbuster_1 in VirusTotal?<br />
`62`
- Based on VirusTotal detection, what is the malware signature of malbuster_2 according to Avira?<br />
![image](https://github.com/user-attachments/assets/a9d6edb8-6b62-4b4a-bc73-50b0bae6d996)<br />
`HEUR/AGEN.1306860`
- malbuster_2 imports the function _CorExeMain. From which DLL file does it import this function?<br />
![image](https://github.com/user-attachments/assets/5b4952fa-3310-47bd-b329-7c17eddda6c6)<br />
`mscoree.dll`
- Based on the VS_VERSION_INFO header, what is the original name of malbuster_2?<br />
![image](https://github.com/user-attachments/assets/8f2efea1-7ed6-4001-bdd9-3151daab6b81)<br />
`7JYpE.exe`
- Using the hash of malbuster_3, what is its malware signature based on abuse.ch?<br />
Go on [abuse.sh](https://urlhaus.abuse.ch/) and submit the hash:<br />
![image](https://github.com/user-attachments/assets/98fd8890-3f0f-4ef6-a947-71ea14e1ab7c)<br />
`TrickBot`
- Using the hash of malbuster_4, what is its malware signature based on abuse.ch?<br />
![image](https://github.com/user-attachments/assets/3d1eec8c-e49f-422b-8e9f-03c0a2f7adc5)<br />
Found it [here](https://bazaar.abuse.ch/sample/00272dd639402fa76db43207d074fe52d4849e5d46008f786b944a789b09afc2/)<br />
`Zloader`
- What is the message found in the DOS_STUB of malbuster_4?<br />
To find the answer I used floss. `floss malbuster_4 > doc.txt`:<br />
![image](https://github.com/user-attachments/assets/e0e841e0-e3c8-4636-a699-5c1fa10efb2d)<br />
`!This Salfram cannot be run in DOS mode.`
- malbuster_4 imports the function ShellExecuteA. From which DLL file does it import this function?<br />
`shell32.dll`
- Using capa, how many anti-VM instructions were identified in malbuster_1?<br />
Run `capa.exe Samples\malbuster_1 -v`:<br />
![image](https://github.com/user-attachments/assets/bc34287e-d9d6-4688-950b-36de875aea3c)<br />
`3`
- Using capa, which binary can log keystrokes?<br />
![image](https://github.com/user-attachments/assets/443c90b4-d700-48b7-ab79-8cc672413a0e)<br />
`malbuster_3`
- Using capa, what is the MITRE ID of the DISCOVERY technique used by malbuster_4?<br />
Run `capa.exe Samples\malbuster_4`:<br />
![image](https://github.com/user-attachments/assets/5a7098a2-6769-4858-9468-da784e9c8a3d)<br />
`T1083`
- Which binary contains the string GodMode?<br />
Run `floss Samples\malbuster_2 > doc.txt`, then open the .txt file and search for the string using CTRL+f:<br />
![image](https://github.com/user-attachments/assets/3655b9d6-8ae1-429f-9358-450cb34827a5)<br />
`malbuster_2`
- Which binary contains the string Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)?<br />
Found it at the beginning of malbuster_1 in PEstudio:<br />
![image](https://github.com/user-attachments/assets/203925a4-bc78-4ff4-add7-1f3b8fb2a970)<br />
`malbuster_1`

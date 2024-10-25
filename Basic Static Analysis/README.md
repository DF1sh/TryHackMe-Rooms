# Basic Static Analysis

### String search
- On the Desktop in the attached VM, there is a directory named 'mal' with malware samples 1 to 6. Use floss to identify obfuscated strings found in the samples named 2, 5, and 6. Which of these samples contains the string 'DbgView.exe'?<br />
![image](https://github.com/user-attachments/assets/4b80fa66-c8d0-462d-856d-53237714bc7a)<br />
`6`

### Fingerprinting malware
- In the samples located at Desktop\mal\ directory in the attached VM, which of the samples has the same imphash as file 3?<br />
Open file `3` using PEstudio. Its imphash is `F397831B8900AFF7FBEF2FFDE97C2603`. File `1` has the same imphash:<br />
![image](https://github.com/user-attachments/assets/ddcbbfa2-3fe2-42a7-a61a-27dd6fae0e36)<br />
`1`
- Using the ssdeep utility, what is the percentage match of the above-mentioned files?<br />
![image](https://github.com/user-attachments/assets/fa3bb0db-303d-4448-a6ac-592552640f09)<br />
`93`

### Signature-based detection
Open a terminal on the desktop and run `capa mal\4`:
- How many matches for anti-VM execution techniques were identified in the sample?<br />

- Does the sample have to capability to suspend or resume a thread? Answer with Y for yes and N for no.<br />
![image](https://github.com/user-attachments/assets/f86cd2dd-3c5a-4417-bc24-31adfe2747b6)<br />
`Y`
- What MBC behavior is observed against the MBC Objective 'Anti-Static Analysis'?<br />
`86`
![image](https://github.com/user-attachments/assets/bb553356-81e6-4d2a-a382-121830fde49c)<br />
`Disassembler Evasion::Argument Obfuscation [B0012.001]`
- At what address is the function that has the capability 'Check HTTP Status Code'?<br />
Open powershell and run the same command in very verbose mode (`-vv`)<br />
`0x486921`

### Leveraging the PE header
- Open the sample Desktop\mal\4 in PEstudio. Which library is blacklisted?<br />
Open PEstudio and click on `imports`:<br />
`rpcrt4.dll`
- What does this dll do?<br />
Check the description column of the dll:<br />
`Remote Procedure Call Runtime`


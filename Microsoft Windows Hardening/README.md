# Microsoft Windows Hardening

### Understanding General Concepts
- What is the startup type of App Readiness service in the services panel?<br />
![image](https://github.com/user-attachments/assets/5ec001de-e046-4dd9-9ac1-91e722ff2899)<br />
`Manual`
- Open Registry Editor and find the key “tryhackme”. What is the default value of the key?<br />
![image](https://github.com/user-attachments/assets/3b1ab675-3141-4195-a437-e70e76674596)<br />
`{THM_REG_FLAG}`
- Open the Diagnosis folder and go through the various log files. Can you find the flag? `{THM_1000710}`

### Identity & Access Management
- Find the name of the Administrator Account of the attached VM.<br />
![image](https://github.com/user-attachments/assets/93100d0c-97ce-4b73-bbed-f94b59ae7d60)<br />
`Harden`
- Go to the User Account Control Setting Panel (Control Panel > All Control Panel Items > User Accounts). What is the default level of Notification?<br />
![image](https://github.com/user-attachments/assets/24975b02-ec9a-4d87-b659-7c502bd589ec)<br />
`Always Notify`
- How many standard accounts are created in the VM? `0`

### Network Management
- Open Windows Firewall and click on Monitoring in the left pane - which of the following profiles is active? Domain, Private, Public? `Private`
- Find the IP address resolved for the website tryhack.me in the Virtual Machine as per the local hosts file.<br />
![image](https://github.com/user-attachments/assets/6bd96824-a3e5-4a1f-982a-b47a8b403f7f)<br />
- Open the command prompt and enter arp -a. What is the Physical address for the IP address 255.255.255.255?<br />
`ff-ff-ff-ff-ff-ff`

### Application Management
- Windows Defender Antivirus is configured to exclude a particular extension from scanning. What is the extension?<br />
![image](https://github.com/user-attachments/assets/fae21006-f98f-4946-8c5b-c8a2caaad639)<br />
`.ps`
- A Word document is received from an unknown email address. It is best practice to open it immediately on your personal computer (yay/nay). `nay`
- What is the flag you received after executing the Office Hardening Batch file? `{THM_1101110}`

### Storage Management
- A security engineer has misconfigured the attached VM and stored a BitLocker recovery key in the same computer. Can you read the last six digits of the recovery key?<br />
![image](https://github.com/user-attachments/assets/708c485a-ad47-4ac0-a1a5-3a5262e707c3)<br />
`377564`
- How many characters does the BitLocker recovery key have in the attached VM? `48`
- A backup file is placed on the Desktop of the attached VM. What is the extension of that file? `.bkf`

### Updating Windows
- What is the CVE score for the vulnerability CVE ID CVE-2022-32230?  <br />
Found the answer [here](https://www.cvedetails.com/cve/CVE-2022-32230/): `7.8`



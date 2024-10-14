# Secret Recipe

### Introduction
- How many Files are available in the Artifacts folder on the Desktop? `6`

### Windows Registry Forensics
I will use `Registry Explorer` to answer the following questions
- What is the Computer Name of the Machine found in the registry? <br />
The answer is under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\`:<br />
![image](https://github.com/user-attachments/assets/cf1bfbdc-9e7e-4c0a-9580-11ab99e72848)<br />
`JAMES`
- When was the Administrator account created on this machine? (Format: yyyy-mm-dd hh:mm:ss)<br />
The answer is at `HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users`. Look at the last modification date: <br />
![image](https://github.com/user-attachments/assets/83f59e2a-dc20-473b-b177-b81c09ddacaa)<br />
`2021-03-17 14:58:48`
- What is the RID associated with the Administrator account?<br />
`500`
- How many User accounts were observed on this machine?<br />
![image](https://github.com/user-attachments/assets/3c37c68a-756f-4566-b6f9-145511a95aa8)<br />
`7`
- There seems to be a suspicious account created as a backdoor with RID 1013. What is the Account Name?<br />
`bdoor`
- What is the VPN connection this host connected to?<br />
I searched for `vpn` and I found something:<br />
![image](https://github.com/user-attachments/assets/21a90e29-8469-4c1f-bbd9-f061f58b14a1)<br />
`ProtonVPN`
- When was the first VPN connection observed? (Format: YYYY-MM-DD HH:MM:SS)<br />
`2022-10-12 19:52:36`
- There were three shared folders observed on his machine. What is the path of the third share?<br />
![image](https://github.com/user-attachments/assets/60f74d82-a616-47b0-8d8b-99e6b3f1b9f4)<br />
`C:\RESTRICTED FILES`
- What is the Last DHCP IP assigned to this host?<br />`172.31.2.197`
- The suspect seems to have accessed a file containing the secret coffee recipe. What is the name of the file?<br />`secret-recipe.pdf`
- The suspect ran multiple commands in the run windows. What command was run to enumerate the network interfaces?<br /> `pnputil /enum-interfaces` 
- In the file explorer, the user searched for a network utility to transfer files. What is the name of that tool?<br /> `netcat`
- What is the recent text file opened by the suspect?<br /> `secret-code.txt`
- How many times was Powershell executed on this host?<br /> `3` 
- The suspect also executed a network monitoring tool. What is the name of the tool?<br /> `wireshark`
- Registry Hives also notes the amount of time a process is in focus. Examine the Hives. For how many seconds was ProtonVPN executed?<br /> `343`
- Everything.exe is a utility used to search for files in a Windows machine. What is the full path from which everything.exe was executed?<br /> `C:\Users\Administrator\Downloads\tools\Everything\Everything.exe`

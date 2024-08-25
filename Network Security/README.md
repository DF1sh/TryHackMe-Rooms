# Network Security

### Introduction
- What type of firewall is Windows Defender Firewall? `Host Firewall`

### Methodology
- During which step of the Cyber Kill Chain does the attacker gather information about the target? `Recon`

### Practical Example of Network Security
- What is the password in the secret.txt file? <br />
Run `ftp IP_addr` and log in with the 'anonymous' account. To download the secret.txt file run `get secret.txt`.
![image](https://github.com/user-attachments/assets/67dea185-ceb2-4920-a7dc-8191039c41a8)<br />
The password is `ABC789xyz123`.
- What is the content of the flag.txt in the /root directory? <br />
Log in with root using ssh and the previously found password. The root flag is: `THM{FTP_SERVER_OWNED}`.
- What is the content of the flag.txt in the /home/librarian directory?
Run `cat /home/librarian/flag.txt` to get the flag: `THM{LIBRARIAN_ACCOUNT_COMPROMISED}0`

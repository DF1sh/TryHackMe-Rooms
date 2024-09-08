# Protocols and Servers 2

### Sniffing Attack
- What do you need to add to the command sudo tcpdump to capture only Telnet traffic? `port 23`
- What is the simplest display filter you can use with Wireshark to show only IMAP traffic? `imap`

### Man-in-the-Middle (MITM) Attack
- How many different interfaces does Ettercap offer? <br />
Found the answer [here](https://www.ettercap-project.org/): `3`
- In how many ways can you invoke Bettercap? <br />
Found it [here](https://www.bettercap.org/usage/scripting/): <br />
![image](https://github.com/user-attachments/assets/05fb4ee4-4662-4127-9cf1-1c1ef3ae7260)<br />
`3`

### Transport Layer Security (TLS)
- DNS can also be secured using TLS. What is the three-letter acronym of the DNS protocol that uses TLS?<br />
![image](https://github.com/user-attachments/assets/f8e0dce5-7ef2-43be-bd89-f3f6d79ce4c7)<br />
`DoT`

### Secure Shell (SSH)
- Use SSH to connect to 10.10.247.232 as mark with the password XBtc49AB. Using uname -r, find the Kernel release? <br />
![image](https://github.com/user-attachments/assets/4b3c047c-5022-4d52-b368-7f2e56019f8c)<br />
`5.15.0-119-generic`
- Use SSH to download the file book.txt from the remote system. How many KBs did scp display as download size?<br />
![image](https://github.com/user-attachments/assets/1c4aeb99-efe2-48af-9893-193f195b8a81)<br />
`415`

### Password Attack
- We learned that one of the email accounts is lazie. What is the password used to access the IMAP service on 10.10.247.232?<br />
The command I used is `hydra -l lazie -P /usr/share/wordlists/rockyou.txt 10.10.247.232 imap`:<br />
![image](https://github.com/user-attachments/assets/4c5466da-24d7-40ba-a641-2dfac2a15e07)<br />
`butterfly`

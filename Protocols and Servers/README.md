# Protocols and Servers

### Telnet
- To which port will the telnet command with the default parameters try to connect? `23`

### Hypertext Transfer Protocol (HTTP)
- Launch the attached VM. From the AttackBox terminal, connect using Telnet to 10.10.40.111 80 and retrieve the file flag.thm. What does it contain?<br />
![image](https://github.com/user-attachments/assets/79e04303-4c1d-40e1-beff-6b4aec9c98c5)<br />
`THM{e3eb0a1df437f3f97a64aca5952c8ea0}`

### File Transfer Protocol (FTP)
- Using an FTP client, connect to the VM and try to recover the flag file. What is the flag?<br />
![image](https://github.com/user-attachments/assets/e0ae14dc-47db-4081-9d2b-860857358dd2)<br />
`THM{364db6ad0e3ddfe7bf0b1870fb06fbdf}`

### Simple Mail Transfer Protocol (SMTP)
- Using the AttackBox terminal, connect to the SMTP port of the target VM. What is the flag that you can get? <br />
![image](https://github.com/user-attachments/assets/e88a64cf-6e2e-4e4e-9e19-dc0938e1bb41)<br />

### Post Office Protocol 3 (POP3)
- Connect to the VM (10.10.40.111) at the POP3 port. Authenticate using the username frank and password D2xc9CgD. What is the response you get to STAT?<br />
![image](https://github.com/user-attachments/assets/864db8be-ebbe-47d3-8b4d-294eaa29081f)<br />
`+OK 0 0`
- How many email messages are available to download via POP3 on 10.10.40.111? `0`

### Internet Message Access Protocol (IMAP)
- What is the default port used by IMAP? `143`
 

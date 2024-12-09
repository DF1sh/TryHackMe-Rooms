# Networking Core Protocols

### DNS: Remembering Addresses
- Which DNS record type refers to IPv6? `AAAA`
- Which DNS record type refers to the email server? `MX`

### WHOIS
- When was the x.com record created? Provide the answer in YYYY-MM-DD format.<br />
I used [this online service](https://who.is/whois/x.com):<br />
![image](https://github.com/user-attachments/assets/e8414014-cf50-436b-8d4f-e6e1593e3404)<br />
`1993-04-02`
- When was the twitter.com record created? Provide the answer in YYYY-MM-DD format.<br />
Same thing: `2000-01-21`

### HTTP(S): Accessing the Web
- Use telnet to access the file flag.html on 10.10.171.68. What is the hidden flag?<br />
![image](https://github.com/user-attachments/assets/3d1bbb3b-2fdf-4425-afec-49786077104f)<br />
`THM{TELNET-HTTP}`

### FTP: Transferring Files
- Using the FTP client ftp on the AttackBox, access the FTP server at 10.10.171.68 and retrieve flag.txt. What is the flag found?<br />
![image](https://github.com/user-attachments/assets/3b103ed3-39c5-4e60-96f5-aa0e9c87c0c0)<br />
`THM{FAST-FTP}`

### SMTP: Sending Email
- Which SMTP command indicates that the client will start the contents of the email message? `DATA`
- What does the email client send to indicate that the email message has been fully entered? `.`

### POP3: Receiving Email
- Looking at the traffic exchange, what is the name of the POP3 server running on the remote server?<br />
![image](https://github.com/user-attachments/assets/cd9acc85-aa87-4976-920a-5d438df8bd21)<br />
`dovecot`
- Use telnet to connect to 10.10.171.68’s POP3 server. What is the flag contained in the fourth message?<br />
![image](https://github.com/user-attachments/assets/234c54ac-26c2-4fd9-a1d1-e7a692b737f0)<br />
`THM{TELNET_RETR_EMAIL}`

### IMAP: Synchronizing Email
- What IMAP command retrieves the fourth email message? `FETCH 4 body[]`

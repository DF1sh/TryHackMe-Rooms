# Phishing Prevention

### Introduction
- After visiting the link in the task, what is the MITRE ID for the "Software Configuration" mitigation technique? `M1054`

### SPF (Sender Policy Framework)
- Referencing the dmarcian SPF syntax table, what prefix character can be added to the "all" mechanism to ensure a "softfail" result? <br />
![image](https://github.com/user-attachments/assets/d00ee9c2-7ae5-4b80-8ddf-eb35841b6918)<br />
`~`
- What is the meaning of the -all tag? `fail`
  
### DKIM (DomainKeys Identified Mail)
- Which email header shows the status of whether DKIM passed or failed? <br />
![image](https://github.com/user-attachments/assets/98787114-7c64-4ab6-bd3b-e397b76ac8a4)<br />
`Authentication-Results`

### DMARC (Domain-Based Message Authentication, Reporting, and Conformance)
- Which DMARC policy would you use not to accept an email if the message fails the DMARC check? `p=reject`

### S/MIME (Secure/Multipurpose Internet Mail Extensions)
- What is nonrepudiation? (The answer is a full sentence, including the ".") `The uniqueness of a signature prevents the owner of the signature from disowning the signature.`

### SMTP Status Codes
- What Wireshark filter can you use to narrow down the packet output using SMTP status codes? `smtp.response.code`
- Per the network traffic, what was the message for status code 220? (Do not include the status code (220) in the answer) <br />
Use the filter `smtp.response.code == 220`, then double click one packet to get detailed information: <br />
![image](https://github.com/user-attachments/assets/bf2e18b6-d956-4602-8dba-78879a681d49)<br />
- One packet shows a response that an email was blocked using spamhaus.org. What were the packet number and status code? (no spaces in your answer) `156,553`
- Per the network traffic, what was the message for status code 220? (Do not include the status code (220) in the answer) `<domain> service ready`
- One packet shows a response that an email was blocked using spamhaus.org. What were the packet number and status code? (no spaces in your answer) `156,553`
- Based on the packet from the previous question, what was the message regarding the mailbox? `mailbox name not allowed`
- What is the status code that will typically precede a SMTP DATA command? `354`


### SMTP Traffic Analysis
- What port is the SMTP traffic using? `25`
- How many packets are specifically SMTP? `512`
- What is the source IP address for all the SMTP traffic? `10.12.19.101`
- What is the filename of the third file attachment? `attachment.scr`
- How about the last file attachment? `.zip`

### SMTP and C&C Communication
- Per MITRE ATT&CK, which software is associated with using SMTP and POP3 for C2 communications? `Zebrocy`

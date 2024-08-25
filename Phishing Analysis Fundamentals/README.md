# Phishing Analysis Fundamentals

### The Email Address
- Email dates back to what time frame? `1970s`

### Email Delivery
- What port is classified as Secure Transport for SMTP? `465`
- What port is classified as Secure Transport for IMAP? `993`
- What port is classified as Secure Transport for POP3? `995`

### Email Headers
- What email header is the same as "Reply-to"? `Return-Path`
- Once you find the email sender's IP address, where can you retrieve more information about the IP? `http://www.arin.net`

### Email Body
- In the above screenshots, what is the URI of the blocked image? `https://i.imgur.com/LSWOtDI.png`
- In the above screenshots, what is the name of the PDF attachment? `Payment-updateid.pdf`
- In the attached virtual machine, view the information in email2.txt and reconstruct the PDF using the base64 data. What is the text within the PDF? <br />
Open the email2.txt and copy the entire body of the email. Then go on [Base64 to PDF](https://base64.guru/converter/decode/pdf) and convert the data: <br />
![image](https://github.com/user-attachments/assets/5e047a72-e95c-412c-a963-5353f1e4eb47)<br />
Flag is `THM{BENIGN_PDF_ATTACHMENT}`.

### Types of Phishing
- What trusted entity is this email masquerading as? <br />
Open the email3.eml using thunderbird: <br />
![image](https://github.com/user-attachments/assets/901b7f51-d060-4ed1-86a1-12ab492d667f)<br />
`Home Depot`
- What is the sender's email? `support@teckbe.com`
- What is the subject line?  `Order Placed : Your Order ID OD2321657089291 Placed Successfully`
- What is the URL link for - CLICK HERE? (Enter the defanged URL) <br />
You can use [CyberChef](https://gchq.github.io/CyberChef/) to defang the URL: `hxxp[://]t[.]teckbe[.]com/p/?j3=EOowFcEwFHl6EOAyFcoUFV=TVEchwFHlUFOo6lVTTDcATE7oUE7AUET==`

### Conclusion
- What is BEC? `Business Email Compromise`
 

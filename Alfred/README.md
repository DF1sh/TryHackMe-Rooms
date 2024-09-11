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
Let's run a more detailed scan on this given port:

      nmap -p8080 -sV -sC 10.10.128.203         
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-11 09:15 EDT
      Nmap scan report for 10.10.128.203
      Host is up (0.083s latency).
      
      PORT     STATE SERVICE VERSION
      8080/tcp open  http    Jetty 9.4.z-SNAPSHOT
      | http-robots.txt: 1 disallowed entry 
      |_/
      |_http-server-header: Jetty(9.4.z-SNAPSHOT)
      |_http-title: Site doesn't have a title (text/html;charset=utf-8).
      
      Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
      Nmap done: 1 IP address (1 host up) scanned in 11.53 seconds
We can see that the webserver version is "Jetty 9.4.z-SNAPSHOT".
- What is the user.txt flag?
  
### Switching Shells
- What is the final size of the exe payload that you generated?

### Privilege Escalation
- Use the impersonate_token "BUILTIN\Administrators" command to impersonate the Administrators' token. What is the output when you run the getuid command?
- Read the root.txt file located at C:\Windows\System32\config

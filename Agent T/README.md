# Agent T

### Find The Flag
- What is the flag?<br />
Initial nmap scan shows port 80 open:

      # Nmap 7.94SVN scan initiated Wed Dec 18 10:12:25 2024 as: /usr/lib/nmap/nmap -p80 -sV -sC -oN scan 10.10.25.236
      Nmap scan report for 10.10.25.236
      Host is up (0.070s latency).
      
      PORT   STATE SERVICE VERSION
      80/tcp open  http    PHP cli server 5.5 or later (PHP 8.1.0-dev)
      |_http-title:  Admin Dashboard

This website is running a vulnerable version of PHP, that contains a backdoor for remote code execution, by sending a request with field `User-Agentt` (double t), something like this: `"User-Agentt": "zerodiumsystem('" + payload + "');"`.
<br />
I used [this](https://github.com/flast101/php-8.1.0-dev-backdoor-rce/blob/main/revshell_php_8.1.0-dev.py) exploit to get a reverse shell and the flag:<br />
![image](https://github.com/user-attachments/assets/b2005e31-4a39-44e8-ae24-b7a69c71f8ce)<br />


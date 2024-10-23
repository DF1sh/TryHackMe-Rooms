# TryHack3M: Bricks Heist
(answers can be found at the end of this writeup)
### Challenge
- What is the content of the hidden .txt file in the web folder?<br />
Initial scan shows port 22,80,443 and 3306 open:

      nmap -p22,80,443,3306 -sV -sC -Pn 10.10.180.110 -oN scan
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-22 08:55 EDT
      Nmap scan report for 10.10.180.110
      Host is up (0.10s latency).
      
      PORT     STATE SERVICE  VERSION
      22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
      | ssh-hostkey: 
      |   3072 de:68:ef:f3:78:99:a5:de:38:ef:a5:8e:5f:29:ec:b3 (RSA)
      |   256 28:09:b0:61:b8:c2:69:5f:0c:e5:9e:f4:11:be:06:29 (ECDSA)
      |_  256 77:9d:d5:8f:14:60:3a:64:d3:73:9a:c7:2f:f0:31:40 (ED25519)
      80/tcp   open  http     WebSockify Python/3.8.10
      |_http-server-header: WebSockify Python/3.8.10
      |_http-title: Error response
      | fingerprint-strings: 
      |   GetRequest: 
      |     HTTP/1.1 405 Method Not Allowed
      |     Server: WebSockify Python/3.8.10
      |     Date: Tue, 22 Oct 2024 11:54:34 GMT
      |     Connection: close
      |     Content-Type: text/html;charset=utf-8
      |     Content-Length: 472
      |     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
      |     "http://www.w3.org/TR/html4/strict.dtd">
      |     <html>
      |     <head>
      |     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
      |     <title>Error response</title>
      |     </head>
      |     <body>
      |     <h1>Error response</h1>
      |     <p>Error code: 405</p>
      |     <p>Message: Method Not Allowed.</p>
      |     <p>Error code explanation: 405 - Specified method is invalid for this resource.</p>
      |     </body>
      |     </html>
      |   HTTPOptions: 
      |     HTTP/1.1 501 Unsupported method ('OPTIONS')
      |     Server: WebSockify Python/3.8.10
      |     Date: Tue, 22 Oct 2024 11:54:34 GMT
      |     Connection: close
      |     Content-Type: text/html;charset=utf-8
      |     Content-Length: 500
      |     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
      |     "http://www.w3.org/TR/html4/strict.dtd">
      |     <html>
      |     <head>
      |     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
      |     <title>Error response</title>
      |     </head>
      |     <body>
      |     <h1>Error response</h1>
      |     <p>Error code: 501</p>
      |     <p>Message: Unsupported method ('OPTIONS').</p>
      |     <p>Error code explanation: HTTPStatus.NOT_IMPLEMENTED - Server does not support this operation.</p>
      |     </body>
      |_    </html>
      443/tcp  open  ssl/http Apache httpd
      | http-robots.txt: 1 disallowed entry 
      |_/wp-admin/
      |_http-generator: WordPress 6.5
      | ssl-cert: Subject: organizationName=Internet Widgits Pty Ltd/stateOrProvinceName=Some-State/countryName=US
      | Not valid before: 2024-04-02T11:59:14
      |_Not valid after:  2025-04-02T11:59:14
      |_http-title: Brick by Brick
      |_http-server-header: Apache
      | tls-alpn: 
      |   h2
      |_  http/1.1
      |_ssl-date: TLS randomness does not represent time
      3306/tcp open  mysql    MySQL (unauthorized)
      1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
      SF-Port80-TCP:V=7.94SVN%I=7%D=10/22%Time=6717A0BC%P=x86_64-pc-linux-gnu%r(
      SF:GetRequest,291,"HTTP/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nServer:
      SF:\x20WebSockify\x20Python/3\.8\.10\r\nDate:\x20Tue,\x2022\x20Oct\x202024
      SF:\x2011:54:34\x20GMT\r\nConnection:\x20close\r\nContent-Type:\x20text/ht
      SF:ml;charset=utf-8\r\nContent-Length:\x20472\r\n\r\n<!DOCTYPE\x20HTML\x20
      SF:PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x20\x20\x2
      SF:0\x20\x20\"http://www\.w3\.org/TR/html4/strict\.dtd\">\n<html>\n\x20\x2
      SF:0\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20http-equiv=\"
      SF:Content-Type\"\x20content=\"text/html;charset=utf-8\">\n\x20\x20\x20\x2
      SF:0\x20\x20\x20\x20<title>Error\x20response</title>\n\x20\x20\x20\x20</he
      SF:ad>\n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>Error\
      SF:x20response</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code:\x20
      SF:405</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Message:\x20Method\x20Not\x
      SF:20Allowed\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code\x20ex
      SF:planation:\x20405\x20-\x20Specified\x20method\x20is\x20invalid\x20for\x
      SF:20this\x20resource\.</p>\n\x20\x20\x20\x20</body>\n</html>\n")%r(HTTPOp
      SF:tions,2B9,"HTTP/1\.1\x20501\x20Unsupported\x20method\x20\('OPTIONS'\)\r
      SF:\nServer:\x20WebSockify\x20Python/3\.8\.10\r\nDate:\x20Tue,\x2022\x20Oc
      SF:t\x202024\x2011:54:34\x20GMT\r\nConnection:\x20close\r\nContent-Type:\x
      SF:20text/html;charset=utf-8\r\nContent-Length:\x20500\r\n\r\n<!DOCTYPE\x2
      SF:0HTML\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x
      SF:20\x20\x20\x20\x20\"http://www\.w3\.org/TR/html4/strict\.dtd\">\n<html>
      SF:\n\x20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20http
      SF:-equiv=\"Content-Type\"\x20content=\"text/html;charset=utf-8\">\n\x20\x
      SF:20\x20\x20\x20\x20\x20\x20<title>Error\x20response</title>\n\x20\x20\x2
      SF:0\x20</head>\n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<
      SF:h1>Error\x20response</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20
      SF:code:\x20501</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Message:\x20Unsupp
      SF:orted\x20method\x20\('OPTIONS'\)\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x2
      SF:0<p>Error\x20code\x20explanation:\x20HTTPStatus\.NOT_IMPLEMENTED\x20-\x
      SF:20Server\x20does\x20not\x20support\x20this\x20operation\.</p>\n\x20\x20
      SF:\x20\x20</body>\n</html>\n");
      Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Port 3306 is open but there must be some sort of ACL:<br />
![image](https://github.com/user-attachments/assets/8aa39ef7-7fdc-4e99-a8e8-c4e4d11a317a)<br />

Nmap finds robots.txt inside the https server:<br />
![image](https://github.com/user-attachments/assets/f8aab5bc-73ac-4e11-a79f-faf78f607a36)<br />
`/wp-admin` is a wordpress login page, but we don't have any credential. I tried stuff like `admin` or `root`, but these usernames are not even valid. I need to at least find a valid username. <br />
After a while I decided to use wpscan `wpscan --url https://bricks.thm --passwords /usr/share/wordlists/rockyou.txt --usernames administrator --force`. The output of wpscan, among other things, showed me that the web site is using a theme called `bricks`, version 1.9.5. I found an anauthenticated RCE [here](https://github.com/Chocapikk/CVE-2024-25600). Just follow the steps provided in this github page to get a shell!<br />
`THM{fl46_650c844110baced87e1606453b93f22a}`
- What is the name of the suspicious process?<br />
Run `systemctl --type=service --state=running` to list .service. Find the TRYHACK3M service:<br />
![image](https://github.com/user-attachments/assets/99a08d0d-e61a-4690-ace9-1a3ea2974fb0)<br />
`nm-inet-dialog`
- What is the service name affiliated with the suspicious process?<br /> `ubuntu.service`
- What is the log file name of the miner instance?<br />
![image](https://github.com/user-attachments/assets/b35c5c46-97e8-413d-9188-065e27f64fd7)<br />
`inet.conf`
- What is the wallet address of the miner instance?<br />
![image](https://github.com/user-attachments/assets/5c03d45d-7dd8-4748-be4e-b612a6faa9f7)<br />
Take this ID, hex decode it, and double base64-decode it and you get two bitcoin addresses(starting with "bc1"): `bc1qyk79fcp9hd5kreprce89tkh4wrtl8avt4l67qabc1qyk79fcp9had5kreprce89tkh4wrtl8avt4l67qa`. The answer is the first address only:<br />
`bc1qyk79fcp9hd5kreprce89tkh4wrtl8avt4l67qa`

- The wallet address used has been involved in transactions between wallets belonging to which threat group?<br />
Compute the hash of the miner binary and submit it on virustotal: <br />
`LockBit`






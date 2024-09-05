# Zeek Exercises

### Anomalous DNS
- Investigate the dns-tunneling.pcap file. Investigate the dns.log file. What is the number of DNS records linked to the IPv6 address? <br />
![image](https://github.com/user-attachments/assets/dc2465d6-2cf6-4093-861b-7fa1448a366c)<br />
`320`
- Investigate the conn.log file. What is the longest connection duration? <br />
Run `cat conn.log | zeek-cut duration | sort -n | uniq` to get the answer: `9.420791`
- Investigate the dns.log file. Filter all unique DNS queries. What is the number of unique domain queries?<br />
The command that worked for me is `cat dns.log | zeek-cut query | sort | cut -d '.' -f 2- | uniq | sort | uniq`. <br />
`6`
- There are a massive amount of DNS queries sent to the same domain. This is abnormal. Let's find out which hosts are involved in this activity. Investigate the conn.log file. What is the IP address of the source host?
I used `cat dns.log | zeek-cut query id.orig_h`: `10.20.57.3`

### Phishing
- Investigate the logs. What is the suspicious source address? Enter your answer in defanged format.<br />
![image](https://github.com/user-attachments/assets/1471382d-44a7-424a-9198-34c96fd8631c)<br />
Use [CyberChef](https://gchq.github.io/CyberChef/) to degang it: `10[.]6[.]27[.]102`
- Investigate the http.log file. Which domain address were the malicious files downloaded from? Enter your answer in defanged format. <br />
![image](https://github.com/user-attachments/assets/e1066cfe-2deb-49af-8049-94e8152eaa28)<br />
`smart-fax[.]com`
- Investigate the malicious document in VirusTotal. What kind of file is associated with the malicious document? <br />
Run `zeek -C -r phishing.pcap hash-demo.zeek`. Now: <br />
![image](https://github.com/user-attachments/assets/5c89e666-e3a1-400b-970f-ae5614f3b64b)<br /> 
Now take the MD5 hash and submit it on [VirusTotal](https://www.virustotal.com/gui/home/upload): `VBA`
- Investigate the extracted malicious .exe file. What is the given file name in Virustotal? <br />
![image](https://github.com/user-attachments/assets/9e828dd0-6182-4d59-b571-6a34898f02f6)<br />
`PleaseWaitWindow.exe`
- Investigate the malicious .exe file in VirusTotal. What is the contacted domain name? Enter your answer in defanged format. <br />
![image](https://github.com/user-attachments/assets/f89c8abc-9832-477e-a031-369dec937701)<br />
`hopto[.]org`
- Investigate the http.log file. What is the request name of the downloaded malicious .exe file? `knr.exe`

### Log4J
- Investigate the log4shell.pcapng file with detection-log4j.zeek script. Investigate the signature.log file. What is the number of signature hits? <br />
Run `cat signatures.log | zeek-cut uid | wc -l` to get the answer: `3`
- Investigate the http.log file. Which tool is used for scanning? <br />
Run `cat http.log | zeek-cut user_agent` to find out: `Nmap`
- Investigate the http.log file. What is the extension of the exploit file? <br />
![image](https://github.com/user-attachments/assets/f1f80373-1b2b-4524-97e6-f32b28bdaa79)<br />
`.class`
- Investigate the log4j.log file. Decode the base64 commands. What is the name of the created file?<br />
![image](https://github.com/user-attachments/assets/e252a19b-45ff-4bed-ab65-a1b6b3b2c55a)<br />
Decode theese codes to find out: `pwned`

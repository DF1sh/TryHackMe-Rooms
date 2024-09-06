# TShark Challenge II: Directory

### Case: Directory Curiosity!
- What is the name of the malicious/suspicious domain? Enter your answer in a defanged format.<br />
`tshark -r directory-curiosity.pcap -Y 'dns'` worked for me: <br />
`jx2-bavuong[.]com`
- What is the total number of HTTP requests sent to the malicious domain?<br />
![image](https://github.com/user-attachments/assets/153a6d93-825b-42e6-92c0-6bc00e452935)<br />
`14`
- What is the IP address associated with the malicious domain? Enter your answer in a defanged format. `141[.]164[.]41[.]174`
- What is the server info of the suspicious domain?<br />
With this command `tshark -r directory-curiosity.pcap -Y 'http contains jx2-bavuong.com'` I found out that packet 41 contains a response to the first request made to the malicious domain, so I inferred that it might contain information about the server itself. <br />
So I ran `tshark -r directory-curiosity.pcap -c 41 -x` to read the contents of it: <br />
`Apache/2.2.11 (Win32) DAV/2 mod_ssl/2.2.11 OpenSSL/0.9.8i PHP/5.2.9`
- Follow the "first TCP stream" in "ASCII". Investigate the output carefully. What is the number of listed files? <br />
I run `tshark -r directory-curiosity.pcap -z follow,tcp,ascii,0 -q`<br />
![image](https://github.com/user-attachments/assets/bec2bd21-7cc3-44f3-9b45-57154e00191a)<br />
`3`
- What is the filename of the first file? Enter your answer in a defanged format. `123[.]php`
- Export all HTTP traffic objects. What is the name of the downloaded executable file? Enter your answer in a defanged format. <br />
I run `tshark -r directory-curiosity.pcap --export-objects http,. -q`. Putting the output inside the same folder was not a good idea, lol. `vlauto[.]exe`
- What is the SHA256 value of the malicious file?<br />
![image](https://github.com/user-attachments/assets/325814fc-75a0-45d4-91ec-f7a19233e6f0)<br />
`b4851333efaf399889456f78eac0fd532e9d8791b23a86a19402c1164aed20de`
- Search the SHA256 value of the file on [VirtusTotal](https://www.virustotal.com/gui/home/upload). What is the "PEiD packer" value? <br />
Go on VirusTotal to find out: <br />
![image](https://github.com/user-attachments/assets/f3b4a116-b723-49d6-aaba-df23d9460300)<br />
`.NET executable`
- Search the SHA256 value of the file on VirtusTotal. What does the "Lastline Sandbox" flag this as?<br />
I found it under the "Behaviour" section; pressed CTRL+G and searched for "lastline": <br />
![image](https://github.com/user-attachments/assets/b0c6f09f-3433-4650-af3e-82dc62f2c573)<br />
`MALWARE TROJAN`

# Carnage

### Traffic Analysis
- What was the date and time for the first HTTP connection to the malicious IP?<br />
First, change the view of the time format: <br />
![image](https://github.com/user-attachments/assets/7963ba3a-565a-409e-820e-6f91585c99b3)<br />
Now filter for HTTP and get the timestamp of the first packet: `2021-09-24 16:44:38`
- What is the name of the zip file that was downloaded? <br />
![image](https://github.com/user-attachments/assets/cb9d4cd8-2377-4405-b796-0467bcbcf54f)<br />
`documents.zip`
- What was the domain hosting the malicious zip file? <br />
![image](https://github.com/user-attachments/assets/61f99b33-3ba7-4461-b6f5-4347af07e1ef)<br />
`attirenepal.com`
- Without downloading the file, what is the name of the file in the zip file? <br />
Click on File-->Export Objects-->HTTP, and select the one we are interested about: <br />
![image](https://github.com/user-attachments/assets/9a84f750-5447-401a-b604-8026038d9d5e)<br />
And here's the content of the file: <br />
![image](https://github.com/user-attachments/assets/8024eb99-b795-42c0-aa96-5887fd70f461)<br />
`chart-1530076591.xls`
- What is the name of the webserver of the malicious IP from which the zip file was downloaded? <br />
Open the OK response from the web server to get the answer: <br />
![image](https://github.com/user-attachments/assets/5a6c65a7-c309-4efe-8a59-44c8117fe7ca)<br />
`LiteSpeed`
- What is the version of the webserver from the previous question? <br />
![image](https://github.com/user-attachments/assets/c94f4f4c-3df2-4ea3-b6c8-a5cf28a43a94)<br />
`PHP/7.2.34`
- Malicious files were downloaded to the victim host from multiple domains. What were the three domains involved with this activity? <br />
I followed the hint and used the filter `tls.handshake.type == 1 and (frame.time >= "2021-09-24 16:45:11") && (frame.time <= "2021-09-24 16:45:30")`:<br />
`finejewels.com.au, thietbiagt.com, new.americold.com`
- Which certificate authority issued the SSL certificate to the first domain from the previous question? <br />
The first domain is `finejewels.com.au`, which has IP address of `148.72.192.206`. So I put a filter "ip.addr = 148.72.192.206". Then after the TCP handshake, I look for the TLS handshake, specifically the message containing the certificate(right after client hello and server hello): <br />
![image](https://github.com/user-attachments/assets/12ea5475-03a2-4094-9288-6935b6583ef4)<br />
`GoDaddy`
- What are the two IP addresses of the Cobalt Strike servers? Use VirusTotal (the Community tab) to confirm if IPs are identified as Cobalt Strike C2 servers. (answer format: enter the IP addresses in sequential order) <br />
Since cobalt strike uses GET and POST requests, I filter with http.request.method == "GET". From there I click on Statistics-->Conversations to better look at the IP addresses, and I just look all of them on virus total: <br />
`185.106.96.158, 185.125.204.174`
- What is the Host header for the first Cobalt Strike IP address from the previous question? <br />
I used the filter "ip.addr == 185.106.96.158 && http": <br />
![image](https://github.com/user-attachments/assets/b3d5a636-c0e9-4115-87c9-a80c0569dc60)<br />
`ocsp.verisign.com`
- What is the domain name for the first IP address of the Cobalt Strike server? You may use VirusTotal to confirm if it's the Cobalt Strike server (check the Community tab). <br />
Just check on the "Relations" section in VirusTotal.<br />
`survmeter.live`
- What is the domain name of the second Cobalt Strike server IP?  You may use VirusTotal to confirm if it's the Cobalt Strike server (check the Community tab). <br />
Same thing as before: `securitybusinpuff.com`
- What is the domain name of the post-infection traffic? <br />
I follow the hint and filter by POST requests: <br />
![image](https://github.com/user-attachments/assets/153189fe-aaa7-4109-920e-14fd2457266d)<br />
I can see all these weird directories in which the infected machine is sending data. This is probably a C2 server, and the host is `maldivehost.net`.
- What are the first eleven characters that the victim host sends out to the malicious domain involved in the post-infection traffic? <br />
![image](https://github.com/user-attachments/assets/12c22dd0-8f92-4e8d-847f-bed53b7bc71a)<br />
`zLIisQRWZI9`
- What was the length for the first packet sent out to the C2 server? <br />
![image](https://github.com/user-attachments/assets/17ee8e75-2d44-4e20-89db-1a8633fe5cff)<br />
`281`
- What was the Server header for the malicious domain from the previous question? <br />
Find the OK response to the previous POST request, and find the `Server` header: <br />
![image](https://github.com/user-attachments/assets/df39cdba-8b79-4d6a-b47a-748571e5d96d)<br />
`Apache/2.4.49 (cPanel) OpenSSL/1.1.1l mod_bwlimited/1.4`
- The malware used an API to check for the IP address of the victim’s machine. What was the date and time when the DNS query for the IP check domain occurred? (answer format: yyyy-mm-dd hh:mm:ss UTC) <br />
I use the filter `dns && frame contains "api"`: <br />
![image](https://github.com/user-attachments/assets/27b2a259-5da2-48b8-910d-4cb6655c9375)<br />
`2021-09-24 17:00:04`
- What was the domain in the DNS query from the previous question? <br /> `api.ipify.org`
- Looks like there was some malicious spam (malspam) activity going on. What was the first MAIL FROM address observed in the traffic? <br />
For this one I just filtered with `smtp` and found the first "MAIL FROM" message: <br />
![image](https://github.com/user-attachments/assets/9e1a0db9-9aea-4c57-ae62-829c183200f4)<br />
`farshin@mailfa.com`
- How many packets were observed for the SMTP traffic? <br />
Again filtered with `smtp`, then clicked on "Statistics" and "Capture File Properties": <br />
![image](https://github.com/user-attachments/assets/c73f585b-76b2-4dd7-b6f3-9418d1fb9d0e)<br />
`1439`

# TShark: CLI Wireshark Features

### Command-Line Wireshark Features I | Statistics I
- Use the "write-demo.pcap" to answer the questions. What is the byte value of the TCP protocol?<br />
![image](https://github.com/user-attachments/assets/7d8c108b-409a-464e-9804-20711cfece66)<br />
`62`
- In which packet lengths row is our packet listed?
![image](https://github.com/user-attachments/assets/458217c4-6c55-4a4a-a448-50c0e72d4f5a)<br />
`40-79`
- What is the summary of the expert info? <br />
![image](https://github.com/user-attachments/assets/a9f1c09a-4012-454f-9b54-f75c36424b60)<br />
`Connection establish request (SYN): server port 80`
- Use the "demo.pcapng" to answer the question. List the communications. What is the IP address that exists in all IPv4 conversations? Enter your answer in defanged format.<br />
![image](https://github.com/user-attachments/assets/1785cf7b-a58b-46a4-9dcc-426c8c8ff0da)<br />
To defang it, I'm going to use [CyberChef](https://gchq.github.io/CyberChef/): `145[.]254[.]160[.]237`

### Command-Line Wireshark Features II | Statistics II
- Use the "demo.pcapng" to answer the questions. Which IP address has 7 appearances? Enter your answer in defanged format. <br />
![image](https://github.com/user-attachments/assets/43e35cb0-f9cb-4095-a6c5-d1e97cae415c)<br />
`216[.]239[.]59[.]99`
- What is the "destination address percentage" of the previous IP address?<br />
![image](https://github.com/user-attachments/assets/6a6c634e-c0cd-438d-9c7b-5742e3a79a6b)<br />
`6.98%`
- Which IP address constitutes "2.33% of the destination addresses"? Enter your answer in defanged format. <br />
Look at the previous image to find the answer: `145[.]253[.]2[.]203`
- What is the average "Qname Len" value?<br />
Run `tshark -r demo.pcapng -z dns,tree -q` to get the answer: `29.00`

### Command-Line Wireshark Features III | Streams, Objects and Credentials
- Use the "demo.pcapng" to answer the questions. Follow the "UDP stream 0". What is the "Node 0" value? Enter your answer in defanged format. <br />
Run `tshark -r demo.pcapng -z follow,udp,ascii,0`: <br />
![image](https://github.com/user-attachments/assets/cca2b7ce-95c2-41ae-8016-6c23eaf6ec74)<br />
`145[.]254[.]160[.]237:3009`
- Follow the "HTTP stream 1". What is the "Referer" value? Enter your answer in defanged format. <br />
Run `tshark -r demo.pcapng -z follow,http,ascii,1 -q` to get the answer: `hxxp[://]www[.]ethereal[.]com/download[.]html`
- Use the "credentials.pcap" to answer the question. What is the total number of detected credentials?<br />
The command that worked for me is `tshark -r credentials.pcap -z credentials -q | nl`: `75`

### Advanced Filtering Options | Contains, Matches and Fields
- Use the "demo.pcapng" to answer questions. What is the HTTP packet number that contains the keyword "CAFE"? <br />
![image](https://github.com/user-attachments/assets/c4e9aba6-def5-42b0-a555-75fcc2ec26f4)<br />
`27`
- Filter the packets with "GET" and "POST" requests and extract the packet frame time. What is the first time value found?<br />
![image](https://github.com/user-attachments/assets/9a32924c-bee1-4a14-bc1e-9fb030418e9d)<br />
`May 13, 2004 10:17:08.222534000 UTC`

### Use Cases | Extract Information
- Use the "hostnames.pcapng" to answer the questions. What is the total number of unique hostnames?<br />
![image](https://github.com/user-attachments/assets/7fdd3c47-6689-4429-a307-5b4c314e14c4)<br />
`30`
- What is the total appearance count of the "prus-pc" hostname? <br />
![image](https://github.com/user-attachments/assets/8e896a74-e8fb-4d22-9cc7-10f049389496)<br />
`12`
- Use the "dns-queries.pcap" to answer the question. What is the total number of queries of the most common DNS query?<br />
![image](https://github.com/user-attachments/assets/0a013e38-4935-4273-a75b-0ac30ef657b2)<br />
`472`
- Use the "user-agents.pcap" to answer questions. What is the total number of the detected "Wfuzz user agents"?<br />
![image](https://github.com/user-attachments/assets/0a8bf00a-1bb8-478f-a804-5d2861bd8157)<br />
`12`
- What is the "HTTP hostname" of the nmap scans? Enter your answer in defanged format.<br />
![image](https://github.com/user-attachments/assets/0fcfc1a0-3b88-4bbe-8a15-e40f9f16575a)<br />
`172[.]16[.]172[.]129`

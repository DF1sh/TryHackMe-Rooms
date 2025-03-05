# DNS Manipulation

### What is DNS?
- If you were on Windows, what command could you use to query a txt record for 'youtube.com'? `nslookup -type=txt youtube.com`
- If you were on Linux, what command could you use to query a txt record for 'facebook.com'? `dig facebook.com TXT`
- AAAA stores what type of IP Address along with the hostname? `IPv6`
- Maximum characters for a DNS TXT Record is 256. (Yay/Nay) `Nay`
- What DNS Record provides a domain name in reverse-lookup? (Research) `PTR`
- What would the reverse-lookup be for the following IPv4 Address? (192.168.203.2) (Research)<br />
![image](https://github.com/user-attachments/assets/95a29842-7cc2-4752-ae20-11c7e0ebd666)<br />
`2.203.168.192.in-addr.arpa`

### What is DNS Exfiltration?
DNS exfiltration is a way of exfiltrating data from a compromised network. Opening a new port / connection from the target machine can be suspicious. Instead, port 53 TCP/UDP is usually allowed and less suspicious, so DNS exfiltration is a way of evading detection.<br />
- What is the maximum length of a DNS name? (Research) (Length includes dots!) `253`

### DNS Exfiltration - Practice
- What is the Transaction name? (Type it as you see it)<br />
![image](https://github.com/user-attachments/assets/0e7355a0-242b-4c24-b2e8-bba4ee44bf0e)<br />
`Network Equip.`
- How much was the Firewall? (Without the $) `2500`
- Which file contains suspicious DNS queries?<br />
![Screenshot 2025-03-05 143452](https://github.com/user-attachments/assets/1f4931c8-b8a1-4fe8-bfbf-65e52e6029d4)<br />
`cap3.pcap`
- Enter the plain-text after you have decoded the data using packetyGrabber.py found in ~/dns-exfil-infil/ folder.<br />
![Screenshot 2025-03-05 143726](https://github.com/user-attachments/assets/72758a05-847a-4cf9-be6a-9d3f761570b0)<br />
`administrator:s3cre7P@ssword`

### What is DNS Infiltration?
- What type of DNS Record is usually used to infiltrate data into a network? `TXT`

### DNS Infiltration - Practice
- Enter the output from the executed python file `4.4.0-186-generic`

### DNS Tunneling
- What program was used to Tunnel HTTP over DNS? `iodine`

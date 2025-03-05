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
<br />

- How much was the Firewall? (Without the $)
- Which file contains suspicious DNS queries?
- Enter the plain-text after you have decoded the data using packetyGrabber.py found in ~/dns-exfil-infil/ folder.

### What is DNS Infiltration?
- What type of DNS Record is usually used to infiltrate data into a network?

### DNS Infiltration - Practice
- Enter the output from the executed python file

### DNS Tunneling
- What program was used to Tunnel HTTP over DNS?

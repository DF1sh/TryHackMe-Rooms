# Wireshark: Traffic Analysis

### Nmap Scans
- Use the "Desktop/exercise-pcaps/nmap/Exercise.pcapng" file. What is the total number of the "TCP Connect" scans? <br />
The filter to be used is: `tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size > 1024 `
![image](https://github.com/user-attachments/assets/25440297-bea5-42af-91d3-aee1b3aa7428)<br />
`1000`

- Which scan type is used to scan the TCP port 80? `TCP Connect`
- How many "UDP close port" messages are there? <br />
The filter is: `icmp.code==3`. The answer is `1083`.
- Which UDP port in the 55-70 port range is open? <br />
The filter is `udp.dstport >= 55 && udp.dstport <= 70`, or `udp.dstport in {55 .. 70}`: <br />
![image](https://github.com/user-attachments/assets/df170f19-2ab3-4508-afc1-de7645371a9b)<br />
We can see that there are three ports: 67,68 and 69. 67 and 69 are getting 'destination unreachable', so the answer is `68`.


### ARP Poisoning & Man In The Middle!
- Use the "Desktop/exercise-pcaps/arp/Exercise.pcapng" file. What is the number of ARP requests crafted by the attacker? <br />
Use the filter `arp.opcode == 1 && arp.src.hw_mac==00:0c:29:e2:18:b4` to get the answer: `284`.
- What is the number of HTTP packets received by the attacker? <br />
The filter is `http && eth.dst == 00:0c:29:e2:18:b4`, the number of packets is `90`.
- What is the number of sniffed username&password entries? <br />
If we use the filter `http.request.method == "POST" && eth.dst == 00:0c:29:e2:18:b4` we get the number of POST requests. 
![image](https://github.com/user-attachments/assets/c9f7224a-9a19-4100-b45a-49a32a3877f5) <br />
By analyzing them, we can see that POST requests on the resource `/userinfo.php` contains username and password fields. There are 8 such requests, however if we inspect them, only 6 of them contain username and password. So the answer is `6`.
- What is the password of the "Client986"? <br />
![image](https://github.com/user-attachments/assets/874b593f-50b4-4ea3-9be8-6b0f54e5a038)<br />
`clientnothere!`
- What is the comment provided by the "Client354"? <br />
![image](https://github.com/user-attachments/assets/d8a0ef2d-a4cd-4a20-915d-fa63e6e9ae26) <br />
`Nice work!`

### Identifying Hosts: DHCP, NetBIOS and Kerberos
- Use the "Desktop/exercise-pcaps/dhcp-netbios-kerberos/dhcp-netbios.pcap" file. What is the MAC address of the host "Galaxy A30"?
- How many NetBIOS registration requests does the "LIVALJM" workstation have?
- Which host requested the IP address "172.16.13.85"?
- Use the "Desktop/exercise-pcaps/dhcp-netbios-kerberos/kerberos.pcap" file. What is the IP address of the user "u5"? (Enter the address in defanged format.)
- What is the hostname of the available host in the Kerberos packets?

### Tunneling Traffic: DNS and ICMP
- Use the "Desktop/exercise-pcaps/dns-icmp/icmp-tunnel.pcap" file. Investigate the anomalous packets. Which protocol is used in ICMP tunnelling?
- Use the "Desktop/exercise-pcaps/dns-icmp/dns.pcap" file. Investigate the anomalous packets. What is the suspicious main domain address that receives anomalous DNS queries? (Enter the address in defanged format.)

### Cleartext Protocol Analysis: FTP
- Use the "Desktop/exercise-pcaps/ftp/ftp.pcap" file. How many incorrect login attempts are there?
- What is the size of the file accessed by the "ftp" account?
- The adversary uploaded a document to the FTP server. What is the filename?
- The adversary tried to assign special flags to change the executing permissions of the uploaded file. What is the command used by the adversary?

### Cleartext Protocol Analysis: HTTP
- Use the "Desktop/exercise-pcaps/http/user-agent.cap" file. Investigate the user agents. What is the number of anomalous  "user-agent" types?
- What is the packet number with a subtle spelling difference in the user agent field?
- Use the "Desktop/exercise-pcaps/http/http.pcapng" file. Locate the "Log4j" attack starting phase. What is the packet number?
- Locate the "Log4j" attack starting phase and decode the base64 command. What is the IP address contacted by the adversary? (Enter the address in defanged format and exclude "{}".)

### Encrypted Protocol Analysis: Decrypting HTTPS
- Use the "Desktop/exercise-pcaps/https/Exercise.pcap" file. What is the frame number of the "Client Hello" message sent to "accounts.google.com"?
- Decrypt the traffic with the "KeysLogFile.txt" file. What is the number of HTTP2 packets?
- Go to Frame 322. What is the authority header of the HTTP2 packet? (Enter the address in defanged format.)
- Investigate the decrypted packets and find the flag! What is the flag?

### Bonus: Hunt Cleartext Credentials!
- Use the "Desktop/exercise-pcaps/bonus/Bonus-exercise.pcap" file. What is the packet number of the credentials using "HTTP Basic Auth"?
- What is the packet number where "empty password" was submitted?

### Bonus: Actionable Results!
- Use the "Desktop/exercise-pcaps/bonus/Bonus-exercise.pcap" file. Select packet number 99. Create a rule for "IPFirewall (ipfw)". What is the rule for "denying source IPv4 address"?
- Select packet number 231. Create "IPFirewall" rules. What is the rule for "allowing destination MAC address"?

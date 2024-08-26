# Wireshark: Packet Operations

### Statistics | Summary
- Investigate the resolved addresses. What is the IP address of the hostname starts with "bbc"?<br />
Open `Exercise.pcapng` with Wireshark. Then click on "Statistics" and "Resolved Addresses": <br />
![image](https://github.com/user-attachments/assets/ab2c43b9-e011-416a-8460-7dd2b7b5f08a)<br />
`199.232.24.81`
- What is the number of IPv4 conversations? Click on Statistics-->Conversations:<br />
![image](https://github.com/user-attachments/assets/956deb2b-a077-4b0a-b850-33a19447ce54)<br />
`435`.
- How many bytes (k) were transferred from the "Micro-St" MAC address? <br />
Go to "Endpoints" and check "name resolution": <br />
![image](https://github.com/user-attachments/assets/e74202dd-162c-4712-b912-61069783d148)<br />
`7474`
- What is the number of IP addresses linked with "Kansas City"?<br />
On the same window, click on the "IPv4" section and scroll down until you find "Kansas City": `4`.
- Which IP address is linked with "Blicnet" AS Organisation? `188.246.82.7`

### Statistics | Protocol Details
- What is the most used IPv4 destination address? `10.100.1.33`
- What is the max service request-response time of the DNS packets? <br />
![image](https://github.com/user-attachments/assets/22afa637-f649-4e07-8ab9-d1a4c2a47a23) <br />
`0.467897`.
- What is the number of HTTP Requests accomplished by "rad[.]msn[.]com"? <br />
Go to Statistics-->HTTP-->requests and scroll down until you find rad[.]msn[.]com. The answer is `39`.

### Packet Filtering | Protocol Filters
- What is the number of IP packets? the filter is "ip" <br />
![image](https://github.com/user-attachments/assets/30033647-bdf5-4abd-a4db-d7cc053f6ec1)<br />
`81420`.
- What is the number of packets with a "TTL value less than 10"? The filter is "ip.ttl < 10": `66`
- What is the number of packets which uses "TCP port 4444"? The filter is "tcp.port == 4444": `632`
- What is the number of "HTTP GET" requests sent to port "80"? The filter is "http.request.method == "GET" && tcp.dstport == 80": `527`
- What is the number of "type A DNS Queries"? `51` 

### Advanced Filtering
- Find all Microsoft IIS servers. What is the number of packets that did not originate from "port 80"? The filter is "http.server contains "Microsoft-IIS" && tcp.srcport != 80": `21`
- Find all Microsoft IIS servers. What is the number of packets that have "version 7.5"? `71`
- What is the total number of packets that use ports 3333, 4444 or 9999? The filter is "tcp.port in {4444 3333 9999}": `2235`
- What is the number of packets with "even TTL numbers"? `77289`
- Change the profile to "Checksum Control". What is the number of "Bad TCP Checksum" packets? `34185`
- Use the existing filtering button to filter the traffic. What is the number of displayed packets? `261`


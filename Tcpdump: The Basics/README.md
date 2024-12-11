# Tcpdump: The Basics

### Introduction
- What is the name of the library that is associated with tcpdump? `libpcap`

### Basic Packet Capture
- What option can you add to your command to display addresses only in numeric format? `-n`

### Filtering Expressions
- How many packets in traffic.pcap use the ICMP protocol?<br />
Run `sudo tcpdump -r traffic.pcap -n icmp | wc -l`:<br />
![image](https://github.com/user-attachments/assets/9a7e829d-3a75-498c-8365-f88b84e7f950)<br />
`26`
- What is the IP address of the host that asked for the MAC address of 192.168.124.137?<br />
Run `sudo tcpdump -r traffic.pcap -n arp | grep 192.168.124.137`:<br />
![image](https://github.com/user-attachments/assets/997707ae-58b5-4af6-9369-9baaae1a3695)<br />
`192.168.124.148`
- What hostname (subdomain) appears in the first DNS query?<br />
Run `sudo tcpdump -r traffic.pcap -n port 53` and check the first result:<br />
![image](https://github.com/user-attachments/assets/b413e0b2-3ca9-43aa-aed9-39e363e69526)<br />
`mirrors.rockylinux.org`

### Advanced Filtering
- How many packets have only the TCP Reset (RST) flag set?<br />
Run `sudo tcpdump -r traffic.pcap "tcp[tcpflags] == tcp-rst" | wc -l`:<br />
![image](https://github.com/user-attachments/assets/8735595f-f7d0-4089-bbaa-b85c7b077e9e)<br />
`57`
- What is the IP address of the host that sent packets larger than 15000 bytes?<br />
Run `sudo tcpdump -r traffic.pcap greater 15000 -n`:<br />
![image](https://github.com/user-attachments/assets/9ee6ca13-6ea7-4807-b9a2-4bf10c5c0c94)<br />
`185.117.80.53`

### Displaying Packets
- What is the MAC address of the host that sent an ARP request?<br />
Run `sudo tcpdump -r traffic.pcap arp -e`:<br />
![image](https://github.com/user-attachments/assets/43b54ffe-9a7a-4d89-8009-5c90ee4d8ac8)<br />
`52:54:00:7c:d3:5b`

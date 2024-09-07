# Nmap Live Host Discovery

### Subnetworks
Follow the steps provided in the task: <br />
- How many devices can see the ARP Request? `4`
- Did computer6 receive the ARP Request? (Y/N) `N`
- How many devices can see the ARP Request? `4`
- Did computer6 reply to the ARP Request? (Y/N) `Y`

### Enumerating Targets
- What is the first IP address Nmap would scan if you provided 10.10.12.13/29 as your target? <br />
![image](https://github.com/user-attachments/assets/82f173af-435b-4012-97a0-d7076e1db155)<br />
`10.10.12.8`
- How many IP addresses will Nmap scan if you provide the following range 10.10.0-255.101-125? <br />
Run `nmap -sL -n 10.10.0-255.101-125 | wc -l`, take the result minus two lines for the banner info: `6400`

### Discovering Live Hosts
Follow the steps provided in the task: <br />
- What is the type of packet that computer1 sent before the ping? `ARP Request`
- What is the type of packet that computer1 received before being able to send the ping? `ARP Response`
- How many computers responded to the ping request? `1`
- What is the name of the first device that responded to the first ARP Request? `router`
- What is the name of the first device that responded to the second ARP Request? `computer5`
- Send another Ping Request. Did it require new ARP Requests? (Y/N) `N`

### Nmap Host Discovery Using ARP
- How many devices are you able to discover using ARP requests? `3`

### Nmap Host Discovery Using ICMP
- What is the option required to tell Nmap to use ICMP Timestamp to discover live hosts? `-PP`
- What is the option required to tell Nmap to use ICMP Address Mask to discover live hosts? `-PM`
- What is the option required to tell Nmap to use ICMP Echo to discover live hosts? `-PE`

### Nmap Host Discovery Using TCP and UDP
- Which TCP ping scan does not require a privileged account? `TCP SYN Ping`
- Which TCP ping scan requires a privileged account? `TCP ACK Ping`
- What option do you need to add to Nmap to run a TCP SYN ping scan on the telnet port? `-PS23`

### Using Reverse-DNS Lookup
- We want Nmap to issue a reverse DNS lookup for all the possibles hosts on a subnet, hoping to get some insights from the names. What option should we add? `-R`

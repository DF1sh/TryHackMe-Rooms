# Networking Essentials

### DHCP: Give Me My Network Settings
- How many steps does DHCP use to provide network configuration? `4`
- What is the destination IP address that a client uses when it sends a DHCP Discover packet? `255.255.255.255`
- What is the source IP address a client uses when trying to get IP network configuration over DHCP? `0.0.0.0`

### ARP: Bridging Layer 3 Addressing to Layer 2 Addressing
- What is the destination MAC address used in an ARP Request? `ff:ff:ff:ff:ff:ff`
- In the example above, what is the MAC address of 192.168.66.1? `44:df:65:d8:fe:6c`

### ICMP: Troubleshooting Networks
- Using the example images above, how many bytes were sent in the echo (ping) request? `40`
- Which IP header field does the traceroute command require to become zero? `TTL`

### Routing
- Which routing protocol discussed in this task is a Cisco proprietary protocol? `EIGRP`

### NAT
- In the network diagram above, what is the public IP that the phone will appear to use when accessing the Internet? `212.3.4.5`
- Assuming that the router has infinite processing power, approximately speaking, how many thousand simultaneous TCP connections can it maintain? `65`

### Closing Notes
- Click on the View Site button to access the related site. Please follow the instructions on the site to obtain the flag.<br />
The sequence of correct answers in the game are: `ICMP - DHCP - ICMP - NAT` <br />
`THM{computer_is_happy}`

# Secure Network Architecture

### Network Segmentation
- How many trunks are present in this configuration? `4`
- What is the VLAN tag ID for interface eth12? `30`

### Common Secure Network Architecture
- From the above table, what zone would a user connecting to a public web server be in? `External`
- From the above table, what zone would a public web server be in? `DMZ`
- From the above table, what zone would a core domain controller be placed in? `Restricted`

### Network Security Policies and Controls
- According to the corresponding ACL policy, will the first packet result in a drop or accept? `accept`
- According to the corresponding ACL policy, will the second packet result in a drop or accept? `drop`

### Zone-Pair Policies and Filtering
- What is the flag found after filling in all blanks on the static site? `THM{M05tly_53cure}`

### Validating Network Traffic
- Does SSL inspection require a man-in-the-middle proxy? (Y/N) `Y`
- What platform processes data sent from an SSL proxy? `Unified Threat Management `

### Addressing Common Attacks
- Where does DHCP snooping store leased IP addresses from untrusted hosts? `DHCP Binding Database`
- Will a switch drop or accept a DHCPRELEASE packet? `Drop`
- Does dynamic ARP inspection use the DHCP binding database? (Y/N) `Y`
- Dynamic ARP inspection will match an IP address and what other packet detail? `MAC Address`

# Firewall Fundamentals

### What Is the Purpose of a Firewall
- Which security solution inspects the incoming and outgoing traffic of a device or a network? `Firewall`

### Types of Firewalls
- Which type of firewall maintains the state of connections? `stateful firewall`
- Which type of firewall offers heuristic analysis for the traffic? `next-generation firewall`
- Which type of firewall inspects the traffic coming to an application? `proxy firewall`

### Rules in Firewalls
- Which type of action should be defined in a rule to permit any traffic? `allow`
- What is the direction of the rule that is created for the traffic leaving our network? `outbound`

### Windows Defender Firewall
- What is the name of the rule that was created to block all incoming traffic on the SSH port?<br />
Click on `inboud rules` to find out: <br />
![image](https://github.com/user-attachments/assets/2b438c7c-5bcd-439c-8537-561e2a8c6556)<br />
`Core Op`
- A rule was created to allow SSH from one single IP address. What is the rule name? `Infra team`
- Which IP address is allowed under this rule?<br />
![image](https://github.com/user-attachments/assets/5653d8ca-fa70-4914-b68b-eb169f3b88b1)<br />
`192.168.13.7`

### Linux iptables Firewall
- Which Linux firewall utility is considered to be the successor of "iptables"? `nftables`
- What rule would you issue with ufw to deny all outgoing traffic from your machine as a default policy? (answer without sudo) `ufw default deny outgoing`

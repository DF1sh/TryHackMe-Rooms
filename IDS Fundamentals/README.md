# IDS Fundamentals

### What Is an IDS
- Can an intrusion detection system (IDS) prevent the threat after it detects it? Yea/Nay `Nay`

### Types of IDS 
- Which type of IDS is deployed to detect threats throughout the network? `Network Intrusion Detection System`
- Which IDS leverages both signature-based and anomaly-based detection techniques? `Hybrid IDS`

### IDS Example: Snort
- Which mode of Snort helps us to log the network traffic in a PCAP file? `Packet Logging Mode`
- What is the primary mode of Snort called? `Network Intrusion Detection System Mode`

### Snort Usage
- Where is the main directory of Snort that stores its files? `/etc/snort`
- Which field in the Snort rule indicates the revision number of the rule? `rev`
- Which protocol is defined in the sample rule created in the task? `icmp`
- What is the file name that contains custom rules for Snort? `local.rules`

### Practical Lab
- What is the IP address of the machine that tried to connect to the subject machine using SSH?<br />
![image](https://github.com/user-attachments/assets/50dbca12-2657-4669-b285-d0464bc99301)<br />
`10.11.90.211`
- What other rule message besides the SSH message is detected in the PCAP file? `Ping Detected`
- What is the sid of the rule that detects SSH?<br />
![image](https://github.com/user-attachments/assets/04ac079b-e4fa-4b5a-a0cf-845563bc5528)<br />
`1000002`

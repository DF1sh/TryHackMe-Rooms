# Snort Challenge - The Basics

### Writing IDS Rules (HTTP)
- Write a single rule to detect "all TCP port 80 traffic" packets in the given pcap file. What is the number of detected packets? <br />
Move to the TASK-2 folder. To write new rules, we need to edit `local.rules`. The rule we need is: <br />

      alert tcp any any -> any 80 (msg:"TCP traffic on port 80 detected"; sid:1000001; rev:1;)
   
To run snort and test this rules on the .pcap file, run the following command: `snort -c local.rules -A full -l . -r mx-3.pcap -K ASCII` <br />
![image](https://github.com/user-attachments/assets/46ab7687-65c9-4517-ba91-680c54b28237) <br />
The number of detected HTTP packets is `164`. <br /><br />

- Investigate the log file. What is the destination address of packet 63? <br />
Run the command `sudo snort -r snort.log.1724491962 -n 63` to get the answer: `216.239.59.99`<br />
- What is the ACK number of packet 64? <br />
Run the command `sudo snort -r snort.log.1724491962 -n 64` to get the answer: `0x2E6B5384` <br />
- What is the SEQ number of packet 62? <br />
Run the command `sudo snort -r snort.log.1724491962 -n 62` <br />
![image](https://github.com/user-attachments/assets/d5a10956-4f0d-4d8f-8184-27f39e087e57)<br />
`0x36C21E28`. <br />
- What is the TTL of packet 65? `128` <br />
- What is the source IP of packet 65? `145.254.160.237` <br />
- What is the source port of packet 65? `3372` <br />


### Writing IDS Rules (FTP)
Write a single rule to detect "all TCP port 21"  traffic in the given pcap.  <br />
Similarly as before, the rule we need to add is: <br />

      alert tcp any any <> any 21 (msg:"TCP traffic on port 21 detected"; sid:1000001; rev:1;)
This will capture every packet (in every direction) having destination port 21. <br />
- What is the number of detected packets? <br />
After running `snort -c local.rules -A full -l . -r ftp-png-gif.pcap`, the number of detected packets by snort are `307`. <br />

- Investigate the log file. What is the FTP service name? <br />
My guess is that the name of the FTP service is probably inside the banner, therefore it should be inside the very first packets. Try to inspect only the first 5 packets and see what happens. To read the content of the packet we can use the `-X` flag. <br />
Therefore run the command `snort -r snort.log.1724497351 -X -n 5`. The 4th packet has the answer we are looking for:
![image](https://github.com/user-attachments/assets/85dbbbe3-791c-4e43-8129-fd833f7a7018) <br />
`Microsoft FTP Service`. <br />

- Write a rule to detect failed FTP login attempts in the given pcap. What is the number of detected packets? <br />
By looking at the contents of the packet, notice that each failed FTP login attempt prompts a default message with the pattern "530 User". We want to filter every packet with this pattern; to do that we can use the `content` parameter. The rule is:

      alert tcp any any <> any 21 (msg:"Failed login detected"; content:"530 User"; sid:1000001; rev:1;)
And again run the command `snort -c local.rules -A full -l . -r ftp-png-gif.pcap`. <br />
![image](https://github.com/user-attachments/assets/2840e4f9-4988-4c86-bef6-bab1824f2629)<br />
The number of detected failed login attempts is `41`. <br />

- Write a rule to detect successful FTP logins in the given pcap. The process is similar as before, but filter for the pattern "230 User" instead. The answer is `1`. <br />
- Write a rule to detect FTP login attempts with a valid username but no password entered yet. Now filter for "331 Password" to get the answer: `42`. <br />
- Write a rule to detect FTP login attempts with the "Administrator" username but no password entered yet. <br />
For this we're going to need identify two different patterns on the same packets. The first pattern is "331 Password" and the second is "Administrator". Therefore the final rule is:

      alert tcp any any <> any 21 (msg:"Failed login detected"; content:"Administrator"; content:"331 Password"; sid:1000001; rev:1;)

The number of such login attempts detected by snort is `7`. <br />

### Writing IDS Rules (PNG)

### Writing IDS Rules (Torrent Metafile)

### Troubleshooting Rule Syntax Errors

### Using External Rules (MS17-010)

### Using External Rules (Log4j)

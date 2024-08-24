# Snort Challenge - The Basics

### Writing IDS Rules (HTTP)
- Write a single rule to detect "all TCP port 80 traffic" packets in the given pcap file. What is the number of detected packets? <br />
Move to the TASK-2 folder. To write new rules, we need to edit `local.rules`. The rule we need is: `alert tcp any any <> any any (msg: "Block Port 80"; sid: 100001; rev:1;)` <br />
To run snort and test this rules on the .pcap file, run the following command: `snort -c local.rules -A full -l . -r mx-3.pcap -K ASCII` <br />
![image](https://github.com/user-attachments/assets/46ab7687-65c9-4517-ba91-680c54b28237) <br />
The number of detected HTTP packets is `164`. <br /><br />

- Investigate the log file. What is the destination address of packet 63? <br />
Run the command `sudo snort -r snort.log.1724491962 -n 63` to get the answer: `216.239.59.99`<br />
- What is the ACK number of packet 64? <br />
Run the command `sudo snort -r snort.log.1724491962 -n 64` to get the answer: `0x2E6B5384` <br />

### Writing IDS Rules (FTP)

### Writing IDS Rules (PNG)

### Writing IDS Rules (Torrent Metafile)

### Troubleshooting Rule Syntax Errors

### Using External Rules (MS17-010)

### Using External Rules (Log4j)

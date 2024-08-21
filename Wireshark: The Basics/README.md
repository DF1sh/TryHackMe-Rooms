# Wireshark: The Basics

### Introduction
- Which file is used to simulate the screenshots? `http1.pcapng` <br />
- Which file is used to answer the questions? `Exercise.pcapng` <br />

### Tool Overview
- Read the "capture file comments". What is the flag? `TryHackMe_Wireshark_Demo` <br />
- What is the total number of packets? `58620` <br />
- What is the SHA256 hash value of the capture file? `f446de335565fb0b0ee5e5a3266703c778b2f3dfad7efeaeccb2da5641a6d6eb` <br />

### Packet Dissection
- View packet number 38. Which markup language is used under the HTTP protocol? `eXtensible Markup Language` <br />
- What is the arrival date of the packet? (Answer format: Month/Day/Year) `05/13/2004` <br />
- What is the total number of packets? `47` <br />
- What is the TCP payload size? `424` <br />
- What is the e-tag value? `9a01a-4696-7e354b00` <br />

### Packet Navigation
- Search the "r4w" string in packet details. What is the name of artist 1? `r4w8173` <br />
- Go to packet 12 and read the comments. What is the answer? `911cd574a42865a956ccde2d04495ebf` <br />
- There is a ".txt" file inside the capture file. Find the file and read it; what is the alien's name? `PACKETMASTER` <br />
- Look at the expert info section. What is the number of warnings? `1636` <br />

### Packet Filtering
- Go to packet number 4. Right-click on the "Hypertext Transfer Protocol" and apply it as a filter. Now, look at the filter pane. What is the filter query? `http` <br />
- What is the number of displayed packets? `1089` <br />
- Go to packet number 33790 and follow the stream. What is the total number of artists? `3` <br />
- What is the name of the second artist? `Blad3` <br />

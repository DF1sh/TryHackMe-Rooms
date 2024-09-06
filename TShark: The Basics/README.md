# TShark: The Basics

### Command-Line Packet Analysis Hints | TShark and Supplemental CLI Tools
- View the details of the demo.pcapng file with "capinfos". What is the "RIPEMD160" value?
![image](https://github.com/user-attachments/assets/ba75685d-8d9e-47bb-8b08-3789fc883ce9)<br />
`6ef5f0c165a1db4a3cad3116b0c5bcc0cf6b9ab7`

### TShark Fundamentals I | Main Parameters I
- What is the installed TShark version in the given VM? <br />
Run `tshark -v` to get the answer: `3.2.3`
- List the available interfaces with TShark. What is the number of available interfaces in the given VM? <br />
Run `tshark -D` to get the answer: `12`

### TShark Fundamentals I | Main Parameters II
- Read the "demo.pcapng" file with TShark. What are the assigned TCP flags in the 29th packet? <br />
Run `tshark -r demo.pcapng -c 29`: `PSH, ACK`
- What is the "Ack" value of the 25th packet?<br />
Run `tshark -r demo.pcapng -c 25`: `12421`
- What is the "Window size value" of the 9th packet?<br />
Run `tshark -r demo.pcapng -c 9`:<br />
![image](https://github.com/user-attachments/assets/13c68bd5-8a9e-4e57-ad47-999fb695eafc)<br />
`9660`

### TShark Fundamentals II | Capture Conditions
- Which parameter can help analysts to create a continuous capture dump? `-b`
- Can we combine autostop and ring buffer parameters with TShark? y/n `y`

### TShark Fundamentals III | Packet Filtering Options: Capture vs. Display Filters
- Which parameter is used to set "Capture Filters"? `-f`
- Which parameter is used to set "Display Filters"? `-Y`

### TShark Fundamentals IV | Packet Filtering Options: Capture Filters
- What is the number of packets with SYN bytes? <br />
What worked for me is `tshark -r demo.pcapng -Y "tcp" | grep SYN`:<br />
![image](https://github.com/user-attachments/assets/47ed724c-2566-48e3-b8d1-016f3abca8a6)<br />
`2`
- What is the number of packets sent to the IP address "10.10.10.10"? `7`
- What is the number of packets with ACK bytes? `8`

### TShark Fundamentals V | Packet Filtering Options: Display Filters
- What is the number of packets with a "65.208.228.223" IP address?<br />
![image](https://github.com/user-attachments/assets/7286eb5e-f4f1-431c-975a-e79e1cea0ee6)<br />
`34`

- What is the number of packets with a "TCP port 3371"?<br />
![image](https://github.com/user-attachments/assets/e28cf599-d9bc-492a-bf1b-552cd554e0a1)<br />
`7`

- What is the number of packets with a "145.254.160.237" IP address as a source address?<br />
![image](https://github.com/user-attachments/assets/aca4d843-2233-4b0d-97a1-960fec0b2b98)<br />
`20`

- Rerun the previous query and look at the output. What is the packet number of the "Duplicate" packet?<br />
Run `tshark -r demo.pcapng -Y 'tcp.analysis.duplicate_ack'`:<br />
![image](https://github.com/user-attachments/assets/84e164c0-6a36-424f-99ed-f2cd38e908b9)<br />
`37`

# Nmap Basic Port Scans

### TCP and UDP Ports
- Which service uses UDP port 53 by default? `DNS`
- Which service uses TCP port 22 by default? `SSH`
- How many port states does Nmap consider? `6`
- Which port state is the most interesting to discover as a pentester? `Open`

### TCP Flags
- What 3 letters represent the Reset flag? `RST`
- Which flag needs to be set when you initiate a TCP connection (first packet of TCP 3-way handshake)? `SYN`

### TCP Connect Scan
- Launch the VM. Open the AttackBox and execute nmap -sT 10.10.39.247 via the terminal. A new service has been installed on this VM since our last scan. Which port number was closed in the scan above but is now open on this target VM? <br />
![image](https://github.com/user-attachments/assets/94cb0370-1125-4811-b972-9a6b91cff6f9)<br />
`110`
- What is Nmap’s guess about the newly installed service? `POP3`

### TCP SYN Scan
- Launch the VM. Some new server software has been installed since the last time we scanned it. On the AttackBox, use the terminal to execute nmap -sS 10.10.39.247. What is the new open port?<br />
![image](https://github.com/user-attachments/assets/87c06743-c01b-4ca5-a881-3997b4dde227)<br />
`6667`
- What is Nmap’s guess of the service name? `IRC`

### UDP Scan
- Launch the VM. On the AttackBox, use the terminal to execute nmap -sU -F -v 10.10.39.247. A new service has been installed since the last scan. What is the UDP port that is now open? <br />
![image](https://github.com/user-attachments/assets/f8700b44-465f-425c-80b0-0fc0f7334c38)<br />
`53`
- What is the service name according to Nmap? `domain`

### Fine-Tuning Scope and Performance 
- What is the option to scan all the TCP ports between 5000 and 5500? `-p5000-5500`
- How can you ensure that Nmap will run at least 64 probes in parallel? `--min-parallelism=64`
- What option would you add to make Nmap very slow and paranoid? `-T0` <br />
To avoid IDS alerts, -T0 scans one port at a time and waits 5 minutes between sending each probe, lol

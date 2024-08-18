# Nmap

### Introduction
- What networking constructs are used to direct traffic to the right application on a server? `Ports`<br />
- How many of these are available on any network-enabled computer? `65535`<br />
- [Research] How many of these are considered "well-known"? (These are the "standard" numbers mentioned in the task) `1024`<br />

### Nmap Switches
- What is the first switch listed in the help menu for a 'Syn Scan' (more on this later!)? `-sS`<br />
- Which switch would you use for a "UDP scan"? `-sU`<br />
- If you wanted to detect which operating system the target is running on, which switch would you use? `-O`<br />
- Nmap provides a switch to detect the version of the services running on the target. What is this switch? `-sV`<br />
- The default output provided by nmap often does not provide enough information for a pentester. How would you increase the verbosity? `-v`<br />
- Verbosity level one is good, but verbosity level two is better! How would you set the verbosity level to two?(Note: it's highly advisable to always use at least this option) `-vv`<br />
- What switch would you use to save the nmap results in three major formats? `-oA`<br />
- What switch would you use to save the nmap results in a "normal" format? `-oN`<br />
- A very useful output format: how would you save results in a "grepable" format? `-oG`<br />
- Sometimes the results we're getting just aren't enough. If we don't care about how loud we are, we can enable "aggressive" mode. This is a shorthand switch that activates service detection, operating system detection, a traceroute and common script scanning. How would you activate this setting? `-A`<br />
- How would you set the timing template to level 5? `-T5`<br />
- How would you tell nmap to only scan port 80? `-p 80`<br />
- How would you tell nmap to scan ports 1000-1500? `-p 1000-1500`<br />
- How would you tell nmap to scan all ports? `-p-`<br />
- How would you activate a script from the nmap scripting library (lots more on this later!)? `--script`<br />
- How would you activate all of the scripts in the "vuln" category? `--script=vuln`<br />

### Overview
- Read the Scan Types Introduction. `No answers needed`<br />

### TCP Connect Scans
- Which RFC defines the appropriate behaviour for the TCP protocol? `RFC 9293`<br />
- If a port is closed, which flag should the server send back to indicate this? `RST`<br />

### SYN Scans
- There are two other names for a SYN scan, what are they? `Half-Open, Stealth`<br />
- Can Nmap use a SYN scan without Sudo permissions (Y/N)? `N`<br />

### UDP Scans
- If a UDP port doesn't respond to an Nmap scan, what will it be marked as? `open|filtered`<br />
- When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so? `ICMP`<br />

### NULL, FIN and Xmas
- Which of the three shown scan types uses the URG flag? `xmas`<br />
- Why are NULL, FIN and Xmas scans generally used? `Firewall Evasion`<br />
- Which common OS may respond to a NULL, FIN or Xmas scan with a RST for every port? `Microsoft Windows`<br />

### ICMP Network Scanning
- How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation) `nmap -sn 172.16.0.0/16`<br />

### Overview
- What language are NSE scripts written in? `Lua`<br />
- Which category of scripts would be a very bad idea to run in a production environment? `intrusive`<br />

### Working with the NSE
- What optional argument can the ftp-anon.nse script take? `maxlist`<br />

### Searching for Scripts
- Search for "smb" scripts in the /usr/share/nmap/scripts/ directory using either of the demonstrated methods. What is the filename of the script which determines the underlying OS of the SMB server? `smb-os-discovery.nse`<br />
- Read through this script. What does it depend on? `smb-brute`<br />

### Firewall Evasion
- Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the -Pn switch? `ICMP`<br />
- [Research] Which Nmap switch allows you to append an arbitrary length of random data to the end of packets? `--data-length`<br />

### Practical
- Does the target ip respond to ICMP echo (ping) requests (Y/N)? `N`<br />
- Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered? `999`<br />
- There is a reason given for this -- what is it? Note: The answer will be in your scan results. Think carefully about which switches to use -- and read the hint before asking for help! `No Response`<br />
- Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open? `5`<br />
- Open Wireshark (see Cryillic's Wireshark Room for instructions) and perform a TCP Connect scan against port 80 on the target, monitoring the results. Make sure you understand what's going on. Deploy the ftp-anon script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N) `Y`<br />

# Introductory Networking

### The OSI Model: An Overview
- Which layer would choose to send data over TCP or UDP? `4`<br />
- Which layer checks received information to make sure that it hasn't been corrupted? `2`<br />
- In which layer would data be formatted in preparation for transmission? `2`<br />
- Which layer transmits and receives data? `1`<br />
- Which layer encrypts, compresses, or otherwise transforms the initial data to give it a standardised format? `6`<br />
- Which layer tracks communications between the host and receiving computers? `5`<br />
- Which layer accepts communication requests from applications? `7`<br />
- Which layer handles logical addressing? `3`<br />
- When sending data over TCP, what would you call the "bite-sized" pieces of data? `Segments`<br />
- [Research] Which layer would the FTP protocol communicate with? `7`<br />
- Which transport layer protocol would be best suited to transmit a live video? `UDP`<br />

### Encapsulation
- How would you refer to data at layer 2 of the encapsulation process (with the OSI model)? `Frames`<br />
- How would you refer to data at layer 4 of the encapsulation process (with the OSI model), if the UDP protocol has been selected? `Datagrams`<br />
- What process would a computer perform on a received message? `De-encapsulation`<br />
- Which is the only layer of the OSI model to add a trailer during encapsulation? `Data Link`<br />
- Does encapsulation provide an extra layer of security (Aye/Nay)? `Aye`<br />

### The TCP/IP Model
- Which model was introduced first, OSI or TCP/IP? `TCP/IP`<br />
- Which layer of the TCP/IP model covers the functionality of the Transport layer of the OSI model (Full Name)? `Transport`<br />
- Which layer of the TCP/IP model covers the functionality of the Session layer of the OSI model (Full Name)? `Application`<br />
- The Network Interface layer of the TCP/IP model covers the functionality of two layers in the OSI model. These layers are Data Link, and?.. (Full Name)? `Physical`<br />
- Which layer of the TCP/IP model handles the functionality of the OSI network layer? `Internet`<br />
- What kind of protocol is TCP? `Connection-based`<br />
- What is SYN short for? `Synchronise`<br />
- What is the second step of the three way handshake? `SYN/ACK`<br />
- What is the short name for the "Acknowledgement" segment in the three-way handshake? `ACK`<br />

### Ping
- What command would you use to ping the bbc.co.uk website? `ping bbc.co.uk`<br />
- Ping muirlandoracle.co.uk. What is the IPv4 address? `217.160.0.152`<br />
- What switch lets you change the interval of sent ping requests? `-i`<br />
- What switch would allow you to restrict requests to IPv4? `-4`<br />
- What switch would give you a more verbose output? `-v`<br />

### Traceroute
- Use traceroute on tryhackme.com. Can you see the path your request has taken? `No answer needed`<br />
- What switch would you use to specify an interface when using Traceroute? `-i`<br />
- What switch would you use if you wanted to use TCP SYN requests when tracing the route? `-T`<br />
- [Lateral Thinking] Which layer of the TCP/IP model will traceroute run on by default (Windows)? `Internet`<br />

### WHOIS
- Perform a whois search on facebook.com `No answer needed`<br />
- What is the registrant postal code for facebook.com? `94025`<br />
- When was the facebook.com domain first registered (Format: DD/MM/YYYY)? `29/03/1997`<br />
- Perform a whois search on microsoft.com. (Note: Please ensure you have read the task above before attempting the next questions.) `No answer needed`<br />
- Which city is the registrant based in? `Redmond`<br />
- [OSINT] What is the name of the golf course that is near the registrant address for microsoft.com? `Bellevue Golf Course`<br />
- What is the registered Tech Email for microsoft.com? `msnhst@microsoft.com`<br />

### Dig
- What is DNS short for? `Domain Name System`<br />
- What is the first type of DNS server your computer would query when you search for a domain? `Recursive`<br />
- What type of DNS server contains records specific to domain extensions (i.e. .com, .co.uk*, etc)*? Use the long version of the name. `Top-Level Domain`<br />
- Where is the very first place your computer would look to find the IP address of a domain? `Hosts File`<br />
- [Research] Google runs two public DNS servers. One of them can be queried with the IP 8.8.8.8, what is the IP address of the other one? `8.8.4.4`<br />
- If a DNS query has a TTL of 24 hours, what number would the dig query show? `86400`<br />

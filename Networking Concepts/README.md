# Networking Concepts

### OSI Model
- Which layer is responsible for connecting one application to another? `4`
- Which layer is responsible for routing packets to the proper network? `3`
- In the OSI model, which layer is responsible for encoding the application data? `6`
- Which layer is responsible for transferring data between hosts on the same network segment? `2`

### TCP/IP Model
- To which layer does HTTP belong in the TCP/IP model? `Application Layer`
- How many layers of the OSI model does the application layer in the TCP/IP model cover? `3`

### IP Addresses and Subnets
- Which of the following IP addresses is not a private IP address? ... `49.69.147.197`
- Which of the following IP addresses is not a valid IP address? ... `192.168.305.19`

### UDP and TCP
- Which protocol requires a three-way handshake? `TCP`
- What is the approximate number of port numbers (in thousands)? `65`

### Encapsulation
- On a WiFi, within what will an IP packet be encapsulated? `Frame`
- What do you call the UDP data unit that encapsulates the application data? `Datagram`
- What do you call the data unit that encapsulates the application data sent over TCP? `Segment`
 
### Telnet
- Use telnet to connect to the web server on 10.10.250.142. What is the name and version of the HTTP server?<br />
Run `telnet 10.10.250.142 80`, and then prompt:

      GET / HTTP/1.1
      Host: telnet.thm
![image](https://github.com/user-attachments/assets/44f2389f-26f8-4f4b-a6bc-879cb74afbec)<br />
`lighttpd/1.4.63`
- What flag did you get when you viewed the page? `THM{TELNET_MASTER}`

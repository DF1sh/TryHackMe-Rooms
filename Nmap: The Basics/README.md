# Nmap: The Basics

### Host Discovery: Who Is Online
- What is the last IP address that will be scanned when your scan target is 192.168.0.1/27?
Run `nmap -sL 192.168.0.1/27` to get the answer: <br />
`192.168.0.31`

### Port Scanning: Who Is Listening
- How many TCP ports are open on the target system at 10.10.24.178?<br />
![image](https://github.com/user-attachments/assets/6f95a6f4-5dae-4572-be40-421b66dee1f6)<br />
`6`
- Find the listening web server on 10.10.24.178 and access it with your browser. What is the flag that appears on its main page? <br />
Open a browser and visit `http://10.10.24.178:8008` to get the answer<br />
`THM{SECRET_PAGE_38B9P6}`

### Version Detection: Extract More Information
- What is the name and detected version of the web server running on 10.10.24.178? <br />
![image](https://github.com/user-attachments/assets/fd0a3651-ab2f-4195-8045-31239e7dfa05)<br />
`lighttpd 1.4.74`

### Timing: How Fast is Fast
- What is the non-numeric equivalent of -T4? `-T aggressive` <br />
By the way this is a very interesting table:<br />
![image](https://github.com/user-attachments/assets/2c96bf56-ba59-4db7-8f5e-81fcce1dde2f)<br />


### Output: Controlling What You See
- What option must you add to your nmap command to enable debugging? `-d`

### Conclusion and Summary
- What kind of scan will Nmap use if you run nmap 10.10.24.178 with local user privileges? `Connect Scan` <br />

This was new to me: "Nmap would automatically use SYN scan (-sS) if you are running it with sudo privileges and will default to connect scan (-sT) if run as a local user." Good to know

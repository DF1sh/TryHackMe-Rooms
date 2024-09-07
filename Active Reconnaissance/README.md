# Active Reconnaissance

### Web Browser
- Browse to the following website and ensure that you have opened your Developer Tools on AttackBox Firefox, or the browser on your computer. Using the Developer Tools, figure out the total number of questions.
Open the given web page, inspect the source code and view the script.js, scroll down to find the answer: <br />
![image](https://github.com/user-attachments/assets/19a6b52e-0e44-4ab5-8401-4e0b01d40d7c)<br />
`8`

### Ping
- Which option would you use to set the size of the data carried by the ICMP echo request? `-s`
- What is the size of the ICMP header in bytes? <br />
![image](https://github.com/user-attachments/assets/053015c5-42ae-445f-88cb-155afca96bbc)<br />
`8`
- Does MS Windows Firewall block ping by default? (Y/N) `Y`
- Deploy the VM for this task and using the AttackBox terminal, issue the command ping -c 10 MACHINE_IP. How many ping replies did you get back? <br />
![image](https://github.com/user-attachments/assets/2cd247de-9cb8-426b-aabe-985a8d97a10e)<br />
`10`

### Traceroute
- In Traceroute A, what is the IP address of the last router/hop before reaching tryhackme.com?
![image](https://github.com/user-attachments/assets/ec4d61c2-54b7-43e4-ac6c-e7c77eccd3ab)<br />
`172.67.69.208`
- In Traceroute B, what is the IP address of the last router/hop before reaching tryhackme.com? <br />
![image](https://github.com/user-attachments/assets/aa20f94c-36f7-4877-ba4b-79bb7cb3011e)<br />
`104.26.11.229`
- In Traceroute B, how many routers are between the two systems? `26`

### Telnet
- Start the attached VM from Task 3 if it is not already started. On the AttackBox, open the terminal and use the telnet client to connect to the VM on port 80. What is the name of the running server? 
![image](https://github.com/user-attachments/assets/29aed172-887d-45c6-9235-6d2f9080cea8)<br />
`Apache`
- What is the version of the running server (on port 80 of the VM)? `2.4.61`

### Netcat
- Start the VM and open the AttackBox. Once the AttackBox loads, use Netcat to connect to the VM port 21. What is the version of the running server? <br />
![image](https://github.com/user-attachments/assets/028a5fd4-d5a4-4947-b4d0-54b516cde6a4)<br />
`0.17`

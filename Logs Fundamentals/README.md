# Logs Fundamentals

### Introduction to Logs
- Where can we find the majority of attack traces in a digital system? `Logs`

### Types of Logs
- Which type of logs contain information regarding the incoming and outgoing traffic in the network? `Network Logs`
- Which type of logs contain the authentication and authorization events? `Security Logs`

### Windows Event Logs Analysis
- What is the name of the last user account created on this system?<br />
Open Event Viewer and filter by Event ID = 4720: <br />
![image](https://github.com/user-attachments/assets/ce6f2301-2378-4306-b322-caa325e367d5)<br />
`hacked`
- Which user account created the above account?<br />
`Administrator`
- On what date was this user account enabled? Format: M/D/YYYY <br />
`6/7/2024`
- Did this account undergo a password reset as well? Format: Yes/No <br />
Now filter by Event ID = 4724: <br />
![image](https://github.com/user-attachments/assets/7a181344-cc5e-42de-8064-0fc2dc833f03)<br />
`Yes`

### Web Server Access Logs Analysis
- What is the IP which made the last GET request to URL: “/contact”? <br />
![image](https://github.com/user-attachments/assets/81f34293-0ebb-425d-bb0d-4c810c99fd4d)<br />
`10.0.0.1`
- When was the last POST request made by IP: “172.16.0.1”?<br />
![image](https://github.com/user-attachments/assets/d0cee7c9-e7d9-4d82-8e2a-eb7052b0b338)<br />
`06/Jun/2024:13:55:44`
- Based on the answer from question number 2, to which URL was the POST request made?<br />
`/contact`

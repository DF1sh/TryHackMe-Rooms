# ItsyBitsy

### Scenario - Investigate a potential C2 communication alert
- How many events were returned for the month of March 2022?<br />
![image](https://github.com/user-attachments/assets/7ea8d1cc-2c0d-4534-be5d-568f633d4753)<br />
`1482`
- What is the IP associated with the suspected user in the logs? <br />
![image](https://github.com/user-attachments/assets/63ec00a1-7a4f-49be-ac73-c2ab928cf566)<br />
`192.166.65.54`
- The user’s machine used a legit windows binary to download a file from the C2 server. What is the name of the binary?<br />
![image](https://github.com/user-attachments/assets/74501114-d5ff-4d51-883b-be98428ab384)<br />
`bitsadmin`
- The infected machine connected with a famous filesharing site in this period, which also acts as a C2 server used by the malware authors to communicate. What is the name of the filesharing site?<br />
Add the filter `user_agent :"bitsadmin"`:<br />
![image](https://github.com/user-attachments/assets/0fdc2b07-53c4-49a5-9610-823974bdf9d3)<br />
`pastebin.com`
- What is the full URL of the C2 to which the infected host is connected?<br />
![image](https://github.com/user-attachments/assets/d6653b7c-5b53-414c-a56e-7322674e9401)<br />
`pastebin.com/yTg0Ah6a`
- A file was accessed on the filesharing site. What is the name of the file accessed?<br />
Go to `pastebin.com/yTg0Ah6a`:<br />
![image](https://github.com/user-attachments/assets/28e3ab98-b3e7-4e5a-bf17-ddc16439c68e)<br />
`secret.txt`
- The file contains a secret code with the format THM{_____}. `THM{SECRET__CODE}`

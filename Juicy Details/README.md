# Juicy Details

### Reconnaissance
- What tools did the attacker use? (Order by the occurrence in the log)<br />
For this one I had to manually check the `access.log` file to find the names of the tools: `nmap, hydra, sqlmap, curl, feroxbuster`
- What endpoint was vulnerable to a brute-force attack? <br />
![image](https://github.com/user-attachments/assets/bd59779c-395d-4ea8-adac-590c24ffa712)<br />
`/rest/user/login`
- What endpoint was vulnerable to SQL injection?<br />
![image](https://github.com/user-attachments/assets/2b40f0c1-4299-4294-8bff-203c2650f0fa)<br />
`/rest/products/search`
- What parameter was used for the SQL injection? `q`
- What endpoint did the attacker try to use to retrieve files? (Include the /)<br />
The attacker downloaded some files from the FTP server, located at `/ftp`:<br />


### Stolen data
- What section of the website did the attacker use to scrape user email addresses?
- Was their brute-force attack successful? If so, what is the timestamp of the successful login? (Yay/Nay, 11/Apr/2021:09:xx:xx +0000)
- What user information was the attacker able to retrieve from the endpoint vulnerable to SQL injection?
- What files did they try to download from the vulnerable endpoint? (endpoint from the previous task, question #5) 
- What service and account name were used to retrieve files from the previous question? (service, username)
- What service and username were used to gain shell access to the server? (service, username)

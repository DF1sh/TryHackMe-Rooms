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
![image](https://github.com/user-attachments/assets/cd08c956-0d73-4a0e-b207-eb242f0b34d6)<br />

### Stolen data
- What section of the website did the attacker use to scrape user email addresses? `product reviews`
- Was their brute-force attack successful? If so, what is the timestamp of the successful login? (Yay/Nay, 11/Apr/2021:09:xx:xx +0000)<br />
Do a `cat access.log | grep Hydra` and take the timestamp of the last POST request.<br />
`Yay, 11/Apr/2021:09:16:31 +0000`
- What user information was the attacker able to retrieve from the endpoint vulnerable to SQL injection?<br />
Run `cat access.log | grep search`
![image](https://github.com/user-attachments/assets/ac89097e-0a08-4fce-9f7f-254794301904)<br />
`email, password`
- What files did they try to download from the vulnerable endpoint? (endpoint from the previous task, question #5) `coupons_2013.md.bak, www-data.bak`
- What service and account name were used to retrieve files from the previous question? (service, username) `ftp, anonymous`
- What service and username were used to gain shell access to the server? (service, username)<br />
The `auth.log` files contains ssh login attempts to the used www-data.<br />
`ssh, www-data`

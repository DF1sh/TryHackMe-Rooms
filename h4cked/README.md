![image](https://github.com/user-attachments/assets/bbdef18c-c80a-4946-97cb-1a179684eab9)# h4cked

### Oh no! We've been hacked!
- The attacker is trying to log into a specific service. What service is this? `ftp`
- There is a very popular tool by Van Hauser which can be used to brute force a series of services. What is the name of this tool? `Hydra`
- The attacker is trying to log on with a specific username. What is the username?<br />
![image](https://github.com/user-attachments/assets/e7f1a16e-f9cc-43fc-8a2f-efa72e8ca08d)<br />
`jenny`
- What is the user's password?<br />
![image](https://github.com/user-attachments/assets/6a10396a-a98e-47fe-9507-1ff6f90f2ae1)<br />
`password123`
- What is the current FTP working directory after the attacker logged in?<br />
![image](https://github.com/user-attachments/assets/be6c8727-32d3-4595-a97e-af323323cda3)<br />
`/var/www/html`
- The attacker uploaded a backdoor. What is the backdoor's filename? `shell.php`
- The backdoor can be downloaded from a specific URL, as it is located inside the uploaded file. What is the full URL?<br />
![image](https://github.com/user-attachments/assets/ed19c533-6367-4a4c-8100-5b6b556b2200)<br />
`http://pentestmonkey.net/tools/php-reverse-shell `
- Which command did the attacker manually execute after getting a reverse shell?
![image](https://github.com/user-attachments/assets/62a644db-0b25-4b29-9ea6-67c48b2f7975)<br />
- `whoami`
- What is the computer's hostname? `wir3`
- Which command did the attacker execute to spawn a new TTY shell?<br />
![image](https://github.com/user-attachments/assets/06eadbbc-9bef-4075-ac42-dcde403c0028)<br />
`python3 -c 'import pty; pty.spawn("/bin/bash")'`
- Which command was executed to gain a root shell? `sudo su`
- The attacker downloaded something from GitHub. What is the name of the GitHub project?<br />
![image](https://github.com/user-attachments/assets/605a2e03-8cff-4564-bcdf-9125072d1696)<br />
`Reptile`
- The project can be used to install a stealthy backdoor on the system. It can be very hard to detect. What is this type of backdoor called? `Rootkit`

### Hack your way back into the machine
- Read the flag.txt file inside the Reptile directory<br />
First of all I bruteforce the login on FTP:<br />
![image](https://github.com/user-attachments/assets/29609fc6-5616-47cd-940a-758103d09f63)<br />
Then update the shell.php file to connect to your IP address, open a netcat listener and get the flag!

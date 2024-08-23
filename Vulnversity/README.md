# Vulnversity

### Reconnaissance
- Scan the box; how many ports are open? `6` <br />
- What version of the squid proxy is running on the machine? `3.5.12` <br />
- How many ports will Nmap scan if the flag -p-400 was used? `400` <br />
- What is the most likely operating system this machine is running? `Ubuntu` <br />
- What port is the web server running on? `6` <br />
- What is the flag for enabling verbose mode using Nmap? `-v` <br />

### Locating directories using Gobuster
- What is the directory that has an upload form page? `/internal/` <br />

### Compromise the Webserver
- What common file type you'd want to upload to exploit the server is blocked? Try a couple to find out. `.php` <br />
- What extension is allowed after running the above exercise? `.phtml` <br />
- What is the name of the user who manages the webserver? `bill` <br />
- What is the user flag? `8bd7992fbe8a6ad22a63361004cfcedb` <br />

### Privilege Escalation
- On the system, search for all SUID files. Which file stands out? `/bin/systemctl` <br />
- What is the root flag value? `a58ff8579f0a9270368d33a9966c7fd5` <br />

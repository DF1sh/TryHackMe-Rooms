# Linux Fundamentals Part 3

### Terminal Text Editors
- Edit "task3" located in "tryhackme"'s home directory using Nano. What is the flag? `THM{TEXT_EDITORS}` <br />

### General/Useful Utilities
- Download the file http://MACHINE_IP:8000/.flag.txt onto the TryHackMe AttackBox. Remember, you will need to do this in a new terminal.
What are the contents? `THM{WGET_WEBSERVER}` <br />

### Processes 101
- If we were to launch a process where the previous ID was "300", what would the ID of this new process be? `301` <br />
- If we wanted to cleanly kill a process, what signal would we send it? `SIGTERM` <br />
- Locate the process that is running on the deployed instance (MACHINE_IP). What flag is given? `THM{PROCESSES}` <br />
- What command would we use to stop the service "myservice"? `systemctl stop myservice` <br />
- What command would we use to start the same service on the boot-up of the system? `systemctl enable myservice` <br />
- What command would we use to bring a previously backgrounded process back to the foreground? `fg` <br />

### Maintaining Your System: Automation
- When will the crontab on the deployed instance (MACHINE_IP) run? `@reboot` <br />

### Maintaining Your System: Logs
- What is the IP address of the user who visited the site? `10.9.232.111` <br />
- What file did they access? `catsanddogs.jpg` <br />

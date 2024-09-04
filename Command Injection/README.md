# Command Injection

### Discovering Command Injection
- What variable stores the user's input in the PHP code snippet in this task? `$title`
- What HTTP method is used to retrieve data submitted by a user in the PHP code snippet? `GET`
- If I wanted to execute the id command in the Python code snippet, what route would I need to visit? `/id`

### Exploiting Command Injection
- What payload would I use if I wanted to determine what user the application is running as? `whoami`
- What popular network tool would I use to test for blind command injection on a Linux machine? `ping`
- What payload would I use to test a Windows machine for blind command injection? `timeout`

### Remediating Command Injection
- What is the term for the process of "cleaning" user input that is provided to an application? `sanitisation`

### Practical: Command Injection (Deploy)
- What user is this application running as? <br />
![image](https://github.com/user-attachments/assets/16d66c80-ab70-4dd6-b5cd-fc8d5b58a570)<br />
`www-data`
- What are the contents of the flag located in /home/tryhackme/flag.txt? <br />
![image](https://github.com/user-attachments/assets/8d92eae9-5e66-48f2-8ce5-0936b948b82c) <br />
`THM{COMMAND_INJECTION_COMPLETE}`

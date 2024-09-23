# Linux Forensics

### OS and account information
- Which two users are the members of the group audio? <br />
![image](https://github.com/user-attachments/assets/f3930074-1c73-4a7c-bac9-cd49776ddb32)<br />
`ubuntu,pulse`
- In the attached VM, there is a user account named tryhackme. What is the uid of this account?<br />
![image](https://github.com/user-attachments/assets/20551591-ef3b-4bc0-a869-dd347dfbc125)<br />
`1001`
- A session was started on this machine on Sat Apr 16 20:10. How long did this session last?<br />
![image](https://github.com/user-attachments/assets/ec13e439-ff9e-4a25-8b44-ec6d285dc4a8)<br />
`01:32`

### System Configuration
- What is the hostname of the attached VM?<br />
![image](https://github.com/user-attachments/assets/7d3f86f2-aabf-4e9b-bb49-65bab5f6ff8f)<br />
`Linux4n6`
- What is the timezone of the attached VM?<br />
![image](https://github.com/user-attachments/assets/06de95ff-0a44-4a6f-902d-fc1b9711b705)<br />
`sia/Karachi`
- What program is listening on the address 127.0.0.1:5901?<br />
![image](https://github.com/user-attachments/assets/4c635d91-eb44-4a20-80f6-fda0fdb9e7ac)<br />
`Xtigervnc`
- What is the full path of this program?<br />
![image](https://github.com/user-attachments/assets/fdfb55ae-59a0-4735-b843-cd0a03ee1f69)<br />
`/usr/bin/Xtigervnc`

### Persistence mechanisms
- In the bashrc file, the size of the history file is defined. What is the size of the history file that is set for the user Ubuntu in the attached machine?<br />
Run `cat .bashrc` and read through the output to find the answer: <br />
![image](https://github.com/user-attachments/assets/3396e969-4487-4962-92ca-033b58391135)<br />
`2000`

### Evidence of Execution
- The user tryhackme used apt-get to install a package. What was the command that was issued?<br />
Move to `/home/tryhackme/` and run `sudo cat .bash_history`:<br />
![image](https://github.com/user-attachments/assets/4970b960-e7b4-458c-bebe-2d2f89c94f68)<br />
`sudo apt-get install apache2`
- What was the current working directory when the command to install net-tools was issued?<br />
Move to `/home/ubuntu` and read through the .bash_history file. There are no `cd` commands, so the directory working directory didn't change.<br />
`/home/ubuntu`

### Log files
- Though the machine's current hostname is the one we identified in Task 4. The machine earlier had a different hostname. What was the previous hostname of the machine?<br />
The command that I used is `cat /var/log/syslog | head`:<br />
![image](https://github.com/user-attachments/assets/06b8adb9-686a-497c-9a37-17f8908c2a59)<br />
`tryhackme`

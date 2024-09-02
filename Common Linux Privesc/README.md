# Common Linux Privesc

### Enumeration
- What is the target's hostname? <br />
Login through ssh with credentials user3:password. <br />
![image](https://github.com/user-attachments/assets/ae64269c-989d-4e83-b07b-6f6951ad177f)
`polobox`
- Look at the output of /etc/passwd how many "user[x]" are there on the system? <br />
![image](https://github.com/user-attachments/assets/a5150043-3a76-4187-b3a8-e49ffd20461e)<br />
`8`
- How many available shells are there on the system? <br />
![image](https://github.com/user-attachments/assets/ddf941f4-efa0-4e6c-bf3c-2f34cd6cdc03)<br />
`4`
- What is the name of the bash script that is set to run every 5 minutes by cron? <br />
Run `cat /etc/crontab` to get the answer: `autoscript.sh`
- What critical file has had its permissions changed to allow some users to write to it? `/etc/passwd`

### Abusing SUID/GUID Files
- What is the path of the file in user3's directory that stands out to you? <br />
Run `find / -perm -04000 2>/dev/null` to find out: `/home/user3/shell`

### Exploiting Writeable /etc/passwd 
- Having read the information above, what direction privilege escalation is this attack? `vertical`
- Before we add our new user, we first need to create a compliant password hash to add! We do this by using the command: "openssl passwd -1 -salt [salt] [password]". What is the hash created by using this command with the salt, "new" and the password "123"? <br />
Run `openssl passwd -1 -salt "new" "123"` to create the hash: `$1$new$p7ptkEKU1HnaHpRtzNizS1`
- Great! Now we need to take this value, and create a new root user account. What would the /etc/passwd entry look like for a root user with the username "new" and the password hash we created before. `new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash`

### Escaping Vi Editor
- Let's use the "sudo -l" command, what does this user require (or not require) to run vi as root? <br />
![image](https://github.com/user-attachments/assets/f6b6bd1e-d27c-4d17-ab41-0d162746d9b2) <br />
`NOPASSWD`

### Exploiting Crontab
- What is the flag to specify a payload in msfvenom? `p`
- What directory is the "autoscript.sh" under? `/home/user4/Desktop`

### Exploiting PATH Variable
- Let's go to user5's home directory, and run the file "script". What command do we think that it's executing? `ls`
- Now we're inside tmp, let's create an imitation executable. The format for what we want to do is: echo "[whatever command we want to run]" > [name of the executable we're imitating]. What would the command look like to open a bash shell, writing to a file with the name of the executable we're imitating `echo "/bin/bash" > ls`
- Great! Now w e've made our imitation, we need to make it an executable. What command do we execute to do this? `chmod +x ls`

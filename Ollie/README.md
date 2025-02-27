# Ollie

### Ollie
Nmap scan shows ports 22,80 and 1337 open. 
Port 80 contains phpIPAM 1.4.5 login page. I found [here](https://www.exploit-db.com/exploits/50963) that this version is vulnerable to authenticated remote code execution. So I need to log in. Port 1337 actually gives me the right credentials. You just have to say that ollie is a bulldog!.<br />
After logging in, I run the above exploit and get access to www-data. Right after that, I re-used the same password found on port 1337 to access ollie's account with `su ollie`. This gives me the user flag. For privesc, I was stuck for about two hours. My last weapon was to use pspy64 to check if there were any hidden cronjohs or services. And I actually found something interesting:<br />
![image](https://github.com/user-attachments/assets/f2745a87-497b-4caf-a8c8-9bf38a5cfdc9)<br />
Also if I run `grep -i feedme /var/log/syslog` I see that there are a lot of instances of this service in the logs. So I guess it's like a cronjob. To see what this service is doing, run `systemctl cat feedme.service`:<br />
![image](https://github.com/user-attachments/assets/e27ae529-8f65-4cc4-b6da-2b6112b11f27)<br />
It's executing `/usr/bin/feedme`. I have write permission on that file, so I simply add a reverse shell on it:<br />
![image](https://github.com/user-attachments/assets/511434bb-6ab7-40d5-bcd0-ebf35d98ec9f)<br />
Then I listen on port 9001 on my attack box and wait for the root reverse shell. This gets me the root flag.

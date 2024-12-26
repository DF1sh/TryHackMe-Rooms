# Lesson Learned?

### Find the Flag
- What's the flag?<br />
The solution to this challenge is to exploit the answer of the server to a failed login attempt. If I try to submit random credentials: <br />
![image](https://github.com/user-attachments/assets/50a79201-cec7-4354-8f27-cb2866c26443)<br />
The server responds with "Invalid username and password". My guess is that if I submit a valid username, but the wrong password, the server will respond something like "Invalid password". To enumerate users I will use `hydra`. The idea is to bruteforce
the login page trying every user with the same password "password", and if the server responds with "Invalid username and password" the username is not valid, but if it responds with something different than that, then the username might be right.
The command to do that is the following: `ydra -L /usr/share/wordlists/SecLists/Usernames/Names/names.txt -p password 10.10.205.143 http-post-form "/:username=^USER^&password=password:Invalid username and password"`. This command tells hydra to ignore every
username that generates this response, and to display everything else. <br />
![image](https://github.com/user-attachments/assets/83bf15c6-fbe9-4e85-b6ec-51e210535c37)<br />
There we go, `arnold` is a valid username! Let's now try to bruteforce his password in a similar fashion. If I use the username `arnold`, this is the answer of the server: <br />
![image](https://github.com/user-attachments/assets/232f0e5d-7525-4523-b362-f447e5d667a8)<br />
"Invalid password". So the new command should be `hydra -l arnold -P /usr/share/wordlists/rockyou.txt 10.10.205.143 http-post-form "/:username=arnold&password=^PASS^:Invalid password"`. However this bruteforce didn't work. I waited about 20 minutes but didn't find any password. 
So i tried to run again the user enumeration command, and found out that there are actually much more valid users: <br />
![image](https://github.com/user-attachments/assets/7e59a083-2bdd-416d-8add-ad3e3aa17832)<br />
Well, time to try to bruteforce every single one of them D: I'll give 5 minutes each at maximum. Let's see how it goes.<br />
NOTHING WORKED.
I then tried running sqlmap and after a while found this message: <br />
![image](https://github.com/user-attachments/assets/966f74fd-0c96-4206-8adb-b3c026e48691)<br />
So apparently this is an SQLi vulnerability, but I can't use sqlmap because it submits `OR 1=1`. I restart the machine and do it manually. The following worked for me:

      username: kelly'#
      password: asd
![image](https://github.com/user-attachments/assets/9b2688b8-17b6-4896-9ea5-4d958f0372e5)<br />





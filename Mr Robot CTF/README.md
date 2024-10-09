# Mr Robot CTF

### Hack the machine
- What is key 1?<br />

Initial scan: 

    nmap 10.10.50.111 
    Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-07 08:56 EDT
    Nmap scan report for 10.10.50.111
    Host is up (0.15s latency).
    Not shown: 997 filtered tcp ports (no-response)
    PORT    STATE  SERVICE
    22/tcp  closed ssh
    80/tcp  open   http
    443/tcp open   https
Enumerate the webserver, and find `robots.txt`:<br />
![image](https://github.com/user-attachments/assets/ac2da683-6f9e-40f6-b9e4-1b29f50feaba)<br />
key 1 = `073403c8a58a1f80d943455fb30724b9` 

- What is key 2? <br />
The other file, `fsocity.dic` contains a wordlist. This wordlist can be used to enumerate correct usernames. This is because the webpage responds "incorrect username" if the username is not correct:<br />
![image](https://github.com/user-attachments/assets/81509d1f-7c5c-4e55-b063-21ff9500bb93)<br />
And "incorrect password" if the username is correct, but the password is not:<br />
![image](https://github.com/user-attachments/assets/09f241e2-f05f-4d40-a9de-dc5ff079bf4d)<br />
`Elliot` is a valid username. Moreover, when exploring directories with gobuster, `/license` exposed a base64 encoded password: <br />
![image](https://github.com/user-attachments/assets/effd9274-62b0-4a1f-ab49-e5f844b991dd)<br />
The decoded value is `elliot:ER28-0652`. These are the credentials to log in the admin panel. To get a reverse shell, upload a php shell inside `Themes->editor->search.php`. The reverse shell I uploaded is from pentest monkey and can be found in `rev.php` of this folder.<br />
![image](https://github.com/user-attachments/assets/287c3013-da1e-4a11-b6d6-132e1ee59ded)<br />
We are logged as user `daemon` and have access to `robot`'s home directory, but can't access key2of3.txt, but we have access to what looks to be a hashed password.<br />
![image](https://github.com/user-attachments/assets/ebbe805c-896e-4914-b837-40533b94dce1)<br />
he command to crack it is `john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`:<br />
![image](https://github.com/user-attachments/assets/e4a33e46-59ea-4d60-a1b7-0869aac6e50e)<br />
The credentials are `robot:abcdefghijklmnopqrstuvwxyz`. Thus we have key 2: `822c73956184f694993bede3eb39f959`

- What is key 3? <br />
Running `find / -perm -04000 2>/dev/null` there's an interesting SUID binary<br />
![image](https://github.com/user-attachments/assets/81d223be-a433-47c4-b016-716495e64f04)<br />
The SUID on nmap can be easily exploited with `nmap --interactive`:<br />
![image](https://github.com/user-attachments/assets/b15efcc0-7311-4fe5-8888-82e7b1e494c9)<br />
Thus, we can access key 3 inside /root: <br />
![image](https://github.com/user-attachments/assets/9bdad738-8989-4425-8fc0-19a6ae5da27e)<br />
`04787ddef27c3dee1ee161b21670b4e4`


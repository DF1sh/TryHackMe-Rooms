# Startup

### Startup
Nmap scan shows ports 21,22 and 80 open. FPT server allows anonymous login and contains two files: <br />
![image](https://github.com/user-attachments/assets/a181dca6-c70e-4fb0-a568-d3ae7b2607de)<br />

    Whoever is leaving these damn Among Us memes in this share, it IS NOT FUNNY. People downloading documents from our website will think we are a joke! Now I dont know who it is, but Maya is looking pretty sus
So I might have a username, `maya`.
Also, the webserver contains a directory `/files` with the same content:<br />
![image](https://github.com/user-attachments/assets/0dd1ad9d-f708-4afa-831e-5f62034ebcd9)<br />
Since everyone has read-write-execute permissions on the `ftp` folder from the FTP server, I can upload any file I want on it. So I'm going to upload the php reverse shell from pentest monkey, and call it `shell.php`. Then I open a netcat listener and visit `http://target_IP/ftp/shell.php` and get a reverse shell!<br />
The secret recipe is in `/`. Furthermore, inside the root directory there's also a pcapfile inside `/incidents`. That's unusual so I decide to download it on my machine and analyze it with wireshark. After a bit I found a possible password:<br />
![image](https://github.com/user-attachments/assets/1e2f7185-2f36-4602-b2e1-1ba8dedebf6e)<br />
`c4ntg3t3n0ughsp1c3`. I use this password to log into `lennie`'s account and get the root flag. Now, for privesc, inside `lennie`'s home directory there's a directory called `scripts` with the following script:<br />
![image](https://github.com/user-attachments/assets/18d9d83f-4cdc-4361-b959-d3ce673e0f30)<br />
This script is owned by root and I can't execute it, so I'm guessing it is a cronjob. The good new is that I'm the owner of `/etc/print.sh`, so I can just modify it to get a root reverse shell, if it's actually a cronjob. And it works I am now root:!<br />
![image](https://github.com/user-attachments/assets/8f92dbc4-26c1-4299-8ee7-8f61dfd9c22b)<br />



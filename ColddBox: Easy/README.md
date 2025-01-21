# ColddBox: Easy

### ColddBox: Easy
Nmap scan shows ports 80(apache) and 4512(ssh) open.
The webpage is powered by wordpress 4.1.31. I used wpscan to enumerate users and found the following valid users: philip, hugo and c0ldd. I then used the following command `wpscan --url http://10.10.216.252 -U c0ldd -P /usr/share/wordlists/rockyou.txt` 
and I was able to find c0ldd's password, and log into the admin panel.
Now that I'm admin, I go to `http://10.10.216.252/wp-admin/plugin-editor.php`:<br />
![image](https://github.com/user-attachments/assets/5dcdd5a4-aa19-405c-b96b-c77a2c51467d)<br />
From here I believe I can upload a php script that executes a reverse shell.<br />
In particular I edited `askimet.php`. In the script I put the reverse shell from [pentest monkey](https://github.com/pentestmonkey/php-reverse-shell):<br />
![image](https://github.com/user-attachments/assets/7739fbac-26fc-4bb0-a199-00217a652e38)<br />
Now I visit `http://10.10.216.252/wp-content/plugins/akismet/akismet.php` and the reverse shell is on.<br />
At this point for privesc, I used linpeas to enumerate the system and it finds so many different things to move laterally and escalate privileges. I'm going to use the most straightforward:<br />
![image](https://github.com/user-attachments/assets/2668a1bc-f6d4-4155-92b3-401aff26aa37)<br />
The exploit for this SUID can be easily found on [gtfobins](https://gtfobins.github.io/gtfobins/find/#suid). Just run `find . -exec /bin/sh -p \; -quit` and become root!

# LazyAdmin

### LazyAdmin
Nmap scan shows ports 22 and 80 open. Directory enumeration shows `/content`, with the following page: <br />
![image](https://github.com/user-attachments/assets/3cf9e25b-6c57-435a-a37c-ae155879a98d)<br />
This is `Basic CMS`. Exploring the website, I found a `.sql` file inside `/content/inc/mysql_backup/`:<br />
![image](https://github.com/user-attachments/assets/a5e3e935-1918-4943-b55d-9d21cefdad58)<br />
So I downloaded it and it contains the following query: <br />
![image](https://github.com/user-attachments/assets/dd462737-78cd-43af-850e-42e2b7096565)<br />
If I use crackstation to try and crack that hash, it works and finds the password. So I can now log into the admin panel located at `/content/as`. <br />
Searching online, I found that sweet rice 1.5.1 is vulnerable to file upload. Go to `Media Center`. <br />
![image](https://github.com/user-attachments/assets/412b06b8-4a4f-40e5-aacd-52c490b7d3a2)<br />
Here, you can upload a zip file containing a php cmd or reverse shell (remember to check the option "Extract zip archive"). Then you can execute the reverse shell by accessing `/content/attachment/`. That's enough to get the user flag.<br /><br />
Now for privesc, inside `itguy`'s home directory there's a file with mysql credentials, but they seem not to be helpful. If I run `sudo -l`, I get: <br />
![image](https://github.com/user-attachments/assets/942e9f5a-80a1-4d3e-8c21-233f715d4e8e)<br />
`backuppl` is owned by root, and this is its content: <br />
![image](https://github.com/user-attachments/assets/446b545a-ba9a-4c59-9f93-13ec48915e6e)<br />
`/etc/copy.sh` is writable by me, so I just insert a reverse shell in that file, then open a netcat listener, and then run `sudo /usr/bin/perl /home/itguy/backup.pl` to spawn a reverse root shell and get the root flag. 






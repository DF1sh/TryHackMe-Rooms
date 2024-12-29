# Dav

### Dav
Nmap scan shows port 80 open. It's a default apache webserver. Gobuster directory enumeration finds `/webdav`, which requires authentication to access: <br />
![image](https://github.com/user-attachments/assets/41dd1474-c5d5-49da-9c04-cad6cd7943d5)<br />
WebDav stands for **Web Distributed Authoring and Versioning** which is an extension of the Hypertext Transfer Protocol that allows clients to perform remote Web content creation operations. It provides the ability to create a file or folder, edit a file in place, copy or move or delete a file on a remote web server.<br /><br />
Searching online for a bit, I found a set of default credentials that worked. I'm not going to say them but I found them [here](https://shahjerry33.medium.com/rce-via-webdav-power-of-put-7e1c06c71e60).
So to upload a reverse shell, I'll use the php one from PentestMonkey. To upload it on the webdav, run `curl -T shell.php http://10.10.31.233/webdav/ -u user:password`. Now there should be a new file inside `/webdav`. Open a netcat listener and click on it to spawn a reverse shell. This was enough to get the user flag. <br />
For prives: if I run `sudo -l`, I get: <br />
![image](https://github.com/user-attachments/assets/3ceca8f1-be70-49ce-8c92-c45d45b4aefa)<br />
Just run `sudo /bin/cat /root/root.txt` to read the root flag.

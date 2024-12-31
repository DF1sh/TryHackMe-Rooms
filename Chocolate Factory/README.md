# Chocolate Factory

### Challenges
Nmap scan finds so many ports open: <br />
![image](https://github.com/user-attachments/assets/10fa40a2-7dd2-4de5-b06e-41697c23a27d)<br />
I'll ignore everything and start from the webserver. <br />
Luckily my decision was the right one. Directory enumeration shows `/home.php`, which allows you to run system commands: <br />
![image](https://github.com/user-attachments/assets/b74784dd-3901-4523-b67a-7cabaecc810a)<br />
Just spawn a reverse shell from here. <br />
Inside `/var/www/html/`, there's a file called `key_rev_key`. I don't know what this is, but it contains the key which is the answer to the first question:<br />
![image](https://github.com/user-attachments/assets/8be5f7ea-d5cb-4d3a-8e8e-7ee6f0435c3e)<br />
Enumerating the system, I found a private RSA key inside charlie's home directory, in a file called `teleport`:<br />
![image](https://github.com/user-attachments/assets/cc76c291-5330-4951-9000-6e538f984835)<br />
So I'll use it to log into charlie's ssh account. If I run `sudo -l` with charlie, I get: <br />
![image](https://github.com/user-attachments/assets/dc1fadb6-563d-475e-84ec-75cd787cf07b)<br />
The exploit for `vi` is on [gtfobins](https://gtfobins.github.io/gtfobins/vi/#sudo). Just run `sudo vi -c ':!/bin/sh' /dev/null` and you spawn a root shell. 
Inside root's home directory there's a file `root.py`. It asks me to prompt the previously found key to decrypt a text. Running it (with python2) gives me the root flag. 
![image](https://github.com/user-attachments/assets/402f62ae-a2e3-4a70-ad61-261cd717b486)<br />

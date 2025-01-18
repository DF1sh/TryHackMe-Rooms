# Brute It

### Brute It
Nmap scan shows ports 22 and 80 open. Port 80 is a default apache webserver. Directory enumeration shows `/admin` directory that contains a login page. The source code contains a comment with a hint: <br />
![image](https://github.com/user-attachments/assets/75cfa600-3580-4c01-ac12-9273237dee32)<br />
The username is admin. I try to bruteforce the login with the following hydra command: `hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.195.237 http-form-post "/admin/:user=^USER^&pass=^PASS^:invalid"`. The admin panel provides me with john's private ssh key. So I save it on my machine. <br />
It is protected by a password. To crack it, run `ssh2john id_rsa_john hash` and then `john hash --wordlist=/usr/share/wordlists/rockyou.txt`. Now run `chmod 600 id_rsa_john` and log into john's ssh account to get the user flag. <br />
Now for privesc, if I run `sudo -l`, I get: <br />
![image](https://github.com/user-attachments/assets/ad7add77-9207-4149-beb2-ca571acdfb76)<br />
Technically there's a way to become root with `cat` without cracking root's password, but since there's a question about it, let's do it. Use `cat` to read `/etc/shadow`. Save root's line on a file (I called it `roothash`) and run `john roothash --wordlist=/usr/share/wordlists/rockyou.txt` and become root!


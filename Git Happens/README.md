# Git Happens

### Git Happens
Nmap scan shows only port 80 open. It is a simple login page, but some enumeration finds a `/.git` directory, which contains the entire git project, including old versions.<br />
![image](https://github.com/user-attachments/assets/9e08c071-651e-4fba-8554-267956fdcf0a)<br />
To extract the git project locally from a remote `.git` directory over http, I'm going to use a tool called [git-dumper](https://github.com/arthaud/git-dumper).<br />
Once downloaded, just run `./git_dumper.py http://website.com/.git ~/website`. <br />






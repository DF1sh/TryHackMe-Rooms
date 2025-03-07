# Git Happens

### Git Happens
Nmap scan shows only port 80 open. It is a simple login page, but some enumeration finds a `/.git` directory, which contains the entire git project, including old versions.<br />
![image](https://github.com/user-attachments/assets/9e08c071-651e-4fba-8554-267956fdcf0a)<br />
To extract the git project locally from a remote `.git` directory over http, I'm going to use a tool called [git-dumper](https://github.com/arthaud/git-dumper).<br />
Once downloaded, just run `./git_dumper.py http://website.com/.git ~/website`. <br />
![Screenshot 2025-03-07 103554](https://github.com/user-attachments/assets/9c70a249-c6f4-4e98-9886-7f9e84e3a1db)<br />
And now I have the entire project, including all the versions inside the `.git` folder. Apparently there's only the master branch: <br />
![image](https://github.com/user-attachments/assets/f4fa47ac-06c2-459f-a9c4-f0c6e4635c4e)<br />
So I run `git log --oneline master` to see all the commits made on this branch, so that I can start searching critical information in previous versions:<br />
![image](https://github.com/user-attachments/assets/1da3e397-99f5-4e6d-8307-a4d543216514)<br />
In particular, I found the password inside the second commit, with `git show 395e087`:<br />
![image](https://github.com/user-attachments/assets/bb359c67-55ad-478d-8aa8-064e20770e1b)<br />







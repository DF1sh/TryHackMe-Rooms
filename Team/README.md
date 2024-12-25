# Team

### Flags
nmap shows port 21,22 and 80 open. Port 80 is a default apache web server, with a modified title: <br />
![image](https://github.com/user-attachments/assets/3af43de3-e744-4a30-9f74-e998bdf522a9)<br />
So I add team.thm to /etc/hosts. <br />
The following command enumerats virtual hosts: `gobuster vhost -u "http://10.10.131.44" --domain team.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain`
![image](https://github.com/user-attachments/assets/0378dcbf-233b-4619-85ff-15a0e87ca9eb)<br />
`dev.team.thm` is vulnerable to directory traversal: <br />
![image](https://github.com/user-attachments/assets/cdced0a2-ee87-4d6b-b1ef-bc3bbb5e9644)<br />
Enumerating directories in `http://team.thm/scripts/` I found a file named `script.txt`:<br />
![image](https://github.com/user-attachments/assets/e0cbc233-29e1-4e08-b464-b0a45d3600c9)<br />
The last line hints at the fact that there's a script with a different extension that contains credentials. So I need to run gobuster again but enumerating more extensions. So I run `gobuster dir -u "http://team.thm/scripts" -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-directories-lowercase.txt -x php,txt,html,sh,bash,conf,config,bak,backup,old,src,dat,bin,tmp,hidden,secret`:<br />
![image](https://github.com/user-attachments/assets/06295db3-0ee6-4996-92b9-b6de503eb9d7)<br />
This was enough to get the credentials for the ftpuser. Inside the ftp server theres a file with the following contents: <br />
![image](https://github.com/user-attachments/assets/13c8874d-0934-4c76-bcd5-71320c0a06fd)<br />
So I use the path traversal vulnerability to get the id_rsa file at `http://dev.team.thm/script.php?page=/etc/ssh/sshd_config`. I copy it on my machine, change it's permission with `chmod 600 id_rsa_bale` and use it to log in with `ssh dale@10.10.117.144 -i id_rsa_bale`. This got me the first flag. <br />
If I run `sudo -l` I can run a bash file with gyles privileges: <br />
![image](https://github.com/user-attachments/assets/a5760e8b-bd58-4c19-9053-caf3863fac56)<br />
This is very easy to exploit: <br />
![image](https://github.com/user-attachments/assets/9c405740-28c1-443a-bb9f-6928c54d2fa4)<br />
Now as gyles, I found a cronjob inside `/opt`:<br />
![image](https://github.com/user-attachments/assets/970365e0-39e8-4c31-938a-f1e132f54dd6)<br />
This script runs `/usr/local/bin/main_backup.sh`: <br />
![image](https://github.com/user-attachments/assets/0c51a56b-4034-44f2-9ee4-4b96934610bd)<br />
Like shown in the picture above, that script is owned by the admin's group. Gyles is part of the admin group so he can edit it. So I'll add a reverse shell in it: <br />
![image](https://github.com/user-attachments/assets/6ab02036-262b-4a62-b05f-f6613061f517)<br />




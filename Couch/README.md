# Couch

### Couch
Nmap scan shows ports 22 and 5984 open. 

    PORT     STATE SERVICE VERSION
    22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 34:9d:39:09:34:30:4b:3d:a7:1e:df:eb:a3:b0:e5:aa (RSA)
    |   256 a4:2e:ef:3a:84:5d:21:1b:b9:d4:26:13:a5:2d:df:19 (ECDSA)
    |_  256 e1:6d:4d:fd:c8:00:8e:86:c2:13:2d:c7:ad:85:13:9c (ED25519)
    5984/tcp open  http    CouchDB httpd 1.6.1 (Erlang OTP/18)
    |_http-title: Site doesn't have a title (text/plain; charset=utf-8).
    |_http-server-header: CouchDB/1.6.1 (Erlang OTP/18)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

![image](https://github.com/user-attachments/assets/b120150b-e51c-4bb0-975e-4c7a47d99f9a)<br />
I enumerate directories using ffuf: `ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -u http://10.10.179.90:5984/FUZZ -e .txt,.html,.php -mc 200,301,302 -s` and I find: <br />
![image](https://github.com/user-attachments/assets/fa6ac851-2d8f-465a-aac7-c7803fbd4754)<br />
Searching online for a bit, I found [this website](https://www.ionos.com/digitalguide/hosting/technical-matters/work-with-couchdb-from-the-command-line/) that explains very well how to work with couchDB from the terminal. <br />
I run `curl -X GET http://10.10.179.90:5984/_all_dbs` and get the list of databases: <br />
![image](https://github.com/user-attachments/assets/3c01e92d-da0b-4de1-9463-b467e6e698ce)<br />
I move on with my research and find in [this guide](https://guide.couchdb.org/draft/tour.html) that the administration tool is inside `/_utils`: <br />
![image](https://github.com/user-attachments/assets/738be0da-15b3-4735-8c9f-ec94586e9de0)<br />
That's definitely easier now. Now, inside `/secret/a1320dd69fb4570d0a3d26df4e000be7 ` there is a set of credentials for the user `atena`. I use the password to log into atena's ssh account and get the user flag.<br />
Privesc to root is pretty straightforward: <br />
![image](https://github.com/user-attachments/assets/3aec8823-9fe7-4da1-ac61-a90aced29bb0)<br />
Basically inside atena bash history file there's this command: `docker -H 127.0.0.1:2375 run --rm -it --privileged --net=host -v /:/mnt alpine`. This means that atena can run the command `docker`, which is usually only reserved for privileged users like root, since it can be easily used to become root. <br />
This command mounts the entire file system `/` inside `/mnt`. It is also run with the flag `--privileged`, meaning that I'll be root inside that container. The flag is located at `/mnt/root/root.txt`.





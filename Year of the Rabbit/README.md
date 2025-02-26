# Year of the Rabbit

### Year of the Rabbit
Nmap scan shows ports 21,22 and 80 open. The webserver contains a `/assets` directory. Inside the file `style.css` there's a hint to a secret folder.<br />
![image](https://github.com/user-attachments/assets/c540d5cc-d297-42a3-8192-4c18f2424a02)<br />
This page contains some js that doesn't allow me to view the page because it redirects me to the rickroll video. So I decide to capture the response with burpsuite, and if I intercept the response to the request, I get this: <br />
![image](https://github.com/user-attachments/assets/fc393df0-2b28-42e4-8d39-3e91f2d27c73)<br />
I get redirected to another page: `/WExYY2Cv-qU`. Inside this directory there's an image of a hot babe. I download it and find some interesting stuff inside of it using the `strings` command: <br />
![image](https://github.com/user-attachments/assets/515a8af3-7e94-424c-bc70-9e828bda286d)<br />
So I know the FTP user and I have a list of passwords, I will just create a wordlist and use hydra to find the right one. This finds me the right password, and I'm able to log into the ftp server. Inside the FTP server there's a file containing credentials, but there's somethig wrong with it xd<br />
![image](https://github.com/user-attachments/assets/6f0d87e8-79bf-4b9d-ab7b-703e5da0e3c7)<br />
I asked chatGPT what the fuck is that, and it's a code writte in **brainfuck**. So I use [this website](https://www.dcode.fr/brainfuck-language) to decode it, and it contains the credentials for Eli's ssh account. Once logged in I have a message to gwendoline: <br />
![image](https://github.com/user-attachments/assets/0868db01-5663-486d-b4e6-9a0eca068d0f)<br />
I use the `find` command to locate this secret:<br />
![image](https://github.com/user-attachments/assets/403fcd08-9978-45b0-8cd7-919f2499154d)<br />
This directory contains gwendoline's password. I used it to log into her account and get the flag. Next, if I run `sudo -l`, I get: <br />
![image](https://github.com/user-attachments/assets/0aee3021-9531-4071-b30d-60a3c231efa6)<br />
I can execute this command for every user except for root. But there's a clever way to exploit it, and it's explained [here](https://www.exploit-db.com/exploits/47502). Run `sudo -u#-1 /usr/bin/vi /home/gwendoline/user.txt` and then follow the steps provided by [GTFObins](https://gtfobins.github.io/gtfobins/vi/#sudo):<br />
![image](https://github.com/user-attachments/assets/af561c55-a8ca-4baf-a546-26d896ac9976)<br />
This spawns a root shell and I get the root flag.






# Inferno

### Inferno
Nmap scan finds like 200 ports open.. I decide to look at port 80. The webserver contains a directory `/inferno`, but it requires authentication.<br />
![image](https://github.com/user-attachments/assets/c1dfeb29-ebfb-4769-8497-774944bda39f)<br />
At this point I was stuck for a while, so I decided to try to bruteforce this basic login using hydra, and the username `admin`. I used the following command: `hydra -l admin -P /usr/share/wordlists/rockyou.txt http-get://10.10.122.69/inferno` and found a valid set of credentials. <br />
`/inferno` contains a login page, I used the same credentials as before and was able to log into a `Codiad` instance. Codiad is essentially a web-based IDE. Looking online I found [this RCE](https://github.com/WangYihang/Codiad-Remote-Code-Execute-Exploit?tab=readme-ov-file) that worked fine: <br />
![image](https://github.com/user-attachments/assets/bb547f37-de41-4294-8aa9-5cd2ee56487f)<br >
I get kicked always from the reverse shell and have to re-do it every time. But I was lucky enough to find an interesting file inside `/home/dante/Downloads`, called `downloads.dat`. Here's the content of it: <br />
![image](https://github.com/user-attachments/assets/801aa66d-cc90-4da3-9f72-f1e95fc11602)<br />
This is hex-encoded. I use cyberchef to decode it: <br />
![image](https://github.com/user-attachments/assets/d8742fe1-577b-43dc-948c-69552b5aa1ad)<br />
And I get `dante`'s credentials to use it on ssh. I still get kicked out of the shell, I don't know how to fix this, there's probably some cronjob or daemon that keeps doing it but I don't know how to fix it. Anyway, if I run `sudo -l` I get this: <br />
![image](https://github.com/user-attachments/assets/5d81a48d-c47d-4d50-87d3-0724a8119e52)<br />
The exploit for sudo privileges on `tee` can be found on [gtfobins](https://gtfobins.github.io/gtfobins/tee/#sudo). This privilege allows me to write content on any file I want on the file system. What I do is to modify the file `/etc/sudoers`, to grant `dante` the same privileges of root. To do that, I run `echo "dante ALL=(ALL) NOPASSWD: ALL" | sudo tee -a /etc/sudoers`. <br />
Now dante can execute any command with sudo, so just run `sudo su` and become root!<br />
![image](https://github.com/user-attachments/assets/973b43f9-a96b-42f7-82e4-85c6ede9915f)<br />

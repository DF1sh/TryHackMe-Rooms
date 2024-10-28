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
To do that, I created (thanks, Mr. GPT), a python script called `brutecookie.py` that you can find inside this folder.



ftpuser:W3stV1rg1n14M0un741nM4m4

- What is the user flag?
- What is the root flag?

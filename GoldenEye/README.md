# GoldenEye

### GoldenEye
Nmap scan shows ports 25,80,55006 and 55007 open.<br />
![image](https://github.com/user-attachments/assets/ab4c7f53-550b-45a7-a4e3-d3b82c873474)<br />
Web app contains the following terminal.js file: <br />
![image](https://github.com/user-attachments/assets/33293bd7-b95c-4abf-b605-1e547dc9d347)<br />
I decode the password using cyberchef: <br />
![image](https://github.com/user-attachments/assets/9059eedd-5fab-4b5d-9d39-72addf05909b)<br />
So I use this credentials to log into `/sev-home/`<br />
![image](https://github.com/user-attachments/assets/1b242f47-9f0b-47ba-923d-0f799b06dc3b)<br />
I then try to bruteforce login with `Boris` on the pop3 service hosted on port 55007, with: `hydra -l boris -P /usr/share/wordlists/rockyou.txt -f 10.10.95.201 pop3 -s 55007`.<br /> 
I also did the same with the user `natalya` and found her password. So I logged in the pop3 service with natalya's credentials and retrieved one of her emails: <br />
![image](https://github.com/user-attachments/assets/d0ba9c98-921e-4bea-b083-4de08e35427d)<br />
Then I follow the instructions provided in the task log in into `http://severnaya-station.com/gnocertdir/` with xenia:<br />
![image](https://github.com/user-attachments/assets/ca2c0b23-e0e3-4b53-b281-f9feef899e90)<br />
Navigating on the web app, I found another user: <br />
![image](https://github.com/user-attachments/assets/7bcd533e-0ac6-4db5-bbc0-039512c11e34)<br />
I bruteforce login with doak on pop3 service, and found another email: <br />
![image](https://github.com/user-attachments/assets/befd94c5-7a9b-4d16-854d-e70b5c3d1972)<br />
I use this credentials to log into dr_doak's account on the web application. Now there's a secret.txt file in his account: <br />
![image](https://github.com/user-attachments/assets/94c73aed-4fd9-4e0f-b9a2-6497fa8faf31)<br />
So I download the image with wget and used exiftool to see if there's any hidden information inside the metadata of the image: <br />
![image](https://github.com/user-attachments/assets/00581deb-0dad-4408-a2d0-aa8a48f5f0ef)<br />
So I use this password to log into the admin's account on the web app. To get rce and a reverse shell, go on `http://severnaya-station.com/gnocertdir/admin/settings.php?section=systempaths` and put a python reverse shell: <br />
![image](https://github.com/user-attachments/assets/b5ac490b-64a5-4627-8cc8-abb117e0bb7d)<br />
Now add a new blog post: <br />
![image](https://github.com/user-attachments/assets/a08f308f-b122-4ed4-92e4-8106235c65d8)<br />
And trigger the spell checker: <br />
![image](https://github.com/user-attachments/assets/85981900-c98c-43b5-a2c7-196f574a61f6)<br />
This will give you access to the remote machine. 








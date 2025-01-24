# Tech_Supp0rt: 1

### Tech_Supp0rt: 1
Nmap scan shows ports 22,80,139 and 445 open.<br />
SMB server allows login with empty credentials. Inside the SMB server there's a file with the following content:<br />
![image](https://github.com/user-attachments/assets/0f7b4ec8-ce2d-4166-9e2a-acd1444aba22)<br />
So we have a set of credentials and also a `/subrion` directory. The problem is that if I visit the directory, I get redirected to another IP address and directory:<br />
![image](https://github.com/user-attachments/assets/76cec22e-70d4-4d47-b55a-7768458de2cd)<br />
If I try to access the panel at `/subrion/panel`, I get in: <br />
![image](https://github.com/user-attachments/assets/8f8e484f-c412-4a67-868a-26aad7221b2f)<br />
About the admin password, it it not hashed, it is actually encoded, and I was able to find the right encoding sequence on cyberchef:<br />
![image](https://github.com/user-attachments/assets/1f03bda9-a978-443e-92c6-1a4e63df6a7d)<br />
Now I found [this exploit](https://www.exploit-db.com/exploits/49876) that's an arbitrary file upload (authenticated) for subrion CMS 4.2.1. Download the script and run `python3 file_upload.py -u http://10.10.16.179/subrion/panel/ --user admin --pass Scam2021`.<br />
This will spawn a reverse shell.<br />
Next, inside the wordpress config.php file I found mysql credentials:<br />
![image](https://github.com/user-attachments/assets/6976df2c-7eb1-47bd-8506-c89cf1ab540e)<br />
That is also the password to access the `scamsite` user. Now if I run `sudo -l`:<br />
![image](https://github.com/user-attachments/assets/6bcf0413-3df7-46d5-82c2-f4d5a70a700d)<br />
The exploit for this can be easily found on [gtfobins](https://gtfobins.github.io/gtfobins/iconv/#sudo). Just run `sudo /usr/bin/iconv -f 8859_1 -t 8859_1 /root/root.txt` to read the flag.



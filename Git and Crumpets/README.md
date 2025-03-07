# Git and Crumpets

### Git and Crumpets
Nmap scan shows ports 22 and 80. But port 80 redirects me to the rick roll video, so there's nothing on the main page. However I can still enumerate directories. I try to do that, but I see that after a while my IP address gets blocked by the website. Even if I visit the page on a browser I can't do it.<br />
What I try to do next is to restart the machine, and this time run an nmap ACK scan:<br />
![image](https://github.com/user-attachments/assets/18f6a3e7-f522-43ed-8504-b5a383134596)<br />
I try to connect to it but nothing, I get blocked again. So i restart again the machine. This time i decided to run `curl` on the target IP, and here's what I get:<br />
![image](https://github.com/user-attachments/assets/761588ef-1a9f-4bb0-b3c4-4e6846dd69d7)<br />
So I added "git.git-and-crumpets.thm" to my `/etc/hosts` file and visit `http://git.git-and-crumpets.thm`:<br />
![image](https://github.com/user-attachments/assets/b8a10178-6167-4c44-9405-de2caee461cd)<br />
Since I have no credentials, I register a new account, and I find two repositories:<br />
![image](https://github.com/user-attachments/assets/fac69041-0e98-4cce-8923-f8b443b247eb)<br />
Looking at the first repository, if I click on `commits`, I can see 5 commits:<br />
![image](https://github.com/user-attachments/assets/87cd0dc4-840e-4bdd-8682-826b193d264e)<br />
But here's what happens if I click on the three dots in the image above:<br />
![image](https://github.com/user-attachments/assets/ede0ba91-6982-49e8-afc1-fa45c00d5f83)<br />
So I downloaded his avatar using `wget`, and used `exiftool` to read metadata from the image:<br />
![image](https://github.com/user-attachments/assets/3dfb369b-04ee-4509-af85-f94965ff8bdf)<br />
And so I was able to log into scone's account with `scones:Password`. 





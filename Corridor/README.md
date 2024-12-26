# Corridor

### Escape the Corridor
- What is the flag?<br />
Looking at the webserver, if I press CTRL+U to access the source code I see this: <br />
![image](https://github.com/user-attachments/assets/eb7886fc-d564-4eac-92db-1d58f6d53de9)<br />
These file names look a lot like hashes, as suggested in the room. Infact If I take the first one and submit it to [crackstation](https://crackstation.net/): <br />
![image](https://github.com/user-attachments/assets/b5a7fa04-aaeb-44b8-b474-8ad115e8a5a1)<br />
I get 1. If I try it with the second image: <br />
![image](https://github.com/user-attachments/assets/94f33c80-70bd-4907-ae36-bddde8444779)<br />
It's two. Since this room is about IDOR, I will try to access the image `0`.
Since the hash used is MD5, I run `echo -n "0" | md5sum`:<br />
![image](https://github.com/user-attachments/assets/2bf9de41-c2c8-4b74-bc88-e99dc3fddfa4)<br />
Now If I access `/cfcd208495d565ef66e7dff9f98764da`: <br />
![image](https://github.com/user-attachments/assets/c3789172-1a50-46d9-9ae9-48f8f9c0371b)<br />



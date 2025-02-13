# Classic Passwd

### Classic Passwd
This was a very simple debugging challenge. Looking at the binary with gdb, it performs some cryptic operation that scrambles some variables, but I don't care about that, I don't need to analyze it, I can just let the program do its thing and put a breakpoint to see the password: <br />
![image](https://github.com/user-attachments/assets/8a5fbeda-e353-4017-8722-5927d5cae5c6)<br />
Inside a function called `vuln`, at the bottom there's a `strcmp` call. I'll put a breakpoint on it with the command `break  strcmp@plt`. I then run the program and prompt a random password: <br />
![image](https://github.com/user-attachments/assets/285f5f79-100c-48d6-8df6-d50154698153)<br />
Next, since the arguments of the `strcmp` are inside rax and rdx, I looked their contents and found the password inside rdx: <br />
![image](https://github.com/user-attachments/assets/b62d9dad-24a9-47cd-b397-4ca0fd938243)<br />



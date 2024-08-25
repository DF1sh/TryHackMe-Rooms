# Operating System Security

### Introduction to Operating System Security
Which of the following is not an operating system?
- AIX
- Android
- Chrome OS
- Solaris
- Thunderbird <br />
`Thunderbird`

### Common Examples of OS Security
Which of the following is a strong password, in your opinion?
- iloveyou
- 1q2w3e4r5t
- LearnM00r
- qwertyuiop <br />
`LearnM00r`

### Practical Example of OS Security
- Based on the top 7 passwords, let’s try to find Johnny’s password. What is the password for the user johnny? <br />
After logging with sammie, run `sudo - johnny` and insert the correct password: `abc123` <br />
- Once you are logged in as Johnny, use the command history to check the commands that Johnny has typed. We expect Johnny to have mistakenly typed the root password instead of a command. What is the root password?<br />
![image](https://github.com/user-attachments/assets/cb5004e7-ce0d-45ec-9d35-61fa7a0f7483)<br />
`happyHack!NG`
- While logged in as Johnny, use the command su - root to switch to the root account. Display the contents of the file flag.txt in the root directory. What is the content of the file?<br />
![image](https://github.com/user-attachments/assets/520a3d97-b175-4bd5-b4f3-9e12f5fe985e)<br />
`THM{YouGotRoot}`


# Surfer

### Surfer
`/robots.txt` shows the presence of `/backup/chat.txt` with the following contents:<br />
![image](https://github.com/user-attachments/assets/11e85b54-e1d5-4958-bfa5-a65c02d6a130)<br />
Knowing that, I can log in. Moving around I find this hint: <br />
![image](https://github.com/user-attachments/assets/9eea5bbc-e757-4f42-8d89-41866ad3182a)<br />
And if I click on it: <br />
![image](https://github.com/user-attachments/assets/49bfac1e-6171-4b3f-be03-709ef7f14e7a)<br />
Knowing this, I use burpsuite to capture the request when exporting the pdf with information about the system, to access `/internal/admin.php`:<br />
![image](https://github.com/user-attachments/assets/84bda3c2-1458-452a-81c5-b2eda763e866)<br />
This got me the flag.


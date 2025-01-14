# Insecure Randomness

### Few Important Concepts
- What measures the amount of randomness or unpredictability in a system? `entropy`
- Is it a good practice to keep the same seed value for all cryptographic functions? (yea/nay) `nay`

### Types of Random Number Generators
- You prepare a game involving immediate interaction and random event simulation but with no critical security requirements. Which type of RNG would be most appropriate for this purpose? Write the correct option only. `b`

### Weak or Insufficient Entropy
- What is the flag value after logging in as the victim user?<br />
Just follow the steps provided in the task: <br />
![image](https://github.com/user-attachments/assets/30d2e655-0faf-453f-bc7b-d17231677b04)<br />
` THM{VICTIM_SIGNED_IN}`
- What is the flag value after logging in as the master user? `THM{ADMIN_SIGNED_IN007}`
- What is the PHP function used to create the token variable in the code above? `time()`

### Predictable Seed in PRNGs
- What is the flag value after logging in as magic@mail.random.thm? <br />
After doing the provided steps you get something like this: <br />
![image](https://github.com/user-attachments/assets/d867cb59-3ee1-4ac2-9bca-a5c158fcd8b3)<br />
You can now just use them to access emails by visiting: `http://random.thm:8090/case/magic_link_login.php?token={predicted_token}`:<br />
`THM{MAGIC_SIGNED_IN11010}`
- What is the flag value after logging in as hr@mail.random.thm?<br />
Do the same process but using the email above: `THM{HR_SIGNED_IN1337}`
- What is the PHP function used to seed the RNG in the code above? `mt_srand`

### Mitigation Measures
- Which of the following can be considered as a weak seed value? Write the correct letter only. `d`

# Burp Suite: Intruder

### What is Intruder
- In which Intruder tab can we define the "Attack type" for our planned attack? `Positions`

### Positions
- What symbol defines the start and the end of a payload position? `§`

### Payloads
- Which Payload processing rule could we use to add characters at the end of each payload in the set? `Add suffix`

### Introduction to Attack Types
- What attack type cycles through the payloads inserting one payload at a time into each position defined in the request? `Sniper`

### Sniper
- If you were using Sniper to fuzz three parameters in a request with a wordlist containing 100 words, how many requests would Burp Suite need to send to complete the attack? `300`
- How many sets of payloads will Sniper accept for conducting an attack? `1`

### Battering Ram
- If you have a wordlist with two words in it (admin and Guest) and the positions in the request template look like this: username=§pentester§&password=§Expl01ted§. What would the body parameters of the first request that Burp Suite sends be? `username=admin&password=admin`

### Pitchfork
- What is the maximum number of payload sets we can load into Intruder in Pitchfork mode? `20`

### Cluster Bomb
- We have three payload sets. The first set contains 100 lines, the second contains 2 lines, and the third contains 30 lines. How many requests will Intruder make using these payload sets in a Cluster bomb attack? `6000`

### Practical Example
- What username and password combination indicates a successful login attempt? The answer format is "username:password". <br />
Capture a login request with burpsuite and send it to intruder. Set the following targets: <br />
![image](https://github.com/user-attachments/assets/496e28b2-c8e8-4a68-bcb6-47719b20d2a7)<br />
Now move to "Payloads", set payload 1 and load the wordlist `usernames.txt`, then set payload 2 and load the wordlist `passwords.txt`. Now click on "Start attack" and wait a few minutes(if you are using community edition): <br />
![image](https://github.com/user-attachments/assets/0bfba71f-75aa-4183-b8c6-b81010cd853a)<br />
`m.rivera:letmein1`

### Practical Challenge
- Which attack type is best suited for this task? `Sniper`
- Either using the Response tab in the Attack Results window or by looking at each successful (i.e. 200 code) request manually in your browser, find the ticket that contains the flag. What is the flag? <br />
Capture a ticket request while logged in (this will grant us the cookie to access the tickets), then send the request to Intruder. This will be our target: <br />
![image](https://github.com/user-attachments/assets/fd9b7ef4-bcbe-483e-a678-eec57daefc48)<br />
We're going to use the sniper attack, with a payload made of numbers from 0 to 100. <br />
![image](https://github.com/user-attachments/assets/97da671f-7a38-4d9e-857e-5639731c7f8e)<br />
We can see that some requests return a 200 status code. Access those tickets to find the flag: <br />
![image](https://github.com/user-attachments/assets/7e7462e2-b329-4ed1-b586-decc0161e1a5)<br />
`THM{MTMxNTg5NTUzMWM0OWRlYzUzMDVjMzJl}`


### Extra Mile Challenge
- What username and password combination indicates a successful login attempt? The answer format is "username:password". <br />
Follow the steps described in the task to get the flag: <br />
![image](https://github.com/user-attachments/assets/802aa0c1-0af4-4d17-8837-a2edb7f72f3f)<br />
`o.bennett:bella1`


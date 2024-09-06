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

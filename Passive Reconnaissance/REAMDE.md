# Passive Reconnaissance

### Passive Versus Active Recon
- You visit the Facebook page of the target company, hoping to get some of their employee names. What kind of reconnaissance activity is this? (A for active, P for passive) `P`
- You ping the IP address of the company webserver to check if ICMP traffic is blocked. What kind of reconnaissance activity is this? (A for active, P for passive) `A`
- You happen to meet the IT administrator of the target company at a party. You try to use social engineering to get more information about their systems and network infrastructure. What kind of reconnaissance activity is this? (A for active, P for passive) `A`

### Whois
- When was TryHackMe.com registered? <br />
Run `whois tryhackme.com`: <br />
![image](https://github.com/user-attachments/assets/e3c9e9b4-194c-47dd-a5e0-5b2abff8c5f4)<br />
`20180705`
- What is the registrar of TryHackMe.com? `namecheap.com`
- Which company is TryHackMe.com using for name servers? `cloudflare.com`

### nslookup and dig
- Check the TXT records of thmlabs.com. What is the flag there? <br />
![image](https://github.com/user-attachments/assets/7e0d31b1-867d-4989-bc0f-d120f73a8926)<br />

### DNSDumpster
- Lookup tryhackme.com on DNSDumpster. What is one interesting subdomain that you would discover in addition to www and blog?<br />
![image](https://github.com/user-attachments/assets/3451115a-e294-45c5-8bab-6d4d5c02ea16)<br />
`remote`

### Shodan.io
- According to Shodan.io, what is the 2nd country in the world in terms of the number of publicly accessible Apache servers?<br />
Search for "apache" on [Shodan.io](https://www.shodan.io/).<br />
![image](https://github.com/user-attachments/assets/9af3314c-8aa1-4a57-a0d5-c2468787ca89)<br />
`Germany`
- Based on Shodan.io, what is the 3rd most common port used for Apache? `8080`
- Based on Shodan.io, what is the 3rd most common port used for nginx? `5001`

# Gobuster: The Basics

### Gobuster: Introduction
- What flag to we use to specify the target URL? `-u`
- What command do we use for the subdomain enumeration mode? `dns`

### Use Case: Directory and File Enumeration
- Which flag do we have to add to our command to skip the TLS verification? Enter the long flag notation. `--no-tls-validation`
- Enumerate the directories of www.offensivetools.thm. Which directory catches your attention?<br />
> Run `gobuster dir -u www.offensivetools.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`<br />
![image](https://github.com/user-attachments/assets/7dfae52f-52e9-4dfd-bb5b-5a419dcf9dc2)<br />
`secret`
- Continue enumerating the directory found in question 2. You will find an interesting file there with a .js extension. What is the flag found in this file?<br />
Run `gobuster dir -u www.offensivetools.thm/secret -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x js`<br />
![image](https://github.com/user-attachments/assets/b4558389-aad7-4c75-9ad5-cfda47921304)<br />
Open this resource to read the flag: `THM{ReconWasASuccess}`

### Use Case: Subdomain Enumeration
- Apart from the dns keyword and the -w flag, which shorthand flag is required for the command to work? `-d`
- Use the commands learned in this task, how many subdomains are configured for the offensivetools.thm domain?<br />
Run `gobuster dns -d offensivetools.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt`<br />
![image](https://github.com/user-attachments/assets/450cdab0-7983-42d2-b611-e2dc5e66aafe)<br />
`4`

### Use Case: Vhost Enumeration
- Use the commands learned in this task to answer the following question: How many vhosts on the offensivetools.thm domain reply with a status code 200?<br />
Run `gobuster vhost -u "http://10.10.8.124" --domain offensivetools.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain --exclude-length 250-320`<br />
![image](https://github.com/user-attachments/assets/d014cebe-ea58-4c2d-b91f-81b14bc33891)<br />
`4`

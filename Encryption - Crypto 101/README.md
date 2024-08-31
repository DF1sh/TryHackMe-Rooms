# Encryption - Crypto 101

### Key terms
- Are SSH keys protected with a passphrase or a password? `passphrase`

### Why is Encryption important?
- What does SSH stand for? `Secure Shell`
- How do webservers prove their identity? `certificates`
- What is the main set of standards you need to comply with if you store or process payment card details? `PCI-DSS`

### Crucial Crypto Maths
- What's 30 % 5? `0`
- What's 25 % 7 `4`
- What's 118613842 % 9091 `3565`

### Types of Encryption
- Should you trust DES? Yea/Nay `Nay`
- What was the result of the attempt to make DES more secure so that it could be used for longer? `Triple DES`
- Is it ok to share your public key? Yea/Nay `Yea`

### RSA - Rivest Shamir Adleman
- p = 4391, q = 6659. What is n? `29239669`

### Digital signatures and Certificates
- Who is TryHackMe's HTTPS certificate issued by? `E5`

### SSH Authentication
- What algorithm does the key use? `RSA`
- Crack the password with John The Ripper and rockyou, what's the passphrase for the key? <br />
To crack the passphrase, run the command `ssh2john id_rsa_1593558668558.id_rsa > idrsa.txt`. This will format the rsa file in a way that john can read it and crack it. Now run `john --wordlist=/usr/share/wordlists/rockyou.txt idrsa.txt` to crack the passphrase: <br />
![image](https://github.com/user-attachments/assets/163f3f5b-07ac-4e1d-bb9a-4acd04a20cd4)<br />
`delicious`

### PGP, GPG and AES
- You have the private key, and a file encrypted with the public key. Decrypt the file. What's the secret word? <br />
We have a private key called `tryhackme.key` and an encrypted message called `message.gpg`. In order to decrypt the message with the given key, we need to first import the key with the command: `gpg --import tryhackme.key`. Now we can decrypt the message with the command `gpg -d message.gpg` <br />
![image](https://github.com/user-attachments/assets/5452d37c-333e-44ef-a0c4-111624438308)<br />
`Pineapple`

# Introduction to Cryptography

### Introduction
- You have received the following encrypted message: “Xjnvw lc sluxjmw jsqm wjpmcqbg jg wqcxqmnvw; xjzjmmjd lc wjpm sluxjmw jsqm bqccqm zqy.” Zlwvzjxj Zpcvcol <br />
You can guess that it is a quote. Who said it?<br />
![image](https://github.com/user-attachments/assets/0af09d35-b3e8-4eaf-9f43-5801241924cd)<br />
`Miyamoto Musashi`

### Symmetric Encryption
- Decrypt the file quote01 encrypted (using AES256) with the key s!kR3T55 using gpg. What is the third word in the file?<br />
Run the command `gpg --output original_message.txt --decrypt quote01.txt.gpg`: `waste`
- Decrypt the file quote02 encrypted (using AES256-CBC) with the key s!kR3T55 using openssl. What is the third word in the file?<br />
Run the command `openssl aes-256-cbc -d -in quote02 -out original_message.txt`: `science`
- Decrypt the file quote03 encrypted (using CAMELLIA256) with the key s!kR3T55 using gpg. What is the third word in the file?<br />
Run the command `gpg --output original_message.txt --decrypt quote03.txt.gpg`: `understand`

### Asymmetric Encryption
- Bob has received the file ciphertext_message sent to him from Alice. You can find the key you need in the same folder. What is the first word of the original plaintext?<br />
Run the command `openssl pkeyutl -decrypt -in ciphertext_message -inkey private-key-bob.pem -out decrypted.txt`: <br />
![image](https://github.com/user-attachments/assets/cb7fbaeb-44bc-4ac0-9337-e9f70e01fc59)<br />
`Perception`
- Take a look at Bob’s private RSA key. What is the last byte of p? `e7`
- Take a look at Bob’s private RSA key. What is the last byte of q? `27`

### Diffie-Hellman Key Exchange
- A set of Diffie-Hellman parameters can be found in the file dhparam.pem. What is the size of the prime number in bits? `4096`
- What is the prime number’s last byte (least significant byte)? `4f`

### Hashing
- What is the SHA256 checksum of the file order.json? <br />
Run `sha256sum order.json`:<br />
`2c34b68669427d15f76a1c06ab941e3e6038dacdfb9209455c87519a3ef2c660`
- Open the file order.json and change the amount from 1000 to 9000. What is the new SHA256 checksum? `11faeec5edc2a2bad82ab116bbe4df0f4bc6edd96adac7150bb4e6364a238466`
- Using SHA256 and the key 3RfDFz82, what is the HMAC of order.txt? <br />
Run `hmac256 3RfDFz82 order.txt`: <br />
`c7e4de386a09ef970300243a70a444ee2a4ca62413aeaeb7097d43d2c5fac89f`

### PKI and SSL/TLS
- What is the size of the public key in bits? <br />
Run the command: `openssl x509 -in cert.pem -text`. `4096`
- Till which year is this certificate valid? `2039`

### Authenticating with Passwords
- You were auditing a system when you discovered that the MD5 hash of the admin password is 3fc0a7acf087f549ac2b266baf94b8b1. What is the original password?<br />
I used crackstation.net: <br />
![image](https://github.com/user-attachments/assets/498aee21-3c19-44f8-8b93-e15884e39b6c)<br />
`qwerty123`


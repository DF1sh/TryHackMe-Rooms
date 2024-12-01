# Hashing Basics

### Hash Functions
- What is the SHA256 hash of the passport.jpg file in ~/Hashing-Basics/Task-2?<br />
Move in the task folder and run `sha256sum passport.jpg`: `77148c6f605a8df855f2b764bcc3be749d7db814f5f79134d2aa539a64b61f02`
- What is the output size in bytes of the MD5 hash function?<br />
MD5 outputs are 128 bit long, which is `16` bytes.
- If you have an 8-bit hash output, how many possible hash values are there?<br />
2 to the power of 8 is `256`

### Insecure Password Storage for Authentication
- What is the 20th password in rockyou.txt?<br />
![image](https://github.com/user-attachments/assets/be7bce3f-0e62-43ef-8f97-42fb67bc0345)<br />
`qwerty`

### Using Hashing for Secure Password Storage
- Manually check the hash “4c5923b6a6fac7b7355f53bfe2b8f8c1” using the rainbow table above.<br /> `inS3CyourP4$$`
- Crack the hash “5b31f93c09ad1d065c0491b764d04933” using an online tool.<br />
I submitted it on [Hashes.com](https://hashes.com/en/decrypt/hash): <br />
![image](https://github.com/user-attachments/assets/422622f7-6453-40ea-a7d1-78ef28162d9d)<br />
`tryhackme`
- Should you encrypt passwords in password-verification systems? Yea/Nay <br /> `Nay`

### Recognising Password Hashes
- What is the hash size in yescrypt?<br /> `256`
- What’s the Hash-Mode listed for Cisco-ASA MD5?<br />
Found the answer [here](https://hashcat.net/wiki/doku.php?id=example_hashes): <br />
![image](https://github.com/user-attachments/assets/c2bcfd55-193c-4806-8498-3c34fecb7644)<br />
`2410`

- What hashing algorithm is used in Cisco-IOS if it starts with $9$?<br />
Same thing:<br />
![image](https://github.com/user-attachments/assets/6466876f-f6d5-4790-9833-cf4e2b553252)<br />
`scrypt`

### Password Cracking
- Use hashcat to crack the hash, $2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG, saved in ~/Hashing-Basics/Task-6/hash1.txt.<br />
To answer each of the following question, you're going to need to find the hash mode to tell hashcat. To do that, go [here](https://hashcat.net/wiki/doku.php?id=example_hashes) and press CTRL+G to quickly find the mode you need. <br />
Move to the task folder, run ` hashcat -m 3200 -a 0 hash1.txt /usr/share/wordlists/rockyou.txt` and wait a minute. <br />
`85208520`
- Use hashcat to crack the SHA2-256 hash, 9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1, saved in saved in ~/Hashing-Basics/Task-6/hash2.txt.<br />
Move to the task folder, run `hashcat -m 1400 -a 0 hash2.txt /usr/share/wordlists/rockyou.txt` and wait a minute. <br />
`halloween`
- Use hashcat to crack the hash, $6$GQXVvW4EuM$ehD6jWiMsfNorxy5SINsgdlxmAEl3.yif0/c3NqzGLa0P.S7KRDYjycw5bnYkF5ZtB8wQy8KnskuWQS3Yr1wQ0, saved in ~/Hashing-Basics/Task-6/hash3.txt.<br />
Move to the task folder, run `hashcat -m 1800 -a 0 hash3.txt /usr/share/wordlists/rockyou.txt` and wait a minute.<br />
`spaceman`
- Crack the hash, b6b0d451bbf6fed658659a9e7e5598fe, saved in ~/Hashing-Basics/Task-6/hash4.txt.<br />
This time I used crackstation: <br />
![image](https://github.com/user-attachments/assets/1b163d1a-1f5e-466a-abbf-66fc5a785f88)<br />
`funforyou`

### Hashing for Integrity Checking
- What is SHA256 hash of libgcrypt-1.11.0.tar.bz2 found in ~/Hashing-Basics/Task-7?<br />
Move in the task folder and run `sha256sum libgcrypt-1.11.0.tar.bz2 `:<br />
`09120c9867ce7f2081d6aaa1775386b98c2f2f246135761aae47d81f58685b9c`
- What’s the hashcat mode number for HMAC-SHA512 (key = $pass)?<br />
Can be found in the [hashcat manpage](https://hashcat.net/wiki/doku.php?id=example_hashes): <br />
![image](https://github.com/user-attachments/assets/257d6b6c-7a14-4c4e-913d-c05bcc5773f8)<br />
`1750`

### Conclusion
- Use base64 to decode RU5jb2RlREVjb2RlCg==, saved as decode-this.txt in ~/Hashing-Basics/Task-8. What is the original word?<br /> `ENcodeDEcode`

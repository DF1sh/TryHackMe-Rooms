# Hashing - Crypto 101

### Key Terms
- Is base64 encryption or encoding? `encoding`

### What is a hash function?
- What is the output size in bytes of the MD5 hash function? `16`
- Can you avoid hash collisions? (Yea/Nay) `Nay`
- If you have an 8 bit hash output, how many possible hashes are there? `256`

### Uses for hashing
- Crack the hash "d0199f51d2728db6011945145a1b607a" using the rainbow table manually. <br />
If the value is trivial, you can try to use [Crackstation](https://crackstation.net/): <br />
![image](https://github.com/user-attachments/assets/c2b506a4-63cf-4e5e-8a9b-f82b35147a56)
`basketball`
- Crack the hash "5b31f93c09ad1d065c0491b764d04933" using online tools. Personally i found it [here](https://md5.gromweb.com/): `tryhackme`
- Should you encrypt passwords? Yea/Nay `Nay`

### Recognising password hashes
- How many rounds does sha512crypt ($6$) use by default? `5000 `
- What's the hashcat example hash (from the website) for Citrix Netscaler hashes? Go [here](https://hashcat.net/wiki/doku.php?id=example_hashes) to find the answer:  `1765058016a22f1b4e076dccd1c3df4e8e5c0839ccded98ea`
- How long is a Windows NTLM hash, in characters? `32`

### Password Cracking
- Crack this hash: $2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG <br />
![image](https://github.com/user-attachments/assets/feed4658-c028-4f9d-8b34-999c71663ee0) <br />
Cracked it with john the ripper: `85208520`
- Crack this hash: 9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1 `halloween` (found it on Cracksttion)
- Crack this hash: $6$GQXVvW4EuM$ehD6jWiMsfNorxy5SINsgdlxmAEl3.yif0/c3NqzGLa0P.S7KRDYjycw5bnYkF5ZtB8wQy8KnskuWQS3Yr1wQ0 <br />
![image](https://github.com/user-attachments/assets/f4c869d1-6297-47a0-87ec-e895eb30807f) <br />
Cracked using john the ripper: `spaceman`
- Bored of this yet? Crack this hash: b6b0d451bbf6fed658659a9e7e5598fe `funforyou` (again, Crackstation)

### Hashing for integrity checking
- What's the SHA1 sum for the amd64 Kali 2019.4 ISO? http://old.kali.org/kali-images/kali-2019.4/ `186c5227e24ceb60deb711f1bdc34ad9f4718ff9`
- What's the hashcat mode number for HMAC-SHA512 (key = $pass)? <br />
![image](https://github.com/user-attachments/assets/78bb5f4d-3927-4ded-ac0a-c6fe96e028e6) <br />
`1750`

# Public Key Cryptography Basics

### Common Use of Asymmetric Encryption
- In the analogy presented, what real object is analogous to the public key? `Lock`

### RSA
- Knowing that p = 4391 and q = 6659. What is n? `29239669`
- Knowing that p = 4391 and q = 6659. What is ϕ(n)? `29228620`

### Diffie-Hellman Key Exchange
- Consider p = 29, g = 5, a = 12. What is A? `7`
- Consider p = 29, g = 5, b = 17. What is B? `9`
- Knowing that p = 29, a = 12, and you have B from the second question, what is the key calculated by Bob? (key = Ba mod p) `24`
- Knowing that p = 29, b = 17, and you have A from the first question, what is the key calculated by Alice? (key = Ab mod p) `24`

### SSH
- Check the SSH Private Key in ~/Public-Crypto-Basics/Task-5. What algorithm does the key use? `RSA`

### Digital Signatures and Certificates
- What does a remote web server use to prove itself to the client? `Certificate`
- What would you use to get a free TLS certificate for your website? `Let's Encrypt`

### PGP and GPG
- Use GPG to decrypt the message in ~/Public-Crypto-Basics/Task-7. What secret word does the message hold?<br />
![image](https://github.com/user-attachments/assets/b2728bfe-2b66-40b4-b32d-bc27d836315d)<br />
`Pineapple`

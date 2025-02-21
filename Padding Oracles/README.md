# Padding Oracles

### Padding Schemes
- In cryptography, extra bytes are added to fill the remaining space in the last block during encryption, or decryption is called? `Padding`
- What is the byte value padded after padding the term HelloWorld? `06`

### Block Cipher Modes
- The encryption mode in which each plaintext block is XORed with the previous ciphertext block before being encrypted is called? `Cipher Block Chaining`
- What is the last byte after encrypting the word Hacker using the secret MyActualSecrets1?<br />
![image](https://github.com/user-attachments/assets/f9f57667-8007-49b1-bcb5-9769c40d0fb7)<br />
`54`

### CBC Mode - Decryption
- What is the plaintext after decrypting b1e090de4abbc8b54769ba79a98a4cffaf59a89e58bcc474794d1e8b7e5315b2 using the secret key abcdefghijklmnop? `THM{Encryption_007}`
- What should the IV size be in bytes if you try decrypting a string using AES (16-byte block size)? `16`

### How the Attack Works
- What is the flag value after decrypting the ciphertext? `THM-{brUt3-f0rC3}`
- While performing a padding oracle attack, what is the expected value for the last plaintext byte if you only modify the 16th byte of the modified IV? Use notations like 01, 02, 03, etc. only. `01`
- The foundation of the padding oracle lies in the formula Pi ​= Dk(Ci) {OPERATOR} Ci−1. What is the missing operator in the formula? `XOR`
 
### Automation
- What is the status code shown on the page when an "Invalid padding" error occurs?<br />
![image](https://github.com/user-attachments/assets/9c93b52b-3684-449d-a974-571debbb8997)<br />
`400`
- What is the decrypted value (ASCII) for the ciphertext 31323334353637383930313233343536bdcc4a2319946dc9b30203d89dba9fce with a block size of 16?<br />
![image](https://github.com/user-attachments/assets/e3ec2c58-7ce3-49eb-b539-e780cec44251)<br />
`Got_The_Flag007`

### Best Practices
- Is it a good practice to display padding errors on the production server (yea/nay)? `nay`

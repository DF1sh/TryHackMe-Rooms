# Length Extension Attacks

### Hash Functions
- What property prevents an attacker from reversing a hash to get the original input? `Pre-image Resistance`
- What property ensures that no two different messages produce the same hash? `Collision Resistance`

### Hashing Internals
- What block size does SHA-256 use? `512`
- What function ensures data is aligned to fit block size requirements? `Padding`
- How many words does SHA-256’s internal state have? `8`

### Understanding Length Extension Attacks
- What hashing method prevents length extension attacks by using a secret key? `HMAC`

### Practical - Attacking Signatures
- What is the flag in the image?<br />
Visit the following URL: `http://lea.thm/labs/lab1/product.php?file=1%2epng%80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00h%2f%2e%2e%2f4%2epng&signature=a9f7878a39b10d0a9d3d1765d3e83dd34b0b0242fa7e1567f085a5a9c467337a`:<br />
![image](https://github.com/user-attachments/assets/9c9f2ca9-76e2-4fc4-8700-af608788813b)<br />
`THM{L3n6th_3Xt33ns10nssss}`

### Practical - Modifying a Signed Cookie
- What is the flag?<br />
Modify the cookies in the browser according to the steps provided in the task: <br />
![image](https://github.com/user-attachments/assets/ba128110-ba98-43c1-b6d2-56ad7cb61dff)<br />
`THM{l3n6th_2_4dM1n}`

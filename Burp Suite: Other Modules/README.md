# Burp Suite: Other Modules

### Decoder: Overview
- Which feature attempts auto-decode of the input? `Smart decode`

### Decoder: Encoding/Decoding
- Base64 encode the phrase: Let's Start Simple. What is the base64 encoded version of this text? <br />
![image](https://github.com/user-attachments/assets/7f7e827d-9575-4f06-b6ae-3326931f1bf2)<br />
`TGV0J3MgU3RhcnQgU2ltcGxl`
- URL Decode this data: %4e%65%78%74%3a%20%44%65%63%6f%64%69%6e%67. What is the plaintext returned? <br />
![image](https://github.com/user-attachments/assets/a438950b-2364-47f1-9746-f33ed9d56442)<br />

- Use Smart decode to decode this data: .... What is the decoded text? <br />
![image](https://github.com/user-attachments/assets/4968a17c-9cf4-4651-832a-782952b4c29e)<br />
`47`
- Encode this phrase: Encoding Challenge. Start with base64 encoding. Take the output of this and convert it into ASCII Hex. Finally, encode the hex string into octal. What is the final string? <br />
![image](https://github.com/user-attachments/assets/90e78e16-7e48-4b07-9a26-70ed1e3ebb2b)<br />
`24034214a720270024142d541357471232250253552c1162d1206c`

### Decoder: Hashing
- Using Decoder, what is the SHA-256 hashsum of the phrase: Let's get Hashing!? Convert this into an ASCII Hex string for the answer to this question. <br />
![image](https://github.com/user-attachments/assets/ba368ece-00c1-4261-b6ea-1d8088bedd1f)<br />
`6b72350e719a8ef5af560830164b13596cb582757437e21d1879502072238abe`
- Generate an MD4 hashsum of the phrase: Insecure Algorithms. Encode this as base64 (not ASCII Hex) before submitting. <br />
![image](https://github.com/user-attachments/assets/a87e9f29-2f73-47c3-8430-4e767f4bfa20)<br />
`TcV4QGZZN7y7lwYFRMMoeA==`
- "Some joker has messed with my SSH key! There are four keys in the directory, and I have no idea which is the real one. The MD5 hashsum for my key is 3166226048d6ad776370dc105d40d9f8 — could you find it for me?" What is the correct key name? <br />
![image](https://github.com/user-attachments/assets/e422dde0-aa88-46ec-b1c6-70516f6d5d04)<br />
`key3`

### Sequencer: Overview
- What does Sequencer allow us to evaluate? `Entropy`

### Sequencer: Live Capture
- What is the overall quality of randomness estimated to be? `excellent`

### Organizer: Overview
- Are saved requests read-only? (yea/nay) `yea`

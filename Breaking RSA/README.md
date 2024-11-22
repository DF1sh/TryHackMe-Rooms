# Breaking RSA

### Capture the flag
- How many services are running on the box?<br />
Nmap scan shows ports 22 and 80 open:
![image](https://github.com/user-attachments/assets/ed96ad56-d0a3-47c6-a9ce-2c2ea645fc0d)<br />
`2`
- What is the name of the hidden directory on the web server? (without leading '/')<br />
![image](https://github.com/user-attachments/assets/26f52d6c-f6c7-4513-a5ec-535a14c3ae24)<br />
`development`
- What is the length of the discovered RSA key? (in bits)<br />
To answer this question I made Mr. GPT create a script for me, You can find it in this folder, named `get_key_length.py`(The `id_rsa.pub` file must be in the same folder of the script):<br />
![image](https://github.com/user-attachments/assets/813fee8b-3f81-4d0b-b606-617370f75db9)<br />
`4096`. This key length is actually secure.
- What are the last 10 digits of n? (where 'n' is the modulus for the public-private key pair)<br />

`1225222383ca`
- What is the numerical difference between p and q?<br />
- What is the flag?<br />

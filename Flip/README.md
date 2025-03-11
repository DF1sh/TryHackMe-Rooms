# Flip

### Flip
Let's understand the code I am provided with: <br />
![image](https://github.com/user-attachments/assets/1bc1b166-61ce-4f03-9e61-6e8f8613e1cf)<br />
This code creates a random key and initial vector of 16 bytes each. These parameters are used for the later AES encryption. It then asks me to prompt username and password, but they cannot be `admin:sUp3rPaSs1`.<br />
![image](https://github.com/user-attachments/assets/5d117681-de20-4857-8a8a-e7a79cf161b2)<br />
It then leaks the ciphertext of the username and password I provided, encrypted with the random key and iv. <br />
Then essentially the script wants me to provide the ciphertext of the string `access_username=admin&password=sUp3rPaSs1`. The ciphertext must use AES with the same key and iv used for the initial leaked ciphertext.<br /><br />
To get the flag I need to perform an attack that works specifically on AES-CBC, that is called bit-flipping attack. I didn't really dive too deep into this attack, but I understood that it exploits how AES-CBC works, specifically the fact that even if I don't know the original plaintext(which in this case I do), if I flip 1 bit on the ciphertext, this will result in another bit flipped in the plaintext(specifically the corresponding bit of the block after). But if I do that in blocks that are not the first block, then all the blocks before it will become garbage, so it's usually good to target only the first block, which is exactly what I'm going to do. <br />
![image](https://github.com/user-attachments/assets/4c8cbaf3-4984-4583-8241-69f62f75d492)<br />
As you can see, I changed `admin` to `bdmin`, and left the password the same, so that the server doesn't reject my input. Then I need to provide a ciphertext that decrypts to `access_username=admin&password=sUp3rPaSs1`. The leaked one decrypts into `access_username=admin&password=sUp3rPaSs1` (notice `bdmin` instead of `admin`). Notice also that `access_username=` is exactly 16 bytes, meaning that the first `b` (first letter of `bdmin`) is the very first byte of the second block! (AES uses blocks of 16 bytes, in this case) <br />
To flip the last bit of the first byte of the second block, I need to flip the last bit of the first byte of the first block.<br />
![image](https://github.com/user-attachments/assets/cee2191e-4665-4ecf-9ab8-00afa96313c1)<br />
So since each byte is 2 hexadecimal digits, I just modify the second hexadecimal digit by 1 unit(which corresponds to flipping the last bit of the byte). Thus, the server decrypts the string to `access_username=admin&password=sUp3rPaSs1`.

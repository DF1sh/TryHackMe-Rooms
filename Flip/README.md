# Flip

### Flip
Let's understand the code I am provided with: <br />
![image](https://github.com/user-attachments/assets/1bc1b166-61ce-4f03-9e61-6e8f8613e1cf)<br />
This code creates a random key and initial vector of 16 bytes each. These parameters are used for the later AES encryption. It then asks me to prompt username and password, but they cannot be `admin:sUp3rPaSs1`.<br />
![image](https://github.com/user-attachments/assets/5d117681-de20-4857-8a8a-e7a79cf161b2)<br />
It then leaks the ciphertext of the username and password I provided, encrypted with the random key and iv. <br />
Then essentially the script wants me to provide the ciphertext of the string `access_username=admin&password=sUp3rPaSs1`. The ciphertext must use AES with the same key and iv used for the initial leaked ciphertext. <br />
So essentially I get to chose a cleartext and a ciphertext, only once. And I have to use this knowledge to find what key and iv is being used, so that I can use those parameters to encrypt the message `access_username=admin&password=sUp3rPaSs1`.

TO BE CONTINUED....

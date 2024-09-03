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
- How many programs is "user" allowed to run via sudo? <br />
![image](https://github.com/user-attachments/assets/b100cc7e-6b4e-4df8-8810-8fa82ed825f1)<br />
`11`
- One program on the list doesn't have a shell escape sequence on GTFOBins. Which is it? `apache2`


### Cron Jobs - PATH Environment Variable
- What is the value of the PATH variable in /etc/crontab? <br />
![image](https://github.com/user-attachments/assets/4d02cfcd-373a-452e-8b6d-297e65ad4b1b)<br />
`/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin`

### Passwords & Keys - History Files
- What is the full mysql command the user executed?<br />
![image](https://github.com/user-attachments/assets/dd05b66d-f34d-42f3-b181-b71d372d4935)<br />
`mysql -h somehost.local -uroot -ppassword123`

### Passwords & Keys - Config Files
- What file did you find the root user's credentials in? <br />
![image](https://github.com/user-attachments/assets/218f0260-5165-4f00-8b8a-9f46273b6521)<br />
`/etc/openvpn/auth.txt`

### NFS
- What is the name of the option that disables root squashing? `no_root_squash`


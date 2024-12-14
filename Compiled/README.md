# Compiled
I would like to thank my dear friend [Simone](https://github.com/SimoneCiferri) who did this CTF with me and makes everything fun 

### Welcome
- What is the password?<br />
Im presented with a 64 bit ELF binary that waits for the user to input the right password:<br />
![image](https://github.com/user-attachments/assets/888e3bf6-2c56-448f-9cdd-99d58bd6de33)<br />
I will use IDA and GDB to solve this room. The `strings` command is not really enough to solve the challenge. So let's disassemble this son of a b****.<br />
![image](https://github.com/user-attachments/assets/9d80ccdd-f1ac-46d5-85fc-264f4a456d28)<br />
Here I highlighted the most important part of this code block. After prompting the string `Password: `, the `scanf` function is called, taking as parameters the string "DoYouEven%sCTF" and the user input.<br />
Right after that, the binary calls `strcmp` with parameters the string "__dso_handle" and the user input. It then performs a `cmp` instruction:<br />
![image](https://github.com/user-attachments/assets/be73cf2b-ecb7-4627-9d67-686027636e7f)<br />
The goal is to reach the code block on the bottom left, where the string `Correct` is prompted. To do that, the input string must be equal to the string "_init". <br />
At first, I thought the solution was something like `DoYouEven_initCTF`. But that's not the right password. So I decided to run the binary with GDB to understand better its behavior. <br />
So I run `gdb Compiled-1688545393558.Compiled`. I then put a breakpoint on the `strcmp` function, and run `run`:<br />
![image](https://github.com/user-attachments/assets/d0e48d44-520d-428f-931b-7b78b081a8d5)<br />
As a test, I prompted the password `DoYouEvenciaoCTF`. At this point I expected to find the string "ciao" in the `rdi` register. But that was not the case. To see the content of the string pointed by rdi, run `info r` to get information about registers:<br />
![image](https://github.com/user-attachments/assets/d844cc1a-d479-4a01-8a8c-c6c0a16c5b95)<br />
Then run `x/s 0x7fffffffdcc0`:<br />
![image](https://github.com/user-attachments/assets/424d7cce-c6f3-4618-8cd2-a8c74e820fb6)<br />
This is where I found out what the problem was. The function `scanf("DoYouEven%sCTF, &s1)` expects the string to start with "DoYouEven", but then saves in the `s1` variable the string provided as input AND everything AFTER that. That's why it it not "ciao", but "ciaoCTF". <br /> Why, you ask? I have no idea.<br />
So to pass the second `cmp` instruction(meaning s1="_init"), the right password is `DoYouEven_init`. 








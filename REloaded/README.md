# REloaded

For this challenges I'm using IDA Freeware on Windows.

### Level 0
The flag can be easily found from the strings. From IDA: <br />
![image](https://github.com/user-attachments/assets/8dcb9c12-1516-483e-b1a0-e96f74e5e0a3)<br />
`L3v3lZ340_is_D02e`

### Level 1
I started by inspecting the strings. Then I saw the subroutinse where they were referenced. In particular, I found the string "Thats ur lucky number !!!" inside sub_401410:<br />
![image](https://github.com/user-attachments/assets/4e35dacd-7854-4d88-8e1a-e1b6bf1f9554)<br />
As you can see, it compares the argument with `1709`. If they are the same, then we go to the left block and we win. So the answer is `1709`.


### Level 2
Again, the process was very similar as before. First, I located the following subroutine using strings: <br />
![image](https://github.com/user-attachments/assets/173110f3-8073-457c-89ad-a0768e6a4731)<br />
But I needed to go to the right block because the left block was just going to stop the execution. For that I put a breakpoint on the  `jg` instruction and changed the ZERO FLAG from 1 to 0, so that the execution goes to the right block. One of the subroutines of the block contains the following code: <br />
![image](https://github.com/user-attachments/assets/7c149b1a-cc5a-4a47-8700-5a1217663025)<br />
There's a `strcmp` function which seems to decide the outcome of the execution. So I put a breakpoin on it, and, to see the contents of the two strings that are getting compared, I right-click on the hex-view and select "Synchronize with EAX". And as shown in the picture above, there's the flag! <br />
`L3_1s_20t_Th3_L131t)`

### Level 3
Damn. I had an hard time on this one. First of all, I located the following subrouting looking at where the string "Enter the flag ::" was being referenced:  <br />
![image](https://github.com/user-attachments/assets/3cd46112-60ae-4819-b069-0d364cded58b)<br />
Let's see what's inside sub-4014AF: <br />
![image](https://github.com/user-attachments/assets/987c07b3-5c31-4a93-8d73-e4681c22f442)<br />
There's the "Rooted !!!" message. I want to go there. However the password is actually XORed before being compared to a value. If I just put a breakpoint at the last jump, I get that the password is `SOJdsa*K3`. But it is not, that is the XORed value of the password. <br />
To see the clear text password, I have to check its value before it gets xored. To do so, I move into sub_401410, which contains  the xor: <br />
![image](https://github.com/user-attachments/assets/ec3b1b44-5ac6-43e5-a60b-8e62a4af963c)<br /> A
I started debugging and enumerating memory contents of various variables, and here's the content of that memory location: <br />
![image](https://github.com/user-attachments/assets/37d38857-c38c-4dca-8277-8413c419bea2)<br />
`THMctf-L4`

### Level 4
I had no strings to reference this time. I look manually every subroutine and found sub_401453 that contains APIs such as printf or strlen, which looks like where the execution might go. Here's how the function is structured: <br />
![image](https://github.com/user-attachments/assets/3ef4d004-4164-47ea-8a26-0f000abfc4d1)<br />
![image](https://github.com/user-attachments/assets/ac8f1eb1-a1e0-4b0d-a64b-b163f49e67b9)<br />
Essentially it takes user input in `arg_0`, and encrypts it using a code, and then prints with `printf` the ciphertext. I found the code in a very similar way of the previous level. I put a breakpoint at the very beginning of the function: <br />
![image](https://github.com/user-attachments/assets/8e5be34a-f387-4f05-b0e9-7b628c8bf176)<br />
I then synchronized the hex-view with EAX, and there's the code! <br />
`Alan Turing Was a Geniuse`

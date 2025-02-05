# 0x41haz

### 0x41haz
The binary works like this:<br />
![image](https://github.com/user-attachments/assets/9684dbb7-9fd9-4460-9e04-8a48a7528f8e)<br />
I need to find the password by looking at the binary. I open it using IDA freeware. This is the main:<br />
![image](https://github.com/user-attachments/assets/f6017ef3-0e55-47ad-b91c-10450e0bd74e)<br />
Next, we have the following blocks:<br />
![image](https://github.com/user-attachments/assets/ecaa1c37-0409-4094-8462-c16f0ae1029e)<br />
If the lenght of the password is not 13, then we fail. If it's 13, then a loop starts, from an index (I called it "index") that goes from 0 to 12. And this is the content of the loop:<br />
![image](https://github.com/user-attachments/assets/e805b7aa-a95f-4096-9677-52a8179ef28a)<br />
The problem is that `var_16` contains only 8 characters (decoded in hexadecimal it's `fg$52@@2`), but the loop is 13!. But here's what interesting. If we look at all the variables:<br />
![image](https://github.com/user-attachments/assets/c887a46d-687f-445a-a8f0-ade3df9e5285)<br />
Yes, `var_16` is only 8 characters, but then there's `var_E` that is `40265473h`, 4 characters! and then there's `var_A` which is the character `L`. They sum up to 13. I can feel my dopamine rn.<br />

    var_16 = fg$52@@2
    var_E = @&Ts
    var_A = L
Let's do it!<br />
![image](https://github.com/user-attachments/assets/fb8db4f7-e3fb-480e-8b21-8ccd03473c83)<br />
Fuck.<br /><br />

I was stuck for a while here. I looked at an external write up. Basically I had to change the 6th byte of the signature that defines the endiannes of the program.<br />
After changing that byte to `01`, the strings are now reversed. <br />
![image](https://github.com/user-attachments/assets/5a4a2e80-d584-4927-8d92-625f2ca27d15)<br />
The password was actually: `2@@25$gfsT&@L`





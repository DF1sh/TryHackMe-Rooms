# Reversing ELF

### Crackme1
![image](https://github.com/user-attachments/assets/420f424f-705a-41f2-91e4-a168c76302a7)<br />

### Crackme2
Run `strings crackme2` to find the password.<br />
![image](https://github.com/user-attachments/assets/20e15cb2-0978-44c6-995e-051ea10022e1)<br />
![image](https://github.com/user-attachments/assets/863e506a-eac0-4dc6-999e-b3083f9b6983)<br />

### Crackme3
Again, run `strings crackme3`:<br />
![image](https://github.com/user-attachments/assets/92e3d89d-4e7e-40bc-996a-c992119f9579)<br />
![image](https://github.com/user-attachments/assets/4bd1e2e8-34ea-4887-a7cc-ed288176c682)<br />

### Crackme4
For this one I used `gdb`, put a breakpoint on the first `strcmp` function and analyzed registers to see the password:<br />
![image](https://github.com/user-attachments/assets/1c04087a-23d2-4206-98fd-ff163df59f34)<br />


### Crackme5
I had to use IDA for this one, strings wasn't enough <br />
![image](https://github.com/user-attachments/assets/15311915-e301-4b46-9d9e-178b6931c005)<br />
`OfdlDSA|3tXb32~X3tX@sX`4tXtz`

### Crackme6
Inside this binary there a function called `my_secure_test`:<br />
![image](https://github.com/user-attachments/assets/ef469572-5560-4572-aa2e-cfdcc9acd864)<br />
It contains all the characters of the password. You just have to scroll:<br />
![image](https://github.com/user-attachments/assets/8925b8e6-cae9-4845-b06a-136480545975)<br />
![image](https://github.com/user-attachments/assets/e74efb53-d275-4efe-be97-a608d2d53453)<br />

### Crackme7
This is how the binary behaves:<br />
![image](https://github.com/user-attachments/assets/9f596d7a-2b75-4900-8815-ed9bedac2caa)<br />
When analyzing with IDA, I found a block that I guess it's my goal to reach:<br />
![image](https://github.com/user-attachments/assets/e59d392a-db52-4718-bd03-d0958a518448)<br />
And it is reached with these two blocks.<br />
![image](https://github.com/user-attachments/assets/a35aa166-32e1-488b-9c07-e6de5dccc429)<br />
My guess is that I have to prompt `31337`, infact:<br />
![image](https://github.com/user-attachments/assets/bc6ec526-be2c-48b4-bf45-ccdce2f297ac)<br />

### Crackme8
My goal is to reach the bottom-right block:<br />
![image](https://github.com/user-attachments/assets/eb910bda-d534-4a00-96fc-0195934a7c8c)<br />
In particular I want to focus on the last compare before the jump to that block. What is this `_atoi` function? :<br />
![image](https://github.com/user-attachments/assets/2c85c379-a92b-486c-afde-e46fc3a7ce3c)<br />
![image](https://github.com/user-attachments/assets/ffb3dd5d-31db-4227-9f24-33d5f6f27eed)<br />
So I think I need to find a string such that, when converted to a number, it's `3405705229`. <br />
Also, if I decompile the code(I used an online tool), I get this:<br />
![image](https://github.com/user-attachments/assets/3140ed04-5bee-4161-b5a6-ddbbcea507aa)<br />
![image](https://github.com/user-attachments/assets/172a8353-ec29-4990-97ce-4af82a640050)<br />


# x86 Assembly Crash Course

### Opcodes and Operands
- What are the hex codes that denote the assembly operations called? `Opcodes`
- Which type of operand is denoted by square brackets? `memory operand`

### General Instructions
- In mov eax, ebx, which register is the destination operand? `eax`
- What instruction performs no action? `nop`

### Flags
- Which flag will be set if the result of the operation is zero? (Answer in abbreviation) `ZF`
- Which flag will be set if the result of the operation is negative? (Answer in abbreviation) `SF`

### Arithmetic and Logical Instructions
- In a subtraction operation, which flag is set if the destination is smaller than the subtracted value? `Carry Flag`
- Which instruction is used to increase the value of a register `inc`
- Do the following instructions have the same result? (yea/nay)<br />
xor eax, eax<br />
mov eax, 0<br />
`yea`

### Conditionals and Branching
- Which flag is set as a result of the test instruction being zero? `Zero flag`
- Which of the below operations uses subtraction to test two values? 1 or 2?<br />
1. cmp eax, ebx
2. test eax, ebx<br />
`1`
- Which flag is used to identify whether a jump will be taken or not after a jz or jnz instruction? `Zero flag`

### Stack and Function calls
- Which instruction is used for performing a function call? `call`
- Which instruction is used to push all registers to the stack? `pusha`

### Practice Time
- While running the MOV instructions, what is the value of [eax] after running the 4th instruction? (in hex)<br />
![image](https://github.com/user-attachments/assets/0210a6f2-1277-4476-8d97-cf988d33efbf)<br />
`0x00000040`
- What error is displayed after running the 6th instruction from the MOV instruction section?<br />
![image](https://github.com/user-attachments/assets/663ef6d3-75d6-4e1a-b223-892c438cfe17)<br />
`Memory to memory data movement is not allowed.`
- Run the instructions from the stack section. What is the value of eax after the 9th instruction? (in hex)<br />
![image](https://github.com/user-attachments/assets/3377bd27-4162-47a0-9134-0fab176a5521)<br />
`0x00000025`
- Run the instructions from the stack section. What is the value of edx after the 12th instruction? (in hex) `0x00000010`
- Run the instructions from the stack section. After POP ecx, what is the value left at the top of the stack? (in hex) `0x00000010`
- Run the cmp and test instructions. Which flags are triggered after the 3rd instruction? (Note: Use these abbreviations in alphabetical order with no spaces: CF,PF,SF,ZF)<br />
![image](https://github.com/user-attachments/assets/753871d6-f2c2-43c8-ab00-a1550c67491a)<br />
`PF,ZF`
- Run the test and the cmp instructions. Which flags are triggered after the 11th instruction? (Note: Use these abbreviations in alphabetical order with no spaces: CF,PF,SF,ZF) `CF,SF`
- Run the instructions from the lea section. What is the value of eax after running the 9th instruction? (in hex) `0x0000004B`
- Run the instructions from the lea section. What is the final value found in the ECX register? (in hex)<br />
![image](https://github.com/user-attachments/assets/c7fc30b4-6ae7-4efa-83fb-0c7c311e98a7)<br />
`0x00000045`

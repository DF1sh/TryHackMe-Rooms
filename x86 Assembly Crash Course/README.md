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
- While running the MOV instructions, what is the value of [eax] after running the 4th instruction? (in hex)
- What error is displayed after running the 6th instruction from the MOV instruction section?
- Run the instructions from the stack section. What is the value of eax after the 9th instruction? (in hex)
- Run the instructions from the stack section. What is the value of edx after the 12th instruction? (in hex)
- Run the instructions from the stack section. After POP ecx, what is the value left at the top of the stack? (in hex)
- Run the cmp and test instructions. Which flags are triggered after the 3rd instruction? (Note: Use these abbreviations in alphabetical order with no spaces: CF,PF,SF,ZF)
- Run the test and the cmp instructions. Which flags are triggered after the 11th instruction? (Note: Use these abbreviations in alphabetical order with no spaces: CF,PF,SF,ZF)
- Run the instructions from the lea section. What is the value of eax after running the 9th instruction? (in hex)
- Run the instructions from the lea section. What is the final value found in the ECX register? (in hex)

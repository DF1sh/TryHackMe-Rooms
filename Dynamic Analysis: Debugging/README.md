# Dynamic Analysis: Debugging

### The Need for Advanced Dynamic Analysis
- Malware sometimes checks the time before and after the execution of certain instructions to find out if it is being analysed. What type of analysis technique is bypassed by this attack? `basic dynamic analysis`
- What is a popular technique used by malware authors to obfuscate malware code from static analysis and unwrap it at runtime? `Packing`

### Introduction to Debugging
- Can we recover the pre-compilation code of a compiled binary for debugging purposes? Write Y for Yes or N for No `N`
- Which type of debugger is used for debugging compiled binaries? `assembly-level debugger`
- Which debugger works at the lowest level among the discussed debuggers? `Kernel-level debugger`

### Familiarization With a Debugger
- In which tab is the disassembly view shown in x32dbg? `CPU tab`
- If a process opens a file or a process, where can we see information regarding that opened file or process? `Handles tab`

### Debugging in Practice
- The attached VM has a crackme in the directory Desktop > crackme-arebel. In that crackme, there is a TLS callback with a conditional jump. Is this conditional jump taken? Write Y for Yes or N for No<br />
I'm using IDA for personal preference. To answer this question, click on the TLS callback function and put a breakpoint in it's memory location. Then step into the next couple of instructions until you reach the `cmp` instruction.
At this point you can look that the value of the zero flag (ZF) is 1, so the flag is set, and therefore the jump won't be performed:<br />
![image](https://github.com/user-attachments/assets/e96c56a8-618e-4d2a-af4e-5aa7e67bf3ff)<br />
`N`
- What is the value of the Zero Flag in the above-mentioned conditional jump? `1`
- Which API call in the mentioned sample is used for enumerating running processes?<br />
After some online search, I found the answer in the [documentation](https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-createtoolhelp32snapshot) of `CreateToolhelp32Snapshot`.
- From which Windows DLL is the API SuspendThread being called? `Kernel32.dll`

### Bypassing unwanted execution path
- What is it called when a binary's assembly code is permanently altered to get the desired execution path? `Patching`

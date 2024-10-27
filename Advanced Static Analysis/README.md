# Advanced Static Analysis

### Malware Analysis: Overview
- Does advanced static analysis require executing the malware in a controlled environment? (yay/nay) `nay`

### Connecting to the VM
- How many files are present in the Code_Constructs folder on the Desktop? `5`

### Ghidra: A Quick Overview
- How many function calls are present in the Exports section? `1`
- What is the only API call found in the User32.dll under the Imports section? `MessageBoxA`
- How many times can the "Hello World" string be found with the Search for Strings utility?<br />
![image](https://github.com/user-attachments/assets/3f530d68-558c-42b0-9a70-fd7748381033)<br />
`1`
- What is the virtual address of the CALL function that displays "Hello World" in a messagebox? `004073d7`

### Identifying C Code Constructs in Assembly
- What value gets printed by the while loop in the while-loop.exe program?<br />
![image](https://github.com/user-attachments/assets/4a2718bd-a816-43a3-991d-bf08c2609230)<br />
`_ITs_Fun_to_Learn_at_THM_`
- How many times, the while loop will run until the condition is met? `4`
- Examine the while-loop.exe in Ghidra. What is the virtual address of the instruction, that CALLS to print out the sentence "That's the end of while loop .."? `00401543`
- In the if-else.exe program, examine the strings and complete the sentence "This program demonstrates..........."<br />
![image](https://github.com/user-attachments/assets/91a9ca5a-5396-43ad-a3a2-f1899016941e)<br />
`This program demonstrates if-else statement `
- What is the virtual address of the CALL to the main function in the if-else.exe program?<br />
![image](https://github.com/user-attachments/assets/fb84ba25-ddb0-4704-97c8-607e27fceb7c)<br />
`00401509`

### An Overview of Windows API Calls
- When a process is created in suspended state, which hexadecimal value is assigned to the dwCreationFlags parameter?<br />
Found the answer [here](https://learn.microsoft.com/en-us/windows/win32/procthread/process-creation-flags):<br />
![image](https://github.com/user-attachments/assets/a8960645-1212-4fea-b026-2d38eb6c1a77)<br />
`0x00000004`

### Process Hollowing: Overview
- Which API is used to to write malicious code to the allocated memory during process hollowing?
`WriteProcessMemory()`

### Analyzing Process Hollowing
- What is the MD5 hash of the benign.exe sample?<br />
We have PEstudio in the VM, so use that to find the MD5 hash.<br />
![image](https://github.com/user-attachments/assets/d5cd8910-b316-4391-b542-444b56c8bd59)<br />
`E60A461B80467A4B1187AE2081F8CA24`
- How many API calls are returned if we search for the term 'Create' in the Symbol Tree section?<br />
![image](https://github.com/user-attachments/assets/f7814602-516d-4b6b-8af4-26116ef25423)<br />
`2`
- What is the first virtual address where the CreateProcessA function is called?<br />
![image](https://github.com/user-attachments/assets/54080ce0-6e21-4a59-8e6a-fcff467597d7)<br />
`0040108f`
- Which process is being created in suspended state by using the CreateProcessA API call?<br />
![image](https://github.com/user-attachments/assets/c21c82ea-61c6-4a73-8e7a-a98b435eb318)<br />
`iexplore.exe`
- What is the first virtual address where the CreateFileA function is called?<br />
![image](https://github.com/user-attachments/assets/3571bf0c-3b10-4055-9e37-d77fb09f887a)<br />
`004010f0`
- What is the suspicious process being injected into the victim process?<br />
![image](https://github.com/user-attachments/assets/a141199f-8672-4c14-8455-a60e7edb6799)<br />
`evil.exe`
- Based on the Function Graph, what is the virtual address of the code block that will be executed if the program doesn’t find the suspicious process?<br />
![image](https://github.com/user-attachments/assets/05002d98-5a2a-4e71-a63a-6979e58320ed)<br />
`00401101`
- Which API call is found in the import functions used to unmap the process's memory?<br />
![image](https://github.com/user-attachments/assets/1f2f8ba1-c170-4959-8fc3-3b6a19f05beb)<br />
`NtUnmapViewOfSection`
- How many calls to the WriteProcessMemory function are found in the code? (.text section)<br />
![image](https://github.com/user-attachments/assets/6fe2ab63-539b-418a-baac-d403b2be41aa)<br />
`2`
- What is the full path of the suspicious process shown in the strings?<br />
![image](https://github.com/user-attachments/assets/6793cf5e-0a95-487b-97ef-941a0aafafeb)<br />
`C:\\Users\\THM-Attacker\\Desktop\\Injectors\\evil.exe`

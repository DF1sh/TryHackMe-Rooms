# Windows Internals

### Processes
Open procmon inside the "Process Monitor" folder, and open the LogFile, like so: <br />
![image](https://github.com/user-attachments/assets/54840ea5-fe2f-4051-b48d-ed8d823a3db0)<br />
- What is the process ID of "notepad.exe"?<br />
Click on "Filter" and filter by process name, like so: <br />
![image](https://github.com/user-attachments/assets/a56eff8c-6323-488c-94dd-04f758e9a0b2)<br />
![image](https://github.com/user-attachments/assets/d6a53b4a-b8e3-49a0-b3ca-5e654f749df9)<br />
`5984`
- What is the parent process ID of the previous process?<br />
Click on one of the "notepad.exe" entries and select "properties" to find the answer:<br />
![image](https://github.com/user-attachments/assets/3fefeffa-1c91-4931-b9fc-c35eca676c7f)<br />
`3412`
- What is the integrity level of the process?<br />
The same panel shows the answer: `High`

### Threads
- What is the thread ID of the first thread created by notepad.exe?<br />
Find the operation `Thread Create`:<br />
![image](https://github.com/user-attachments/assets/d3577917-9af8-473c-b4b4-81d8daf5e0c7)<br />
``
- What is the stack argument of the previous thread? <br />
![image](https://github.com/user-attachments/assets/117b1638-6cf5-4783-b2b0-b9c9c8cd67ce)
`6584`

### Virtual Memory
- What is the total theoretical maximum virtual address space of a 32-bit x86 system?<br /> `4 GB`
- What default setting flag can be used to reallocate user process address space?<br /> `increaseuserva`
- What is the base address of "notepad.exe"?What is the base address of "notepad.exe"?<br />
![image](https://github.com/user-attachments/assets/535b0e96-df24-4900-b706-c030209cc5d2)<br />
`0x7ff652ec0000`

### Dynamic Link Libraries
- What is the base address of "ntdll.dll" loaded from "notepad.exe"?<br />
![image](https://github.com/user-attachments/assets/a68dc29e-d05f-418a-a942-4d8c7f55d7a8)<br />
`0x7ffd0be20000`
- What is the size of "ntdll.dll" loaded from "notepad.exe"?<br />
Open the properties:<br />
![image](https://github.com/user-attachments/assets/294e538d-3bd7-4cd8-82d5-be71e432dbdb)<br />
`0x1ec000`
- How many DLLs were loaded by "notepad.exe"?<br />
Use the following filters: <br />
![image](https://github.com/user-attachments/assets/6822051e-083a-4667-9086-57c77767dff7)<br />
`51`

### Portable Executable Format
- What PE component prints the message "This program cannot be run in DOS mode"?<br /> `DOS Stub`
- What is the entry point reported by DiE?<br />
![image](https://github.com/user-attachments/assets/22fdabe0-e495-43c9-a7d0-23b7faefc6a3)<br />
`000000014001acd0`
- What is the value of "NumberOfSections"?<br />
![image](https://github.com/user-attachments/assets/a0095f90-e584-4714-b23e-c4a1c26461c2)<br />
`0006`
- What is the virtual address of ".data"?<br />
![image](https://github.com/user-attachments/assets/3eb0203a-4b70-47d6-8825-8df43486bb70)<br />
`00024000`
- What string is located at the offset "0001f99c"?<br />
![image](https://github.com/user-attachments/assets/2e5ffd8d-8cfc-4d89-a30c-d950cc40cbf0)<br />
`Microsoft.Notepad`

### Interacting with Windows Internals
Open a command prompt and execute the provided file: "inject-poc.exe" and answer the questions below.<br />
- Enter the flag obtained from the executable below.<br />
![image](https://github.com/user-attachments/assets/3780d9fd-cbd9-4982-bc5a-a3af2070eac6)<br />
`THM{1Nj3c7_4lL_7h3_7h1NG2}`


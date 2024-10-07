# Dissecting PE Headers

### Overview of PE headers
- What data type are the PE headers? `STRUCT`

### IMAGE_DOS_HEADER and DOS_STUB
- How many bytes are present in the IMAGE_DOS_HEADER? `64`
- What does MZ stand for? `Mark Zbikowski`
- In what variable of the IMAGE_DOS_HEADER is the address of IMAGE_NT_HEADERS saved? `e_lfanew`
- In the attached VM, open the PE file Desktop/Samples/zmsuz3pinwl in pe-tree. What is the address of IMAGE_NT_HEADERS for this PE file?<br /> `0x000000f8`

### IMAGE_NT_HEADERS
- In the attached VM, there is a file Desktop\Samples\zmsuz3pinwl. Open this file in pe-tree. Is this PE file compiled for a 32-bit machine or a 64-bit machine?<br />
![image](https://github.com/user-attachments/assets/e0735a83-1ece-4aea-b951-1fd8b16c6821)<br />
`32-bit machine`
- What is the TimeDateStamp of this file?<br />
![image](https://github.com/user-attachments/assets/631a1307-f28e-4b14-8272-741bbf274e17)<br />
`0x62289d45 Wed Mar  9 12:27:49 2022 UTC`

### OPTIONAL_HEADER
- Which variable from the OPTIONAL_HEADER indicates whether the file is a 32-bit or a 64-bit application? `Magic`
- What Magic value indicates that the file is a 64-bit application? `0x020B`
- What is the subsystem of the file Desktop\Samples\zmsuz3pinwl? <br />
![image](https://github.com/user-attachments/assets/ed614759-d6f3-4a34-8ade-6996f55fbe1c)<br />
`0x0003 WINDOWS_CUI`

### IMAGE_SECTION_HEADER
- How many sections does the file Desktop\Samples\zmsuz3pinwl have? `7`
- What are the characteristics of the .rsrc section of the file Desktop\Samples\zmsuz3pinwl<br />
![image](https://github.com/user-attachments/assets/a0ffd0aa-788b-48de-879a-1658e766ba5d)<br />
`0xe0000040 INITIALIZED_DATA | EXECUTE | READ | WRITE`

### IMAGE_IMPORT_DESCRIPTOR
- The PE file Desktop\Samples\redline imports the function CreateWindowExW. From which dll file does it import this function?<br />
`User32.dll`

### Packing and Identifying packed executables
- Which of the files in the attached VM in the directory Desktop\Samples seems to be a packed executable?<br />
`zmsuz3pinwl`

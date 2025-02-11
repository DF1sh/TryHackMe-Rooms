### Introduction to Windows API

### Subsystem and Hardware Interaction
- Does a process in the user mode have direct hardware access? (Y/N) `N`
- Does launching an application as an administrator open the process in kernel mode? (Y/N) `N`

### Components of the Windows API
- What header file imports and defines the User32 DLL and structure? `winuser.h`
- What parent header file contains all other required child and core header files? `windows.h`

### OS Libraries
- What overarching namespace provides P/Invoke to .NET? `system`
- What memory protection solution obscures the process of importing API calls? `ASLR`

### API Call Structure
- Which character appended to an API call represents an ANSI encoding? `A`
- Which character appended to an API call represents extended functionality? `Ex`
- What is the memory allocation type of 0x00080000 in the VirtualAlloc API call?<br />
Found the answer [here](https://learn.microsoft.com/it-it/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc):<br />
![image](https://github.com/user-attachments/assets/01d87730-b8d7-406c-94b5-859236c737e8)<br />
`MEM_RESET`

### C API Implementations
- Do you need to define a structure to use API calls in C? (Y/N) `N`

### .NET and PowerShell API Implementations
- What method is used to import a required DLL? `DllImport`
- What type of method is used to reference the API call to obtain a struct? `External`

### Commonly Abused API Calls
- Which API call returns the address of an exported DLL function? `GetProcAddress`
- Which API call imports a specified DLL into the address space of the calling process? `LoadLibrary`

### Malware Case Study
- What Win32 API call is used to obtain a pseudo handle of our current process in the keylogger sample? `GetCurrentProcess`
- What Win32 API call is used to set a hook on our current process in the keylogger sample? `SetWindowsHookEx`
- What Win32 API call is used to obtain a handle from the pseudo handle in the keylogger sample? `GetModuleHandle`
- What Win32 API call is used unset the hook on our current process in the keylogger sample? `UnhookWindowsHookEx`
- What Win32 API call is used to allocate memory for the size of the shellcode in the shellcode launcher sample? `VirtualAlloc`
- What native method is used to write shellcode to an allocated section of memory in the shellcode launcher sample? `Marshal.Copy`
- What Win32 API call is used to create a new execution thread in the shellcode launcher sample? `CreateThread`
- What Win32 API call is used to wait for the thread to exit in the shellcode launcher sample? `WaitForSingleObject`

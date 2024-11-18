# Anti-Reverse Engineering

### Anti-Debugging (Overview)
- What is the name of the Windows API function used in a common anti-debugging technique that detects if a debugger is running? `IsDebuggerPresent`

### Anti-Debugging using Suspend Thread
- What is the Windows API function that enumerates windows on the screen so the malware can check the window name? `EnumWindows`
- What is the hex value of a nop instruction? `90`
- What is the instruction found at memory location 004011CB?<br />
![image](https://github.com/user-attachments/assets/7413d7c1-564a-4b75-90d9-7d45a0891c15)<br />
`add esp,8`

### VM Detection (Overview)
- What is the name of the identifiable process used by malware to check if the machine is running inside VirtualBox? `vboxservice`
- What is the OUI automatically assigned specifically to VMware?<br />
Found the answer [here](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.networking.doc/GUID-1B6A280E-0C77-4775-8F84-4B3F40673178.html): `00:50:56`
- Using Task Manager, what process indicates that the machine for this room is an Amazon EC2 Virtual Machine?<br />
![image](https://github.com/user-attachments/assets/a44cf63c-2f41-4886-aae3-18e20bf5bb14)<br />
`amazon-ssm-agent.exe`

### VM Detection by Checking the Temperature
- In the C code snippet, what is the full WQL query used to get the temperature from the Win32_TemperatureProbe class? `SELECT * FROM MSAcpi_ThermalZoneTemperature`
- What register holds the memory address that tells the debugger what instruction to execute next? `EIP`
- Before uReturn is compared to zero, what is the memory location pointed to by [ebp-4] <br />
Had to see the hint for this:<br />
![image](https://github.com/user-attachments/assets/d26d4039-fb32-4a8d-9753-cee5c63b621e)<br />
`0019FF1C`

### Packers (Overview)
- What is the decoded string of the base64 encoded string "VGhpcyBpcyBhIEJBU0U2NCBlbmNvZGVkIHN0cmluZy4="? `This is a BASE64 encoded string.`

### Identifying and Unpacking
- According to DetectItEasy, what is the version of the Microsoft Linker used for linking packed.exe?<br />
![image](https://github.com/user-attachments/assets/def15b49-8864-432a-882b-ddec87937eff)<br/>
`14.16`

- According to pestudio, what is the entropy of the UPX2 section of packed.exe? <br />
![image](https://github.com/user-attachments/assets/f2bb17a6-82c4-49f7-bff7-accf6e822d8c)<br />
`2.006`

# Osquery: The Basics

### Osquery: Interactive Mode
- How many tables are returned when we query "table process" in the interactive mode of Osquery? <br />
![image](https://github.com/user-attachments/assets/0e795291-38db-46a5-8377-91d8f337f8c6)<br />
`3`
- Looking at the schema of the processes table, which column displays the process id for the particular process?<br />
![image](https://github.com/user-attachments/assets/39e66108-cb65-4cfc-8faf-47cfeeda7564)<br />
`pid`
- Examine the .help command, how many output display modes are available for the .mode command? <br />
![image](https://github.com/user-attachments/assets/9d508282-5767-4d9a-b0e6-a693076c744c)<br />
`5`

### Schema Documentation
- In Osquery version 5.5.1, how many common tables are returned, when we select both Linux and Window Operating system? <br />
Check the documentation to find the answer: <br />
![image](https://github.com/user-attachments/assets/7667a0b1-e2de-4f5f-87f6-f6ed4d4b576f)<br />
`56`
- In Osquery version 5.5.1, how many tables for MAC OS are available? <br />
Do the same thing: `180`
- In the Windows Operating system, which table is used to display the installed programs? `programs`
- In Windows Operating system, which column contains the registry value within the registry table? <br />
![image](https://github.com/user-attachments/assets/05587d3c-9e19-4a5f-a546-a3d92a54716e)<br />
`data`


### Creating SQL queries
- Using Osquery, how many programs are installed on this host? <br />
![image](https://github.com/user-attachments/assets/127497c7-80ec-407b-b590-3d9a9e35ee44)<br />
`19selec`
- Using Osquery, what is the description for the user James?<br />
![image](https://github.com/user-attachments/assets/5edfee9b-aba1-42e7-b715-6252adb9f901)<br />
`Creative Artist`
- When we run the following search query, what is the full SID of the user with RID '1009'? Query: select path, key, name from registry where key = 'HKEY_USERS'; `S-1-5-21-1966530601-3185510712-10604624-1009`
- When we run the following search query, what is the Internet Explorer browser extension installed on this machine? Query: select * from ie_extensions; <br />
![image](https://github.com/user-attachments/assets/ac9858ce-d666-41dc-b2d0-ef48cf8990af)<br />
`C:\Windows\System32\ieframe.dll`
- After running the following query, what is the full name of the program returned? Query: select name,install_location from programs where name LIKE '%wireshark%'; <br />
![image](https://github.com/user-attachments/assets/cb889cf3-a7ee-4f0b-b258-e723204c9188)<br />


### Challenge and Conclusion
- Which table stores the evidence of process execution in Windows OS? `userassist`
- One of the users seems to have executed a program to remove traces from the disk; what is the name of that program? <br />
![image](https://github.com/user-attachments/assets/abd54cee-443f-43e9-a5e7-7a4f0d96388b)<br />
`DiskWipe.exe`
- Create a search query to identify the VPN installed on this host. What is name of the software? <br />
Run the following query: `SELECT * FROM programs WHERE LOWER(name) LIKE '%vpn%';` <br />
![image](https://github.com/user-attachments/assets/53adbfc7-cf89-4a37-a986-75fe022fa377)<br />
`ProtonVPN`
- How many services are running on this host? <br />
![image](https://github.com/user-attachments/assets/c03bf2d9-64cc-4219-981a-2240b7ce9634)<br />
`214`
- A table autoexec contains the list of executables that are automatically executed on the target machine. There seems to be a batch file that runs automatically. What is the name of that batch file (with the extension .bat)? <br />
Run the query: `SELECT * FROM autoexec WHERE path LIKE '%.bat';`<br />
![image](https://github.com/user-attachments/assets/e471b018-54d4-44bb-9017-8b2c83b98c17)<br />
`batstartup.bat`
- What is the full path of the batch file found in the above question? (Last in the List) `C:\Users\James\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\batstartup.bat`

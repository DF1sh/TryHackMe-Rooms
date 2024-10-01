# Velociraptor

### Deployment 
There's a .txt file on the desktop that will show us what commands to run on the Ubuntu subsystem.<br />
![image](https://github.com/user-attachments/assets/218c1f5c-bf99-40b3-a80c-88ac8d01b35d)<br />
Follow the steps provided in the task to correctly access the velociraptor's GUI.<br />
- Using the documentation, how would you launch an Instant Velociraptor on Windows?<br />
![image](https://github.com/user-attachments/assets/479ed9a5-80a9-4b72-a825-9419b3a09efd)<br />
`velociraptor.exe gui`

### Interacting with client machines
- What is the hostname for the client?<br />
![image](https://github.com/user-attachments/assets/cc443bb9-c9a6-4b9c-8bd7-3146db89373c)<br />
`thm-velociraptor.eu-west-1.compute.internal`
- What is listed as the agent version?<br />
`2021-04-11T22:11:10Z`
- In the Collected tab, what was the VQL command to query the client user accounts?<br />
Move to the "Collected" tab, and check the requests: <br />
![image](https://github.com/user-attachments/assets/2e6c0c50-2091-4bc5-a386-ec38fe1aea3c)<br />
`LET Generic_Client_Info_Users_0_0=SELECT Name, Description, Mtime AS LastLogin FROM Artifact.Windows.Sys.Users()`
- In the Collected tab, check the results for the PowerShell whoami command you executed previously. What is the column header that shows the output of the command?<br />
![image](https://github.com/user-attachments/assets/5901d865-c410-4718-94d5-65e6108dd889)<br />
`Stdout`
- In the Shell, run the following PowerShell command Get-Date. What was the PowerShell command executed with VQL to retrieve the result?<br />
![image](https://github.com/user-attachments/assets/17b3b33a-5f0a-4be8-90d1-4d251dbb61de)<br />
`powershell -ExecutionPolicy Unrestricted -encodedCommand RwBlAHQALQBEAGEAdABlAA==`

### Creating a new collection
- Earlier you created a new artifact collection for Windows.KapeFiles.Targets. You configured the parameters to include Ubuntu artifacts. Review the parameter description for this setting. What is this parameter specifically looking for?<br />
`Ubuntu on Windows Subsystem for Linux`
- Review the output. How many files were uploaded?<br />
Select "Uploaded Files":<br />
![image](https://github.com/user-attachments/assets/5aa68429-f7e2-4594-a7f0-d3cb2203cc25)<br />
It says that there are 19 rows, but for some reason the answer is `20`, idk

### VFS (Virtual File System)
- Which accessor can access hidden NTFS files and Alternate Data Streams? (format: xyz accessor)<br /> `ntfs accessor`
- Which accessor provides file-like access to the registry? (format: xyz accessor)<br /> Found the answer [here](https://docs.velociraptor.app/docs/gui/vfs/):  `registry accessor`
- What is the name of the file in $Recycle.Bin?<br />
![image](https://github.com/user-attachments/assets/adae1f47-f25d-4700-85f5-bb1809f2839e)<br />
`desktop.ini`
- There is hidden text in a file located in the Admin's Documents folder. What is the flag?<br />
![image](https://github.com/user-attachments/assets/5ea29891-2e4c-4aed-a90e-d7047db8641b)<br />
`THM{VkVMT0NJUkFQVE9S}`

### VQL (Velociraptor Query Language)
The answers to the following questions can be found researching the [VQL documentation](https://docs.velociraptor.app/docs/vql/):<br />
- What is followed after the SELECT keyword in a standard VQL query?<br />
![image](https://github.com/user-attachments/assets/3021e801-1935-44b9-89db-5facffa2df62)<br />
`Column Selectors`
- What goes after the FROM  keyword?<br /> `VQL Plugin`
- What is followed by the WHERE keyword?<br /> `Filter expression`
- What can you type in the Notepad interface to view a list of possible completions for a keyword?<br />
![image](https://github.com/user-attachments/assets/753795d6-79b0-428c-9a68-395f5cdfd744)<br />
`?`
- What plugin would you use to run PowerShell code from Velociraptor?<br />
The answer for this can be found [here](https://docs.velociraptor.app/docs/extending_vql/): <br />
![image](https://github.com/user-attachments/assets/94c07432-67d8-4f52-a2cd-c31cce205706)<br />
`execve()`

### Forensic Analysis VQL Plugins
- What are the arguments for parse_mft()?<br />
The answer is [here](https://docs.velociraptor.app/docs/forensic/ntfs/): <br />
![image](https://github.com/user-attachments/assets/d32b891b-b6e2-4443-801f-15371cb90a83)<br />
`parse_mft(filename="C:/$MFT", accessor="ntfs")`
- What filter expression will ensure that no directories are returned in the results?<br /> `IsDir`

### Hunt for a nightmare
- What is the name in the Artifact Exchange to detect Printnightmare?<br /> `Windows.Detection.PrintNightmare`
- Per the above instructions, what is your Select clause? (no spaces after commas)<br /> `SELECT “C:/” + FullPath AS Full_Path,FileName AS File_Name,parse_pe(file=”C:/” + FullPath) AS PE`
- What is the name of the DLL that was  placed by the attacker?<br /> `nightmare.dll`
- What is the PDB entry?`C:\Users\caleb\source\repos\nightmare\x64\Release\nightmare.pdb`

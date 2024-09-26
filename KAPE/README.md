# KAPE

### Introduction to KAPE
- From amongst kape.exe and gkape.exe, which binary is used to run GUI version of KAPE? `gkape.exe`

### Target Options
- What is the file extension for KAPE Targets? `.tkape`
- What type of Target will we use if we want to collect multiple artifacts with a single command? `Compound Targets`

### Module Options
- What is the file extension of the Modules files? `.mkape`
- What is the name of the directory where binary files are stored, which may not be present on a typical system, but are required for a particular KAPE Module? `bin`

### KAPE GUI
- In the second to last screenshot above, what target have we selected for collection? `KapeTriage`
- In the second to last screenshot above, what module have we selected for processing? `!EZParser`
- What option has to be checked to append date and time information to triage folder name? `%d`
- What option needs to be checked to add machine information to the triage folder name? `%m`

### KAPE CLI
- Run the command kape.exe in an elevated shell. Take a look at the different switches and variables. What variable adds the collection timestamp to the target destination?<br />
Open cmd in privileged mode and run `kape.exe`:<br />
![image](https://github.com/user-attachments/assets/2f82843e-e8ff-4107-a2e2-db6bbe5c8da8)<br />
`%d`
- What variable adds the machine information to the target destination? `%m`
- Which switch can be used to show debug information during processing?<br />
![image](https://github.com/user-attachments/assets/957a1196-6415-4e3c-8b47-3320bfe1ed0d)<br />
`debug`
- Which switch is used to list all targets available?<br />
![image](https://github.com/user-attachments/assets/389ff0ac-2133-4b12-aa2c-8135e6a839fc)<br />
`tlist`
- Which flag, when used with batch mode, will delete the _kape.cli, targets and modules files after the execution is complete?<br />
![image](https://github.com/user-attachments/assets/7f2f3ccc-2043-4f93-b030-f26dcc990bae)<br />
`cu`

### Hands-on Challenge
Set the options in GKAPE as they are setup in task 5, then use EzViewer to open csv files:
- Two USB Mass Storage devices were attached to this Virtual Machine. One had a Serial Number  0123456789ABCDE. What is the Serial Number of the other USB Device? `1C6F654E59A3B0C179D366AE`
- 7zip, Google Chrome and Mozilla Firefox were installed from a Network drive location on the Virtual Machine. What was the drive letter and path of the directory from where these software were installed? `Z:\setups`
- What is the execution date and time of CHROMESETUP.EXE in MM/DD/YYYY HH:MM? `11/25/2021 3:33`
- What search query was run on the system? `RunWallpaperSetup.cmd`
- When was the network named Network 3 First connected to? `11/30/2021 15:44`
- KAPE was copied from a removable drive. Can you find out what was the drive letter of the drive where KAPE was copied from? `E:`

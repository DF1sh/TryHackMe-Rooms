# Windows PowerShell

### What Is PowerShell
- What do we call the advanced approach used to develop PowerShell? `object-oriented`

### PowerShell Basics
- How would you retrieve a list of commands that start with the verb Remove? [for the sake of this question, avoid the use of quotes (" or ') in your answer] `Get-Command -Name Remove`
- What cmdlet has its traditional counterpart echo as an alias?<br />
Run `get-alias`:<br />
![image](https://github.com/user-attachments/assets/1d40ce9e-2d9f-42d2-ae4b-51b3d1c4d9bd)<br />
`Write-Output`
- What is the command to retrieve some example usage for the cmdlet New-LocalUser? `Get-Help New-LocalUser -examples`

### Navigating the File System and Working with Files
- What cmdlet can you use instead of the traditional Windows command type? `Get-Content`
- What PowerShell command would you use to display the content of the "C:\Users" directory? [for the sake of this question, avoid the use of quotes (" or ') in your answer] ` Get-ChildItem -Path C:\Users`
- How many items are displayed by the command described in the previous question?<br />
![image](https://github.com/user-attachments/assets/e4bdabab-e5d3-4a4d-967d-1022d7de151f)<br />
`4`

### Piping, Filtering, and Sorting Data
- How would you retrieve the items in the current directory with size greater than 100? [for the sake of this question, avoid the use of quotes (" or ') in your answer] `Get-ChildItem | Where-Object -Property Length -gt 100`

### System and Network Information
- Other than your current user and the default "Administrator" account, what other user is enabled on the target machine?<br />
![image](https://github.com/user-attachments/assets/40930ac1-b1d4-407f-86a5-0e5b5d531b60)<br />
`p1r4t3`
- This lad has hidden his account among the others with no regard for our beloved captain! What is the motto he has so bluntly put as his account's description? `A merry life and a short one.`
- Now a small challenge to put it all together. This shady lad that we just found hidden among the local users has his own home folder in the "C:\Users" directory. 
Can you navigate the filesystem and find the hidden treasure inside this pirate's home?<br />
![image](https://github.com/user-attachments/assets/5678e2dd-dffc-4d9e-98f7-32a9795b939b)<br />
`THM{p34rlInAsh3ll}`

### Real-Time System Analysis
- In the previous task, you found a marvellous treasure carefully hidden in the target machine. What is the hash of the file that contains it?<br />
Run `Get-FileHash -Path .\big-treasure.txt` to get the answer: `71FC5EC11C2497A32F8F08E61399687D90ABE6E204D2964DF589543A613F3E08`
- What property retrieved by default by Get-NetTCPConnection contains information about the process that has started the connection?<br />
Run `Get-NetTCPConnection` and look at the columns names to get the answer: `OwningProcess`
- .... With this information and the PowerShell knowledge you have built so far, can you find the service name?<br />
Run `Get-Service | where-object -Property "DisplayName" -eq "A merry life and a short one."`:<br />
![image](https://github.com/user-attachments/assets/ae56b932-a8b1-4450-ba8a-44519604f946)<br />
`p1r4t3-s-compass`

### Scripting
- What is the syntax to execute the command Get-Service on a remote computer named "RoyalFortune"? Assume you don't need to provide credentials to establish the connection. [for the sake of this question, avoid the use of quotes (" or ') in your answer] `Invoke-Command -ComputerName RoyalFortune -ScriptBlock { Get-Service }`

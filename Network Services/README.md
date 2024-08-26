# Network Services

### Understanding SMB
- What does SMB stand for? `Server Message Block`
- What type of protocol is SMB? `response-request`
- What do clients connect to servers using? `TCP/IP`
- What systems does Samba run on? `Unix`

### Enumerating SMB
- Conduct an nmap scan of your choosing, How many ports are open?<br />
![image](https://github.com/user-attachments/assets/05a5cf22-5bef-42e8-9a8b-ef4cb7f20b8f) <br />
`3`
- What ports is SMB running on? `139/445`
- Let's get started with Enum4Linux, conduct a full basic enumeration. For starters, what is the workgroup name? <br />
Run `enum4linux IP_addr` to get the answer: `WORKGROUP`
- What comes up as the name of the machine? <br />
![image](https://github.com/user-attachments/assets/1d6ec2a9-902c-4e17-a046-810235682846)<br />
`POLOSMB`
- What operating system version is running? `6.1`
- What share sticks out as something we might want to investigate? `profiles`

### Exploiting SMB
- What would be the correct syntax to access an SMB share called "secret" as user "suit" on a machine with the IP 10.10.10.2 on the default port? `smbclient //10.10.10.2/secret -U suit -p 445`
- Lets see if our interesting share has been configured to allow anonymous access, I.E it doesn't require authentication to view the files. We can do this easily by:
  - using the username "Anonymous"
  - connecting to the share we found during the enumeration stage
  - and not supplying a password. <br />
Does the share allow anonymous access? Y/N? `Y`
- Great! Have a look around for any interesting documents that could contain valuable information. Who can we assume this profile folder belongs to? <br />
Login with anonymous access: `smbclient //IP_addr/profiles -U anonymous`. <br />
![image](https://github.com/user-attachments/assets/f4a96b68-56ff-41a5-800c-952991c06ca6)<br />
`John Cactus`
- What service has been configured to allow him to work from home? `ssh`
- Okay! Now we know this, what directory on the share should we look in? `.ssh`
- This directory contains authentication keys that allow a user to authenticate themselves on, and then access, a server. Which of these keys is most useful to us? `id_rsa`
- What is the smb.txt flag? <br />
Get the id_rsa file from the SMB share. Change permissions so that you can use it with ssh: `chown 600 id_rsa` and then connect to the "cactus" account on the target IP: `ssh cactus@10.10.243.185 -i id_rsa`<br />
![image](https://github.com/user-attachments/assets/7043279b-5c73-4a2f-b625-a4741bb0c203)<br />
`THM{smb_is_fun_eh?}`

### Understanding Telnet
- What is Telnet?
- What has slowly replaced Telnet?
- How would you connect to a Telnet server with the IP 10.10.10.3 on port 23?
- The lack of what, means that all Telnet communication is in plaintext?

### Enumerating Telnet
- How many ports are open on the target machine?
- What port is this?
- This port is unassigned, but still lists the protocol it's using, what protocol is this?
- Now re-run the nmap scan, without the -p- tag, how many ports show up as open?
- Based on the title returned to us, what do we think this port could be used for?
- Who could it belong to? Gathering possible usernames is an important step in enumeration.

### Exploiting Telnet
- Great! It's an open telnet connection! What welcome message do we receive?
- Let's try executing some commands, do we get a return on any input we enter into the telnet session? (Y/N)
- Now, use the command "ping [local THM ip] -c 1" through the telnet session to see if we're able to execute system commands. Do we receive any pings? Note, you need to preface this with .RUN (Y/N)
- What word does the generated payload start with?
- What would the command look like for the listening port we selected in our payload?
- Success! What is the contents of flag.txt?

### Understanding FTP
- What communications model does FTP use?
- What's the standard FTP port?
- How many modes of FTP connection are there?    

### Enumerating FTP
- How many ports are open on the target machine?
- What port is ftp running on?
- What variant of FTP is running on it?
- What is the name of the file in the anonymous FTP directory?
- What do we think a possible username could be?

### Exploiting FTP
- What is the password for the user "mike"?
- What is ftp.txt?



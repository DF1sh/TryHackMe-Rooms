# Network Services 2

### Understanding NFS
- What does NFS stand for? `Network File System`
- What process allows an NFS client to interact with a remote directory as though it was a physical device? `Mounting`
- What does NFS use to represent files and directories on the server? `file handle`
- What protocol does NFS use to communicate between the server and client? `RPC`
- What two pieces of user data does the NFS server take as parameters for controlling user permissions? Format: parameter 1 / parameter 2 `user id / group id`
- Can a Windows NFS server share files with a Linux client? (Y/N) `Y`
- Can a Linux NFS server share files with a MacOS client? (Y/N) `Y`
- What is the latest version of NFS? [released in 2016, but is still up to date as of 2020] This will require external research. `4.2`

### Enumerating NFS
- Conduct a thorough port scan scan of your choosing, how many ports are open? <br />
![image](https://github.com/user-attachments/assets/f5948d9c-57bc-4cf9-80b2-64a3c86fe6c4) <br />
7`
- Which port contains the service we're looking to enumerate? `2049`
- Now, use /usr/sbin/showmount -e [IP] to list the NFS shares, what is the name of the visible share? <br />
![image](https://github.com/user-attachments/assets/7ce70853-3efd-49d7-bce7-08f747d4866f) <br />
`/home`
- First, use "mkdir /tmp/mount" to create a directory on your machine to mount the share to. This is in the /tmp directory- so be aware that it will be removed on restart. Then, use the mount command we broke down earlier to mount the NFS share to your local machine. Change directory to where you mounted the share- what is the name of the folder inside? `cappucino`
- Interesting! Let's do a bit of research now, have a look through the folders. Which of these folders could contain keys that would give us remote access to the server?
![image](https://github.com/user-attachments/assets/1b83e4e6-a002-42f9-8af5-fbdc4a0736b1)<br />
`ssh`
- Which of these keys is most useful to us? `id_rsa`
- Can we log into the machine using ssh -i <key-file> <username>@<ip> ? (Y/N) `Y`

### Exploiting NFS
- Now, we're going to add the SUID bit permission to the bash executable we just copied to the share using "sudo chmod +[permission] bash". What letter do we use to set the SUID bit set using chmod? `s`
- Let's do a sanity check, let's check the permissions of the "bash" executable using "ls -la bash". What does the permission set look like? Make sure that it ends with -sr-x. `-rwsr-sr-x`
- Great! If all's gone well you should have a shell as root! What's the root flag? `THM{nfs_got_pwned}`

### Understanding SMTP
- What does SMTP stand for?
- What does SMTP handle the sending of? (answer in plural)
- What is the first step in the SMTP process?
- What is the default SMTP port?
- Where does the SMTP server send the email if the recipient's server is not available?
- On what server does the Email ultimately end up on?
- Can a Linux machine run an SMTP server? (Y/N)
- Can a Windows machine run an SMTP server? (Y/N)

### Enumerating SMTP
- First, lets run a port scan against the target machine, same as last time. What port is SMTP running on?
- Okay, now we know what port we should be targeting, let's start up Metasploit. What command do we use to do this?
- Let's search for the module "smtp_version", what's it's full module name?
- Great, now- select the module and list the options. How do we do this?
- Have a look through the options, does everything seem correct? What is the option we need to set?
- Set that to the correct value for your target machine. Then run the exploit. What's the system mail name?
- What Mail Transfer Agent (MTA) is running the SMTP server? This will require some external research.
- Good! We've now got a good amount of information on the target system to move onto the next stage. Let's search for the module "smtp_enum", what's it's full module name?
- What option do we need to set to the wordlist's path?
- Once we've set this option, what is the other essential paramater we need to set?
- Okay! Now that's finished, what username is returned?

### Exploiting SMTP
- What is the password of the user we found during our enumeration stage?
- Great! Now, let's SSH into the server as the user, what is contents of smtp.txt

### Understanding MySQL
- What type of software is MySQL?
- What language is MySQL based on?
- What communication model does MySQL use?
- What is a common application of MySQL?
- What major social network uses MySQL as their back-end database? This will require further research.


### Enumerating MySQL
- As always, let's start out with a port scan, so we know what port the service we're trying to attack is running on. What port is MySQL using?
- Search for, select and list the options it needs. What three options do we need to set? (in descending order).
- Run the exploit. By default it will test with the "select version()" command, what result does this give you?
- Great! We know that our exploit is landing as planned. Let's try to gain some more ambitious information. Change the "sql" option to "show databases". how many databases are returned?

### Exploiting MySQL
- First, let's search for and select the "mysql_schemadump" module. What's the module's full name?
- Great! Now, you've done this a few times by now so I'll let you take it from here. Set the relevant options, run the exploit. What's the name of the last table that gets dumped?
- Awesome, you have now dumped the tables, and column names of the whole database. But we can do one better... search for and select the "mysql_hashdump" module. What's the module's full name?
- Again, I'll let you take it from here. Set the relevant options, run the exploit. What non-default user stands out to you?
- Another user! And we have their password hash. This could be very interesting. Copy the hash string in full, like: bob:*HASH to a text file on your local machine called "hash.txt".
- Now, we need to crack the password! Let's try John the Ripper against it using: "john hash.txt" what is the password of the user we found?What is the user/hash combination string?
- Awesome. Password reuse is not only extremely dangerous, but extremely common. What are the chances that this user has reused their password for a different service? What's the contents of MySQL.txt?

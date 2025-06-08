# Linux System Hardening

### Physical Security
- What command can you use to create a password for the GRUB bootloader? `grub2-mkpasswd-pbkdf2`
- What does PBKDF2 stand for? `Password-Based Key Derivation Function 2`

### Filesystem Partitioning and Encryption
- What does LUKS stand for? `Linux Unified Key Setup`
- ... What is the flag in the secret vault? `THM{LUKS_not_LUX}`

### Firewall
- There is a firewall running on the Linux VM. It is allowing port 22 TCP as we can ssh into the machine. It is allowing another TCP port; what is it?
- What is the allowed UDP port?

### Remote Access
- What flag is hidden in the sshd_config file?

### Securing User Accounts
- One way to disable an account is to edit the passwd file and change the account’s shell. What is the suggested value to use for the shell?
- What is the name of the RedHat and Fedora systems sudoers group?
- What is the name of the sudoers group on Debian and Ubuntu systems?
- Other than tryhackme and ubuntu, what is the username that belongs to the sudoers group?

### Software and Services
- Besides FTPS, what is another secure replacement for TFTP and FTP?

### Update and Upgrade Policies
- What command would you use to update an older Red Hat system?
- What command would you use to update a modern Fedora system?
- What two commands are required to update a Debian system? (Connect the two commands with &&.)
- What does yum stand for?
- What does dnf stand for?
- What flag is hidden in the sources.list file?

### Audit and Log Configuration
- What command can you use to display the last 15 lines of kern.log?
- What command can you use to display the lines containing the word denied in the file secure?

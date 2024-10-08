# Linux Privilege Escalation 

### What is Privilege Escalation?
- Read the above: `No answer needed` <br /><br />

###  Enumeration
- What is the hostname of the target system?: `wade7363` <br />
- What is the Linux kernel version of the target system?: `3.13.0-24-generic` <br />
- What Linux is this?: `Ubuntu 14.04 LTS` <br />
- What version of the Python language is installed on the system? `2.7.6` <br />
- What vulnerability seem to affect the kernel of the target system? (Enter a CVE number) `CVE-2015-1328` <br />


### Automated Enumeration Tools
- Install and try a few automated enumeration tools on your local Linux distribution: `No answer needed` <br />

### Privilege Escalation: Kernel Exploits
- find and use the appropriate kernel exploit to gain root privileges on the target system.: `No answer needed` <br />
- What is the content of the flag1.txt file?: `THM-28392872729920` <br />

### Privilege Escalation: Sudo
- How many programs can the user "karen" run on the target system with sudo rights?: `3` <br />
- What is the content of the flag2.txt file?: `THM-402028394` <br />
- How would you use Nmap to spawn a root shell if your user had sudo rights on nmap?: `sudo nmap --interactive` <br />
- What is the hash of frank's password?: `$6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1` <br />

### Privilege Escalation: SUID
- Which user shares the name of a great comic book writer?: `gerryconway` <br />
- What is the password of user2?: `Password1` <br />
- What is the content of the flag3.txt file?: `THM-3847834` <br />

### Privilege Escalation: Capabilities
- Complete the task described above on the target system: `No answer needed` <br />
- How many binaries have set capabilities?: `6` <br />
- What other binary can be used through its capabilities?: `view` <br />
- What is the content of the flag4.txt file?: `THM-9349843` <br />

### Privilege Escalation: Cron Jobs
- How many user-defined cron jobs can you see on the target system?: `4` <br />
- What is the content of the flag5.txt file?: `THM-383000283` <br />
- What is Matt's password?: `123456` <br />

### Privilege Escalation: PATH
- What is the odd folder you have write access for?: `/home/murdoch` <br />
- Exploit the $PATH vulnerability to read the content of the flag6.txt file: `No answer needed` <br />
- What is the content of the flag6.txt file?: `THM-736628929` <br />


### Privilege Escalation: NFS
- How many mountable shares can you identify on the target system?: `3` <br />
- How many shares have the "no_root_squash" option enabled?: `3` <br />
- Gain a root shell on the target system: `No answer needed` <br />
- What is the content of the flag7.txt file?: `THM-89384012` <br />

# RootMe

### Reconnaissance
- Scan the machine, how many ports are open? `2` <br />
- What version of Apache is running? `2.4.29` <br />
- What service is running on port 22? `ssh` <br />
- Find directories on the web server using the GoBuster tool. `No answer needed` <br />
- What is the hidden directory? `/panel/` <br />

### Getting a shell
- user.txt `THM{y0u_g0t_a_sh3ll}` <br />

### Privilege escalation
- Search for files with SUID permission, which file is weird? `/usr/bin/python` <br />
- Find a form to escalate your privileges. `No answer needed` <br />
- root.txt `THM{pr1v1l3g3_3sc4l4t10n}` <br />

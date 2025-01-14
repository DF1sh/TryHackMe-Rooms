# Mustacchio

### Mustacchio
Nmap scan shows ports 22,80 and 8765 open. First is ssh. last two are webserver (apache and nginx). Port 8765 contains an admin panel. Furthemore, enumerating the webserver on port 80 shows a `/custom` directory, that contains a file called `users.bak`. I downloaded it and it seems to be a backup sql file: <br />
![image](https://github.com/user-attachments/assets/5313203a-d719-4202-a64f-069249d7a9ca)<br />
The username is `admin`, the password can be easily cracked using crackstation. Once inside the admin panel on port 8765, there's a comment inside the source code: <br />
![image](https://github.com/user-attachments/assets/60a81adf-7118-46be-acda-d82d5c78c471)<br />
I have a username, `barry`. The admin panel allows me to add comments in the website. If I submit an empty request: <br />
![image](https://github.com/user-attachments/assets/8c745c63-40f7-4c14-95e8-67c4c4a54fd4)<br />

There's also another interesting comment: <br />
![image](https://github.com/user-attachments/assets/8f7d50b9-2dc0-47b6-8863-d0e69339e091)<br />
Also, If I click `submit` without any input, I get:<br />
![image](https://github.com/user-attachments/assets/79be0710-5363-4481-a796-b3cd7e9da20a)<br />
It contains the following message: <br />
![image](https://github.com/user-attachments/assets/b05b85c7-d003-42cc-9fc3-675682ecd65f)<br />
This tells me what format the xml input should have. This an XXE vulnerability. If I use this payload: <br />

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
    <comment>
        <name>Example Name</name>
        <author>John Doe</author>
        <com>&ent;</com>
    </comment>
I get the following:<br />
![image](https://github.com/user-attachments/assets/0e9708e2-6e3d-449a-b3dd-205b841825c7)<br />
An XXE attack occurs when XML input containing a reference to an external entity is processed by a poorly configured XML parser. The following payload:

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///home/barry/.ssh/id_rsa"> ]>
    <comment>
        <name>Example Name</name>
        <author>John Doe</author>
        <com>&ent;</com>
    </comment>

gets me barry's ssh private key. But it's protected by a passphrase. To crack it, run `ssh2john id_rsa_barry > hash.txt`, then `john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt`.<br />
Now for privesc: there's a SUID file `/home/joe/live_log` in which I have root privileges, and it executes the command "tail -f /var/log/nginx/access.log". If I make a request to the webserver using "test" as user-agent, I get the following feedback: <br />
![image](https://github.com/user-attachments/assets/fbbf22ed-cc0c-4fed-b991-0c4a3f74dd9c)<br />
The problem with this command is that it's executing `tail`, not `/usr/bin/tail` or whatever. The path is relative. This means that I can change the environment variables to execute my own `tail` command. Create a malicious `tail` file inside barry's home directory:

    #!/bin/bash
    /bin/bash
Now run `chmod +x tail` and run `export PATH=/home/barry:$PATH`. Now just run the SUID binary and you should have a root shell. 





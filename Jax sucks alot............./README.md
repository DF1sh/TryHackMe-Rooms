# Jax sucks alot.............

### Jax sucks alot.............
Nmap shows ports 22 and 80 open. Port 80 is just one page, I enumerated with nikto, ffuf etc.. and there's only this page I need to exploit: <br />
![image](https://github.com/user-attachments/assets/48558b18-0e5a-485a-ae59-4e5f5a746ffb)<br />
If I capture a response and a request with burpsuite, I can see that the response contains a `set-cookie` header: <br />
![image](https://github.com/user-attachments/assets/328eb1dd-6ae1-4612-b951-f5f90b56e6e8)<br />
If I base64 decode the string, I get: `{"email":"test?email=test"}`. <br />
After testing a bit, this is a nodejs json deserialization vulnerability. To test if it works,
I'm going to send the following payload `eyJlbWFpbCI6Il8kJE5EX0ZVTkMkJF9mdW5jdGlvbigpeyByZXR1cm4gJ0RFU0VSSUFMSVpFJzsgfSgpIn0=` as cookie value. This is the base64 encoded string of `{"email":"_$$ND_FUNC$$_function(){ return 'DESERIALIZE'; }()"}`:<br />
![image](https://github.com/user-attachments/assets/0e7010a3-d667-4755-9210-1136bf921400)<br />
This confirms that the code gets executed. To spawn a reverse shell, I'm going to create a `shell.sh` file locally, and then open a python webserver, then use `curl` as payload command. 

# JPGChat

### JPGChat
Nmap scan shows ports 22 and 3000 open. <br />
![image](https://github.com/user-attachments/assets/8f8f9f2b-a87f-45d1-8927-a5792ff899b5)<br />
I found the github page [here](https://github.com/Mozzie-jpg/JPChat/blob/main/jpchat.py). The code of this chat is the following: <br />

    #!/usr/bin/env python3
    
    import os
    
    print ('Welcome to JPChat')
    print ('the source code of this service can be found at our admin\'s github')
    
    def report_form():
    
    	print ('this report will be read by Mozzie-jpg')
    	your_name = input('your name:\n')
    	report_text = input('your report:\n')
    	os.system("bash -c 'echo %s > /opt/jpchat/logs/report.txt'" % your_name)
    	os.system("bash -c 'echo %s >> /opt/jpchat/logs/report.txt'" % report_text)
    
    def chatting_service():
    
    	print ('MESSAGE USAGE: use [MESSAGE] to message the (currently) only channel')
    	print ('REPORT USAGE: use [REPORT] to report someone to the admins (with proof)')
    	message = input('')
    
    	if message == '[REPORT]':
    		report_form()
    	if message == '[MESSAGE]':
    		print ('There are currently 0 other users logged in')
    		while True:
    			message2 = input('[MESSAGE]: ')
    			if message2 == '[REPORT]':
    				report_form()
    
    chatting_service()
We can see that the service takes user input and uses it inside the function `os.system()` This is a simple command injection vulnerability. The payload is `;` + any bash command you want, in my case I use `busybox` to get a reverse shell.<br />
![image](https://github.com/user-attachments/assets/3805a929-ccfd-4b17-ab05-589f46acbe97)<br />
This got me the user flag as the user `wes`. Now for privesc, if I run `sudo -l`:<br />
![image](https://github.com/user-attachments/assets/2729d2b3-815d-44fb-8747-96e6c0b9a91b)<br />
Ok so you can see that the PYTHONPATH variable will be preserved when executing this command, and that I have the SETENV privilege. Just like system binaries, also python libraries are stored somewhere in the system, and there's a PYTHONPATH variable that can be used to tell the system where to go look for the libraries, much like the PATH variable for system binaries. <br />
The SETENV privilege allows me to set the PYTHONPATH variable to what ever I want. <br />
![image](https://github.com/user-attachments/assets/aacc5c45-83e7-4332-91ff-5f8c5ea4355c)<br />
The script imports the `compare` library. Furthermore, every library can have an additional file called `__init__.py`. This is python code that gets executed every time the library is loaded. You see where this is going. <br />
I create a file inside `/home/wes/compare/` and I call it `__init__.py`. I put the following code in it: <br />
![image](https://github.com/user-attachments/assets/0c35907e-2201-4414-afd5-f46ce0da56d1)<br />
Next, I change the PYTHONPATH environment: `export PYTHONPATH=/home/wes/:$PYTHONPATH`. Now I listen on port 22 and execute `sudo /usr/bin/python3 /opt/development/test_module.py` to get a reverse root shell!<br />
![image](https://github.com/user-attachments/assets/d5418a36-5ce8-46b6-8d2a-5e581ae1caf4)<br />



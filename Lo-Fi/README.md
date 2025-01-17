# Lo-Fi

### Lo-Fi
Nmap scan shows ports 22 and 80 open. Enumerating the application for a bit, I found that it's vulnerable to path traversal: <br />
![image](https://github.com/user-attachments/assets/1b3befe9-fae1-499a-bdef-cf70f3db49a6)<br />
To get the flag, I just visit `http://10.10.147.234/?page=..//..//..//..//flag.txt`. 

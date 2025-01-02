# Lian_Yu

### Find the Flags
Nmap scan shows ports 21,22,80,111 and 46439 open. 

    PORT      STATE SERVICE VERSION
    21/tcp    open  ftp     vsftpd 3.0.2
    22/tcp    open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
    | ssh-hostkey: 
    |   1024 56:50:bd:11:ef:d4:ac:56:32:c3:ee:73:3e:de:87:f4 (DSA)
    |   2048 39:6f:3a:9c:b6:2d:ad:0c:d8:6d:be:77:13:07:25:d6 (RSA)
    |   256 a6:69:96:d7:6d:61:27:96:7e:bb:9f:83:60:1b:52:12 (ECDSA)
    |_  256 3f:43:76:75:a8:5a:a6:cd:33:b0:66:42:04:91:fe:a0 (ED25519)
    80/tcp    open  http    Apache httpd
    |_http-title: Purgatory
    |_http-server-header: Apache
    111/tcp   open  rpcbind 2-4 (RPC #100000)
    | rpcinfo: 
    |   program version    port/proto  service
    |   100000  2,3,4        111/tcp   rpcbind
    |   100000  2,3,4        111/udp   rpcbind
    |   100000  3,4          111/tcp6  rpcbind
    |   100000  3,4          111/udp6  rpcbind
    |   100024  1          32857/udp6  status
    |   100024  1          39951/tcp6  status
    |   100024  1          44276/udp   status
    |_  100024  1          46439/tcp   status
    46439/tcp open  status  1 (RPC #100024)

Directory enumeration on the webserver finds `/island` with the following content: <br />
![image](https://github.com/user-attachments/assets/4df4e7b5-773b-4e6b-82e8-4a5cbeb5644a)<br />
The code word is `vigilante`. <br />
At this point I am stuck for a bit. I decide to look at the hint and apparenlty there's a web directory composed by 4 digits. I have no idea which wordlist contains such a name, so I created one with `seq 0 9999 > numbers.txt` and then run `gobuster dir -u "http://10.10.13.240/island" -w numbers.txt`. <br />
This actually finds directory `/island/2100`. I'm glad I looked at the hint. This page contains another hint: <br />
![image](https://github.com/user-attachments/assets/e4ce76fc-25d1-4cc8-a015-6a14b312c998)<br />
I need to find a file with extension .ticket. I run `gobuster dir -u "http://10.10.13.240/island/2100" -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -x ticket` and find `/green_arrow.ticket`:<br />
![image](https://github.com/user-attachments/assets/5801b3fe-8b43-4654-bf85-02fd9935f75b)<br />
At first I thought this was the FTP password, but it didnt work. So I started trial and error decoding it with [cyberchef](https://gchq.github.io/CyberChef/), and found the right password after decoding it base58:<br />
![image](https://github.com/user-attachments/assets/05a6d454-3511-407a-b5c8-6f74e42ded2e)<br />
The FTP server contains an image called `aa.jpg`. I was able to extract files from it with `stegseek`:<br />
![image](https://github.com/user-attachments/assets/d06fbe86-05cd-4533-a39e-1bce13d3ff02)<br />
This image contains a .zip file. When extracted, there are two files: <br />
![image](https://github.com/user-attachments/assets/cb4bc9df-44d2-45fb-8b6a-0496201f83aa)<br />
Furthermore, when navigating on the FTP server, I saw that there are two users on this box: <br />
![image](https://github.com/user-attachments/assets/87290cb6-90ca-45c4-ad6e-fcffc86042f0)<br />
So I was able to use that password to log into slade's ssh account. <br />
For privesc, if I run `sudo -l` I get: <br />
![image](https://github.com/user-attachments/assets/17f66974-90d7-4c32-a413-4beab653fae2)<br />
The exploit for this can be found on  [gtfobins](https://gtfobins.github.io/gtfobins/pkexec/#sudo). Just type `sudo pkexec /bin/sh`.



# Jack-of-All-Trades

### Flags
Nmap scan shows ports 22 and 80 open. 
    
    PORT   STATE SERVICE VERSION
    22/tcp open  http    Apache httpd 2.4.10 ((Debian))
    |_http-server-header: Apache/2.4.10 (Debian)
    |_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
    |_http-title: Jack-of-all-trades!
    80/tcp open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)
    | ssh-hostkey: 
    |   1024 13:b7:f0:a1:14:e2:d3:25:40:ff:4b:94:60:c5:00:3d (DSA)
    |   2048 91:0c:d6:43:d9:40:c3:88:b1:be:35:0b:bc:b9:90:88 (RSA)
    |   256 a3:fb:09:fb:50:80:71:8f:93:1f:8d:43:97:1e:dc:ab (ECDSA)
    |_  256 65:21:e7:4e:7c:5a:e7:bc:c6:ff:68:ca:f1:cb:75:e3 (ED25519)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

The ports are swapped. Port 22 is a website and port 80 is ssh. To access the website on port 22 from firefox, type on the search bar `about:config` and set this option: <br />
![image](https://github.com/user-attachments/assets/48660d89-583d-412b-9d15-1ac743f5bbda)<br />
The source code of the website shows a hint: <br />
![image](https://github.com/user-attachments/assets/001fa36d-9192-45af-901f-a822cef38f8b)<br />
The decoded string is `Remember to wish Johny Graves well with his crypto jobhunting! His encoding systems are amazing! Also gotta remember your password: u?WtKSraq`<br />
Next, Inside `/recovery.php`:<br />
![image](https://github.com/user-attachments/assets/14ee9fb7-ad58-4b52-86d5-94e4f1780408)<br />
there's another comment that's encoded first in hexadecimal and then in base32: <br />
![image](https://github.com/user-attachments/assets/6825aa84-3a7e-4a65-9292-f98ccabd4fb9)<br />
That string encoded in base64 also neeeded to be rotated to be able to read it: <br />
![image](https://github.com/user-attachments/assets/d705cfa5-9fc3-4100-aa91-2bff734eec4b)<br />
This is a bitly "compressed" URL. I use an online tool to "expand" it: <br />
![image](https://github.com/user-attachments/assets/5726cf94-813f-4b6e-b1e0-a4dd9f92e709)<br />
At this point I was stuck for a bit. But then I decided to download the images from the webpage and try to see if jack left any data inside these images. I startd with `stego.jpg`:<br />
![image](https://github.com/user-attachments/assets/3d2d8dd9-a123-45d5-8a9c-d26576be50b5)<br />
The passphrase I used is the one I found earlier: `u?WtKSraq`.
Inside `header.jpg` there are the credentials. I use them to access `/recovery.php`:<br />
![image](https://github.com/user-attachments/assets/f48ffeb7-9539-462c-a693-37d11120d21f)<br />
So just add `?cmd=whoami`, and that's it. I have remote code execution, so I spawn a reverse shell. Inside the `/home` there's jack home directory, but I can't access it. But I found a file with passwords:<br />
![image](https://github.com/user-attachments/assets/813ab68e-caf7-4ad9-9e28-31fbb09b501f)<br />
I use this wordlist to bruteforce jack's ssh account with: `hydra -l jack -P passwordlist 10.10.107.175 ssh -s 80`, and it works and got the first flag.
Now with jack if I run `find / -perm -4000 2>/dev/null` to find SUID binaries, I get this: <br />
![image](https://github.com/user-attachments/assets/96bfd514-293b-46e7-a70a-fef2dafb4d31)<br />
SUID bit on `strings` means that I can read whatever I want. So I run `strings /root/root.txt` and get the second flag.







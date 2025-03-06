# CTF collection Vol.1

### What does the base said?
VEhNe2p1NTdfZDNjMGQzXzdoM19iNDUzfQ==<br />
I used [cyberchef](https://cyberchef.org/) to base64 decode it.

### Meta meta
Meta! meta! meta! meta...................................<br />
I First download the image with `wget` and then find the flag with `exiftool`:<br />
![image](https://github.com/user-attachments/assets/3f989e17-ba12-4595-926a-73a1838fef7c)<br />

### Mon, are we going to be okay?
Something is hiding. That's all you need to know.<br />
I use `steghide` to extract stenografic data from the image:<br />
![image](https://github.com/user-attachments/assets/15614384-f9fd-4cb9-b117-64452c1105e7)<br />
The message contains the flag.

### Erm......Magick
![image](https://github.com/user-attachments/assets/f7dbd828-9158-420a-8ca0-6c3442c7affe)<br />

### QRrrrr
Such technology is quite reliable.<br />
![image](https://github.com/user-attachments/assets/f0ff4520-c3a7-4823-8e7c-26a66b25f8e9)<br />

### Reverse it or read it?
Both works, it's all up to you.<br />
![image](https://github.com/user-attachments/assets/3bfd43c3-7ecb-42ba-ace1-3d78212db570)<br />

### Another decoding stuff
3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L<br />
The string is base58 encoded:<br />
![image](https://github.com/user-attachments/assets/894131ef-23f9-4828-ad70-5bf0c0ed5067)<br />

### Left or right 
Left, right, left, right... Rot 13 is too mainstream. Solve this: MAF{atbe_max_vtxltk}<br />
This time I used ROT13 Bruteforce recipe:<br />
![image](https://github.com/user-attachments/assets/ba3071d1-83d8-406c-82c7-3e199b8c8484)<br />

### Make a comment
No downloadable file, no ciphered or encoded text. Huh .......<br />
The flag can be found in the source HTML code of this task:<br />
![image](https://github.com/user-attachments/assets/782e17d4-8c06-41cc-85ca-f9fcea72903e)<br />

### Can you fix it?
I accidentally messed up with this PNG file. Can you help me fix it? Thanks, ^^<br />
I have to fix the signature of the png file. In [this wikipedia page](https://en.wikipedia.org/wiki/List_of_file_signatures) there's a list of signature of each estension:<br />
![image](https://github.com/user-attachments/assets/c283ed6b-e1d0-4cc6-b161-69be2631057d)<br />
Now the image is fixed and there's the flag on it.

### Read it
Some hidden flag inside Tryhackme social account.<br />
Had to look at an external writeup for this cuz I couldn't find the right webpage. Sorry :'(

### Spin my head
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++++++++++++.------------.+++++.>+++++++++++++++++++++++.<<++++++++++++++++++.>>-------------------.---------.++++++++++++++.++++++++++++.<++++++++++++++++++.+++++++++.<+++.+.>----.>++++.<br />
This is [brainfuck](https://www.dcode.fr/brainfuck-language) language:<br />
![image](https://github.com/user-attachments/assets/4d8a92a1-e88c-490c-b32f-fdec06bbd47e)<br />

### An exclusive!
S1: 44585d6b2368737c65252166234f20626d<br />
S2: 1010101010101010101010101010101010<br />
First of all I used [this website](https://xor.pw/#) to calculate the XOR:<br />
![image](https://github.com/user-attachments/assets/c1a21ea3-693d-4b6e-b199-8453bf735738)<br />
Then I decoded it from Hex to text:<br />
![image](https://github.com/user-attachments/assets/da853345-1d32-462f-9165-f28eba27f485)<br />

### Binary walk
Please exfiltrate my file :)<br />
![image](https://github.com/user-attachments/assets/f8b1a835-1687-424e-88e8-58d14738c15d)<br />
Run `binwalk -e hell_1578018688127.jpg` to extract the data from this image and retrieve the flag.

### Darkness
There is something lurking in the dark. <br />
Open file in Stegsolve.jar and browse the plugins. With “Blue plane 1”, the flag is decoded.

### A sounding QR
How good is your listening skill? P/S: The flag formatted as THM{Listened Flag}, the flag should be in All CAPS<br />
Use [this website](https://soundcloud.com/user-86667759/thm-ctf-vol1) to hear the qrcode and get the flag!

### Dig up the past
Sometimes we need a 'machine' to dig the past <br />
Targetted website: https://www.embeddedhacker.com/ <br />
Targetted time: 2 January 2020 <br />
Use the [wayback machine](https://web.archive.org/web/20200102131252/https://www.embeddedhacker.com).

### Uncrackable!
Can you solve the following? By the way, I lost the key. Sorry >.< MYKAHODTQ{RVG_YVGGK_FAL_WXF}<br />
I use [this website](https://www.guballa.de/vigenere-solver) to break this vigenere code and get the flag.

### Small bases
Decode the following text. 581695969015253365094191591547859387620042736036246486373595515576333693<br />
Dec -> hex -> ascii.

### Read the packet

      GET /flag.txt HTTP/1.1
      Host: 192.168.247.140
      User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
      Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
      Accept-Language: en-US,en;q=0.5
      Accept-Encoding: gzip, deflate
      Connection: keep-alive
      Upgrade-Insecure-Requests: 1
      If-Modified-Since: Fri, 03 Jan 2020 04:36:45 GMT
      If-None-Match: "e1bb7-15-59b34db67925a"
      Cache-Control: max-age=0
      
      HTTP/1.1 200 OK
      Date: Fri, 03 Jan 2020 04:43:14 GMT
      Server: Apache/2.2.22 (Ubuntu)
      Last-Modified: Fri, 03 Jan 2020 04:42:12 GMT
      ETag: "e1bb7-20-59b34eee33e0c"
      Accept-Ranges: bytes
      Vary: Accept-Encoding
      Content-Encoding: gzip
      Content-Length: 52
      Keep-Alive: timeout=5, max=100
      Connection: Keep-Alive
      Content-Type: text/plain
      
      THM{***********}
      
      Found me!



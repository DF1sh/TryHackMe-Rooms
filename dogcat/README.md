# dogcat

### dogcat
Nmap scan shows ports 22 and 80 open. `Gobuster` reveals the presence of a file called `flag.php`:<br />
![image](https://github.com/user-attachments/assets/f3527561-1727-47fb-bd14-3f8fc129f08e)<br />
After some testing, the following payload works to retrieve the code of `dog.php`: `http://10.10.181.198/?view=php://filter/read=convert.base64-encode/resource=dog`:<br />
![image](https://github.com/user-attachments/assets/905918ae-dd45-4f71-846f-67bfa1a742a8)<br />

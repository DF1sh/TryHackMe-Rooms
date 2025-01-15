# Archangel

### Archangel
Nmap scan shows ports 22 and 80 open. The room suggests to find a hidden hostname. I don't know what the domain is but the header of the page suggests that it might be `mafialive.thm`:<br />
![image](https://github.com/user-attachments/assets/fbb156ab-eecb-47da-85d6-882e749db36e)<br />
So I add the following line to the /etc/hosts file: `10.10.142.179 mafialive.thm`. This domain contains the first flag. 
After some enumeration, the following URL: `http://mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/test.php` worked for me to read the contents of the `test.php` file.<br />
With `http://mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/..//..//..//..//var/log/apache2/access.log` I have access to the apache logging file. <br > 
I now perform log poisoning: <br />
![image](https://github.com/user-attachments/assets/81f6d6b3-65e9-4fcb-ba1d-33735e7b53e2)<br />



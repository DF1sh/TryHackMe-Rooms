# Archangel

### Archangel
Nmap scan shows ports 22 and 80 open. The room suggests to find a hidden hostname. I don't know what the domain is but the header of the page suggests that it might be `mafialive.thm`:<br />
![image](https://github.com/user-attachments/assets/fbb156ab-eecb-47da-85d6-882e749db36e)<br />
So I add the following line to the /etc/hosts file: `10.10.142.179 mafialive.thm`. This domain contains the first flag. 
After some enumeration, the following URL: `http://mafialive.thm/test.php?view=/var/www/html/development_testing/..//..//..//..//../etc/passwd` worked for me to read the contents of the `/etc/passwd` file.<br /> 
I now perform log poisoning. First, I intercept a request with burp and substitute the user-agent with this code `<?php phpinfo(); ?>`. If I reload the page: <br />
![image](https://github.com/user-attachments/assets/ba61ea3c-0e32-45e5-8142-9a842567b2e2)<br />
My code gets executed. I have RCE. Now I'll do the same but put `<?php system($_GET[‘cmd’]); ?>` instead.





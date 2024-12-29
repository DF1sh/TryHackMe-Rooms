# Anonforce

### Anonforce Machine
Nmap shows port 21 and 22 open. <br />
FTP server allows anonymous login, and seems to be configured to serve the entire victim file system. It's enough to connect to ftp to get into "meliodas"' home directory to get the user flag. <br />
Inside the filesystem there's a directory called `notread` which is unusual in a normal filesystem: <br />
![image](https://github.com/user-attachments/assets/907ca207-aeab-464d-a32d-b4276f64985c)<br />
It contains two files: `backup.pgp` and `private.asc`. I believe I need to use the second file, which is a private key, to decrypt `backup.pgp`. <br />
To do that I need to run `gpg --import private.asc` to import the private key, and then `gpg --decrypt backup.pgp > outputfile.decrypted` to read the encrypted file. However when I try to import the private key, I get asked to prompt a password. 
This means that it's protected by a passphrase. So I try to crack it using john. To use John, first run `gpg2john private.asc > hashfile`, and then `john hashfile --wordlist=/usr/share/wordlists/rockyou.txt`. <br />
John successfully cracks the passphrase. The decrypted file contains what seems to be the content of `/etc/shadow`:<br />
![image](https://github.com/user-attachments/assets/88abf4ff-170d-48c7-ab18-f6dc1097664a)<br />
I now try to crack these passwords with john. First, put these two lines in the same file (I called it `hashes`), like so: 

    root:$6$07nYFaYf$F4VMaegmz7dKjsTukBLh6cP01iMmL7CiQDt1ycIm6a.bsOIBp0DwXVb9XI2EtULXJzBtaMZMNd2tV4uob5RVM0:18120:0:99999:7:::
    melodias:$1$xDhc6S6G$IQHUW5ZtMkBQ5pUMjEQtL1:18120:0:99999:7:::
Next, run `john hashes --wordlist=/usr/share/wordlists/rockyou.txt`. This gets me the root password. To get the root flag, just log into root's ssh.

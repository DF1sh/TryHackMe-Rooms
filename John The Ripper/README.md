# John The Ripper

### Setting up John the Ripper 
- What is the most popular extended version of John the Ripper? `Jumbo John`

### Wordlists
- What website was the rockyou.txt wordlist created from a breach on? `rockyou.com`

### Cracking Basic Hashes
- What type of hash is hash1.txt? <br />
Download the `Hash-id` tool that will help us identify the hash algorithm used for the hash, with the following command: `wget https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py`.
Running the tool on the hash, it outputs MD5 as possible hash algorithm: <br />
![image](https://github.com/user-attachments/assets/b534481d-986b-49b6-b45c-21249f3851e6) <br />
`md5`
- What is the cracked value of hash1.txt? <br />
Let's try to ckack it running john: `john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt first_task_hashes/hash1.txt` <br />
![image](https://github.com/user-attachments/assets/f7b27611-d7a7-404c-84f3-954ed7d7b837) <br />
`biscuit`
- What type of hash is hash2.txt? <br />
Again run `hash-id.py` to get the answer: `SHA1`
- What is the cracked value of hash2.txt <br />
And again, run john to crack it, changin the format to `raw-sha1`: the cracked password is `kangeroo`
- What type of hash is hash3.txt? `sha256`
- What is the cracked value of hash3.txt <br />
![image](https://github.com/user-attachments/assets/5141014b-54ac-4d9d-8ba0-4d23327faca3) <br />
`microphone`
- What type of hash is hash4.txt? `whirlpool`
- What is the cracked value of hash4.txt <br />
![image](https://github.com/user-attachments/assets/75d6f53c-66cf-42ba-88e3-bb1b4e167bd9) <br />
`colossal`

### Cracking Windows Authentication Hashes
- What do we need to set the "format" flag to, in order to crack this? `nt`
- What is the cracked value of this password? <br />
Run the following command: `john --format=nt --wordlist=/usr/share/wordlists/rockyou.txt ntlm_1605054722641.txt` to crack the hash: `mushroom`

### Cracking /etc/shadow Hashes
- What is the root password? <br />
In order to crack /etc/shadow passwords, you must combine it with the /etc/passwd file in order for John to understand the data it's being given. To do this, we use a tool built into the John suite of tools called unshadow. The command is: `unshadow [path to passwd] [path to shadow]` <br />
Now crack it with the command: `john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt etc_hashes_1605054759028.txt ` <br />
![image](https://github.com/user-attachments/assets/50858c2c-b4f2-431b-b135-e55dd0c79389)<br />
`1234`

### Single Crack Mode
- What is Joker's password? <br />
We want to use single crack mode for the user "Joker". So the first thing to do is to append "Joker" to the hash we want to crack, so that john can create a wordlist based on that. The hash file will look like this: `Joker:7bf6d9bb82bed1302f331fc6b816aada`. <br />
`hash-id.py` suggets me that this is a possible MD5 hash. Now run `john --single --format=raw-md5 hash7_1605054793656.txt`: <br />
![image](https://github.com/user-attachments/assets/3e3309d2-0787-4339-ad35-572dcd17cc9f) <br />
`Jok3r`

### Custom Rules

### Cracking Password Protected Zip Files

### Cracking Password Protected RAR Archives

### Cracking SSH Keys with John 

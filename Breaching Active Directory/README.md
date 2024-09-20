# Breaching Active Directory

### OSINT and Phishing
- What popular website can be used to verify if your email address or password has ever been exposed in a publicly disclosed data breach? `HaveIBeenPwned`

### NTLM Authenticated Services
- What is the name of the challenge-response authentication mechanism that uses NTLM? `NetNtlm`
- What is the username of the third valid credential pair found by the password spraying script? <br />
If we try to access `http://ntlmauth.za.tryhackme.com/`, the web server asks for authorization: <br />
![image](https://github.com/user-attachments/assets/2b9b40d1-45b6-494f-b78f-cb9052909455)<br />
From the task we know that the default password is "Changeme123", and we have been provided with a list of users from the network. We can now use hydra to try and brute force the NTLM authentication with the following command:

      hydra -L usernames.txt -p Changeme123 ntlmauth.za.tryhackme.com http-get '/:A=NTLM:F=401'

In the above command, `http-get` indicates that hydra will use the GET method to execute the attack, `'/:A=NTLM:F=401` indicates that hydra will use the NTLM authentication (A=NTLM), will consider response code = 401 as a failure(F=401), and will attack the root domain (/:). <br />
![image](https://github.com/user-attachments/assets/1933834e-9de4-48b5-89af-5093dffc30d1)<br />
The correct answer is `gordon.stevens` (I didnt want to use the given script from the task)

- How many valid credentials pairs were found by the password spraying script? `4`
- What is the message displayed by the web application when authenticating with a valid credential pair?<br />
I logged in as Gordon, gordon.stevens:Changeme123 <br />
![image](https://github.com/user-attachments/assets/6912b2cd-6c23-4052-8d3b-580b9af43599)<br />
`Hello World`

### LDAP Bind Credentials
- What type of attack can be performed against LDAP Authentication systems not commonly found against Windows Authentication systems? `LDAP Pass-back Attack`
- What two authentication mechanisms do we allow on our rogue LDAP server to downgrade the authentication and make it clear text?<br />
![image](https://github.com/user-attachments/assets/c43e82ec-9ea7-4fb4-9cc2-5ed8cd75da68)<br />
`LOGIN,PLAIN`
- What is the password associated with the svcLDAP account? <br />
Follow the steps provided in the task to set up a rogue LDAP server, then sniff the packets on the breachad interface: `sudo tcpdump -SX -i breachad tcp port 389`<br />
Then change the settings on the printer web interface to point to your rogue ldap server, which is your IP: <br />
![image](https://github.com/user-attachments/assets/b614bcca-1141-4a1f-a170-25a6daa8be5f)<br />
Now click on "test settings", so that the printer will send us the credentials: <br />
![image](https://github.com/user-attachments/assets/508e0ade-8d1f-4187-a9e5-0cf528f18d00)<br />
The password is `tryhackmeldappass1@`.

### Authentication Relays
- What is the name of the tool we can use to poison and capture authentication requests on the network?
- What is the username associated with the challenge that was captured?
- What is the value of the cracked password associated with the challenge that was captured?

### Microsoft Deployment Toolkit
- What Microsoft tool is used to create and host PXE Boot images in organisations?
- What network protocol is used for recovery of files from the MDT server?
- What is the username associated with the account that was stored in the PXE Boot image?
- What is the password associated with the account that was stored in the PXE Boot image?

### Configuration Files
- What type of files often contain stored credentials on hosts?
- What is the name of the McAfee database that stores configuration including credentials used to connect to the orchestrator?
- What table in this database stores the credentials of the orchestrator?
- What is the username of the AD account associated with the McAfee service?
- What is the password of the AD account associated with the McAfee service?


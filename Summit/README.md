# Summit

### Challenge

- What is the first flag you receive after successfully detecting sample1.exe? <br /><br />
    Go to the 'Malware Sandbox' section and analyze `sample1.exe`. The analysis will provide us with the hashes of the malware, specifically the MD5, SHA1 and SHA256 hashes.
    Move to the 'Manage Hashes' section and simply submit one of the provided hashes to the EDR(Endpoint Detection and Response) system, and get the flag: `THM{f3cbf08151a11a6a331db9c6cf5f4fe4}`<br /><br />
- What is the first flag you receive after successfully detecting sample2.exe? <br /><br />
    The analysis of `sample2.exe` will provide us with information about network activity. Specifically, the PID related to the malware attempts an HTTP request to http://154.35.10.113:4444/uvLk8YI32. 
    The IP address 154.35.10.113 might be the C2 server used by the attacker. Therefore, move to the 'Firewall Manager' section and add a new firewall rule with the following keys:
  
        Type: Egress	
        Source: Any
        Destination: 154.35.10.113
        Action: Deny
  This will get us the flag: `THM{2ff48a3421a938b388418be273f4806d}` <br /><br />
- What is the first flag you receive after successfully detecting sample3.exe? <br /><br />
    The analysis of `sample3.exe` now detects connections the domain name `emudyn.bresonicz.info`. Blocking the previous IP address was not enough, since the attacker might be in possess of multiple servers.
    Therefore, we need to filter out the domain itself. Go to 'DNS Filter' and add the following rule:

        Rule name: Suspicious domain
        Category: Malware
        Domain Name: emudyn.bresonicz.info
        Action: Deny
    This will get us the flag: `THM{4eca9e2f61a19ecd5df34c788e7dce16}`<br /><br />
- What is the first flag you receive after successfully detecting sample1.exe? <br /><br />
- What is the first flag you receive after successfully detecting sample1.exe? <br /><br />
- What is the first flag you receive after successfully detecting sample1.exe? <br /><br />

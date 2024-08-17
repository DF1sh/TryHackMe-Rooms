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
- What is the first flag you receive after successfully detecting sample4.exe? <br /><br />
    Apparently the attacker has enough money to buy multiple domain names; our actions are not sufficient. The analysis of `sample4.exe` shows that the malware tries to modify     
    `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection`. This registry key handles the real-time protection of Windows Defender; by disabling it, the malware has less chances of being detected.       We need to create a rule to detect changes to this registry key. Go to 'Sigma Rule Builder' --> Create Sigma Rule --> Sysmon Event Logs --> Registry Modifications, and submit the following options:

       Registry Key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection
       Registry Name: DisableRealtimeMonitoring
       Value: 1
       ATT&CK ID: Defense Evasion (TA0005)
    This will get us the flag: `THM{c956f455fc076aea829799c0876ee399}`<br /><br />
- What is the first flag you receive after successfully detecting sample5.exe? <br /><br />
    The analysis of `sample5.exe` shows nothing new from other samples. However, we are provided with a file named `outgoing_connections.log`, showing us the following data:
    ![image](https://github.com/user-attachments/assets/b261735d-508c-4237-b973-a98239e78193) <br />
    Among other connections, we can see that some data is being sent at regular intervals (every 30 minutes) with an exact size of 97 bytes. This is very unusual for normal, legitimate traffic, which usually varies in size     and timing depending on the data being sent. I believe this pattern is typical of $\color{brown}{\textsf{beaconing}}$. Beaconing is a tactic used by malware to maintain communication with a C2 server, by sending out these "beacons" to let      the attacker know that the infected system is still alive; it's like a heartbeat message. To block the malware, we might try to block these heartbeat messages.
    Go to 'Sigma Rule Builder' --> Sysmon Event Logs --> Network Connections, and set the following conditions:

      Remote IP: Any
      Remote Port: Any
      Size: 97 bytes
      Frequency: 1800
      ATT&CK ID: Command and Control (TA0011)
  This will get us the flag: `THM{46b21c4410e47dc5729ceadef0fc722e}`<br /><br />
- What is the final flag you receive from Sphinx? <br /><br />
  For the final challenge on `sample6.exe`, we are also provided with a log file:
  ![image](https://github.com/user-attachments/assets/47578ed3-5e6b-4b87-b73b-872d0899b864)<br />
  These logs tell us that a file named `exfiltr8.log` is being used to gather a significant amount of information about the system, including directory contents, system and network information, running services and so on.
  We need to block the usage of this file. Go to 'Sigma Rule Builder' --> Sysmon Event Logs --> File Creation and Modifications, and set the following options:

      File Path: %temp%
      File Name: exfiltr8.log
      ATT&CK ID: Exfiltration (TA0010)
  This will get us the final flag: `THM{c8951b2ad24bbcbac60c16cf2c83d92c}`

  bye :)


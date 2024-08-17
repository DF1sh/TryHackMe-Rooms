# Summit

### Challenge

- What is the first flag you receive after successfully detecting sample1.exe? <br /><br />
    Go to the 'Malware Sandbox' section and analyze `sample1.exe`. The analysis will provide you with the hashes of the malware, specifically the MD5, SHA1 and SHA256 hashes.
    Move to the 'Manage Hashes' section and simply submit one of the provided hashes to the EDR(Endpoint Detection and Response) system, and get the flag: `THM{f3cbf08151a11a6a331db9c6cf5f4fe4}`<br /><br />
- What is the first flag you receive after successfully detecting sample2.exe? <br /><br />
    The analysis of `sample2.exe` will provides with information about network activity. Specifically, the PID related to the malware attempts an HTTP request to [the URL](http://154.35.10.113:4444/uvLk8YI32)

# Friday Overtime

### Challenge Scenario 
- Who shared the malware samples? <br />
![image](https://github.com/user-attachments/assets/8f79ef0e-ed0a-468f-9918-990de00b2c63)<br />
`Oliver Bennett`<br />

- What is the SHA1 hash of the file "pRsm.dll" inside samples.zip? <br />
The attached VM has a terminal emulator available. The command to compute the SHA1 for a file is `sha1sum {file}`. <br />
![image](https://github.com/user-attachments/assets/3e3c4f53-e0d7-4e2e-9775-ccbfe4cabd6f)<br />
The answer is `9d1ecbbe8637fed0d89fca1af35ea821277ad2e8`. <br />
- Which malware framework utilizes these DLLs as add-on modules? <br />
Some OSINT was helpful to find the answer, in particular at [https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot) <br />
The answer is `MgBot`. <br />
- Which MITRE ATT&CK Technique is linked to using pRsm.dll in this malware framework? <br />
I found the answer [here](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/): `T1123` <br />
![image](https://github.com/user-attachments/assets/c3169f2f-b245-42c5-ad1f-1b2837432bea) <br />
- What is the CyberChef defanged URL of the malicious download location first seen on 2020-11-02? <br />
The malicious URL can be found in the previous website: <br />
![image](https://github.com/user-attachments/assets/291460ec-8dd2-48e2-88b9-27692bb0217a)<br />
To defang it, go to CyberChef and search for the "defang" operation. <br />
The defaged URL is `hxxp[://]update[.]browser[.]qq[.]com/qmbs/QQ/QQUrlMgr_QQ88_4296.exe` <br />
- What is the CyberChef defanged IP address of the C&C server first detected on 2020-09-14 using these modules? <br />
- What is the SHA1 hash of the spyagent family spyware hosted on the same IP targeting Android devices on November 16, 2022? <br />

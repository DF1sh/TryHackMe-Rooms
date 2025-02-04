# MAL: Researching

### Checksums 101
- Name the term for an individual piece of binary `Bit`
- What are checksums also known as? `Hashes`
- Name the algorithm that is next in the series after SHA-256 `SHA-512`
- According to this task, how long will you need to hash 6 million files before a MD5 hash collision occurs? `100 Years`
- Who developed the MD5 algorithm? `Ronald Rivest`

### Online Sandboxing
- Name the key term for the type of malware that Emotet is classified as <br/ >
![image](https://github.com/user-attachments/assets/a8870c03-3605-474f-9257-c3ccb319a2fe)<br />
`Trojan`
- Research time! What type of emails does Emotet use as its payload? <br/ > `spam emails`
- Begin analysing the report, what is the timestamp of when the analysis was made? <br/ > `9/16/2019, 13:54:48`
- Name the file that is detected as a "Network Trojan" <br/ >
![image](https://github.com/user-attachments/assets/98228ab4-dc24-46c8-9f58-447ebf489c7d)<br />
`easywindow.exe`
- What is the PID of the first HTTP GET request? <br/ >
![image](https://github.com/user-attachments/assets/924362fd-6ce7-481c-a6fa-5f4dbb9d6e53)<br />
`2748`
- What is the only DNS request that is made after the sample is executed? <br/ >
![image](https://github.com/user-attachments/assets/9520968c-2c49-4d4c-a067-6271ebab189f)<br />
`blockchainjoblist.com`

### Practical: Calculating & Reporting Checksums
- Using the HashTab tool, what is the MD5 checksum for "LoginForm.exe"?<br />
![image](https://github.com/user-attachments/assets/857aea00-5c94-4ad7-a6fa-b5793d528059)<br />
`FF395A6D528DC5724BCDE9C844A0EE89`
- Using Get-FileHash in Powershell, retrieve the SHA256 of "TryHackMe.exe" <br />
![image](https://github.com/user-attachments/assets/db030059-3af7-4d25-8e1f-dc3562188b26)<br />
`6F870C80361062E8631282D31A16872835F7962222457730BC55676A61AD1EE0`
- What would be the syntax to retrieve the SHA256 checksum of "TryHackMe.exe" using CertUtil in Powershell?<br />
`CertUtil -hashfile TryHackMe.exe SHA256`

### VirusTotal
- Navigate to the "Details" tab, what is the other filename and extension reported as present?<br />
![image](https://github.com/user-attachments/assets/a64e3a89-1a0e-4cec-8593-e821e8e9f158)<br />
`HxD.exe`
- In the same "Details" tab, what is the reported compilation timestamp? <br /> `2020-02-28 11:16:36`
- What is the THM{} formatted flag on the report? <br />
Go to the comment section:<br />
![image](https://github.com/user-attachments/assets/79d57aa2-72c0-4b75-9958-44da3e4f33ff)<br />
`THM{TryHackMe_Malware_Series_Research_Flag}`

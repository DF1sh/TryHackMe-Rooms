# MAL: Strings

### What are "strings"?
- What is the name of the account that had the passcode of "12345678" in the intellian example discussed above?<br />
I found the answer at [this link](https://www.cvedetails.com/cve/CVE-2020-8000/): `intellian`
- What is the CVE entry disclosed by the company "Teradata" in their "Viewpoint" Application that has a password within a string?<br />
Found the answer at [this link](https://www.cvedetails.com/cve/CVE-2019-6499/): `CVE-2019-6499`
- According to OWASP's list of "Top Ten IoT" vulnerabilities, name the ranking this vulnerability would fall within, represented as text.<br />
Found the answer [here](https://wiki.owasp.org/index.php/OWASP_Internet_of_Things_Project#tab=IoT_Top_10): `one`

### Practical: Extracting "strings" From an Application
- What is the correct username required by the "LoginForm"?<br />
For these questions I used IDA on my windows machine because I didn't want to open kali VM but it's the same thing:<br />
![image](https://github.com/user-attachments/assets/4112715e-c799-4b44-ad51-490f95867136)<br />
`cmnatic`
- What is the required password to authenticate with? `TryHackMeMerchWhen`
- What is the "hidden" THM{} flag? `THM{Not_So_Hidden_Flag}`

### Strings in the Context of Malware
- What is the key term to describe a server that Botnets recieve instructions from? `Command and Control`
- Name the discussed example malware that uses "strings" to store the bitcoin wallet addresses for payment `Wannacry`

### Practical: Finding Bitcoin Addresses in Ransomware (Deploy!) 
- What was the date of the first transaction made in the Bitcoin wallet of the "WannaCry" developers? Answer format: DD/MM/YYYY<br />
`5/12/2017`
- What is the Bitcoin Address stored within "ComplexCalculator.exe"?<br />
First I put the strings of `ComplexCalculatorv2.exe` into a file called `strings.txt`, with the command `strings.exe ComplexCalculatorv2.exe > strings.txt`.<br />
Next, I looked at the strings with `type strings.txt`, and found the bitcoin address:<br />
![image](https://github.com/user-attachments/assets/dd9a61ff-1e5a-43e9-aafa-3401c931e12e)<br />
`1LVB65imeojrgC3JPZGBwWhK1BdVZ2vYNC`.

### Summary
- What is the name of the toolset provided by Microsoft that allows you to extract the "strings" of an application? `Sysinternals`
- What operator would you use to "pipe" or store the output of the strings command? `>`
- What is the name of the currency that ransomware often uses for payment? `bitcoin`

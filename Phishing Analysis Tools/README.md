# Phishing Analysis Tools

### Email header analysis
- What is the official site name of the bank that capitai-one.com tried to resemble? `capitalone.com`

### Email body analysis
- How can you manually get the location of a hyperlink? `Copy Link Location`

### PhishTool
- Look at the Strings output. What is the name of the EXE file?
`#454326_PDF.exe`

### Phishing Case 1
- What brand was this email tailored to impersonate? <br />
![image](https://github.com/user-attachments/assets/ec209216-3bc9-4e59-9d2c-fbb0554b7422) <br />
`Netflix`
- What is the From email address? <br />
Go to [Message Header Analyzer](https://mha.azurewebsites.net/) to find out, or simply open an email reader such as thunderbird: 
`N e t f I i x <JGQ47wazXe1xYVBrkeDg-JOg7ODDQwWdR@JOg7ODDQwWdR-yVkCaBkTNp.gogolecloud.com>`
- What is the originating IP? Defang the IP address. <br />
  From Message Header Analyzer we have: <br />
  ![image](https://github.com/user-attachments/assets/a5df2159-541d-42b2-94c2-f69bbe2ea912) <br />
  To defang the IP address you can use [CyberChef](https://gchq.github.io/CyberChef/): `209[.]85[.]167[.]226`
- From what you can gather, what do you think will be a domain of interest? Defang the domain. `etekno[.]xyz`
- What is the shortened URL? Defang the URL. `hxxps[://]t[.]co/yuxfZm8KPg?amp=1`

### Phishing Case 2
A malicious attachment from a phishing email inspected in the previous Phishing Room was uploaded to Any Run for analysis. <br />
- What does AnyRun classify this email as? `Suspicious activity`
- What is the name of the PDF file? `Payment-updateid.pdf`
- What is the SHA 256 hash for the PDF file? `CC6F1A04B10BCB168AEEC8D870B97BD7C20FC161E8310B5BCE1AF8ED420E2C24`
- What two IP addresses are classified as malicious? Defang the IP addresses. (answer: IP_ADDR,IP_ADDR) <br />
![image](https://github.com/user-attachments/assets/99898a77-f353-41a8-8b18-c83d4072556a)<br />
`2[.]16[.]107[.]24,2[.]16[.]107[.]83`

- What Windows process was flagged as Potentially Bad Traffic? `svchost.exe`

### Phishing Case 3
A malicious attachment from a phishing email inspected in the previous Phishing Room was uploaded to Any Run for analysis. 
- What is this analysis classified as? `Malicious activity`
- What is the name of the Excel file? `CBJ200620039539.xlsx`
- What is the SHA 256 hash for the file? <br />
![image](https://github.com/user-attachments/assets/fa2490fe-d591-4e57-b94b-a7d0e544cc58) <br />
`5f94a66e0ce78d17afc2dd27fc17b44b3ffc13ac5f42d3ad6a5dcfb36715f3eb`
- What domains are listed as malicious? Defang the URLs & submit answers in alphabetical order. (answer: URL1,URL2,URL3) <br />
![image](https://github.com/user-attachments/assets/e61c4c74-e15c-4af8-a732-e782beab08aa)<br />
`biz9holdings[.]com,findresults[.]site,ww38[.]findresults[.]site`
- What IP addresses are listed as malicious? Defang the IP addresses & submit answers from lowest to highest. (answer: IP1,IP2,IP3) `75[.]2[.]11[.]242,103[.]224[.]182[.]251,204[.]11[.]56[.]48`
- What vulnerability does this malicious attachment attempt to exploit? `cve-2017-11882`

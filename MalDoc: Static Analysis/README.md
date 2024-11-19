# MalDoc: Static Analysis

### Initial Access - Spearphishing Attachment
- From which family does the Locky malware belong to? `ransomware`
- What is the Sub-technique ID assigned to Spearphishing Attachment? `T1566.001`

### PDF Documents - Structure
- Who is the author of the simple.pdf document?<br />
![image](https://github.com/user-attachments/assets/33ca635e-f8f6-47cf-8d13-4ed1afc38a8d)<br />
`Ben`

### Analyzing a PDF Document
- What is the flag found inside the JavaScript code?<br />
Run `peepdf -i simple.pdf` and then `extract js`:<br />
![image](https://github.com/user-attachments/assets/54cad6e1-1714-48ef-a4c8-9e1d6cf1ccc1)<br />
`THM{Luckily_This_Isn't_Harmful}`
- How many OpenAction objects were found within the document?<br />
Run `peepdf simple.pdf` to get the answer: `1`
- How many Encoded objects were found in the document?<br />
Same thing: `2`
- What are the numbers of encoded objects? (Separate with a comma)<br />
`15,18`

### Analyzing Malicious JavaScript
- What is the name of the dumped file that contains information about the URLs?<br />
![image](https://github.com/user-attachments/assets/5829722c-7ac4-426f-b5fb-dfb5c1e5a7bb)<br />
`urls.json`
- How many URLs were extracted from JavaScript?<br />
![image](https://github.com/user-attachments/assets/d7aa5ee9-b93f-4a50-a910-d003c1d543c8)<br />
`9`
- What is the full URL which contains the keyword slideshow? (defang the URL)<br />
Copy it and defang it using [CyberChef](https://cyberchef.org/):<br />
`hxxp://aristonbentre[.]com/slideshow/01uPzXd2YscA/`

### Office Docs Analysis
- What is the author name of the document found during the analysis?<br />
Run `olemeta suspicious.doc` to get the answer:<br />
![image](https://github.com/user-attachments/assets/670db09c-7dce-4313-bc11-7bc802a70279)<br />
`CMNatic`
- How many macros are embedded in the document?<br />
![image](https://github.com/user-attachments/assets/1311401a-ccf2-4a2f-afed-eb23eb51c9d0)<br />
`2`
- What is the URL extracted from the suspicious.doc file?<br />
Run viperMonkey on the suspicious file and decode the base64 encoded string from the powershell command:
`http://thmredteam.thm/stage2.exe`

### OneNote
-  What is the value used in the sleep function?<br />
Performs the steps shown in the task:<br />
![image](https://github.com/user-attachments/assets/46edd2a6-b8f0-4f75-b117-ebb2fedc4684)<br />
`15000`
-  The cURL command is being used to download from a URL and saving the payload in a png file. What is that file name?<br />
`index1.png`
-  How many objects are found in the invoice.one document?<br />
![image](https://github.com/user-attachments/assets/c6af4b94-89b3-475b-812f-63c7fec0137f)<br />
`6`

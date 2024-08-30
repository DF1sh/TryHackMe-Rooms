# The Greenholt Phish

### Just another day as a SOC Analyst
- What is the Transfer Reference Number listed in the email's Subject? <br />
![image](https://github.com/user-attachments/assets/6d5da915-4f11-431d-9c2c-60f76032eca7)<br/>
`09674321`
- Who is the email from? `Mr. James Jackson`
- What is his email address? `info@mutawamarine.com`
- What email address will receive a reply to this email? `info.mutawamarine@mail.com`
- What is the Originating IP? <br />
  Submit the email header in [Message Header Analyzer](https://mha.azurewebsites.net/): <br />
  ![image](https://github.com/user-attachments/assets/ade69e40-c9aa-4282-895e-b7e2bf685602)<br />
  `192.119.71.157`
- Who is the owner of the Originating IP? (Do not include the "." in your answer.)
Perform a [WHOIS](https://lookup.icann.org/en/lookup) lookup on the originating IP: <br />
![image](https://github.com/user-attachments/assets/5c9301f4-5033-48ca-b32d-afe02c01a25f)<br />
  `Hostwinds LLC`
- What is the SPF record for the Return-Path domain? <br />
Use the [dmarcian SPF survey](https://dmarcian.com/spf-survey/) to get the SPF record for the domain: <br />
![image](https://github.com/user-attachments/assets/50e14fa2-fa4f-4967-b61b-3687c2931a0d) <br/>
`v=spf1 include:spf.protection.outlook.com -all`
- What is the DMARC record for the Return-Path domain? <br />
Now use the [dmarcian DMARC checker](https://dmarcian.com/domain-checker/) to find the answer: <br />
![image](https://github.com/user-attachments/assets/e085d9f4-a275-4ee7-b6ed-a96cbe5837c8) <br />
`v=DMARC1; p=quarantine; fo=1`
- What is the name of the attachment? `SWT_#09674321____PDF__.CAB`
- What is the SHA256 hash of the file attachment? <br />
From thunderbird, safely save the attachment by clicking "save" on the bottom-right (don't open it). Then compute the sha256 using the command `sha256sum <file>`: <br />
![image](https://github.com/user-attachments/assets/b0f5c055-9e9c-43ee-bb76-ae4175af0fac)<br />
`2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f`
- What is the attachments file size? (Don't forget to add "KB" to your answer, NUM KB) <br />
Submit the hash on [VirusTotal](https://www.virustotal.com/) to find the asnwer: <br />
![image](https://github.com/user-attachments/assets/2d884c2e-1920-4667-9b87-49b5f62caa6f)<nbr />
`400.26 KB`
- What is the actual file extension of the attachment? `RAR`


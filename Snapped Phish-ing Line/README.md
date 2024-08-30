# Snapped Phish-ing Line

### Challenge Scenario
- Who is the individual who received an email attachment containing a PDF? `William McClean`
- What email address was used by the adversary to send the phishing emails? `Accounts.Payable@groupmarketingonline.icu`
- What is the redirection URL to the phishing page for the individual Zoe Duncan? (defanged format) <br />
Open the attachment on the email, using a text editor: <br />
![image](https://github.com/user-attachments/assets/bd672ed9-02e6-40e3-9c96-e4f339a5ee0f)<br />
Copy the URL and use [CyberChef](https://gchq.github.io/CyberChef/) to defang it: `hxxp[://]kennaroads[.]buzz/data/Update365/office365/40e7baa2f826a57fcf04e5202526f8bd/?email=zoe[.]duncan@swiftspend[.]finance&error`
- What is the URL to the .zip archive of the phishing kit? (defanged format) <br />
Now take the URL and traverse directories up to the "data" directory: <br />
![image](https://github.com/user-attachments/assets/faadd190-3755-499e-9c07-68665503c229)<br />
`hxxp[://]kennaroads[.]buzz/data/Update365[.]zip`
- What is the SHA256 hash of the phishing kit archive?
Download the zip archive, open a terminal and use the command `sha256sum` to comput the hash of the file: <br />
![image](https://github.com/user-attachments/assets/302c3d93-1345-4c1d-a662-27fb08f4b293)<br />
`ba3c15267393419eb08c7b2652b8b6b39b406ef300ae8a18fee4d16b19ac9686`
- When was the phishing kit archive first submitted? (format: YYYY-MM-DD HH:MM:SS UTC) <br />
Now that we have the hash of the phishing kit, we can try to submit it to [VirusTotal](https://www.virustotal.com/) for more details: <br />
![image](https://github.com/user-attachments/assets/7d420bd4-ed8f-4ea6-8d15-a045db7a2807)
`2020-04-08 21:55:50 UTC`
- When was the SSL certificate the phishing domain used to host the phishing kit archive first logged? (format: YYYY-MM-DD) `2020-06-25`
- What was the email address of the user who submitted their password twice? `michael.ascot@swiftspend.finance`
- What was the email address used by the adversary to collect compromised credentials? `m3npat@yandex.com`
- The adversary used other email addresses in the obtained phishing kit. What is the email address that ends in "@gmail.com"? `jamestanner2299@gmail.com`
- What is the hidden flag? `THM{pL4y_w1Th_tH3_URL}`

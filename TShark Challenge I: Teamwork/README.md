# TShark Challenge I: Teamwork

### Case: Teamwork!
- What is the full URL of the malicious/suspicious domain address? Enter your answer in defanged format.<br />
The command that worked for me is `tshark -r teamwork.pcap -Y 'dns'`. I also used [CyberChef](https://gchq.github.io/CyberChef/) to defang the URL: `www[.]paypal[.]com4uswebappsresetaccountrecovery[.]timeseaways[.]com`
- When was the URL of the malicious/suspicious domain address first submitted to VirusTotal?<br />
Submit the URL on VirusTotal:<br />
![image](https://github.com/user-attachments/assets/a2122494-dc7a-41cf-80fa-da4bff2abb47)<br />
Below the 'History' section, we can find the answer: `
2017-04-17 22:52:53 UTC`
- Which known service was the domain trying to impersonate? `PayPal`
- What is the IP address of the malicious domain? Enter your answer in defanged format. <br />
I found the answer from the output of the command used for the first question: `184[.]154[.]127[.]226`
- What is the email address that was used? Enter your answer in defanged format. (format: aaa[at]bbb[.]ccc) <br />
What worked for me is `tshark -r teamwork.pcap -V | grep -Ei "email|mail|[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"`. <br />
`johnny5alive[at]gmail[.]com`

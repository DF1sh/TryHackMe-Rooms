# Intro to Log Analysis

### Investigation Theory
- What's the term for a consolidated chronological view of logged events from diverse sources, often used in log analysis and digital forensics? `Super Timeline`
- Which threat intelligence indicator would 5b31f93c09ad1d065c0491b764d04933 and 763f8bdbc98d105a8e82f36157e98bbe be classified as? `Super Timeline`

### Detection Engineering
- What is the default file path to view logs regarding HTTP requests on an Nginx server? `/var/log/nginx/access.log`
- A log entry containing %2E%2E%2F%2E%2E%2Fproc%2Fself%2Fenviron was identified. What kind of attack might this infer? `Path Traversal`

### Automated vs. Manual Analysis
- A log file is processed by a tool which returns an output. What form of analysis is this? `Automated`
- An analyst opens a log file and searches for events. What form of analysis is this? `Manual`

### Log Analysis Tools: Command Line
- Use cut on the apache.log file to return only the URLs. What is the flag that is returned in one of the unique entries?<br />
Run `cut -d ' ' -f 7 apache.log`:<br />
![image](https://github.com/user-attachments/assets/e3bf9e2d-f248-461a-a5af-906ae439923c)<br />
`c701d43cc5a3acb9b5b04db7f1be94f6`
- In the apache.log file, how many total HTTP 200 responses were logged?<br />
![image](https://github.com/user-attachments/assets/c2b2dbf5-80a2-4c72-a18a-80542537e820)<br />
`52`
- In the apache.log file, which IP address generated the most traffic?<br />
![image](https://github.com/user-attachments/assets/3d030336-fa02-4e21-b222-7f030f564d85)<br />
`145.76.33.201`
- What is the complete timestamp of the entry where 110.122.65.76 accessed /login.php?<br />
Run `cat apache.log | grep 110.122.65.76 | grep /login.php` to get the answer:
`31/Jul/2023:12:34:40 +0000`

### Log Analysis Tools: Regular Expressions
- How would you modify the original grep pattern above to match blog posts with an ID between 22-26? `post=2[2-6]`
- What is the name of the filter plugin used in Logstash to parse unstructured log data? `Grok`

### Log Analysis Tools: CyberChef
- Upload the log file named "access.log" to CyberChef. Use regex to list all of the IP addresses. What is the full IP address beginning in 212?<br />
![image](https://github.com/user-attachments/assets/cba13a37-37db-4c8f-a658-30c350abb39a)<br />
`212.14.17.145`
- Using the same log file from Question #2, a request was made that is encoded in base64. What is the decoded value? `THM{CYBERCHEF_WIZARD}`
- Using CyberChef, decode the file named "encodedflag.txt" and use regex to extract by MAC address. What is the extracted value? `08-2E-9A-4B-7F-61`

### Log Analysis Tools: Yara and Sigma
- What languages does Sigma use? `YAML`
- What keyword is used to denote the "title" of a Sigma rule? `title`
- What keyword is used to denote the "name" of a rule in YARA? `rule`

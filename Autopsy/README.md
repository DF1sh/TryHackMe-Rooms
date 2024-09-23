# Autopsy

### Workflow Overview and Case Analysis
- What is the file extension of the Autopsy files? `.aut`

### Data Sources
- What is the disk image name of the "e01" format? `EnCase`
### The User Interface I

- Expand the "Data Sources" option; what is the number of available sources?<br />
![image](https://github.com/user-attachments/assets/befde4b3-e3d5-4618-9ea7-6f76f398d491)<br />
`4`
- What is the number of the detected "Removed" files? <br />
![image](https://github.com/user-attachments/assets/d52ac980-f217-4a3d-b6fa-bf77fe3ea964)<br />
`10`
- What is the filename found under the "Interesting Files" section?<br />
![image](https://github.com/user-attachments/assets/614dabda-d774-40dc-92d1-3042f10723aa)<br />
`googledrivesync.exe`

### The User Interface II
- What is the full name of the operating system version?<br />
![image](https://github.com/user-attachments/assets/a95958dc-b6c2-45c3-8844-f8d3abf06273)<br />
`Windows 7 Ultimate Service Pack 1`
- What percentage of the drive are documents? Include the % in your answer. `40.8%`
- Generate an HTML report as shown in the task and view the "Case Summary" section. What is the job number of the "Interesting Files Identifier" module?<br />
After creating the report, press CTRL+G and search for "interesting"; it will speed up the process:<br />
![image](https://github.com/user-attachments/assets/aba183b1-b8a6-44a5-b40d-a7c3ecd42bea)<br />
`10`

### Data Analysis
- What is the name of an Installed Program with the version number of 6.2.0.2962?<br />
Select "Keyword search" and search for "6.2.0.2962":<br />
![image](https://github.com/user-attachments/assets/33d094d5-ecdd-44d8-90c0-129caab59c5a)<br />
`Eraser`
- A user has a Password Hint. What is the value?<br />
Similarly, search for "password hint":<br />
![image](https://github.com/user-attachments/assets/ef478b1c-e0e9-4a51-ab72-e5f29ee79a5d)<br />
`IAMAN`
- Numerous SECRET files were accessed from a network drive. What was the IP address?<br />
Search for "secret": <br />
![image](https://github.com/user-attachments/assets/5b54c2c3-c0d4-40b7-94d1-cea0db91463d)<br />
`10.11.11.128`
- What web search term has the most entries?<br />
Select Results -> Extracted Content -> Web search to find the answer: `information leakage cases`
- What was the web search conducted on 3/25/2015 21:46:44?
- What MD5 hash value of the binary is listed as an Interesting File?
- What self-assuring message did the 'Informant' write for himself on a Sticky Note? (no spaces)

### Visualisation Tools
- Using the Timeline, how many results were there on 2015-01-12?
- The majority of file events occurred on what date? (MONTH DD, YYYY)

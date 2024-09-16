# Benign

### Scenario: Identify and Investigate an Infected Host
- How many logs are ingested from the month of March, 2022? <br />
Filtering for last two years worked for me: `13959`
- Imposter Alert: There seems to be an imposter account observed in the logs, what is the name of that user?<br />
Click on "Username" and then on "Rare values": <br />
![image](https://github.com/user-attachments/assets/1c69efe8-508d-4d58-bd3a-3309aa9cb027)<br />
`Amel1a`
- Which user from the HR department was observed to be running scheduled tasks?<br />
![image](https://github.com/user-attachments/assets/b05c123e-0b79-451b-8416-4b6c8ee4cdf2)<br />
Since he's the user running the executables with highest counts, I suppose it's 
`Chris.fort`
- Which user from the HR department executed a system process (LOLBIN) to download a payload from a file-sharing host. <br />
One of the most used commands to download files is "certutil". So the filter I used is `index=win_eventlogs *certutil*`, and it found me one log: <br />
![image](https://github.com/user-attachments/assets/4089168c-bda6-4c85-818b-57d98b14c0c5)<br />
`haroon`
- To bypass the security controls, which system process (lolbin) was used to download a payload from the internet? `certutil.exe`
- What was the date that this binary was executed by the infected host? format (YYYY-MM-DD) `2022-03-04`
- Which third-party site was accessed to download the malicious payload?<br />
![image](https://github.com/user-attachments/assets/36e44c32-ee37-4f0f-a3e3-65cdc7c4a889)<br />
`controlc.com`
- What is the name of the file that was saved on the host machine from the C2 server during the post-exploitation phase? `benign.exe`
- The suspicious file downloaded from the C2 server contained malicious content with the pattern THM{..........}; what is that pattern? <br />
Go to [https://controlc.com/e4d11035](https://controlc.com/e4d11035) to get the answer: <br />
![image](https://github.com/user-attachments/assets/b654e300-27b8-48ec-b450-f530d55260ac)<br />
`THM{KJ&*H^B0}`
- What is the URL that the infected host connected to? `https://controlc.com/e4d11035`

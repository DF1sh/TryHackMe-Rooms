# SOC Fundamentals

### Introduction to SOC
- What does the term SOC stand for? `Security Operations Center `

### Purpose and Components
- The SOC team discovers an unauthorized user is trying to log in to an account. Which capability of SOC is this? `Detection`
- What are the three pillars of a SOC? `People, Process, Technology`

### People
- Alert triage and reporting is the responsibility of? `SOC Analyst (Level 1)`
- Which role in the SOC team allows you to work dedicatedly on establishing rules for alerting security solutions? `Detection Engineer`

### Process
- At the end of the investigation, the SOC team found that John had attempted to steal the system's data. Which 'W' from the 5 Ws does this answer? `Who`
- The SOC team detected a large amount of data exfiltration. Which 'W' from the 5 Ws does this answer? `What`

### Technology
- Which security solution monitors the incoming and outgoing traffic of the network? `Firewall`
- Do SIEM solutions primarily focus on detecting and alerting about security incidents? (yea/nay) `yea`

### Practical Exercise of SOC
![image](https://github.com/user-attachments/assets/0fff721e-5222-4a17-ae06-680e5ab36857)<br />
- What: Activity that triggered the alert? `Port Scan`
- When: Time of the activity? `June 12, 2024 17:24`
- Where: Destination host IP?  `10.0.0.3`
- Who: Source host name? `Nessus`
- Why: Reason for the activity? Intended/Malicious `Intended`
- Additional Investigation Notes: Has any response been sent back to the port scanner IP? (yea/nay) `yea`
- What is the flag found after closing the alert? `THM{000_INTRO_TO_SOC}`

# OpenCTI

### OpenCTI Dashboard 1
- What is the name of the group that uses the 4H RAT malware? <br /><br />
Once connected to the web page of the deployed machine on port 8080, move on the "Arsenal" section and search for the malware "4H RAT". <br />
From the description, we can see that it's been used by the group `Putter Panda`. <br /><br />
- What kill-chain phase is linked with the Command-Line Interface Attack Pattern? <br /><br />
Go to "Arsenal" and search for "Command-Line Interface" --> Attack Pattern, click on the second element on the list: <br />
![image](https://github.com/user-attachments/assets/244402f4-9920-4157-9660-e13da2814ea4)<br />
Here we can find the answer: `Execution-ics`<br />
- Within the Activities category, which tab would house the Indicators? `Observations` <br />

### OpenCTI Dashboard 2
- What Intrusion sets are associated with the Cobalt Strike malware with a Good confidence level? (Intrusion1, Intrusion2) <br /><br />
An **Intrusion Set** is a collection of related cyber attack activities or campaigns attributed to a specific threat actor or group, sharing common tactics, techniques, procedures (TTPs). <br />
Move to the "Arsenal" section and search for "Cobalt Strike". Then move to the "knowledge" tab and then click on the "Intrusion Sets" tab on the right. <br />
This will open a list of intrusion sets related to the given malware. There are only two instruction sets with a "good" confidence level: `CopyKittens, FIN7`. <br /><br />
- Who is the author of the entity? <br />
Search again for the "Cobalt Strike" malware, then, from the results, click on "malware" --> "Cobalt Strike". <br />
![image](https://github.com/user-attachments/assets/45fe6ef9-b047-47aa-aa2d-d417d7074e5c) <br />
This will get us the answer: `The MITRE Corporation`. <br />

### Investigative Scenario
Using the same techniques described for the previous sections, we should be able answer the following questions:
- What is the earliest date recorded related to CaddyWiper?  Format: YYYY/MM/DD `2022/03/15` <br />
- Which Attack technique is used by the malware for execution? `Native API` <br />
- How many malware relations are linked to this Attack technique? `113` <br />
- Which 3 tools were used by the Attack Technique in 2016? (Ans: Tool1, Tool2, Tool3) `BloodHound, Empire, ShimRatReporter` <br />
- What country is APT37 associated with? `North Korea` <br />
- Which Attack techniques are used by the group for initial access? (Ans: Technique1, Technique2) `T1189, T1566` <br />

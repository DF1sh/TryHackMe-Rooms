# Trooper

### Who's The Threat? 
- What kind of phishing campaign does APT X use as part of their TTPs? <br /><br />
We are provided with an OpenCTI client and a report about APT X. Reading through the report it's easy to find the answer: `spear-phishing emails` <br />
- What is the name of the malware used by APT X? `USBferry` <br /><br />
- What is the malware's STIX ID? <br /><br />
Search for "USBferry" on OpenCTI to get the answer: `malware--5d0ea014-1ce9-5d5c-bcc7-f625a07907d0` <br />
- With the use of a USB, what technique did APT X use for initial access? <br /><br />
Move to the "Knowledge" section to find the reference to a MITRE report: [https://attack.mitre.org/software/S0452/](https://attack.mitre.org/software/S0452/). There we can find the technique used for initial access: `Replication through removable media` <br />
- What is the identity of APT X? `Tropic Trooper`  <br /><br />
- On OpenCTI, how many Attack Pattern techniques are associated with the APT? `39` <br /><br />
- What is the name of the tool linked to the APT? <br /><br />
Search for "Tropic Trooper", move to the "knowledge" section and click on the "tool" tag to find the answer: `BITSAdmin` <br />
- Load up the Navigator. What is the sub-technique used by the APT under Valid Accounts? <br /><br />
Open the MITRE Navigator, search for "Trooper". Under the Initial Access tecniques find "valid accounts" technique to find the answer: `Local Accounts` <br />
- Under what Tactics does the technique above fall? `Initial Access, Persistence,  Defense Evasion and Privilege Escalation` <br /><br />
- What technique is the group known for using under the tactic Collection? `Automated Collection` <br /><br />

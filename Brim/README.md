# Brim

### The Basics
- Process the "sample.pcap" file and look at the details of the first DNS log that appear on the dashboard. What is the "qclass_name"? <br />
![image](https://github.com/user-attachments/assets/f7af0d00-6e76-467b-92eb-2eb3ac483a85)<br />
`C_INTERNET`
- Look at the details of the first NTP log that appear on the dashboard. What is the "duration" value? <br />
`0.005`
- Look at the details of the STATS packet log that is visible on the dashboard. What is the "reassem_tcp_size"?<br />
![image](https://github.com/user-attachments/assets/f4058965-9140-4c32-8ddc-3c471c036d0c)<br />
`540`

### Default Queries
- Investigate the files. What is the name of the detected GIF file?<br />
Click on "File Activity": <br />
![image](https://github.com/user-attachments/assets/4391fa00-ec6a-45e9-9630-c82b2e28288c)<br />
`cat01_with_hidden_text.gif`
- Investigate the conn logfile. What is the number of the identified city names? Open the conn.log file and use this filter `_path=="conn" | cut geo.resp.country_code, geo.resp.region, geo.resp.city` to get the answer: `2`
- Investigate the Suricata alerts. What is the Signature id of the alert category "Potential Corporate Privacy Violation"? <br />
This filter `event_type=="alert" | alert.category | sort count` worked for me: `2,012,887`

### Exercise: Threat Hunting with Brim | Malware C2 Detection
- What is the name of the file downloaded from the CobaltStrike C2 connection? <br />
Select "HTTP Requests" to find out: <br />
![image](https://github.com/user-attachments/assets/796087ce-b868-431d-8ad7-97850c8e348f)<br/>
`4564.exe`
- What is the number of CobaltStrike connections using port 443? <br />
Use the following filter `_path=="conn" id.resp_h==104.168.44.45 id.resp_p==443 | count() by id.resp_p` to get the asnwer: `328`
- There is an additional C2 channel in used the given case. What is the name of the secondary C2 channel? `IcedID`

### Exercise: Threat Hunting with Brim | Crypto Mining
- How many connections used port 19999? <br />
Use the following filter: `_path=="conn" id.resp_p==19999 | count() by id.resp_p`: `22`
- What is the name of the service used by port 6666? <br />
Use the filter `_path=="conn" id.resp_p==6666 | cut service | uniq`: <br />
![image](https://github.com/user-attachments/assets/86f1d151-e6d0-49c3-bcaf-3ca1dd86d155)<br />
`irc`
- What is the amount of transferred total bytes to "101.201.172.235:8888"? <br />
Use `_path=="conn" | put total_bytes := orig_bytes + resp_bytes | 101.201.172.235 | 8888`: <br/ >
![image](https://github.com/user-attachments/assets/9793664a-9a60-4f68-8fee-dfc19a805355)<br />
`3,729`
- What is the detected MITRE tactic id?<br />
![image](https://github.com/user-attachments/assets/3763c3b7-c930-46ea-9654-6e643bdf5113)<br />
`TA0040`




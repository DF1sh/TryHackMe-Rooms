# Incident handling with Splunk

### Reconnaissance Phase
- One suricata alert highlighted the CVE value associated with the attack attempt. What is the CVE value?<br />
On the top-right, select "All-time". Now use the following filter: `index=botsv1 imreallynotbatman.com src=40.80.148.42 sourcetype=suricata "alert.signature"="*CVE*"`.<br />
![image](https://github.com/user-attachments/assets/7c8560d0-678a-481f-bbd4-5de5f58bbd34)<br />
`CVE-2014-6271`
- What is the CMS our web server is using?<br />
The filter is `index=botsv1 imreallynotbatman.com src=40.80.148.42 sourcetype="fortigate_utm"`. fortigate_utm contains Fortinet Firewall logs  <br />
![image](https://github.com/user-attachments/assets/244419d3-6995-4825-92dc-241484971f62)<br />
`joomla`
- What is the web scanner, the attacker used to perform the scanning attempts?<br />
The filter I used to find it is: `index=botsv1 imreallynotbatman.com src_ip=40.80.148.42 sourcetype="stream:http"`<br />
![image](https://github.com/user-attachments/assets/528a1b4c-b373-417a-8455-a7fdb13c7972)<br />
`acunetix`
- What is the IP address of the server imreallynotbatman.com?<br />
No need to change filter, just click on dest_ip to find out: <br />
![image](https://github.com/user-attachments/assets/12a4a478-6e26-422e-b3bf-fbcedc6e83f4)<br />
`192.168.250.70`

### Exploitation Phase
- What was the URI which got multiple brute force attempts?<br />
`/joomla/administrator/index.php`
- Against which username was the brute force attempt made?<br />
The filter is `index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST uri="/joomla/administrator/index.php" | table uri src_ip dest_ip form_data`<br />
![image](https://github.com/user-attachments/assets/b4dcff71-8b47-4590-895a-445133d80cdc)<br />
`admin`
- What was the correct password for admin access to the content management system running imreallynotbatman.com?<br />
One request came from a mozilla browser, and not a python script:<br />
![image](https://github.com/user-attachments/assets/cc0b5130-69ec-45ff-9e1d-b122146cf1af)<br />
`batman`
- How many unique passwords were attempted in the brute force attempt? `412`
- What IP address is likely attempting a brute force password attack against imreallynotbatman.com? `23.22.63.114`
- After finding the correct password, which IP did the attacker use to log in to the admin panel?

### Installation Phase
- Sysmon also collects the Hash value of the processes being created. What is the MD5 HASH of the program 3791.exe? <br />
The filter that helped me is `index=botsv1 "3791.exe" source="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1 *MD5*`<br />
![image](https://github.com/user-attachments/assets/d3b9e771-c2d7-4ec6-bbd0-c1dcee8b78ae)<br />
`AAE3F5A29935E6ABCC2C2754D12A9AF0`
- Looking at the logs, which user executed the program 3791.exe on the server? <br />
The filter that helped me is `index=botsv1 "3791.exe" source="WinEventLog:Security"`<br />
![image](https://github.com/user-attachments/assets/67d61d46-ccae-4c09-b209-c9788788c016)<br />
`NT AUTHORITY\IUSR`
- Search hash on the virustotal. What other name is associated with this file 3791.exe? 
Go on VirusTotal and submit the previous MD5 hash, then click on "Details" to get the answer:<br />
![image](https://github.com/user-attachments/assets/032ff099-1a71-4061-af4b-10ac4f33569a)<br />
`ab.exe`

### Action on Objectives

### Command and Control Phase

### Weaponization Phase

### Delivery Phase

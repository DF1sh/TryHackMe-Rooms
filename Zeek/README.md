# Zeek

### Network Security Monitoring and Zeek
- What is the installed Zeek instance version number? Run "zeek -v":  `4.2.1`
- What is the version of the ZeekControl module? `2.4.0`
- Investigate the "sample.pcap" file. What is the number of generated alert files? <br />
![image](https://github.com/user-attachments/assets/7e6d6255-c7e5-452e-9976-c6779207e9a2) <br />
The number of generater .log files is `8`.

### Zeek Logs
- Investigate the sample.pcap file. Investigate the dhcp.log file. What is the available hostname? <br />
![image](https://github.com/user-attachments/assets/905b3a5f-513b-43ea-8504-c936f70782f0)<br />
`Microknoppix`
- Investigate the dns.log file. What is the number of unique DNS queries? <br />
![image](https://github.com/user-attachments/assets/6254e4a0-204e-4c8f-bc4f-76af614b21a3)<br />
`2`

- Investigate the conn.log file. What is the longest connection duration? <br />
For this task, run the following command: `cat conn.log | zeek-cut duration | sort -n`. <br />
`332.319364`

### Zeek Signatures
- Investigate the http.pcap file. Create the  HTTP signature shown in the task and investigate the pcap. What is the source IP of the first event?<br />
Create the following signature:

      signature http-password {
      ip-proto == tcp
      dst-port == 80
      payload /.*password.*/
      event "Cleartext password found"
      }
Then run `cat notice.log | zeek-cut src` to get the answer. `10.10.57.178`

- What is the source port of the second event? Run `cat signatures.log | zeek-cut src_port` to get the answer: `38712`
- Investigate the conn.log. What is the total number of the sent and received packets from source port 38706? <br />
![image](https://github.com/user-attachments/assets/a893dabc-3950-418f-8b59-17d9c34ba459)<br />
`20`
- Create the global rule shown in the task and investigate the ftp.pcap file. Investigate the notice.log. What is the number of unique events? <br />
Create the following rule:

      signature ftp-username {
      ip-proto == tcp
      ftp /.*USER.*/
      event "FTP Username Input Found!"
      }
      
      signature ftp-brute {
          ip-proto == tcp
           payload /.*530.*Login.*incorrect.*/
          event "FTP Brute-force Attempt!"
      }
![image](https://github.com/user-attachments/assets/41eef8e3-9f56-45c3-94fa-801c328d4100)<br />
`1413`

- What is the number of ftp-brute signature matches? <br />
![image](https://github.com/user-attachments/assets/ba3ed2eb-2df4-4b4b-94de-24f8be477f4a)<br />
`1410`

### Zeek Scripts | Fundamentals
- Investigate the smallFlows.pcap file. Investigate the dhcp.log file. What is the domain value of the "vinlap01" host? <br />
![image](https://github.com/user-attachments/assets/31e03999-f508-42d8-ab51-be8929b19c11)<br />
`astaro_vineyard`
- Investigate the bigFlows.pcap file. Investigate the dhcp.log file. What is the number of identified unique hostnames? <br />
Run `cat dhcp.log | zeek-cut host_name | sort -nr | uniq | wc -l` to get the answer: `17`
- Investigate the dhcp.log file. What is the identified domain value?<br />
![image](https://github.com/user-attachments/assets/4a91394b-d342-4a90-a350-a23dfc4667f9)<br />
`jaalam.net`

### Zeek Scripts | Scripts and Signatures
- Go to folder TASK-7/101. Investigate the sample.pcap file with 103.zeek script. Investigate the terminal output. What is the number of the detected new connections? <br />
Run `cat conn.log | zeek-cut uid | sort | uniq | wc -l` to get the answer: `87`
- Go to folder TASK-7/201. Investigate the ftp.pcap file with ftp-admin.sig signature and  201.zeek script. Investigate the signatures.log file. What is the number of signature hits?<br />
Run `cat signatures.log | zeek-cut uid |sort|uniq|wc -l` to get the answer: `1401`
- Investigate the signatures.log file. What is the total number of "administrator" username detections?<br />
![image](https://github.com/user-attachments/assets/762ae307-356b-4d55-8099-e3e5dc32e04f)<br />
`731`
- Investigate the ftp.pcap file with all local scripts, and investigate the loaded_scripts.log file. What is the total number of loaded scripts? <br />
Run `zeek -C -r ftp.pcap 201.zeek local`, and then `cat loaded_scripts.log | zeek-cut name | wc -l` to get the answer: `498`
- Go to folder TASK-7/202. Investigate the ftp-brute.pcap file with "/opt/zeek/share/zeek/policy/protocols/ftp/detect-bruteforcing.zeek" script. Investigate the notice.log file. What is the total number of brute-force detections? `2`

### Zeek Scripts | Frameworks
- Investigate the case1.pcap file with intelligence-demo.zeek script. Investigate the intel.log file. Look at the second finding, where was the intel info found? 
![image](https://github.com/user-attachments/assets/ef29d1fc-94e9-45e9-8b8d-34dab602280c)
`IN_HOST_HEADER`
- Investigate the http.log file. What is the name of the downloaded .exe file? <br />
![image](https://github.com/user-attachments/assets/0f4ff331-bc56-4bf9-a60f-800c2398e247)<br />
`knr.exe`
- Investigate the case1.pcap file with hash-demo.zeek script. Investigate the files.log file. What is the MD5 hash of the downloaded .exe file? <br />
![image](https://github.com/user-attachments/assets/81883805-2e5e-42ed-b3b4-8038258936da)<br />
`cc28e40b46237ab6d5282199ef78c464`
- Investigate the case1.pcap file with file-extract-demo.zeek script. Investigate the "extract_files" folder. Review the contents of the text file. What is written in the file? `Microsoft NCSI`

### Zeek Scripts | Packages
- Investigate the http.pcap file with the zeek-sniffpass module. Investigate the notice.log file. Which username has more module hits?<br />
![image](https://github.com/user-attachments/assets/4a68cf6c-4257-4bf9-9f7b-94158bc0f840)
`BroZeek`
- Investigate the case2.pcap file with geoip-conn module. Investigate the conn.log file. What is the name of the identified City? <br />
![image](https://github.com/user-attachments/assets/fc1b8b7c-7c1f-4ff5-84f8-d3b307370866)<br />
`Chicago`
- Which IP address is associated with the identified City? `23.77.86.54`
- Investigate the case2.pcap file with sumstats-counttable.zeek script. How many types of status codes are there in the given traffic capture? `4`

# Snort

### Interactive Material and VM
- Navigate to the Task-Exercises folder and run the command "./.easy.sh" and write the output <br /><br />
![image](https://github.com/user-attachments/assets/896dfce2-76d3-4bc8-a73d-e23994ba68fb) <br />
`Too Easy!` <br />

### Introduction to IDS/IPS
- Which snort mode can help you stop the threats on a local machine? `HIPS` <br />
- Which snort mode can help you detect threats on a local network? `NIDS` <br />
- Which snort mode can help you detect the threats on a local machine? `HIDS` <br />
- Which snort mode can help you stop the threats on a local network? `NIPS` <br />
- Which snort mode works similar to NIPS mode? `NBA` <br />
- According to the official description of the snort, what kind of NIPS is it? `HIPS` <br />
The answer can be found in the [official snort description](https://www.snort.org/). <br />
![image](https://github.com/user-attachments/assets/3f9478ff-ab2d-42e0-8e5e-e57843dca0bd) <br />
`full-blown`. <br />
- NBA training period is also known as ... `baselining` <br /><br />

### First Interaction with Snort
- Run the Snort instance and check the build number. <br />
![image](https://github.com/user-attachments/assets/f5464ff3-c0e2-4449-83da-619c2db3fc5e) <br />
`149` <br /><br />

- Test the current instance with "/etc/snort/snort.conf" file and check how many rules are loaded with the current build.<br /><br />
Run the following command: `sudo snort -c /etc/snort/snort.conf -T`: <br/>
![image](https://github.com/user-attachments/assets/7eeda179-dac9-4a8b-ae80-63c467a350ec)<br/>
`4151` <br />
- Test the current instance with "/etc/snort/snortv2.conf" file and check how many rules are loaded with the current build. <br /><br />
Run the following command: `sudo snort -c /etc/snort/snortv2.conf -T`: <br/>
![image](https://github.com/user-attachments/assets/0ecf2e02-d610-492e-b6a3-80bb5388d622) <br />
`1`. 

### Operation Mode 2: Packet Logger Mode
- Investigate the traffic with the default configuration file with ASCII mode. <br />
`sudo snort -dev -K ASCII -l .` <br />
Execute the traffic generator script and choose "TASK-6 Exercise". Wait until the traffic ends, then stop the Snort instance. Now analyse the output summary and answer the question. <br />
`sudo ./traffic-generator.sh` <br />
Now, you should have the logs in the current directory. Navigate to folder "145.254.160.237". What is the source port used to connect port 53? <br />
![image](https://github.com/user-attachments/assets/c96e9c36-a1bb-459c-9204-af4439bb12ab) <br />
`3009` <br />
- Use snort.log.1640048004  <br />
Read the snort.log file with Snort; what is the IP ID of the 10th packet? <br />
Move to `Exercise_Files/TASK-6` and run the command `snort -r snort.log.1640048004 -n 10`. <br />
![image](https://github.com/user-attachments/assets/5ed2b8f3-e6a3-4141-9c8b-357adcb16160) <br />
`49313` <br />

- Read the "snort.log.1640048004" file with Snort; what is the referer of the 4th packet? <br />
`Referer` is one of the fields of an HTTP header. To display the content of the packet we can add the flags `-X` or `-d`. <br />
![image](https://github.com/user-attachments/assets/7bd11b72-2152-499e-b69b-4af7486ed7b8)<br />
`http://www.ethereal.com/development.html`. <br />

- Read the "snort.log.1640048004" file with Snort; what is the Ack number of the 8th packet? <br />
![image](https://github.com/user-attachments/assets/abdd6702-27fe-48c8-a58e-f0e399128fbc)<br />
`0x38AFFFF3`<br />

- Read the "snort.log.1640048004" file with Snort; what is the number of the "TCP port 80" packets? <br />
We need to filter out every packet except the ones using TCP and port 80. The syntax is very similar when using tcpdump. The complete command is `snort -r snort.log.1640048004 'tcp and port 80'`. This will give us the answer: `41`. <br />

### Operation Mode 3: IDS/IPS
- Investigate the traffic with the default configuration file. <br />
`sudo snort -c /etc/snort/snort.conf -A full -l .` <br />
Execute the traffic generator script and choose "TASK-7 Exercise". Wait until the traffic stops, then stop the Snort instance. Now analyse the output summary and answer the question. <br />
`sudo ./traffic-generator.sh` <br />
What is the number of the detected HTTP GET methods? <br />
Press CTRL+C to stop snort and get the output: <br />
![image](https://github.com/user-attachments/assets/0b09939e-91f4-49c5-8cfa-93da819010ee)<br />
The answer is `2`. <br />

### Operation Mode 4: PCAP Investigation
- Investigate the mx-1.pcap file with the default configuration file. <br />
`sudo snort -c /etc/snort/snort.conf -A full -l . -r mx-1.pcap` <br />
What is the number of the generated alerts? <br />
![image](https://github.com/user-attachments/assets/2439760d-3733-4c3c-ac71-d0eeb7bc9fc2)<br />
`170` <br />

- Keep reading the output. How many TCP Segments are Queued? `18` <br />
- Keep reading the output. How many "HTTP response headers" were extracted? `3` <br />
- Investigate the mx-1.pcap file with the second configuration file. <br />
`sudo snort -c /etc/snort/snortv2.conf -A full -l . -r mx-1.pcap` <br />
What is the number of the generated alerts? <br />
![image](https://github.com/user-attachments/assets/6ac22de4-1e86-4adf-af16-60b667e8a77a) <br />
`68` <br />

- Investigate the mx-2.pcap file with the default configuration file. <br />
`sudo snort -c /etc/snort/snort.conf -A full -l . -r mx-2.pcap` <br />
What is the number of the generated alerts? Same process as before will lead to the answer: `340 `<br />

- Keep reading the output. What is the number of the detected TCP packets? `82` <br />

- Investigate the mx-2.pcap and mx-3.pcap files with the default configuration file. <br />
`sudo snort -c /etc/snort/snort.conf -A full -l . --pcap-list="mx-2.pcap mx-3.pcap"` <br />
What is the number of the generated alerts? <br />
![image](https://github.com/user-attachments/assets/a5bc5060-de64-49ba-813a-197dc4320246) <br />
`1020`.

### Snort Rule Structure
- Write a rule to filter IP ID "35369" and run it against the given pcap file. What is the request name of the detected packet? <br />
After adding the rule `alert tcp any any <> any any (msg:”ID Test”;id:35369;sid:10000000001; rev:1;)` to the file `/etc/snort/rules/local.rules`, run `snort -c local.rules -A full -l . -r task9.pcap` to find the answer: `TIMESTAMP REQUEST`.
- Create a rule to filter packets with Syn flag and run it against the given pcap file. What is the number of detected packets? `1` <br />
- Write a rule to filter packets with Push-Ack flags and run it against the given pcap file. What is the number of detected packets? `216` <br />
- Create a rule to filter packets with the same source and destination IP and run it against the given pcap file. What is the number of packets that show the same source and destination address? `7` <br />
- Case Example - An analyst modified an existing rule successfully. Which rule option must the analyst change after the implementation? `rev` <br />

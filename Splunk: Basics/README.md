# Splunk: Basics

### Splunk Components
- Which component is used to collect and send data over the Splunk instance? `Forwarder`

### Navigating Splunk
- In the Add Data tab, which option is used to collect data from files and ports?<br />
![image](https://github.com/user-attachments/assets/bf8c106d-e833-44ba-ae04-1a72a314ca9b)<br />
`Monitor`

### Adding Data
- Upload the data attached to this task and create an index "VPN_Logs". How many events are present in the log file?<br />
After following the steps for downloading the logs, we get a total of: <br />
![image](https://github.com/user-attachments/assets/be0bf919-fdb8-41ad-944c-7d5e3bc8934f)<br />
`2862`
- How many log events by the user Maleena are captured?<br />
On the left, click on "UserName" and select Maleena:<br />
![image](https://github.com/user-attachments/assets/cdd0023a-1d01-43e6-8340-d4de5069c332)<br />
`60`
- What is the name associated with IP 107.14.182.38?<br />
Add the following string to the query in the search bar: `Source_ip=107.14.182.38`:<br />
![image](https://github.com/user-attachments/assets/8acd47cb-72f0-46f8-bc67-41dfdba4e27e)<br />
`Smith`
- What is the number of events that originated from all countries except France?<br />
Now add `Source_Country!=France` to the query:<br />
![image](https://github.com/user-attachments/assets/406407e7-1295-400c-821e-8bb2dbed19e4)<br />
`2814`
- How many VPN Events were observed by the IP 107.3.206.58?<br />
Add `Source_ip=107.3.206.58` to the query string:<br />
![image](https://github.com/user-attachments/assets/a3903da1-27b3-40b9-ac2e-b7d546327904)<br />
`14`

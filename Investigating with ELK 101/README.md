# Investigating with ELK 101

### ElasticStack Overview
- Logstash is used to visualize the data. (yay / nay) `nay`
- Elasticstash supports all data formats apart from JSON. (yay / nay) `nay`

### Discover Tab
- Select the index vpn_connections and filter from 31st December 2021 to 2nd Feb 2022. How many hits are returned? <br />
![image](https://github.com/user-attachments/assets/bb240025-d8ca-4f43-bea6-0d720e55128f)<br />
`2861`
- Which IP address has the max number of connections?<br />
Click on "Source IP" to get the answer: <br />
![image](https://github.com/user-attachments/assets/6bfbd4df-42b5-43e1-938c-ba75d78244d2)<br />
`238.163.231.224`
- Which user is responsible for max traffic?<br />
Click on "Username".<br />
![image](https://github.com/user-attachments/assets/122d5ee8-0a94-47e5-8691-6af52fdde5c2)<br />
`James`
- Apply Filter on UserName Emanda; which SourceIP has max hits?<br />
Click on the 'plus' sign to apply the filter for the username "Emanda", then click again on Source IP: <br />
![image](https://github.com/user-attachments/assets/319c8cea-e15c-4b15-a2c7-0d037270413a)<br />
`107.14.1.247`
- On 11th Jan, which IP caused the spike observed in the time chart?<br />
Remove the Emanda filter, and filter for date=11 Jan 2021, then click on "Source IP":<br />
![image](https://github.com/user-attachments/assets/29928086-082a-4c28-915c-4ec182f7f97a)<br />
`172.201.60.191`
- How many connections were observed from IP 238.163.231.224, excluding the New York state?<br />
Add a filter "Source IP is 238.163.231.224". Then click on "Source State" and remove New York to get the answer: `48`.


### KQL Overview
- Create a search query to filter out the logs from Source_Country as the United States and show logs from User James or Albert. How many records were returned?<br />
The filter is shown in the picture below:<br />
![image](https://github.com/user-attachments/assets/57e791fb-2710-45a1-b966-4346ca575034)<br />
`161`
- As User Johny Brown was terminated on 1st January 2022, create a search query to determine how many times a VPN connection was observed after his termination.<br />
![image](https://github.com/user-attachments/assets/ae65b951-6ec0-4734-ab58-58fde0d17641)<br />
`1`

### Creating Visualizations
- Which user was observed with the greatest number of failed attempts? `Simon`
- How many wrong VPN connection attempts were observed in January? `274`


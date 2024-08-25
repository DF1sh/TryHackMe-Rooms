# NetworkMiner

### Tool Overview 1
- Use mx-3.pcap What is the total number of frames? <br />
Open `NetworkMiner.exe` and then open `mx-3.pcap.` Move to the "frame" section and scroll down to get the total number of captured frames. <br />
![image](https://github.com/user-attachments/assets/ce6dcc4d-5034-44d6-966c-b8d51d13fc9b)<br />
The total number of frames is `460`.
- How many IP addresses use the same MAC address with host 145.253.2.203? <br />
![image](https://github.com/user-attachments/assets/8736e759-4080-44ac-aa45-278323104228)<br />
Simply analyze all of these hosts and check if they are using the same MAC as the given IP address, which is `MAC: FEFF20000100 (Unknown)`.
The answer is `2`.
- How many packets were sent from host 65.208.228.223? <br />
![image](https://github.com/user-attachments/assets/719b89c0-f629-49c4-8dc2-34f7a8ab0c00)<br />
`72`.
- What is the name of the webserver banner under host 65.208.228.223? <br />
![image](https://github.com/user-attachments/assets/67957bd5-1cd1-40ed-9225-5f46e1608e95)<br />
`Apache`.
- Use mx-4.pcap What is the extracted username? <br />
Open mx-4.pcap with NetworkMiner.exe. Move to the "Credentials" section, and right-click on the first packet. Select "Copy Username": `#B\Administrator`. <br />
- What is the extracted password? <br />
Do the same thing but now select "Copy Password": `$NETNTLMv2$#B$136B077D942D9A63$FBFF3C253926907AAAAD670A9037F2A5$01010000000000000094D71AE38CD60170A8D571127AE49E00000000020004003300420001001E003000310035003600360053002D00570049004E00310036002D004900520004001E0074006800720065006500620065006500730063006F002E0063006F006D0003003E003000310035003600360073002D00770069006E00310036002D00690072002E0074006800720065006500620065006500730063006F002E0063006F006D0005001E0074006800720065006500620065006500730063006F002E0063006F006D00070008000094D71AE38CD601060004000200000008003000300000000000000000000000003000009050B30CECBEBD73F501D6A2B88286851A6E84DDFAE1211D512A6A5A72594D340A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E00360036002E0033003600000000000000000000000000`.
### Tool Overview 2
- Use mx-7.pcap What is the name of the Linux distro mentioned in the file associated with frame 63075? <br />
Open mx-7.pcap-->Files and filter for "63075". Open the file and get the answer: <br />
![image](https://github.com/user-attachments/assets/2a65e13b-a000-41e6-9c82-d2c6cc0f6366)<br />
`Centos`.
- What is the header of the page associated with frame 75942? <br />
Do the same thing as before, but with the given frame: <br />
![image](https://github.com/user-attachments/assets/a737b386-f87b-49f1-9ed2-e8ba3db80118)<br />
`Password-Ned AB`
- What is the source address of the image "ads.bmp.2E5F0FD9.bmp"? <br />
Again, type the image in the filter keyword section and click on "file details": <br />
![image](https://github.com/user-attachments/assets/be284559-6559-48d9-aa2d-cbdc62587a87)<br />
`80.239.178.187`
- What is the frame number of the possible TLS anomaly? Click on the "Anomalies" section to find out: `36255`<br />
- Use mx-9 file Look at the messages. Which platform sent a password reset email? <br />
Check the "Messages" section to find the answer: `Facebook`
- What is the email address of Branson Matheson? `branson@sandsite.org`<br />

### Version Differences
- Which version can detect duplicate MAC addresses? `2.7`
- Which version can handle frames? `1.6`
- Which version can provide more details on packet details? `1.6`

### Exercises
We should now be able to do these exercises without explicitly explaining how to do them: 
- Use case1.pcap. What is the OS name of the host 131.151.37.122? `Windows — Windows NT 4`
- Investigate the hosts 131.151.37.122 and 131.151.32.91. How many data bytes were received from host 131.151.32.91 to host 131.151.37.122 through port 1065? `192`
- Investigate the hosts 131.151.37.122 and 131.151.32.21. How many data bytes were received from host 131.151.37.122 to host 131.151.32.21 through port 143? `20769`
- What is the sequence number of frame 9? `2AD77400`
- What is the number of the detected "content types"? `2`
- Use case2.pcap. What is the USB product's brand name? `ASIX`
- What is the name of the phone model? `Lumia 535`
- What is the source IP of the fish image? `50.22.95.9`
- What is the password of the "homer.pwned.se@gmx.com"? `spring2015`
- What is the DNS Query of frame 62001? `pop.gmx.com`

<br /><br />

bye :)

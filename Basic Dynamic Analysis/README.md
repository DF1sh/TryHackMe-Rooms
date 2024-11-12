# Basic Dynamic Analysis

### Sandboxing
- If an analyst wants to analyze Linux malware, what OS should their sandbox's Virtual Machine have? `Linux`

### ProcMon
- Monitor the sample ~Desktop\Samples\1.exe using ProcMon. This sample makes a few network connections. What is the first URL on which a network connection is made?<br />
Add the following filter:<br />
![image](https://github.com/user-attachments/assets/abd3cee7-3b9f-4b68-80db-0c76788e98f8)<br />
Apply the filter and also remove every registry activity, scroll down until you find TCP connections.<br />
![image](https://github.com/user-attachments/assets/88df006c-ca0d-42c8-b782-5310de4f3870)<br />
`94-73-155-12.cizgi.net.tr:2448`
- What network operation is performed on the above-mentioned URL? `TCP Reconnect`
- What is the name with the complete full path of the first process created by this sample?<br />
![image](https://github.com/user-attachments/assets/4231b5b1-8d2e-4505-b18f-2e052dcbb378)<br />
`C:\Users\Administrator\Desktop\samples\1.exe`

### API logger and API monitor
- The sample ~Desktop\samples\1.exe creates a file in the C:\ directory. What is the name with the full path of this file?<br />
Open the sample in API logger:<br />
![image](https://github.com/user-attachments/assets/76d2ee12-2d57-49cd-960a-8af02e8dea67)<br />
`C:\myapp.exe`
- What API is used to create this file? `CreateFileA`
- In Question 1 of the previous task, we identified a URL to which a network connection was made. What API call was used to make this connection?<br />
Click on `find` and search for the string `94.73.155.12`:<br />
![image](https://github.com/user-attachments/assets/3f78d038-e119-4261-a716-9cda96eb6749)<br />
`InternetConnectW`
- We noticed in the previous task that after some time, the sample's activity slowed down such that there was not much being reported against the sample. Can you look at the API calls and see what API call might be responsible for it?
![image](https://github.com/user-attachments/assets/32ee5051-4dec-4736-b278-c80ccc19fe98)<br />
`Sleep`

### Process Explorer
- What is the name of the first Mutex created by the sample ~Desktop\samples\1.exe? If there are numbers in the name of the Mutex, replace them with X.<br />
![image](https://github.com/user-attachments/assets/bf02d69a-d662-4b64-8f0c-03651c030a79)<br />
`\Sessions\X\BaseNamedObjects\SMX:XXXX:XXX:WilStaging_XX`
- Is the file signed by a known organization? Answer with Y for Yes and N for No.<br />
![image](https://github.com/user-attachments/assets/4b7e261d-c13f-4440-aa22-d5ab818c9111)<br />
`N`
- Is the process in the memory the same as the process on disk? Answer with Y for Yes and N for No. `N`

### Regshot
- Analyze the sample ~Desktop\Samples\3.exe using Regshot. There is a registry value added that contains the path of the sample in the format HKU\S-X-X-XX-XXXXXXXXXX-XXXXXXXXXX-XXXXXXXX-XXX\. What is the path of that value after the format mentioned here?<br />
`Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store\C:\Users\Administrator\Desktop\samples\3.exe`


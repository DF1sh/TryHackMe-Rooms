# Volatility

### Practical Investigations
- What is the build version of the host machine in Case 001?<br />
Run the command `python3 vol.py -f /Scenarios/Investigations/Investigation-1.vmem windows.info`<br />
![image](https://github.com/user-attachments/assets/7bfa172d-b5e0-4463-a76e-2ab1650f03f1)<br />
`2600.xpsp.080413-2111`
- At what time was the memory file acquired in Case 001?<br />
Run the command `python3 vol.py -f /Scenarios/Investigations/Investigation-1.vmem windows.info`<br />
![image](https://github.com/user-attachments/assets/266cba38-9db8-4c76-9f02-349b5221b909)<br />
`2012-07-22 02:45:08`
- What process can be considered suspicious in Case 001? Note: Certain special characters may not be visible on the provided VM. When doing a copy-and-paste, it will still copy all characters.<br />
![image](https://github.com/user-attachments/assets/ef7114a9-3fd1-44d0-a81c-fbc99e28e7e5)<br />
`reader_sl.exe`
- What is the parent process of the suspicious process in Case 001?<br /> `explorer.exe`
- What is the PID of the suspicious process in Case 001?<br /> `1640`
- What is the parent process PID in Case 001?<br /> `1484`
- What user-agent was employed by the adversary in Case 001?<br />
Run `python3 vol.py -o /tmp -f /Scenarios/Investigations/Investigation-1.vmem windows.memmap --pid 1640 --dump`. Then run `strings /tmp/*.dmp | grep -i "user-agent"`:<br />
![image](https://github.com/user-attachments/assets/9b9f2264-ed9d-4139-86e6-93c4e2cf47e1)<br />
   `Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)`
- Was Chase Bank one of the suspicious bank domains found in Case 001? (Y/N)<br />
Run `strings /tmp/*.dmp | grep "chase"`:  `Y`
- What suspicious process is running at PID 740 in Case 002?<br />
Run ` python3 vol.py -f /Scenarios/Investigations/Investigation-2.raw windows.psscan`:<br />
![image](https://github.com/user-attachments/assets/bbcf278e-b8a0-40d0-935a-9a03aac5c387)<br />
`@WanaDecryptor@`
- What is the full path of the suspicious binary in PID 740 in Case 002?<br />
Run ` python3 vol.py -f /Scenarios/Investigations/Investigation-2.raw windows.dlllist | grep 740`:<br />
`C:\Intel\ivecuqmanpnirkt615\@WanaDecryptor@.exe`
- What is the parent process of PID 740 in Case 002?<br />
Now use the .pslist module:<br />
![image](https://github.com/user-attachments/assets/1970ac96-c933-4886-be24-514ca65f09ea)<br />
`tasksche.exe`
- What is the suspicious parent process PID connected to the decryptor in Case 002?<br /> `1940`
- From our current information, what malware is present on the system in Case 002?<br /> `Wannacry`
- What DLL is loaded by the decryptor used for socket creation in Case 002?<br /> I just looked online what is the dll used to create sockets, lul `Ws2_32.dll`
- What mutex can be found that is a known indicator of the malware in question in Case 002?<br />
Run `python3 vol.py -f /Scenarios/Investigations/Investigation-2.raw windows.handles | grep 1940`: <br />
![image](https://github.com/user-attachments/assets/c7ab51e9-6ac6-4b24-9a95-e92d9f47ba93)<br />
`MsWinZonesCacheCounterMutexA`
- What plugin could be used to identify all files loaded from the malware working directory in Case 002?<br />
`windows.filescan`

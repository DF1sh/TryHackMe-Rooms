# Introductory Researching

### Example Research Question
- In the Burp Suite Program that ships with Kali Linux, what mode would you use to manually send a request (often repeating a captured request numerous times)? <br />
No need to search for this one hehe `Repeater`. 
- What hash format are modern Windows login passwords stored in? Found it [here](https://stackoverflow.com/questions/33814568/what-hashing-algorithm-does-windows-10-use-to-store-passwords): `NTLM`
- What are automated tasks called in Linux? easy `Cron Jobs`
- What number base could you use as a shorthand for base 2 (binary)? please `Base 16`
- If a password hash starts with $6$, what format is it (Unix variant)? found it [here](https://felipe-salles.medium.com/try-hack-me-introductory-researching-d9c2daf29032) LOL `SHA512 crypt`

### Vulnerability Searching
- What is the CVE for the 2020 Cross-Site Scripting (XSS) vulnerability found in WPForms? found it [here](https://nvd.nist.gov/vuln/detail/CVE-2020-10385) `CVE-2020-10385`
- There was a Local Privilege Escalation vulnerability found in the Debian version of Apache Tomcat, back in 2016. What's the CVE for this vulnerability? found it [here](https://nvd.nist.gov/vuln/detail/CVE-2016-1240) `CVE-2016-1240` 
- What is the very first CVE found in the VLC media player? found it [here](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=VLC) `CVE-2007-0017`
- If you wanted to exploit a 2020 buffer overflow in the sudo program, which CVE would you use? found it [here](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-18634) `CVE-2019-18634`
  
### Manual Pages
- SCP is a tool used to copy files from one computer to another. What switch would you use to copy an entire directory? `-r`
- fdisk is a command used to view and alter the partitioning scheme used on your hard drive. What switch would you use to list the current partitions? `-l`
- nano is an easy-to-use text editor for Linux. There are arguably better editors (Vim, being the obvious choice); however, nano is a great one to start with. What switch would you use to make a backup when opening a file with nano? `-b`
- Netcat is a basic tool used to manually send and receive network requests. What command would you use to start netcat in listen mode, using port 12345? `nc -l -p 12345`

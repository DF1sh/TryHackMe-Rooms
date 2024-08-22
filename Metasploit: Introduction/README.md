# Metasploit: Introduction

### Main Components of Metasploit
- What is the name of the code taking advantage of a flaw on the target system? `Exploit` <br />
- What is the name of the code that runs on the target system to achieve the attacker's goal? `Payload` <br />
- What are self-contained payloads called? `Singles` <br />
- Is "windows/x64/pingback_reverse_tcp" among singles or staged payload? `Singles` <br />

### Msfconsole
- How would you search for a module related to Apache? `search apache` <br />
- Who provided the auxiliary/scanner/ssh/ssh_login module? `todb` <br />

### Working with modules
- How would you set the LPORT value to 6666? `set LPORT 6666` <br />
- How would you set the global value for RHOSTS  to 10.10.19.23 ? `setg RHOSTS 10.10.19.23` <br />
- What command would you use to clear a set payload? `unset PAYLOAD` <br />
- What command do you use to proceed with the exploitation phase? `exploit` <br />

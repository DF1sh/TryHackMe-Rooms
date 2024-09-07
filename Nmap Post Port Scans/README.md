# Nmap Post Port Scans

### Service Detection
- Start the target machine for this task and launch the AttackBox. Run nmap -sV --version-light 10.10.182.11via the AttackBox. What is the detected version for port 143? <br />
![image](https://github.com/user-attachments/assets/35f32283-de5d-40e6-861d-7e31bda97f53)<br />
`Dovecot imapd`
- Which service did not have a version detected with --version-light? `rpcbind`

### OS Detection and Traceroute
- Run nmap with -O option against 10.10.67.208. What OS did Nmap detect? `Linux`

### Nmap Scripting Engine (NSE)
- Knowing that Nmap scripts are saved in /usr/share/nmap/scripts on the AttackBox. What does the script http-robots.txt check for? <br />
![image](https://github.com/user-attachments/assets/fb4028a5-dd7f-4ac7-8993-8d01a3493013)<br />
`disallowed entries`
- Can you figure out the name for the script that checks for the remote code execution vulnerability MS15-034 (CVE2015-1635)? <br />
Found it [here](https://nmap.org/nsedoc/scripts/http-vuln-cve2015-1635.html): `http-vuln-cve2015-1635`
- Launch the AttackBox if you haven't already. After you ensure you have terminated the VM from Task 2, start the target machine for this task. On the AttackBox, run Nmap with the default scripts -sC against 10.10.89.112. You will notice that there is a service listening on port 53. What is its full version value?<br />
![image](https://github.com/user-attachments/assets/3acc765a-8354-4042-b9fc-c719843c0931)<br />
`9.18.28-1~deb12u2-Debian`
- Based on its description, the script ssh2-enum-algos “reports the number of algorithms (for encryption, compression, etc.) that the target SSH2 server offers.” What is the name of the server host key algorithm that relies on SHA2-512 and is supported by 10.10.89.112?<br />
Run `nmap 10.10.89.112 --script=ssh2-enum-algos`<br />
![image](https://github.com/user-attachments/assets/27ac2c96-b26f-403a-8c40-5e6ea59323ac)<br />
`rsa-sha2-512`

### Saving the Output
- Check the attached Nmap logs. How many systems are listening on the HTTPS port? `3`
- What is the IP address of the system listening on port 8089? `172.17.20.147`

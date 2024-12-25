# Team

### Flags
nmap shows port 21,22 and 80 open. Port 80 is a default apache web server, with a modified title: <br />
![image](https://github.com/user-attachments/assets/3af43de3-e744-4a30-9f74-e998bdf522a9)<br />
So I add team.thm to /etc/hosts. <br />
The following command enumerats virtual hosts: `gobuster vhost -u "http://10.10.131.44" --domain team.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain`
![image](https://github.com/user-attachments/assets/0378dcbf-233b-4619-85ff-15a0e87ca9eb)<br />
`dev.team.thm` is vulnerable to directory traversal: <br />
![image](https://github.com/user-attachments/assets/cdced0a2-ee87-4d6b-b1ef-bc3bbb5e9644)<br />
TO BE CONTINUED.

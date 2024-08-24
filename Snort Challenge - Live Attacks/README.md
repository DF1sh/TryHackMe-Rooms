# Snort Challenge - Live Attacks

## $\color{brown}Scenario 1|Brute-Force$

Our system  is being attacked using brute force. The goal is to figure out the attack source. First of all we start Snort in sniffer mode. To do that run the command `sudo snort -v -i eth0 -d`. <br />
![image](https://github.com/user-attachments/assets/b288c285-7dbd-42d9-96e4-341733c11b86)<br />
It seems like the IP address `10.10.245.36` is continuously sending packets to our openssh service. Let's try to block this attack; we first need to define a rule to block packets from this IP address(check out the [snort](https://github.com/Cyb3rF1sh/TryHackMe-Rooms/tree/main/Snort) room for a tutorial about snort rules). <br />
First we need to create a `local.rules` file in which we are going to define our rules. Next, the rule I used is the following:

    drop tcp any any <> any 22 (msg:"SSH Connection attempted"; sid:100001; rev:1;)
This is technically not the best rule. We are basically closing our ssh service to everyone instead of just the malicious IP. But I don't care, it works for the task :p <br />
- Stop the attack and get the flag (which will appear on your Desktop). `THM{81b7fef657f8aaa6e4e200d616738254}`
- What is the name of the service under attack? `SSH`
- What is the used protocol/port in the attack? `TCP/22`

## $\color{brown}Scenario 2 | Reverse-Shell$
As before, run `sudo snort -v -l . -i eth0` to sniff some packets. Wait 10/15 seconds, then run `sudo snort -r snort.log.1724527514 -X` to start reading and analyze packets. <br />
Apoarently, someone is communicating with a device inside our network, using port 4444: <br />
![image](https://github.com/user-attachments/assets/c5e3018a-5664-4b0c-aa3d-a7dc8826ecac)<br />
To block this, I defined the following rule

      drop tcp any any <> any 4444 (msg:"rev shell detected"; sid:100001;rev:1;)

Now run `sudo snort -c local.rules -q -Q --daq afpacket -i eth0:eth1 -A full` to block the connection. <br />
- Stop the attack and get the flag (which will appear on your Desktop) `THM{0ead8c494861079b1b74ec2380d2cd24}`
- What is the used protocol/port in the attack? `tcp/4444`
- Which tool is highly associated with this specific port number? `Metasploit` <br /><br />

bye :)
  








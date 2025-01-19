# GLITCH

### GLITCH
Nmap scan shows port 80 open. Doesn't seem to be anything interesting. But looking at the source code I found `/api/access`:<br />
![image](https://github.com/user-attachments/assets/4924230a-e49a-41af-b0a6-eb89e6e24927)<br />
This is the encoded string of `this_is_not_real`. Also, gobuster shows `/secret` directory. If I access it, it's the same as the root webpage. But if I put the token I just found in the request to access the secret, I get a different page. First intercept the request with burpsuite, then substitute the token with `this_is_not_real`:<br />
![image](https://github.com/user-attachments/assets/76e3a6e6-913c-47ae-9a7e-57d18e1cb2bb)<br />
![image](https://github.com/user-attachments/assets/0bd72afa-06eb-4584-9319-5aa9fc68e840)<br />
At this point i'm a bit stuck. I decided to look at the background image to see if there's any hidden info in it. So I run `wget http://10.10.252.148/img/rabbit.png `. Then I use `binwalk`:<br />
![image](https://github.com/user-attachments/assets/45c9f42f-7fc4-4cc3-ba9d-cf3a7199155b)<br />
It shows that at offset 0x0 there's an actual image, while at offset 0x79 there's zlib compressed data. So I run `binwalk --extract  rabbit.png`. This operation extracts a file called `79.zlib`. To decompress it, i asked chat GPT. Run `zlib-flate -uncompress < 79.zlib > decompressed_output`. <br />
Nothing there, I'm in a completely wrong track. I go back to web enumeration, and find `/api/items`!<br />
![image](https://github.com/user-attachments/assets/9fcfce3f-3e3a-45fa-860f-f4ebcb63b4bd)<br />
What the hell is that. <br /><br />
Oh wait i'm stupid. If I use the token to access the root directory of the webpage I get something different than before... I was too focused on the `/secret` directory. <br />
To make sure that I'll alywas use that token to access resources, I'll put that in "Storage" section from the developer tools: <br />
![image](https://github.com/user-attachments/assets/e38e3d33-c8ff-4075-af5e-7c1f187facb1)<br />
![image](https://github.com/user-attachments/assets/ddee6e75-bf5b-4cb9-8671-62c2838a79d3)<br />
After thinking for a while, I decided to test if I could make a POST request on the `/api/items`, to see if I could add an item. So I send the following request with burpsuite: <br />

    POST /api/items HTTP/1.1

    SNIP...
    
    Cookie: token=this_is_not_real
    
    SNIP...
    
    {
        "sin": "laziness"
    }
And I get a strange response: <br />
![image](https://github.com/user-attachments/assets/5a67dd94-1ff3-4c6f-9540-a6687965a13c)<br />
I don't know how to move on and I had to look at an external write up. I'm a clown. <br />
Basically the solution was to bruteforce the API parameters. `/api/items` is the endpoint of the API, and it can be used to get data with GET or to put data with POST. In order to get specific data, API endpoints often use parameters. To bruteforce such parameters, I use the following command: <br />
![image](https://github.com/user-attachments/assets/80e37dd6-5580-48b6-b260-9bd2b025fb62)<br />
There it is, beautiful. The payload to spawn a reverse shell for me was the following: <br />
![image](https://github.com/user-attachments/assets/bb23332a-5eef-4825-ae13-9054e112cf75)<br />
Now for privesc, `user`'s home directory contains a folder named `.firefox`, which contains the state of the firefox instance in the machine, which might also contain saved passwords for websites. To check it, first I compress the `.firefox` folder, then trasnfer it to my local machine. <br />
Then from terminal I run `firefox --profile b5w4643p.default-release`. This opens a new firefox instance with that specific profile, and it endeed contains a password: <br />
![image](https://github.com/user-attachments/assets/5fa08558-0292-4775-aa50-797d14a23c33)<br />
Now that i'm v0id I need to become root. Inside `/opt` there's a `doas` directory, which contains an executable that allows you to run commands as another user. If I look at the configuration file, I get this: <br />
![image](https://github.com/user-attachments/assets/95cb50b3-768a-48d5-a7ad-b7f61ba67c8c)<br />
So to become root, simply run: <br />
![image](https://github.com/user-attachments/assets/0ad2ea92-77cf-4de5-8d36-303bc00c5f13)<br />










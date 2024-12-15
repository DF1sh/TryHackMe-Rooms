# The Sticker Shop

### The sticker shop is finally online!
- What is the content of flag.txt?<br />
Initial scan shows port 22 and 8080 open:<br />
![image](https://github.com/user-attachments/assets/3c226334-4a0a-4938-8bc6-990b96401200)<br />
Looking at the webpage, there's a page to send customer feedback:<br />
![image](https://github.com/user-attachments/assets/18c3de7a-9635-46ff-a8da-edd3f4526399)<br />
Since the room is suggesting that the developers use the same computer for hosting the website and for looking at customer feedback, my first guess is that I need to do XSS. <br />
After some time of trying payloads, the correct one to get the flag is provided in the file named `payload` in this folder. Remember to change the script to adapt to your IP address and to first open a web server with `python3 -m http.server PORT` 


  

![image](https://github.com/user-attachments/assets/92871c0f-5ccf-454a-a8ce-392bd540f844)

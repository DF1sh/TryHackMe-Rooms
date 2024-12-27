# MD2PDF

### Challenge
Nmap shows port 22,80 and 5000 open. This is the webserver: <br />
![image](https://github.com/user-attachments/assets/769f266f-55a3-4d8c-ac76-410356ad01e6)<br />
Gobuster enumeration shows a directory /admin, which I suppose I need to access. If I try to access it, I get: <br />
![image](https://github.com/user-attachments/assets/1bc50b58-35c4-4890-8d44-23d3534363b9)<br />
Some kinds of markdown languages can include HTML. This means that I can use HTML feature of referencing an object from an external source and show it in the page. So for example if I try to convert(taken from Mr. GPT): <br />
`<iframe  src="http://localhost:5000"></iframe>`, I get the following pdf: <br />
![image](https://github.com/user-attachments/assets/12a79a2b-1d67-4d0b-bb33-f78c76530b65)<br />
This means that it's working, and to get the flag, just convert `<iframe  src="http://localhost:5000/admin"></iframe>`


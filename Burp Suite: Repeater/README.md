# Burp Suite: Repeater

### What is Repeater?
- Which sections gives us a more intuitive control over our requests? `Inspector`

### Basic Usage
- Which view will populate when sending a request from the Proxy module to Repeater? `Request`

### Message Analysis Toolbar
- Which option allows us to visualize the page as it would appear in a web browser? `Render`

### Inspector
- Which section in Inspector is specific to POST requests? `Body Parameters`

### Practical Example
- What is the flag you receive?<br />
![image](https://github.com/user-attachments/assets/4984b698-c112-48b8-ad4d-23a66fd66baf)<br />
Make sure you leave two blank lines at the bottom of the request. <br />
![image](https://github.com/user-attachments/assets/6e273218-28af-4dca-a126-aa0e5a23260f)<br />
`THM{Yzg2MWI2ZDhlYzdlNGFiZTUzZTIzMzVi}`

### Challenge
- See if you can get the server to error out with a "500 Internal Server Error" code by changing the number at the end of the request to extreme inputs. What is the flag you receive when you cause a 500 error in the endpoint?<br />
![image](https://github.com/user-attachments/assets/88634988-dcf2-44c6-b11a-d0d7fdee7f23)<br />
`THM{N2MzMzFhMTA1MmZiYjA2YWQ4M2ZmMzhl}`


### Extra-mile Challenge
- Exploit the union SQL injection vulnerability in the site. What is the flag? <br />
![image](https://github.com/user-attachments/assets/4364f46a-bf38-4e40-b20f-c757ec7e1bf5)<br />
`THM{ZGE3OTUyZGMyMzkwNjJmZjg3Mzk1NjJh}`

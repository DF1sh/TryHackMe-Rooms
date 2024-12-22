# Neighbour

### Neighbour
- Find the flag on your neighbor's logged in page!<br />
I'm presented with a login page: <br />
![image](https://github.com/user-attachments/assets/25b30e82-2ec9-4f33-88f1-c9007fc7869a)<br />
Along with guest credentials and the presence of an "admin" account, that I suppose I need to access:<br />
![image](https://github.com/user-attachments/assets/8d4d886c-9f9e-4557-b2e5-a9928fa15f8b)<br />
Gobuster dir search shows the following directories:<br />
![image](https://github.com/user-attachments/assets/f35413ef-af48-4ecf-9875-854293413ef5)<br />
When I log in with guest account, I get to this page: <br />
![image](https://github.com/user-attachments/assets/570e3c13-0d02-44ed-b93c-9f0035aeba8a)<br />
To go in the admin account, just change the URL to perform ad IDOR(Insecure Direct Object Reference) attack. An IDOR is a security vulnerability that occurs when an application provides direct access to objects based on user-supplied input. As a result, unauthorized users can access data or perform actions pertaining to other users simply by modifying a parameter value in a request:<br />
![image](https://github.com/user-attachments/assets/1af47104-db24-489c-9aff-99fbbd4620d0)<br />
`flag{66be95c478473d91a5358f2440c7af1f}`






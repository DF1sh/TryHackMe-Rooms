# Cheese CTF

### Flags

The website is about cheese: <br />
![image](https://github.com/user-attachments/assets/6570b944-15be-45be-b26f-cd57fa11a286)<br />
After moving a bit through the website and some basic enumeration, the only page that seems to be an entry point is the login page: <br />
![image](https://github.com/user-attachments/assets/3216996f-0906-4195-a5cc-c0f725089dfd)<br />
I started trying some basic SQL Injection techniques such as 'or 1=1--, but it didn't work. I even tried to use `sqlmap` but nothing, so I went back to manual enumeration. So, after one frustrating hour of trial and error, I was able to log in with the payload `' || 1=1;-- -`.<br />
The main thing that I learned with this is that, depending on the database, `||` substitutes `or`, and that it is a good practice to insert one more dash `-` to make sure that the comment symbol `--` gets parsed correctly. <br />
I am now inside an admin panel:<br />
![image](https://github.com/user-attachments/assets/7586859f-336d-46f6-8534-d2eeb665a90f)<br />
Moving a bit in the panel, some I'm noticing some strange URLs:<br />
![image](https://github.com/user-attachments/assets/dc7e0d10-0957-4fca-b619-f2d165985e53)<br />
The server is using a **PHP wrapper filter**, which is a technique used to correctly read contents of a given file, even if it is encoded somehow. 


- What is the user.txt flag? 
- What is the root.txt flag?

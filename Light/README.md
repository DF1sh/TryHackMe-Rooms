# Light

### Light
Nmap scan shows ports 22 and 1337 open. Here's how the database works:<br />
![image](https://github.com/user-attachments/assets/8260b0b8-4aeb-4327-8ed2-666eb298aa93)<br />
If I try SQL injection, it tells me that the app is filtering `/*`, `--` and `%0b`. <br />
![image](https://github.com/user-attachments/assets/547acc33-e505-4efc-9016-15f06223a5ae)<br />
Apparently it also filters `UNION`. Also `SELECT` gets filtered. After A LOT of trial and error, I finally found a clue: <br />
![image](https://github.com/user-attachments/assets/d899e684-7a2b-400d-8153-612c307fe112)<br />
If I mix uppercases and lower cases, I can bypass the filter and the server responds to me with the output of the SQL query, which in this case is an error because no `usernames` table exists. Now I'm having troubles trying to find a correct table name. Also something weird happens: <br />
If I use this payload which should bypass the filter: `' or 1=1 limit 1;` <br />
![image](https://github.com/user-attachments/assets/5f15f610-1c0f-4ac9-8a83-a9eb802247ee)<br />
Instead of responding with the output of the query, it just closes the connection. I don't know how to go on, I'll take a break and continue another time. <br />
TO BE CONTINUED...




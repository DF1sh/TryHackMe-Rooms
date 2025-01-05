# SQL Fundamentals

### Databases 101
- What type of database should you consider using if the data you're going to be storing will vary greatly in its format? `Non-relational database`
- What type of database should you consider using if the data you're going to be storing will reliably be in the same structured format? `relational database`
- In our example, once a record of a book is inserted into our "Books" table, it would be represented as a ___ in that table? `row`
- Which type of key provides a link from one table to another? `foreign key`
- which type of key ensures a record is unique within a table? `primary key`

### SQL
- What serves as an interface between a database and an end user? `DBMS`
- What query language can be used to interact with a relational database? `SQL`

### Database and Table Statements
- Using the statement you've learned to list all databases, it should reveal a database with a flag for a name; what is it?<br />
![image](https://github.com/user-attachments/assets/264cd870-8c8f-4183-93a1-87d8770593dd)<br />
`THM{575a947132312f97b30ee5aeebba629b723d30f9}`
- In the list of available databases, you should also see the  task_4_db database. Set this as your active database and list all tables in this database; what is the flag present here?<br />
![image](https://github.com/user-attachments/assets/6fc5276a-7c8a-4f36-aa06-5e957670b36d)<br />


### CRUD Operations
- Using the tools_db database, what is the name of the tool in the hacking_tools table that can be used to perform man-in-the-middle attacks on wireless networks?<br />
![image](https://github.com/user-attachments/assets/35a474ba-20c2-4666-bf3e-85f29b065f19)<br />
`Wi-Fi Pineapple`
- Using the tools_db database, what is the shared category for both USB Rubber Ducky and Bash Bunny?
`USB attacks`

### Clauses
- Using the tools_db database, what is the total number of distinct categories in the hacking_tools table?<br />
![image](https://github.com/user-attachments/assets/7cc2cb61-57cc-417f-bf32-9a6af5c4ef95)<br />
`6`
- Using the tools_db database, what is the first tool (by name) in ascending order from the hacking_tools table?<br />
![image](https://github.com/user-attachments/assets/8c00fdc8-365b-4744-9af3-7ba4aa5a2363)<br />
`Bash Bunny`
- Using the tools_db database, what is the first tool (by name) in descending order from the hacking_tools table?<br />
![image](https://github.com/user-attachments/assets/d4f0cb0a-bc11-475c-be7e-88325d9c0328)<br />
`Wi-Fi Pineapple`

### Operators
- Using the tools_db database, which tool falls under the Multi-tool category and is useful for pentesters and geeks? <br />
![image](https://github.com/user-attachments/assets/8e0a8365-9a02-4aae-9961-9cef1a2d17f9)<br />
`Flipper Zero`
- Using the tools_db database, what is the category of tools with an amount greater than or equal to 300? <br />
![image](https://github.com/user-attachments/assets/3cfce74f-0082-4677-9f70-d1f35d7f6e2b)<br />
`RFID cloning`
- Using the tools_db database, which tool falls under the Network intelligence category with an amount less than 100? <br />
![image](https://github.com/user-attachments/assets/4d768ccc-e622-4319-a31d-8c67ddf8d7cd)<br />
`Lan Turtle`

### Functions
- Using the tools_db database, what is the tool with the longest name based on character length?<br />
![image](https://github.com/user-attachments/assets/3390c6aa-3e9d-42ab-971e-090e73d0d146)<br />
`USB Rubber Ducky`
- Using the tools_db database, what is the total sum of all tools?<br />
![image](https://github.com/user-attachments/assets/64383236-fe97-4369-9b9f-1bc1e0406c67)<br />
`1444`
- Using the tools_db database, what are the tool names where the amount does not end in 0, and group the tool names concatenated by " & ".<br />
![image](https://github.com/user-attachments/assets/55d08e48-f55d-4301-a726-93e42006825c)<br />
`Flipper Zero & iCopy-XS`

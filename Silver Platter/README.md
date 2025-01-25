# Silver Platter

### Silver Platter
Nmap scan shows ports 22,80 and 8080 open. Enumerating the websites a bit, I found out that there's a silverpeas instance running on the machine. I asked chat GPT and this platform is usually located at `/silverpeas`. Infact I found a login page at `http://10.10.9.249:8080/silverpeas/defaultLogin.jsp`:<br />
![image](https://github.com/user-attachments/assets/7449b8a2-b5d0-45c5-9cfe-38d253616e0d)<br />
I also know a potential valid username by looking at the `#contact` main page: <br />
![image](https://github.com/user-attachments/assets/5feaffbf-0f5a-4153-ad89-e70d2a2f4a88)<br />
Initially I tried SQL injection with `sqlmap` but it didn't work. Next I decided to try and bruteforce the login with the user `scr1ptkiddy`. Since the description of this machine suggests that the wordlist rockyou.txt will not work, I decided to take an alternative path. <br />
I created a wordlist made of all the words that are in the main webpage, and used that wordlist for bruteforcing. To do that I used cewl: `cewl -d 3 -m 5 http://10.10.9.249 >> wordlist.txt`. Then I used hydra: `hydra -l scr1ptkiddy -P wordlist.txt 10.10.9.249 -s 8080 http-post-form "/silverpeas/AuthenticationServlet:Login=^USER^&Password=^PASS^&DomainId=0:Login or password incorrect"`. And it worked! <br />
![image](https://github.com/user-attachments/assets/048c5347-1e97-41f2-912c-1b37431167ea)<br />
After logging in, there's a notification from the manager: <br />
![image](https://github.com/user-attachments/assets/9655d928-46cf-4a99-9462-30f2b960873b)<br />
The URL of this message is `10.10.9.249:8080/silverpeas/RSILVERMAIL/jsp/ReadMessage.jsp?ID=5`. What if I change the ID from the URL? If I change the ID from 5 to 6, I get: <br />
![image](https://github.com/user-attachments/assets/25a3a8cb-fb3f-403d-9dfe-6803491f6740)<br />
This is an IDOR vulnerability. Now, for privesc, I notice that tim is part of the `adm` group. This group has access to important log files, including authentication logs inside `/var/log/`. I found a set of database credentials inside `auth.log.2` using the command `grep -iR tyler`. And I used the password to log into tyler's account with `su tyler`.<br />
Now, as tyler, if I run `sudo -l` I get: <br />
![image](https://github.com/user-attachments/assets/fbe30fde-816f-414b-8ee9-522b6303adac)<br />
So, just run `sudo su` and become root!


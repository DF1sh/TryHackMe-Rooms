# HTTP in Detail

### What is HTTP(S)?
- What does HTTP stand for? `HyperText Transfer Protocol` <br /><br />
- What does the S in HTTPS stand for? `secure` <br /><br />
- On the mock webpage on the right there is an issue, once you've found it, click on it. What is the challenge flag? `THM{INVALID_HTTP_CERT}` <br /><br />

### Requests And Responses
- What HTTP protocol is being used in the above example? `HTTP/1.1` <br /><br />
- What response header tells the browser how much data to expect? `Content-Length` <br /><br />

### HTTP Methods
- What method would be used to create a new user account? `POST` <br /><br />
- What method would be used to update your email address? `PUT` <br /><br />
- What method would be used to remove a picture you've uploaded to your account? `DELETE` <br /><br />
- What method would be used to view a news article? `GET` <br /><br />

### HTTP Status Codes
- What response code might you receive if you've created a new user or blog post article? `201` <br /><br />
- What response code might you receive if you've tried to access a page that doesn't exist? `404` <br /><br />
- What response code might you receive if the web server cannot access its database and the application crashes? `503` <br /><br />
- What response code might you receive if you try to edit your profile without logging in first? `401` <br /><br />

### Headers
- What header tells the web server what browser is being used? `User-Agent` <br /><br />
- What header tells the browser what type of data is being returned? `Content-Type` <br /><br />
- What header tells the web server which website is being requested? `Host` <br /><br />

### Cookies
- Which header is used to save cookies to your computer? `Set-Cookie` <br /><br />

### Making Requests
- Make a GET request to /room `THM{YOU'RE_IN_THE_ROOM}` <br /><br />
- Make a GET request to /blog and using the gear icon set the id parameter to 1 in the URL field `THM{YOU_FOUND_THE_BLOG}` <br /><br />
- Make a DELETE request to /user/1 `THM{USER_IS_DELETED}` <br /><br />
- Make a PUT request to /user/2 with the username parameter set to admin `THM{USER_HAS_UPDATED}` <br /><br />
- POST the username of thm and a password of letmein to /login `THM{HTTP_REQUEST_MASTER}` <br /><br />

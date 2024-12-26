# TakeOver

### Help Us
- What's the value of the flag?<br />
This challenge took me more than 1 hour to complete. The reason is that I only tried to enumerate subdomains with tools like `gobuster` or `ffuf`, and actually found the subdomains `blog` and `support`. <br />
At somepoint I even scraped all the html pages to get a list of words that I used to enumerate subdomains, but nothing. <br />
The real solution however, can be found inside the **certificate**(I knew that, it's not common for an easy CTF to use https instead of http). If I inspect the certificate information, this is what I find:<br />
![image](https://github.com/user-attachments/assets/eeb2c66f-fcd3-4639-b977-9e5ebd5d264a)<br />
This is called **Subject Alternative Names**. Essentially this field is used for **multi-domain certificates**, to reduce the complexity of a website, or for economic reasons. Infact if you look at the certificates of the other domains such as `blog.futurevera.thm` or `futurevera.thm`, they have a different certificate with respect to `support.futurevera.thm`.<br />
The **SAN** field of this last certificate specifies that the same certificate is also used for `secrethelpdesk934752.support.futurevera.thm`. <br />

So now if I visit `http://secrethelpdesk934752.support.futurevera.thm`, I get the flag:<br />
![image](https://github.com/user-attachments/assets/4941eb13-300c-4d43-a5fe-02ec5acb2839)<br />

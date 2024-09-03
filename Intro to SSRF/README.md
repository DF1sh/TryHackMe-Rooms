# Intro to SSRF

### What is an SSRF?
- What does SSRF stand for? `Server-Side Request Forgery`
- As opposed to a regular SSRF, what is the other type? `Blind`

### SSRF Examples
- What is the flag from the SSRF Examples site? <br />
For this challenge, the URL that found me the flag is `https://website.thm/item/9?server=server.website.thm/flag?id=9&x=`. <br />
![image](https://github.com/user-attachments/assets/0c2a9750-229c-40e0-acdf-91f8d8b88bee)<br />
`THM{SSRF_MASTER}`

### Finding an SSRF
- What website can be used to catch HTTP requests from a server? `requestbin.com`

### Defeating Common SSRF Defenses
- What method can be used to bypass strict rules? `Open Redirect`
- What IP address may contain sensitive data in a cloud environment? `169.254.169.254`
- What type of list is used to permit only certain input? `Allow List`
- What type of list is used to stop certain input? `Deny List`

### SSRF Practical

right-click on one of the radio buttons on the avatar form and select Inspect: <br />
![image](https://github.com/user-attachments/assets/9b26a648-cd77-4d7e-b7ff-93a0ccbcd85e)<br />
Since we want to access the /private directory, let's try to change `value=/private`. It looks like the web application has a deny list in place and has blocked access to the /private endpoint. <br />
![image](https://github.com/user-attachments/assets/ac3468a9-dca3-4072-a58b-e98089115cb6)<br />
So we can try to bypass this filter using directory traversal. Instead of setting the `value=/private`, set it as `value=x/../private`. <br /> The avatar got updated: <br />
![image](https://github.com/user-attachments/assets/808169c0-c06e-4944-9ac5-719527bfb0ea)<br />
So now if we look at the source code of the page we can see the currently set avatar now contains the contents from the /private directory in base64 encoding: <br />
![image](https://github.com/user-attachments/assets/bec09828-aa0a-4eee-9547-94a3fe1383ad)<br />
Decode it to get the flag: `THM{YOU_WORKED_OUT_THE_SSRF}`





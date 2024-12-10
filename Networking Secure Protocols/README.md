# Networking Secure Protocols

### TLS
- What is the protocol name that TLS upgraded and built upon? `SSL`
- Which type of certificates should not be used to confirm the authenticity of a server? `self-signed certificate`

### HTTPS
- How many packets did the TLS negotiation and establishment take in the Wireshark HTTPS screenshots above? `8`
- What is the number of the packet that contain the GET /login when accessing the website over HTTPS? `10`

### SMTPS, POP3S, and IMAPS
- If you capture network traffic, in which of the following protocols can you extract login credentials: SMTPS, POP3S, or IMAP? `IMAP`

### SSH
- What is the name of the open-source implementation of the SSH protocol? `OpenSSH`

### SFTP and FTPS
- Click on the View Site button to access the related site. Please follow the instructions on the site to obtain the flag. `THM{Protocols_secur3d}`

### VPN
- What would you use to connect the various company sites so that users at a remote office can access resources located within the main branch? `VPN`

### Closing Notes
- One of the packets contains login credentials. What password did the user submit?<br />
Look for a POST request. One of them is sending data in a `/login/...` directory:<br />
![image](https://github.com/user-attachments/assets/4e7c3003-8cec-4484-b6ab-0147236bf3d3)<br />
Double click on it and click on `Follow` --> `HTTP/2 Stream`:<br />
![image](https://github.com/user-attachments/assets/8591d24b-e100-46f2-b674-d753572fab78)<br />
Now take the `pass` parameter and [URL decode it](https://gchq.github.io/CyberChef/) to get the answer: `THM{B8WM6P}`




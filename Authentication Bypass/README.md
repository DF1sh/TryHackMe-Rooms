# Authentication Bypass

### Username Enumeration
- What is the username starting with si*** ? `simon`<br />
- What is the username starting with st*** ? `steve`<br />
- What is the username starting with ro**** ? `robert`<br />

### Brute Force
- What is the valid username and password (format: username/password)? `steve/thunder`<br />

### Logic Flaw
- What is the flag from Robert's support ticket? `THM{AUTH_BYPASS_COMPLETE}`<br />

### Cookie Tampering
- What is the flag from changing the plain text cookie values? `THM{COOKIE_TAMPERING}`<br />
- What is the value of the md5 hash 3b2a1053e3270077456a79192070aa78 ? `463729`<br />
- What is the base64 decoded value of VEhNe0JBU0U2NF9FTkNPRElOR30= ? `THM{BASE64_ENCODING}`<br />
- Encode the following value using base64 {"id":1,"admin":true} `eyJpZCI6MSwiYWRtaW4iOnRydWV9`<br />

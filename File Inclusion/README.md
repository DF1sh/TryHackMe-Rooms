# File Inclusion

### Path Traversal
- What function causes path traversal vulnerabilities in PHP? `file_get_contents` <br />

### Local File Inclusion - LFI
- Give Lab #1 a try to read /etc/passwd. What would the request URI be? `/lab1.php?file=/etc/passwd` <br />
- In Lab #2, what is the directory specified in the include function? `includes` <br />

### Local File Inclusion - LFI #2
- Give Lab #3 a try to read /etc/passwd. What is the request look like? `/lab3.php?file=../../../../etc/passwd%00` <br />
- Which function is causing the directory traversal in Lab #4? `file_get_contents` <br />
- Try out Lab #6 and check what is the directory that has to be in the input field? `THM-profile` <br />
- Try out Lab #6 and read /etc/os-release. What is the VERSION_ID value? `12.04` <br />

### Challenge
- Capture Flag1 at /etc/flag1 `F1x3d-iNpu7-f0rrn` <br />
- Capture Flag2 at /etc/flag2 `c00k13_i5_yuMmy1` <br />
- Capture Flag3 at /etc/flag3 `P0st_1s_w0rk1in9` <br />
- Gain RCE in Lab #Playground /playground.php with RFI to execute the hostname command. What is the output? `lfi-vm-thm-f8c5b1a78692` <br />

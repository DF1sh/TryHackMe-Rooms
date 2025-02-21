# MAL: REMnux - The Redux

### 3. Analysing Malicious PDF's
- How many types of categories of "Suspicious elements" are there in "notsuspicious.pdf"<br />
![image](https://github.com/user-attachments/assets/f1a5bfb6-7bb0-4d90-93f4-26df13cc0519)<br />
`3`
- Use peepdf to extract the javascript from "notsuspicious.pdf". What is the flag?<br />
Run the following commands:<br />
![image](https://github.com/user-attachments/assets/26ec6895-5d2d-40fd-a435-8cd88183448a)<br />
`THM{Luckily_This_Isn't_Harmful}`
- How many types of categories of "Suspicious elements" are there in "advert.pdf"<br />
Do the same thing as before: `6`
- Now use peepdf to extract the javascript from "advert.pdf". What is the value of "cName"?<br />
![image](https://github.com/user-attachments/assets/897e7038-b0a1-4fa6-8483-b3a98f0ba258)<br />
`notsuspicious`

### 4. Analysing Malicious Microsoft Office Macros
- What is the name of the Macro for "DefinitelyALegitInvoice.doc"<br />
![image](https://github.com/user-attachments/assets/870a1ec7-521e-4d5f-af56-775bbf18bf9c)<br />
`DefoLegit`
- What is the URL the Macro in "Taxes2020.doc" would try to launch?<br />
![image](https://github.com/user-attachments/assets/42cd41fb-a0e0-414f-b7b5-b189979e2707)<br />
`http://tryhackme.com/notac2cserver.sh`

### 5. I Hope You Packed Your Bags
- What is the highest file entropy a file can have? `8`
- What is the lowest file entropy a file can have? `0`
- Name a common packer that can be used for applications? `UPX`


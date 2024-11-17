### Threat Hunting With YARA

### Scenario Description
- What technique does ID T1134 describe? `Access Token Manipulation`
- What does the detection rule M_APT_Dropper_Rootsaw_Obfuscated detect? `Detects obfuscated ROOTSAW payloads`

### Opportunities for Threat Hunting
- Which threat hunting style is proactive and uses indicators of attack and TTPs? `structured hunting`
- In which phase of the threat hunting process, tools like YARA or Volatility are used? `Investigation`
- You have received a threat intelligence report consisting only of Indicators of Compromise. What threat hunting style do you recommend to use? `unstructured hunting`

### YARA: Introduction
- Apart from the rule name, which other section is also required in a YARA rule? `condition`

### YARA: Strings and Conditions
- What modifier should be used if you want to search for 2-byte encoded characters? `wide`
- What condition should be used if you want to exclude the defined strings from the matching process? `none of them`

### YARA: How To Use YARA Rules To Hunt for Indicators of Compromise
- What option do you need to pass to ensure you scan all directories recursively?<br />
Create a new .yar file with the provided rules in the task, and use it to scan the TMP folder:<br />
![image](https://github.com/user-attachments/assets/6740c025-e556-4c03-9378-36efb43618eb)<br />
`-r`

### Indicators of Compromise Detected - Now What
- What does DAIR stand for? `Dynamic Approach to Incident Response`

### YARA: Hands-on Exercise
- What is the flag found in exercise 1?<br />
The rule that worked for me is:

      rule regularExpression
              {
                  strings: 
                      $1 = "THM{"
                      
                  condition:  
                      $1
              } 

![image](https://github.com/user-attachments/assets/5ff5b373-c2ca-4d2a-bd12-8f36285edf07)<br />
![image](https://github.com/user-attachments/assets/3ea696e6-e2b8-4358-ad4b-c0837c20d437)<br />
`THM{Threathuntingisawesome}`
- What is the filename found in exercise 2? (Format: filename.extension)<br />
The rule that worked for me is:

      rule textString
          {
            strings: 
                  $1 = "Yet another" wide
                  $2 = "Ridiculous acronym" wide
                  
            condition:  
                  $1 and $2
          } 
![image](https://github.com/user-attachments/assets/6218d5de-5931-4dfc-a7d8-86aa2e3410cb)<br />
`file10.txt`

- What is the filename found in exercise 3? (Format: filename.extension)<br />
The rule that worked for me is:

      rule textString
          {
            strings: 
                  $1 = "THM{This was a really fun exercise}" base64           
            condition:  
                  $1
          }
  
![image](https://github.com/user-attachments/assets/19c1fb24-4c3a-4ee9-9fc1-1b5d09f0e59b)<br />

- What was the XOR key used for encryption in exercise 4?<br />
The rule that worked for me is:

      
      rule xorString
          {
            strings: 
                  $1 = "THM{FoundSomethingHidden}" xor 
                  
            condition:  
                  $1
          } 

![image](https://github.com/user-attachments/assets/9eab0029-e12b-4946-a7c3-b9288afbca39)<br />
`0x01`
- What encrypted string did you find in exercise 4?<br /> `UILzGntoeRnlduihofIheedo`

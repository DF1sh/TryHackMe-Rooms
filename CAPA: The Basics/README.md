# CAPA: The Basics

### Tool Overview: How CAPA Works
- What command-line option would you use if you need to check what other parameters you can use with the tool? Use the shortest format. `-h`
- What command-line options are used to find detailed information on the malware's capabilities? Use the shortest format. `-v`
- What command-line options do you use to find very verbose information about the malware's capabilities? Use the shortest format. `-vv`
- What PowerShell command will you use to read the content of a file? `Get-Content`

### Dissecting CAPA Results Part 1: General Information, MITRE and MAEC
- What is the sha256 of cryptbot.bin?<br />
![image](https://github.com/user-attachments/assets/bfa0d1f1-3f4b-4e56-8cd5-2e0b71df52ae)<br />
`ae7bc6b6f6ecb206a7b957e4bb86e0d11845c5b2d9f7a00a482bef63b567ce4c`
- What is the Technique Identifier of Obfuscated Files or Information? `T1027`
- What is the Sub-Technique Identifier of Obfuscated Files or Information::Indicator Removal from Tools? `T1027.005`
- When CAPA tags a file with this MAEC value, it indicates that it demonstrates behaviour similar to, but not limited to, Activating persistence mechanisms? `launcher`
- When CAPA tags a file with this MAEC value, it indicates that the file demonstrates behaviour similar to, but not limited to, Fetching additional payloads or resources from the internet? `Downloader`

### Dissecting CAPA Results Part 2: Malware Behavior Catalogue
- What serves as a catalogue of malware objectives and behaviours? `Malware Behavior Catalogue`
-  Which field is based on ATT&CK tactics in the context of malware behaviour? `Objective`
- What is the Identifier of "Create Process" micro-behavior? `C0017`
- What is the behaviour with an Identifier of B0009? `Virtual Machine Detection`
- Malware can be used to obfuscate data using base64 and XOR. What is the related micro-behavior for this? `Encode Data`
- Which micro-behavior refers to "Malware is capable of initiating HTTP communications"? `HTTP Communication`

### Dissecting CAPA Results Part 3: Namespaces
- Which top-level Namespace contains a set of rules specifically designed to detect behaviours, including obfuscation, packing, and anti-debugging techniques exhibited by malware to evade analysis? `anti-analysis`
- Which namespace contains rules to detect virtual machine (VM) environments? Note that this is not the TLN or Top-Level Namespace. `anti-vm/vm-detection`
- Which Top-Level Namespace contains rules related to behaviours associated with maintaining access or persistence within a compromised system? This namespace is focused on understanding how malware can establish and maintain a presence within a compromised environment, allowing it to persist and carry out malicious activities over an extended period. `persistence`
- Which namespace addresses techniques such as String Encryption, Code Obfuscation, Packing, and Anti-Debugging Tricks, which conceal or obscure the true purpose of the code? `obfuscation`
- Which Top-Level Namespace Is a staging ground for rules that are not quite polished? `Nursery`

### Dissecting CAPA Results Part 4: Capability
- What rule yaml file was matched if the Capability or rule name is check HTTP status code? `check-http-status-code.yml`
- What is the name of the Capability if the rule YAML file is reference-anti-vm-strings.yml? `reference anti-VM strings`
- Which TLN or Top-Level Namespace includes the Capability or rule name run PowerShell expression? `load-code`
- Check the conditions inside the check-for-windows-sandbox-via-registry.yml rule file from this link. What is the value of the API that ends in Ex is it looking for?<br />
![image](https://github.com/user-attachments/assets/229f2f85-3a0a-4e84-9780-8e1d9fe75605)<br />
`RegOpenKeyEx`

### More Information, more fun!
- Which parameter allows you to output the result of CAPA into a .json file? `-j`
- What tool allows you to interactively explore CAPA results in your web browser? `CAPA Web Explorer`
- Which feature of this CAPA Web Explorer allows you to filter options or results? `Global Search Box`

# Yara

### What is Yara? 
- What is the name of the base-16 numbering system that Yara can detect? `hexadecimal` <br />
- Would the text "Enter your Name" be a string in an application? (Yay/Nay) `Yay` <br />

### Using LOKI and its Yara rule set
- Scan file 1. Does Loki detect this file as suspicious/malicious or benign? <br /><br />
Move to `~/suspicious-files/file1` and run loki with the following command: `python ../../tools/Loki/loki.py -p .` <br />
This will be the output: <br>
![image](https://github.com/user-attachments/assets/50e8dfe0-448e-4192-bfa0-0cd0d8b888bc)<br />
As shown from the result of the IOC scan, we can see that the file ind3x.php is labled as `suspicious`<br><br>
- What Yara rule did it match on? `webshell_metaslsoft` <br />
- What does Loki classify this file as? `Web Shell` <br />
- Based on the output, what string within the Yara rule did it match on? `Str1` <br />
- What is the name and version of this hack tool? `b374k 2.2` <br />
The answer is inside the "FIRST_BYTES" section of the output. The reason is because the first bytes of a tool usually contains metadata about the tool itself. <br /><br />
- Inspect the actual Yara file that flagged file 1. Within this rule, how many strings are there to flag this file? <br /><br />
Move to `/tools/Loki/signature-base/yara`. In this folder there are the yara rules used by loki. In particular there's a file named `thor-webshells.yar`. If we inspect it we can find the rule that matched ind3x.php. <br />
The command `grep -A 15 "webshell_metaslsoft" thor-webshells.yar` will print out the line corresponding to the rule "webshell_metaslsoft" and the following 15 lines: <br />
![image](https://github.com/user-attachments/assets/6649e6a4-b45b-4812-8a97-cbada29a704d) <br />
As we can see, the number of string to match are just `1`. <br /><br />
- Scan file 2. Does Loki detect this file as suspicious/malicious or benign?<br />
Again, we move to `~/suspicious-files/file1` and run the command `python ../../tools/Loki/loki.py -p .`. <br />
![image](https://github.com/user-attachments/assets/67366dd7-1b64-46c0-b130-be4f284aeeda)<br />
As we can see, loki detects this file as `benign`. <br /><br />
- Inspect file 2. What is the name and version of this web shell? <br />
Again, we want to look at the first bytes of the file. Therefore, run the command `head 1ndex.php` to see the first lines. There we can find the answer: `b374k 3.2.3`<br />
### Creating Yara rules with yarGen

### Valhalla

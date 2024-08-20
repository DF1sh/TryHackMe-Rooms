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
- From within the root of the suspicious files directory, what command would you run to test Yara and your Yara rule against file 2? `yara file2.yar file2/1ndex.php` <br />
- Did Yara rule flag file 2? (Yay/Nay) `Yay` <br />
- Copy the Yara rule you created into the Loki signatures directory. `No answer needed` <br />
Run the following command: `cp file2.yar ../tools/Loki/signature-base/yara`<br /><br />
- Test the Yara rule with Loki, does it flag file 2? (Yay/Nay) `Yay` <br />
After adding this new yara rule to the list of rules used by loki, loki is now able to detect the malware. Move to /suspicious_files/file2 and run `python ../../tools/Loki/loki.py -p .`:<br />
![image](https://github.com/user-attachments/assets/c93e4ef0-e56c-47c6-be81-539be298da4f)<br />
- What is the name of the variable for the string that it matched on? `Zepto` <br />
- Inspect the Yara rule, how many strings were generated? `20` <br />
- One of the conditions to match on the Yara rule specifies file size. The file has to be less than what amount? `700KB` <br />
![image](https://github.com/user-attachments/assets/34185e4a-a80b-4b18-aa2d-a484bba4a9f2)<br />

### Valhalla
- Enter the SHA256 hash of file 1 into Valhalla. Is this file attributed to an APT group? (Yay/Nay) `Yay` <br />
- Do the same for file 2. What is the name of the first Yara rule to detect file 2? `Webshell_b374k_rule1` <br />
- Examine the information for file 2 from Virus Total (VT). The Yara Signature Match is from what scanner? `THOR APT Scanner` <br />
- Enter the SHA256 hash of file 2 into Virus Total. Did every AV detect this as malicious? (Yay/Nay) `Nay` <br />
- Besides .PHP, what other extension is recorded for this file? `EXE` <br />
- What JavaScript library is used by file 2? `Zepto` <br />
- Is this Yara rule in the default Yara file Loki uses to detect these type of hack tools? (Yay/Nay) `Nay` <br />


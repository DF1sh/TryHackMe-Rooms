# EXT Analysis

### EXT File System Structure
- What is the member of the ext4_super_block struct that holds the offset value to the first data block? `s_first_data_block`
- What is the offset where we can find the member s_blocks_count_lo in the ext4_super_block struct? (decimal format)<br />
![image](https://github.com/user-attachments/assets/ad85a454-8dd8-447b-8243-0f1216ee148f)<br />
__lee32 is 4 bytes so since it's the second element of the struct, the offset to read it is 4 bytes.
`4`

### Forensic Artifacts in EXT
- What is the inode number for the file /etc/passwd in the VM?<br />
![image](https://github.com/user-attachments/assets/288b87f7-270e-4036-a32d-753615d191c0)<br />
`10083`

### Analyzing File System Timestamps
- What is the btime for the file /etc/passwd? <br />
Look at the picture above to get the answer: `2024-11-28 21:52:28.724316576`

### Tools for EXT Forensics
- Select Data Sources > ext4_case.img_1 Host > ext4_case.img and select the file normal_file.txt. Analyze the data in the File Metadata tab on the bottom pane. What is the inode number of the file?
- What is the creation time of the file timestomped.txt? (Format: YYYY-MM-DD hh:mm:ss)

### Practical
- Identify the timestomped file in the mounted file system in /mnt/ext_exercises. What is the original creation date of the file? (Format: YYYY-MM-DD hh:mm:ss)
- What is the flag in the deleted file that starts with the characters "FFFFFFFFFF" in the mounted file system in /mnt/ext_exercises?

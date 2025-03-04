# Ninja Skills

### Ninja Skills
First I have to find the locations of these files, so I run the following bash script:

    #!/bin/bash
    
    declare -a file_names=("8V2L" "bny0" "c4ZX" "D8B3" "FHl1" "oiMO" "PFbD" "rmfX" "SRSq" "uqyw" "v2Vb" "X1Uy")
    
    search_dir="/"
    for file_name in "${file_names[@]}"; do
        
        find "$search_dir" -type f -name "$file_name" -print 2>/dev/null
    done
- Which of the above files are owned by the best-group group(enter the answer separated by spaces in alphabetical order)<br />
At this point I just ask chat GPT to write scripts for me, lol.
Mr. GTP gave me this script:

      #!/bin/bash
    
      declare -a files=("/etc/8V2L" "/mnt/c4ZX" "/mnt/D8B3" "/var/FHl1" "/opt/oiMO" "/opt/PFbD" "/media/rmfX" "/etc/ssh/SRSq" "/var/log/uqyw" "/home/v2Vb" 
      "/X1Uy")
     
      for file in "${files[@]}"; do
         
          if [ -e "$file" ]; then
           
              group_name=$(stat -c %G "$file")
            
              echo "$file belongs to group: $group_name"
          else
             
              echo "$file does not exist."
          fi
      done

`D8B3 v2Vb`
- Which of these files contain an IP address?<br />
Same thing as before:
`oiMO`
- Which file has the SHA1 hash of 9d54da7584015647ba052173b84d45e8007eba94? `c4ZX`
- Which file contains 230 lines? `bny0`
- Which file's owner has an ID of 502? `X1Uy`
- Which file is executable by everyone? `8V2L`

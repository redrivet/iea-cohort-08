#!/bin/bash

# Infrastructure Engineer Academy 
# Session 1 workshop lab - intermediate/advanced

# Write a shell script that counts all the files ending with .txt in a directory structure - 1st draft done (1workshop.sh)
# Modify the program to find all image files in a directory structure - check
# Write a shell script that find all image files created after a specific date and copies them to a new directory
# beware of edge cases

# find . -type f -exec file --mime-type {} \+ | awk -F: '{if ($2 ~/image\//) print $1}'

find . -type f -print0 | xargs -0 file --mime-type | grep -F 'image/' | cut -d ':' -f 1

# # for filename in ./*; do
#    if [[ -f "$filename" ]]; then
#        base=${filename%.*}
#        ext=${filename#"$base".}
#      mkdir -p "${ext}"
#      cp "$filename" "${ext}"
#    fi
#  done

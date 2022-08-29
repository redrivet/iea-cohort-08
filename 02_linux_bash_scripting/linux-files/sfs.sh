#!/bin/bash
echo "Search for Files"
read -r "filename"
for xfile in "$filename"; do 
	if [ -f "$xfile" ]; then echo "$xfile-nick";
		else
        		echo 'File not found'
	fi
done

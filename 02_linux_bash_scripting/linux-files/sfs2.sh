#!/bin/bash
echo "Search for Files"
read $@
for filename in "$@"; do 
	if [ -f "$@" ]; then echo "$@-nick";
		else echo 'File not found' 
	fi
read $@
for filename in "$@"; do
        if [ -f "$@" ]; then echo "$@-nick";
                else echo 'File not found' 
        fi

read $@
for filename in "$@"; do
        if [ -f "$@" ]; then echo "$@-nick";
                else echo 'File not found' 
        fi
done
done
done


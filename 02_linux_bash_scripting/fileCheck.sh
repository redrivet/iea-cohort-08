#!/bin/bash
############################### 
# 
###############################
# KL                          #
# Last Edit: 8/22/22          #
###############################

#filename=$(echo $1)
if [[ $# == 0 ]]; then
    echo "Please provide a filename or directory..."
else
    for i in "$@"; do
        if [[ ! -e $i ]]; then
            echo "$i does not exist"
            exit 2
        elif [[ ! -s $i ]] && [[ -f $i ]]; then
            echo "$i is empty; Deleting..."
            rm -f $i 
        else
            echo "File Exists..." #> /dev/null
            echo "Inspected by KL" >> $i
        fi
    done
fi
#!/bin/bash 
message="daily jupyter update from $USER@$(hostname -s) on $(date)"
git add .
echo $?
git commit -m "$message"
echo $?
git push origin devbranch
echo $?
#!/bin/bash 
message="daily jupyter update from $USER@$(hostname -s) on $(date)"
git add .
echo $? >> script.log
git commit -m "$message"
echo $? >> script.log
git push origin devbranch
echo $? >> script.log
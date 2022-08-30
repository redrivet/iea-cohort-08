#!/bin/bash 
mv script.log /home/nlawson/scriptlog_&&date
message="daily jupyter update from $USER@$(hostname -s) on $(date)"
#script.log 2>&1
git add .
echo $? > script.log
git commit -m "$message"
echo $? > script.log
git push origin devbranch
echo $? > script.log
script.log 2>&1

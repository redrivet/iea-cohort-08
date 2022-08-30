#!/bin/bash 
mv script.log /home/nlawson/scriptlog_&&date
message="daily jupyter update from $USER@$(hostname -s) on $(date)"
#script.log 2>&1
git add . >script.log 2>&1
echo $? >> script.log
git commit -m "$message"  >>script.log 2>&1
echo $? >> script.log
git push origin devbranch >>script.log 2>&1
echo $? >> script.log


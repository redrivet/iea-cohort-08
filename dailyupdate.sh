#!/bin/bash 
cp script.log /home/nlawson/script.log_$(date (+ ''%Y%m%d%s))
message="daily jupyter update from $USER@$(hostname -s) on $(date)"
#script.log 2>&1
git add . >script.log 2>&1
echo 'exit code' $? >> script.log
git commit -m "$message"  >>script.log 2>&1
echo 'exit code' $? >> script.log
git push origin devbranch >>script.log 2>&1
echo 'exit code' $? >> script.log


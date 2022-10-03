<<<<<<< HEAD
#!/bin/bash

cp script.log "/home/nlawson/scriptlog/script.log_$(date +'%Y%m%d-%H%M%S')"
message="Updated juypter on `date +'%Y-%m-%d %H:%M:%S'`"
git add . >script.log 2>&1 >> script.log
if [ $? -eq 0 ]
then 
  echo "add completed successfully"
else 
  echo 'exit code' $?
  echo "add failed, check log"
  exit 1
fi
git commit -m "$message" >> script.log
###git commit -m "Message" GIT_SUCCESS=$?
if [ $? -eq 0 ]
then 
  echo "commit completed successfully"
else 
  echo 'exit code' $? 
  echo "commit failed, check log"
  exit 1
fi
git push origin devbranch >>script.log 2>&1 >> script.log
if [ $? -eq 0 ]
then 
  echo "push completed successfully"
else 
  echo 'exit code' $?
  echo "push failed, check log"
  exit 1
fi
=======
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
>>>>>>> 03c9c69 (daily jupyter update from CORP\nlawson@a-3cpj9aewpgn6s on Tue Aug 30 14:41:16 CDT 2022)

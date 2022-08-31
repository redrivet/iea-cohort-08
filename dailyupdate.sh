#!/bin/bash 
cp script.log /home/nlawson/scriptlog/script.log_$(date+"%Y%m%d%s") 
message="Updated juypter on `date +'%Y-%m-%d %H:%M:%S'`"
git add . >script.log 2>&1; echo 'exit code' $? >> script.log
if [ $? -eq 0 ]
then 
  echo "add completed successfully"
else 
  echo "add failed, check log"
  exit 1
fi
git commit -m "$message"; echo 'exit code' $? >> script.log
if [ $? -eq 0 ]
then 
  echo "commit completed successfully"
else 
  echo "add failed, check log"
  exit 
fi
git push origin devbranch >>script.log 2>&1; echo 'exit code' $? >> script.log
if [ $? -eq 0 ]
then 
  echo "push completed successfully"
else 
  echo "add failed, check log"
  exit 1
fi

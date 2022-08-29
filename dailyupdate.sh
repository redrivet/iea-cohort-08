#!/bin/bash 
message="daily jupyter update from $USER@$(hostname -s) on $(date)"
git add .
git commit -m "$message"
git push origin devbranch
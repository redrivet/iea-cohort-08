#!/bin/bash

# Infrastructure Engineer Academy 
# Session 1 workshop lab - intermediate/advanced

# Write a shell script that counts all the files ending with .txt in a directory structure - 1st draft done (1workshop.sh)
# Modify the program to find all image files in a directory structure
# Write a shell script that find all image files created after a specific date and copies them to a new directory
# beware of edge cases

# try it without the use of 'find' first

shopt -s extglob # turns on extended pattern matching features

ls -a | grep -c './*.txt'
ls -a ./*.txt | wc -l




#!/bin/bash

# Processing command line args in a bash script
echo "The first arg is $1"
echo "All of the args ($*)"
for arg in "$*"; do
  echo $arg
done

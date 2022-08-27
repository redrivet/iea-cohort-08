#!/bin/bash

# Infrastructure Engineer Academy 
# Session 1 loop lab

# Look for input and notify if none.
if [[ -z "${1:-}" ]]; then
   printf "Nothing specified.  Include a filename as an argument.\n"
fi

# Take any number of arguments
# Report that filename does not exist
# Remove files that are empty
# Mark non-empty files as inspected

for item in "$@"; do
   if [[ ! -f "$item" ]]; then
      printf "Filename '%s$item' does not exist.\n"
   elif [[ ! -s $item ]]; then
      printf "Filename '%s$item' is an empty file and has been removed.\n"
      rm "$item"
   else 
      printf "Filename '%s$item' exists and has been inspected.\n"
      printf "\nInspected by Curtis\n" >> "$item"
   fi
done

#!/bin/env python3

""" Write a Python program which prompts the user for a filename,
    then opens that file and writes the contents of the file to
    a new file, in reverse order.
    
    fileobj = open(filename, mode)
    
    Pseudocode:
        prompt user for filename of an existing file
        open filename provided by user (read mode)
        read the file in line by line
        create a list of the lines
        reverse the list of lines
        create a new filename
        open the output file from the new filename (write/overwrite)
        loop through the list and write lines to new file
        close both files
    """

filename = input(str('Input the name of the file to be opened:   '))
input_file = open(filename, 'r')
lines = []
for line in input_file:
    lines.append(line)
input_file.close()
lines.reverse()
out_filename = filename + ".reversed"
outfile = open(out_filename, "w")
for line in lines:
    outfile.write(line)
outfile.close()
 
#!/bin/env python3

"""Print the letters of a string with a '+' between each pair of letters,
    but do not print a '+' after the final letter, i.e., 'h + e + l + l + o'
    to do this, I want you to iterate through a slice of the string which
    does not contain the last character, and then print the last character by itself
    create a list and use slicing to print the second half of the list,
    followed by the first half of the list. Once you've done this, do
    it again such that it does not print the middle item."""

start_list = ('hello')

print('+'.join(start_list))

chopped_list = ['one' 'two' 'three' 'four' 'five']

for item in chopped_list:
    print(item, sep ' ')

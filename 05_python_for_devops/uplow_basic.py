#!/bin/env python3

"""Playing with .upper, .lower, and stride.
   Alternate capital every other character,
   Every 4th character, every 5th character, etc."""

start_string = input('Please enter a string of characters:  ')

def up_low(string):
    result = ""
    first_char = False
    for char in string:
        if first_char:
            result = result + char.lower()
        else:
            result = result + char.upper()
        first_char = not first_char
    return result

print(up_low(start_string))


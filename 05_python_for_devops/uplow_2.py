#!/bin/env python3

"""Playing with .upper, .lower, and stepping.
   Alternate capital letters, iterating over
   a specified string and step length."""

start_string = input('Enter a string of letters:  ')
start_step = int(input('Choose a step value:  '))
result = ''

for index in range(0, len(start_string), start_step * 2):
    step_one = start_string[index:index+start_step].upper()
    step_two = start_string[index+start_step:index + start_step * 2].lower()
    result += step_one + step_two
print(result)

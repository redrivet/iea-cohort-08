#!/bin/env python3

"""Playing with .upper, .lower, and stride.
   Alternate capital every other character,
   Every 4th character, every 5th character, etc."""

start_string = input('Enter a string of letters:  ').lower()
start_step = int(input('Choose a step value:  '))
result = ''

#for char in start_string:


print(f'start_string is {start_string}')
#start_list = list(start_string)
#print(f'start_list is {start_list}')
step_string = (start_string[0::start_step])
print(f'step_string) is {step_string}')
#step_list = (start_list[0::start_step])
#print(f'start_list by {start_step}s is {step_list}')

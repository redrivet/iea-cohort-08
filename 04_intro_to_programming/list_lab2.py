#!/bin/env python3

"""Lab exercise for lists: Start from an empty list.  Prompt to add any
   number of words.  Enter 'stop' when done.  Output slices of the list."""

add_to_list = []
list_item = input('Enter a word to be added to the list (or stop to end): ')

if len(add_to_list) == 0:
    add_to_list[0:] = [list_item]

while len(add_to_list) != 0:
    add_to_list.append(list_item)
    if list_item == 'stop':
        print('Stopped.')
        break
    else:
        list_item = input('Enter a word to be added to the list (or stop to end): ')

sliced_list = add_to_list[1:-1]

print(f"Original list: {str(add_to_list[1:-1])}")
print(f"Sliced list 1: {str(sliced_list[0::2])}")
print(f"Sliced list 2: {str(sliced_list[1::2])}")

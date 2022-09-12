#!/bin/env python3
"""A combination of list_lab.py and list_lab2.py."""

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

list_one =  {str(add_to_list[1:-1])}
list_two =  {str(sliced_list[0::2])}
list_three = {str(sliced_list[0::2])}

print(f'\nList one: {list_one}')
print(f'List two: {list_two}')
print(f'List three: {list_three}\n')

if list_one == list_two:
    print('Lists one and two are the same.')
else:
    print('Lists one and two are not the same.')

if list_three == list_two:
    print('List three is the same as list two.\n')
else:
    print('List three is not the same as list two.\n')

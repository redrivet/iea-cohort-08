#!/bin/env python3

"""Create a list and use slicing to print the second half of the list,
   followed by the first half of the list. Once you've done this, do
   it again such that it does not print the middle item."""

list_to_add = []
list_item = input('Enter a word to be added to the list (or stop to end): ')

if len(list_to_add) == 0:
    list_to_add[0:] = [list_item]

while len(list_to_add) != 0:
    list_to_add.append(list_item)
    if list_item == 'stop':
        print('Stopped.')
        break
    else:
        list_item = input('Enter a word to be added to the list (or stop to end): ')

sliced_list = list_to_add[1:-1]
half_list = (int(len(sliced_list)/2))

print(f"Original list: {str(list_to_add[1:-1])}")
print(f"Last half of list: {str(sliced_list[half_list::])}")
print(f"First half of list: {str(sliced_list[:half_list])}")
print(f"All but the middle: {str(sliced_list[0:(half_list-1)])} {str(sliced_list[half_list::])}")

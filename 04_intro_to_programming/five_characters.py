#!/usr/bin/env python3

"""A while loop exercise that insists on 5 characters."""

while True:
    enter_five = input('Enter 5 characters: ')

    if len(enter_five) > 5:
        print(f'Sorry.  {enter_five} is too long.')
    elif len(enter_five) < 5:
        print(f'Sorry. {enter_five} is not long enough.')
    elif len(enter_five) == 5:
        print(f'Thanks.  {enter_five} is 5 characters long.')
        break

#!/usr/bin/env python3

"""An even number checker"""

check_even = int(input('Enter a number: '))
if (check_even % 2) == 0:
    print(f'{check_even} is an even number.')
else:
    print(f'{check_even} is an odd number.')

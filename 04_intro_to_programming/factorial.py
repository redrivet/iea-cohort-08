#!/usr/bin/env python3

"""A manual factorial exercise"""

my_num = int(input('Enter a positive integer:  '))
fctrl = 1

for integer in range(1, my_num + 1):
    fctrl = fctrl * integer
print(f'The factorial of {my_num} is {fctrl}.')
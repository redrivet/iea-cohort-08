#!/bin/env python3

""" Use a list comprehension to create a list of the integers
    from 1 to 100 which are not evenly divisible by 5. """

not_div_by_five = [num for num in range(1,101) if num % 5 != 0]
print(f'Numbers between 1 and 100 that are not divisible by 5:  {not_div_by_five}')

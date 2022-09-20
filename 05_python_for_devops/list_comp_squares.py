#!/bin/env python3

""" Use a list comprehension to create a list of the squares of
    integers from 1 to 25. """

squares = [x**2 for x in range(1,26)]
print(f'Sqares between 1 and 25 are:  {squares}.')

#!/bin/env python3

""" Write a function 'calculate' which is passed two operands and an
    operator and returns the calculated calculation, e.g.,
    calculate(2, 4, '+') would return 6

    * Define function that accepts 3 arguments - done
    * Perform the calculation of val1 'operator' val2 -done
    * Addtion:  handle the edge case of dividing by zero - done
"""

def calculate(val1, val2, operator):
    """ Docstring for lab calculator. """
    if operator == '+':
        calculation = val1 + val2
    if operator == '-':
        calculation = val1 - val2
    if operator == '*':
        calculation = val1 * val2
    if operator == '/':
        try:
            calculation = val1 / val2
        except ZeroDivisionError:
            print('Cannot divde by zero.')
            quit()
    return calculation

print(calculate(2, 0, '/'))

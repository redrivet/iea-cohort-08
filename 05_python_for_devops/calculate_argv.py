#!/bin/env python3

# Write a function 'calculate' which is passed two operands and an
# operator, and returns the calculated calculation, e.g.,
# calculate(2, 4, '+') would return 6

# * Define function that accepts 3 arguments - done
# * Perform the calculation of val1 'action' val2 -done
# * Addtion:  handle the edge case of dividing by zero - done

# * extend your calculator to allow 'log' as an operator
#   the second argument is the base, i.e,. calculate(49.0, 7, 'log') = log7(49.0) = 2.0
#   remember that logb(x) = loga(x)/loga(b))
#   for details see: https://docs.python.org/3/library/math.html#math.log
#   use a try/except/else block around your code that computes the log

import operator
import math

def calculate(val1, val2, action):
    """
    This is a simple calculator for the IEA labs.

    :param val1:  an operand to test arithmetic functions.
    :param val2:  the second operand.
    :param action:  symbol for the operation to be performed.
        currently supports + , - , * , /
        math.log(x[,base]) functionality to be added.
    :returns:  calculation specified by operator <action>.
    :raises: ZeroDivisionError if division by zero is attempted.
    """

    if action == '+':
        calculation = operator.add(val1, val2)
    if action == '-':
        calculation = operator.sub(val1, val2)
    if action == '*':
        calculation = operator.mul(val1, val2)
    if action == '/':
        try:
            calculation = operator.truediv(val1, val2)
        except ZeroDivisionError:
            print('Cannot divde by zero.')
            print('0')
            quit()
    #if action == 'log':
    #    calculation = math.log(val2[val1])
    return calculation

print(calculate(49.0, 7, '*'))

##########################################
#### PREVIOUSLY FUNCTIONAL CODE BELOW ####
##########################################

# def calculate(val1, val2, action):
#     """ Docstring for lab calculator. """
#     if action == '+':
#         calculation = val1 + val2
#     if action == '-':
#         calculation = val1 - val2
#     if action == '*':
#         calculation = val1 * val2
#     if action == '/':
#         try:
#             calculation = val1 / val2
#         except ZeroDivisionError:
#             print('Cannot divde by zero.')
#         finally:
#             print('0')
#             quit()
#     return calculation

# print(calculate(2, 0, '/'))

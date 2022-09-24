#!/bin/env python3

""" Use this to copy/paste stuff from other scripts that are
    not working as expected, or as a placeholder to preserve
    something that I haven't managed to break...yet. """

################################################################################


# import operator
# import math

# def calculate(val1, val2, action):
#     """
#     This is a simple calculator for the IEA labs.

#     :param val1:  an operand to test arithmetic functions.
#     :param val2:  the second operand.
#     :param action:  symbol for the operation to be performed.
#     :currently supports '+' , '-' , '*' , '/', and 'log'.
#     :returns:  calculation specified by operator <action>.
#     :raises: ZeroDivisionError if division by zero is attempted.
#     :raises:  ValueError if invalid 'log' operation is attempted.
#     """
#     calculation = ()
#     if action == '+':
#         calculation = operator.add(val1, val2)
#     if action == '-':
#         calculation = operator.sub(val1, val2)
#     if action == '*':
#         calculation = operator.mul(val1, val2)
#     if action == '/':
#         try:
#             calculation = operator.truediv(val1, val2)
#         except ZeroDivisionError:
#             print('Cannot divde by zero.')
#     if action == 'log':
#         try:
#             calculation = math.log(val1, val2)
#         except ValueError:
#             print('math.log(x,[base]) is invalid with base <= zero.')
#     return calculation

# print(calculate(49.0, 7, 'log'))

# ################################################################################

# def sumdigits(digits):
#     """ Insert commas into a string of numbers to indicate thousands etc."""
#     final_sum = int()
#     digit_list = list(str(digits))
#     for item in digit_list:
#         final_sum = final_sum + int(item)
#     if len(str(final_sum)) > 1:
#         return sumdigits(final_sum)
#     return final_sum

# print(sumdigits(750155479))

# ################################################################################

# def add_commas(number):
#     return(f'{number:,d}')
# print(add_commas(2503390971))

# ################################################################################

# start_number = int(input('Enter start number: '))

# def collatz(start_number):
#     while start_number > 1:
#         print(start_number, end = ' ')
#         if start_number % 2: # odd number
#             start_number = 3 * start_number + 1
#         else: # even number
#             start_number = start_number // 2
#     print(start_number)        

# print('Collatz Conjecture sequence: ')

# collatz(start_number)
# ################################################################################

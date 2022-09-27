#!/bin/env python3

"""
# Write a function 'calculate' which is passed two operands and an
# operator, and returns the calculated calculation, e.g.,
# calculate(2, 4, '+') would return 6
# ^^^ DONE ^^^

# Define function that accepts 3 arguments
# Perform the calculation of val1 'action' val2
# Addition:  handle the edge case of dividing by zero
# ^^^ DONE ^^^

# Extend your calculator to allow 'log' as an operator.
# Use the second argument as the base, i.e.:
# calculate(49.0, 7, 'log') = log7(49.0) = 2.0.
# Use a try/except/else block around your code that computes the log.
# ^^^ DONE ^^^

# Next lab:  turn your calculate() function into a standalone program
# which takes 3 command line arguments and invokes calculate() with those arguments

"""

import operator
import math

print("""\nThis is a simple calculator for addition, subtraction,
         multiplication, division, and log.""")
operand1 = input('Enter first number:  ')
operand2 = input('Enter second number:  ')
symbol = input("Enter an action < '+' '-' '*' '/' 'log' >  ")

def calculate(val1, val2, action):
    """
    This is a simple calculator for the labs assignment.

    :param val1:  an operand to test arithmetic functions.
    :param val2:  the second operand.
    :param action:  symbol for the operation to be performed.
    :currently supports '+' , '-' , '*' , '/', and 'log'.
    :returns:  calculation specified by operator <action>.
    :raises: ZeroDivisionError if division by zero is attempted.
    :raises:  ValueError if invalid 'log' operation is attempted.
    """
    calculation = ()
    if action == '+':
        calculation = operator.add(int(val1), int(val2))
    if action == '-':
        calculation = operator.sub(int(val1), int(val2))
    if action == '*':
        calculation = operator.mul(int(val1), int(val2))
    if action == '/':
        try:
            calculation = operator.truediv(int(val1), int(val2))
        except ZeroDivisionError:
            print('Cannot divde by zero.')
    if action == 'log':
        try:
            calculation = math.log(int(val1), int(val2))
        except ValueError:
            print('Error:  log is invalid with base <= zero.')
    return calculation

print(calculate(operand1, operand2, symbol))

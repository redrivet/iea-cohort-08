#!/usr/bin/env python3
"""
Calculate Funciton - used to calculate 2 values based on given operator.
"""
from math import log


def calculate(op1, op2, operator="+"):
    """
    Takes in two operands (op1, op2) and an operator (+, -, *, /)
    to perform a calculation. Exception for Zero Dision handled below.

    Returns answer.
    """
    try:
        int_1 = int(op1)
        int_2 = int(op2)
    except ValueError:
        print("You must enter integers for param1 and param2.")
        return None

    if operator == "-":
        answer = int_1 - int_2
    elif operator == "log":
        try:
            answer = log(int_1) / log(int_2)
        except ValueError:
            print("Cannot log 0")
            answer = None
    elif operator == "/":
        try:
            answer = int_1 / int_2
        except ZeroDivisionError:
            print("You cannot divide by 0!")
            answer = 0
    elif operator == "*":
        answer = int_1 * int_2
    elif operator == "+":
        answer = int_1 + int_2

    return answer

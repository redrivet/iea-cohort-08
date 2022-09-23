#!/bin/env python3

""" Write a function which takes a number as a parameter and returns
    a string version of the number with commas representing thousands,
    e.g., add_commas(12345) would return "12,345"
"""

def add_commas(number):
    return(f'{number:,d}')
print(add_commas(1023))

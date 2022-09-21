#!/bin/env python3

# still in progress

""" Convert an integer to a Roman numeral.
        * Request input of 4 digit integer less than 3999.
        * Refer to dictionary below and find the highest
          decimal value (v) in the dictionary that is less than or
          equal to the provided decimal number (x), and its
          corresponding Roman numeral (n).
        * Calculation: x = x - v
        * Repeat calculation until remainder is zero.
        """

romans = {'M':1000,
          'CM':900,
          'D':500,
          'CD':400,
          'C':100,
          'XC':90,
          'L':50,
          'XL':40,
          'X':10,
          'IX':9,
          'V':5,
          'IV':4,
          'I':1 }

highest = int(input('Enter a 4 digit number less than 3999:  '))
if highest >= 3999:
    print(f"You broke it.  {highest} is too high.  The Romans didn't plan for that.")
else:
    print(f'{highest} is within parameters - test stop during development.')

#def countdown_to_roman():

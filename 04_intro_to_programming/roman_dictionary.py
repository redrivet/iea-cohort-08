#!/usr/bin/env python3

"""Lab: Roman Numerals

write a program that converts Roman numerals to Arabic numerals
use a dictionary where the keys are Roman numerals and the values are Arabic numerals
M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1
for example, MDCLXVI would be 1000 + 500 + 100 + 50 + 10 + 5 + 1 = 1666

once you get that working, think about this additional wrinkle:
a smaller value precedes a larger value, then the correct thing to do
is to subtract the smaller value from the larger value
e.g., IX = 10 - 1 = 9
e.g., MCM = 1000 + (1000 - 100) = 1900

"""

roman_numerals = {
                "M" : 1000,
                "D" : 500,
                "C" : 100,
                "L" : 50,
                "X" : 10,
                "V" : 5,
                "I" : 1,
                }

to_convert = input('Enter a Roman numeral to be converted:  ').upper()

print(to_convert)
for letter in to_convert.split():
    print(roman_numerals[letter], end=' ')
    print()
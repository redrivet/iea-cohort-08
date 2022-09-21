#!/usr/bin/env python3

"""
    Lab - Roman Numerals.  Original assignment:  Write a program that
    converts Roman numerals to decimal numbers.
"""

# Instructor solution
# Given a user input in Roman numerals, convert to the equivalent Arabic numerals
# - Create a constant table of Roman Numeral values
# - Get user input string
# - Loop through the user string one character at a time
#     - Look up the value in the dictionary
#     - If there was a previous value and it was lower than the current value,
#       subtract the previous value from the current value twice, because we added it
#       on the previous iteration instead of subtracting it
#     - Otherwise, just add the current value to the total
#     - Set the previous value to the current value for the next iteration
# - Print out the total value result.
# All caps indicates a constant (unchanging) variable
ROMAN = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}
roman_string = input(str('Please enter a roman numeral string: ')).upper()
# Set total and previous value initially to zero
prev_value = 0
total = 0
# Loop through character by character
for digit in roman_string:
    # Look up the value
    value = ROMAN[digit]
    # If we had a previous value (every time but the first iteration)
    # and it was smaller than this value, that's our special case.
    # Subtract twice, because we would have added on the previous iteration.
    # Otherwise, just add our value to our total.
    if prev_value and prev_value < value:
        total += value - (2 * prev_value)
    else:
        total += value
    # Remember this value for the next iteration
    prev_value = value
print('Arabic: ', total)

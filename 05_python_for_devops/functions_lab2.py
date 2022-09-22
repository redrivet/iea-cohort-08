#!/bin/env python3

""" Write a function which takes an integer as a parameter, and sums up
    its digits. If the resulting sum contains more than 1 digit, the
    function should sum the digits again, e.g., sumdigits(1235) should
    compute the sum of 1, 2, 3, and 5 (11), then compute the sum of 1 and 1, returning 2. 
"""

def sumdigits(digits):
    final_sum = int()
    digit_list = list(str(digits))
    for item in digit_list:
        final_sum = final_sum + int(item)
    if len(str(final_sum)) > 1:
        return sumdigits(final_sum)
    return final_sum

print(sumdigits(750155479))
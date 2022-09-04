#!/usr/bin/env python3

"""Get a list of prime numbers in a range"""

lower = int(input('Enter the lower end of the range: '))
upper = int(input('Enter the upper end of the range: '))

for number in range(lower,upper):
    if number > 1:
        for item in range (2,number):
            if number % item == 0:
                break
        else:
            print(number)

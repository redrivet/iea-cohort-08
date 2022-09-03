#!/usr/bin/env python3

"""Prints a neat little multiplication table."""

for first in range(1, 11):
    # for each iteration of the outer loop, the inner loop
    # will run to completion
    for second in range(1, 11):
        #print(first * second, end=' ')
        #print('%3d' % (first * second), end=' ') # Python 2-style
        print('{:4d}'.format(first * second), end=' ')
    print()

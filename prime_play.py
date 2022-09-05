#!/bin/env python3

"""An implementation of the Sieve of Eratosthones"""

def sieve(value):
    """Returns a dictionary"""
    top  = (value + 1)
    lst = [True] * top
    for i in range(2, int(value**0.5 + 1)):
        if lst[i]:
            for j in range(i*i, top , i):
                lst[j] = False
    final = []
    for i in range(2,top ):
        if lst[i]:
            final.append(i)
    return final

print(sieve(100))

#!/bin/env python3

""" Write a function to demonstrate the Collatz Conjecture:

    for integer n > 1
        if n is odd, then n = n * 3 + 1
        if n is even, then n = n // 2
        ...will always converge to 1
    (your function should take n and keep printing new value of n until n is 1)

"""
start_number = int(input('Enter start number: '))

def collatz(start_number):
    while start_number > 1:
        print(start_number, end = ' ')
        if start_number % 2: # odd number
            start_number = 3 * start_number + 1
        else: # even number
            start_number = start_number // 2
    print(1)

print('Collatz Conjecture sequence: ')

collatz(start_number)

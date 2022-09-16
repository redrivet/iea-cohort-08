#!/bin/env python3

# Instructor solution - optimized
start = 10
stop = 30
# Optimize - we can skip every even number - none are prime (except 2)
if start % 2 == 0:
    start = start + 1
# Loop through the number we want to check for primes (only odds)
for num in range(start, stop + 1, 2):
    # Loop through the numbers that might divide into num
    # Optimize - we never have to check past half the number 
    # because the highest factor of any number is half of it.
    for factor in range(2, num // 2 + 1):
        if num % factor == 0:
            # Divides evenly - not prime!
            break
    else:
        print(num, "is a prime number.")
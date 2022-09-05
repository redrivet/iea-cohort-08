#!/usr/bin/env python3

"""A high/low guessing game."""

import random
target = random.randint(1, 100)
# print(target) # use during testing only
guess = int(input('Welcome to the guessing game.  Guess any number between 1 and 100: '))

while guess != target:
    if guess == 0:
        print('You gave up!  Closing. ')
        break
    elif guess < target:
        print(f'{guess} is too low.')
        guess = int(input('Try again.  Enter number:  '))
    elif guess > target:
        print(f'{guess} is too high.')
        guess = int(input('Try again.  Enter number:  '))
else:
    if guess == target:
        print(f'Good job!  The number was {target}.  You guessed correctly!')

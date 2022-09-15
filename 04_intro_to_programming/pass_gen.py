#!/bin/env python3

####  CAN'T GET THIS TO WORK ###
####  THE WORD LIST IS THE PROBLEM ###

"""Passphrase generator, roughly based on the EFF's diceware model."""

import secrets
# from wordlist import wordlist # NOT SURE WHAT THE HELL THIS IS

#with open('star_wars_words.txt') as file: # TRYING TO USE A FILE INSTEAD


DICE_COUNT = 5
dice_rolls = []
words = { first:12, second:13, }# HERE'S WHERE I'M STUCK

while True:
    try:
        print('According to https://www.eff.org/dice, 6 words makes a good passphrase.')
        phrase_number = int(input('Enter digit from 1 to 6 of number of words in passphrase: '))
        print(int(phrase_number))
        # val = int(phrase_number)
        if phrase_number > 0:
            break
        else:
            print("\nNegative or zero(0) not allowed.  Enter number of words:  \n")
            continue
    except ValueError:
        print("\nInput must be numeric.  Enter number of words:  \n")
        continue

for item in range(phrase_number):
    dice = ''.join(str(secrets.randbelow(6) + 1) for item in range(DICE_COUNT))
    dice_rolls.append(dice)

for i in dice_rolls:
    for key, value in words.items():
        if i == key:
            words.append(value)

print('\n- YOUR WORDS ARE -\n')
for i in words:
    print(i, end=' ')

final_passphrase = " ".join(words).replace(" ", "")

print('\n\n- YOUR PASSPHRASE IS -\n')
print(final_passphrase)
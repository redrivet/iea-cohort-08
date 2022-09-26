#!/bin/env python3

import itertools
import random

"""
Generate a deck of 108 cards for a game of UNO.
Parameters:  none
Returns a list.
"""
def build_deck():
    deck = []
    colors = ["Red", "Green", "Yellow", "Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,0,"Draw Two", "Skip", "Reverse"]
    wildcards = ["Wild", "Wild Draw Four"]
    for color in colors:
        for value in values:
            card_val = "{} {}".format(color, value)
            deck.append(card_val)
            if value != 0:
                deck.append(card_val)
    for i in range(4):
        deck.append(wildcards[0])
        deck.append(wildcards[1])
    print(deck)
    return deck

# now I need to shuffle the desk


uno_deck = build_deck()


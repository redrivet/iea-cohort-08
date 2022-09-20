#!/bin/env python3

""" Generate list from Cartesian product of three variables.
    Start with 3 lists. (color, size, sleeve).
    Use comprehension structure:
        [<element expression> <iteration> [optional filter]] """

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
sleeves = ['short', 'long']

tshirts = [[color, size, sleeve]
    for color in colors
    for size in sizes
    for sleeve in sleeves]

for combo in tshirts:
    print(combo)

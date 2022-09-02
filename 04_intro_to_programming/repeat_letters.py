#!/usr/bin/env python3

"""Asks for a string, then outputs the same string with each character repeated."""

repeat_this = input('Enter a word or string of characters: ')

how_many = 9

repeated = ''.join([character * how_many for character in repeat_this])

print(repeated)

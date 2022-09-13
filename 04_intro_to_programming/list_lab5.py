#!/bin/env python3

"""Create a list and use slicing to print every other word starting
   from the first, followed by every other remaining word."""

word_list = []
while True:
    word = input("Enter a word, type quit to stop:  ")
    if word == "quit":
        break
    word_list.append(word)
print(word_list[::2])
print(word_list[1::2])

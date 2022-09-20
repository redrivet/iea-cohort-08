#!/bin/env python3

""" Generate list from Cartesian product of two variables.
    Start with 3 lists. (color, size, sleeve).
    Use comprehension structure:
        [<element expression> <iteration> [optional filter]]
    Example with two lists:
        colors = ['black', 'white']
        sizes = ['S', 'M', 'L']
        tshirts = [[color, size] for color in colors for size in sizes]
        tshirts """

# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# sleeves = ['short', 'long']

# tshirts = [[color, size, sleeve]
#     for color in colors
#     for size in sizes
#     for sleeve in sleeves]

# for combo in tshirts:
#     print(combo)

#here is a draft of the 'not ending in vowels' portion of the lab
list_of_words = ['blah', 'whatever', 'hello', 'dingle']
no_end_vowel = [word for word in list_of_words if word[-1] not in 'aeiou']
print(no_end_vowel)

# here is the squares portion of the lab
# squares = [num**2 for num in range(1,26)]
# print(squares)

#here is the not divisible by five portion of the lab
div_by_five = [num for num in range(1,101) if num % 5 != 0]
print(div_by_five)
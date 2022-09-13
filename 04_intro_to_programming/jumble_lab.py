#!/bin/env python3

# UNFINISHED

"""Lab: Jumble (Word Scrambling)
   Write a program which presents you with a scrambled word and you
   have to come up with the correctly spelled word.  You can use the
   random module for this.
   random.choice(container) will return a random item from the container
   random.shuffle(container) will shuffle a container so the items are scrambled
   you can't shuffle a string, so you'll need to put the characters into
   a list using the list() function, then shuffle the list, then put them
   back into a string using join()."""

import random

dummy_list = list(random.choice(['cohort', 'engineer', 'academy', 'eight']))
#selected_word = (random.choice(dummy_list))
print(''.join(dummy_list))

# rand_word = list(random.choice(['Pizza','Apple','Earth','World']))
# random.shuffle(rand_word)
# print('' .join(rand_word))

# jumble = ''.join(random.sample(word, k=len(word)))

# while True:
#     print('\nThe Jumble is:', jumble)
#     guess = input('Your Guess: ')
#     if guess == word:
#         print("\nThat's it! You guessed it!\n")
#         print('Thanks for playing')
#         break

#     print("Sorry, that's not it")

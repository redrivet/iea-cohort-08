#!/bin/env python3

""" Given a list of words, create a second list which contains
    all the words from the first list which do NOT end with a vowel. """

list_of_words = ['blah', 'whatever', 'hello', 'dingle', 'phone', 'mouse', 'test']
not_end_vowel = [word for word in list_of_words if word[-1] not in 'aeiou']
end_vowel = [word for word in list_of_words if word[-1] in 'aeiou']
print(f'Given list of words:  {list_of_words}')
print(f'Words that do not end with a vowel: {not_end_vowel}')
print(f'Words that end with a vowel:  {end_vowel}')

#!/bin/env python3

user_string = input("Please enter a phrase: ").lower()
user_stride = int(input("Please select a stride number(less than 10 is ideal): ")) # make sure int is input
new_string = ""
count = 0
#print(user_string) # test print to make sure string is being lowered
for character in user_string:
    if count < user_stride:
        new_string += character.upper()
        count += 1
    elif (count >= user_stride) and (count <  2 * user_stride):
        new_string += character.lower()
        count += 1
        if count == 2 * user_stride:
            count = 0
print(new_string)
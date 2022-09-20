#!/usr/bin/env python3

user_string = input('Please enter a string: ').upper()
stride = int(input('Please enter a stride: '))
count = 0
user_list = []
new_list = []

for c in user_string:
    user_list.append(c)

while count < len(user_string):
    char_set = user_list[:stride]
    if count % 2 != 0:
        for x in char_set:
            new_list.append(x.lower())
    else:
        new_list.append(''.join(char_set))

    del user_list[:stride]
    count += 1

print(''.join(new_list))

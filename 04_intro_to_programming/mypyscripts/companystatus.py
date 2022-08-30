#!/bin/python3

company = "My company"

status = " hired me"

quantity = 5

NewQuantity = input('How long ago were you hired? ')
print('You entered', NewQuantity)
print(company + status + ' ' + str(quantity) + ' years ago.')
print('Wow, we were hired ' + str(int(quantity) - int(NewQuantity)) + ' ' + 'years apart' )

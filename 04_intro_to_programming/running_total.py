#!/usr/bin/env python3

"""Keep adding numbers until user enters a 0.
   CR added a line to keep track of total."""

total = 0

while True: # (JR) infinite loop, so we must have a 'break' somewhere in the loop
    num = int(input('Enter a number: '))
    total += num
    # print((f'Current total --> {total}.  '),end='', sep='') # CR's addition
    if num == 0:
        break

print(total)

# keep adding numbers until user enters a 0

total = 0

while True: # infinite loop, so we must have a 'break' somewhere in the loop
    num = int(input('Enter a number: '))
    total += num
    print(f'Current total ---> {total}',end='', sep='')
    if num == 0:
        break

print(total)

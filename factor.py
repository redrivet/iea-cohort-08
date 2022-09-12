entryno = int(input("Enter a number: "))
factor = 1
for x in range(1,entryno+1):
    factor = factor * x

print(f'the factorial of {entryno} is {factor}')

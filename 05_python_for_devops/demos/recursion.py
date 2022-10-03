def factorial_iterative(num):
    total = 1
    for i in range(num, 0, -1):
        total *= i
    return total


def factorial_recursive(num):
    return 1 if num == 1 else num * factorial_recursive(num - 1)


for num in [5, 7, 21, 43, 256]:
    #i = factorial_iterative(num)
    #print("Number:", num, "Iterative:", i)
    r = factorial_recursive(num)
    print("Number:", num, "Recursive:", r)

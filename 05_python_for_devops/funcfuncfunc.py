#!/usr/bin/env python3

def calculate(op1, op2, operator='+'):
    """
    Takes in two operands (op1, op2) and an operator (+, -, *, /)
    to perform a calculation.

    Returns answer.
    """

    int_1 = int(op1)
    int_2 = int(op2)

    if operator == '-':
        answer = int_1 - int_2
    elif operator == '/':
        answer = int_1 / int_2
    elif operator == '*':
        answer = int_1 * int_2
    elif operator == '+':
        answer = int_1 + int_2

    return answer

# answ = calculate(2, 5, '/')
# print(answ)


def collatz(n):
    """
    This will perform the Collatz Conjecture:

    for integer n > 1
     - if n is even, then n = n // 2
     - if n is odd, then n = n * 3 + 1

     This will continue to loop until number is equal to 1 then breaks.
    """
    number = int(n)
    print(f'Starting at: {number}')
    if number > 1:
        while True:
            if number % 2 == 0:
                number = number // 2
                print(('-' * 12), number)
                if number == 1:
                    break
            else:
                number = (number * 3) + 1
                print(('-' * 12), number)
                if number == 1:
                    break
    else:
        print('Please enter a number that is greater than 1...')

#collatz(23)


def sumdigits(num):
    """
    Takes int and sums up it's digits: 1235 = 1 + 2 + 3 + 5 = 11,
        11 = 1 + 1 = 2

    This should repeat until the remaining answer is only a single digit.
    """
    num_list = [int(n) for n in str(num)]
    ans = sum(num_list)

    if ans > 9:
        return sumdigits(ans)
    else:
        return ans
        
digits = 1234567
digit_sum = sumdigits(digits)
print(f'The Sum of: {digits} is... \n {digit_sum}')


def add_comas(n):
    """
    Takes number as input (n) and should return a formatted string
    with commas in the correct location e.g. 12345 = 12,345
    """
    number_list = [str(number) for number in str(n)]

    if len(number_list) > 3:
        number_list.reverse()
        index = 3
        while index < len(number_list):
            number_list.insert(index, ',')
            index += 4
        number_list.reverse()
        return(''.join(number_list))
    else:
        print('no commas needed')
        return ''.join(number_list)

# with_comas = add_comas(1234578)
# print(with_comas)

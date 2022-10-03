def fizzbuzz(num):
    """Returns 'fizz' for multiples of 3,
       'buzz' for multiples of 5,
       'fizzbuzz' for multiples of both,
       or returns the number passed."""
    result = ''
    if num % 3 == 0:
        result += 'fizz'
    if num % 5 == 0:
        result += 'buzz'
    result = result or num
    return result

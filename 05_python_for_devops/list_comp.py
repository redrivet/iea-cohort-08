colors = ["black", "white"]
sizes = ["S", "M", "L"]
sleeves = ["short", "long"]
tshirts = [
    [color, size, sleeve] for color in colors for size in sizes for sleeve in sleeves
]
print(tshirts)
print(("\n"), ("+" * 20), ("\n"))

# All numbers divisible by 5 from 0 - 100
divisible = [number for number in range(0, 101) if number % 5 != 0]
print(divisible)
print(("\n"), ("+" * 20), ("\n"))

# Squares of numbers from 0 - 25S
squares = [number**2 for number in range(0, 26)]
print(squares)
print(("\n"), ("+" * 20), ("\n"))

# All words that do _not_ end in a vowel from a given list
words = ["one", "two", "three", "four", "five", "six"]
non_vowels = [word for word in words if word[-1] not in "aeiou"]

print(non_vowels)
print(("\n"), ("+" * 20), ("\n"))

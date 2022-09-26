#!/usr/bin/env python3
import sys
from calc import calculate

num1 = sys.argv[1]
num2 = sys.argv[2]
op = sys.argv[3]
answ = calculate(num1, num2, op)
print(answ)

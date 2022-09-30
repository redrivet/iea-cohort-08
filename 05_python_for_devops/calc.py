#!/usr/bin/env python3
#%%bash
# Processing command line args in a bash script
#echo "The first arg is $1"
#echo "input intergers and operator +,-,/, or *"
#from calc import calc
import sys
#if len(sys.argv > 1:
#    name = sys.argv[1]
x1 = sys.argv[1]
x2 = sys.argv[2]
oper = sys.argv[3]
#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])
print('Program arguments', sys.argv)
def caculate(x1,x2,oper):
     
    try:
        result = None
        oper = input('enter operator: +-/*:')
        if oper == '+':
            result = x1 + x2
        elif oper == '-':
            result = x1 - x2
        elif oper == '/':
            result = x1 / x2
        elif oper == '*':
            result = x1 * x2
    
    except ZeroDivisionError:
        print('you cant do this try again')
        return
        
        
    return result
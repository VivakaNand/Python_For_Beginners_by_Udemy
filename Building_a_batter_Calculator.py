# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 02:51:45 2019

@author: VIVEK VISHAN
"""

# Building a batter Calculator
num1 = float(input("Enter first number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")  
    
    

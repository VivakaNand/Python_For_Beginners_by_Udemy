# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 02:50:24 2019

@author: VIVEK VISHAN
"""

# If Statement
is_male = True

if is_male:
    print("You are a male")
else:
    print("You are not a male")



is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")
    

is_male = True
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")
      

is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a male")
else:
    print("You are neither not male nor tall or both")


is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a male")
else:
    print("You are neither not male nor tall or both")
    
    
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")



# If Statements & Compairisions

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3 

print(max_num(3, 4, 5))   

print(max_num(30, 40, 5))



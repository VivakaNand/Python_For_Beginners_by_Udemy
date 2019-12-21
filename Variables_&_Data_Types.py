# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 02:40:12 2019

@author: VIVEK VISHAN
"""

# Variables & Data Types
character_name = "Tom"
character_age = "35"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")
character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didin't like being " + character_age + ".")

# Working with Strings
phrase = "Giraffe Acadmey"
print(phrase)
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3])
print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Elephent"))


# Working with Numbers
print(2 * (4 + 6))
print(10 % 3)

my_num = -5
print((my_num))
print(abs(my_num))
print(pow(4, 6))
print(round(3.7))

from math import* 

print(sqrt(36))



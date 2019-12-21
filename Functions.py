# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 02:48:03 2019

@author: VIVEK VISHAN
"""

#Functions

def say_hi():
    print("Hello User")
    
say_hi()
   


def say_hi():
    print("Hello User")
    
print("Top")
say_hi()
print("Bottom") 


def say_hi(name):
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")
say_hi("Vivek")


def say_hi(name, age):
    print("Hello " + name + ", You are " + age)

say_hi("Mike", "23")
say_hi("Steve", "22")
say_hi("Vivek", "24")




def say_hi(name, age):
    print("Hello " + name + ", You are " + str(age))

say_hi("Mike", 23)
say_hi("Steve", 22)
say_hi("Vivek", 24)



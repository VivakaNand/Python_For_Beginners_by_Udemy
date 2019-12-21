# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 02:55:13 2019

@author: VIVEK VISHAN
"""

# For Loop
for letter in "Giraffe Academy":
    print(letter)
    

friends = ['Jim','Karen','Kevin']    
for friend in friends:
    print(friend)    


for index in range(10):
    print(index) 
    

    
for index in range(3,10):
    print(index)
    
    
friends = ['Jim','Karen','Kevin']   
for index in range(len(friends)):
    print(friends[index])     
    
    
for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")
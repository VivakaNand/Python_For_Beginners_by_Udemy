# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 02:55:48 2019

@author: VIVEK VISHAN
"""

# 2D lists & Nasted Loops
number_grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
        ]
print(number_grid[3][0])



number_grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
        ]
for row in number_grid:
    print(row)
    
    

number_grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
        ]
for row in number_grid:
    for col in row:
        print(col)
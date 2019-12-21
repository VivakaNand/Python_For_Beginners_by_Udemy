# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 02:55:51 2019

@author: VIVEK VISHAN
"""

# Reading a File
employee_file = open("employees.txt", "r")
print(employee_file.readable())
employee_file.close()  



employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()   



employee_file = open("employees.txt", "r")
print(employee_file.readline())
employee_file.close()




employee_file = open("employees.txt", "r")
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
employee_file.close() 


employee_file = open("employees.txt", "r")
print(employee_file.readlines())
employee_file.close()



employee_file = open("employees.txt", "r")
print(employee_file.readlines()[1])
employee_file.close()



employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
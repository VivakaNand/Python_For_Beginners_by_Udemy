# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 03:00:21 2019

@author: VIVEK VISHAN
"""


# Writing to Files

#append string
employee_file = open("employees.txt", "a")
employee_file.write("\nKelly - Customer Services")
employee_file.close()

#overwrite string
employee_file = open("employees.txt", "w")
employee_file.write("Kelly - Customer Services")
employee_file.close()


#writing to html file
employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()

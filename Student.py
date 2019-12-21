# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:23:06 2019

@author: VIVEK VISHAN
"""

class Student:
    
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa 
        
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        
    
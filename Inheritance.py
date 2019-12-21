# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 03:04:20 2019

@author: VIVEK VISHAN
"""

# Inheritance
from Chef import Chef

myChef = Chef()
myChef.make_special_dish()
myChef.make_chicken()
myChef.make_salad()


from ChineseChef import ChineseChef

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()


from ChineseChef import ChineseChef
myChineseChef.make_chicken()
myChineseChef.make_salad()
myChineseChef.make_special_dish()
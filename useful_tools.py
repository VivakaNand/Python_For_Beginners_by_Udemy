# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:50:54 2019

@author: VIVEK VISHAN
"""

import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["Johan Lennon","Paul McCartney","George Harrison","Ringo Star"]


def get_file_ext(filename):
    return filename(filename.index(".") + 1)


def roll_dice(num):
    return random.randint(1,num)
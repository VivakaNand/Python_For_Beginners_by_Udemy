# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 02:52:29 2019

@author: VIVEK VISHAN
"""

#Dictionaries
monthConversion = {
        "Jan":"January",
        "Feb":"Faburary",
        "Mar":"March",
        "Apr":"April",
        "May":"May",
        "Jun":"June",
        "Jul":"July",
        "Aug":"August",
        "Sep":"Septumber",
        "Oct":"October",
        "Nov":"November",
        "Dec":"December",        
        }
print(monthConversion['Dec']) 

print(monthConversion['Nov']) 

print(monthConversion['Mar'])  

print(monthConversion.get("Dec")) 

print(monthConversion.get("Mar")) 

print(monthConversion.get("Oct")) 

print(monthConversion.get("lvu", "Not a walid key"))   




monthConversion = {
        1:"January",
        2:"Faburary",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"Septumber",
        10:"October",
        11:"November",
        12:"December",        
        }
print(monthConversion[2]) 

print(monthConversion[3]) 

print(monthConversion[7]) 


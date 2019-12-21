# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 02:45:28 2019

@author: VIVEK VISHAN
"""

# Lists

friends = ["Raja","Vivek","Mahesh","Vikesh"]
print(friends)

friends = ["Raja","Vivek","Mahesh","Vikesh","sanjay"]
print(friends[1:])

friends = ["Raja","Vivek","Mahesh","Vikesh","sanjay"]
friends[1] = "Mike"
print(friends[:])


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Raja","Vivek","Mahesh","Vikesh","sanjay"]
friends.extend(lucky_numbers)
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Raja","Vivek","Mahesh","Vikesh","sanjay"]
friends.append("Viko")
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Raja","Vivek","Mahesh","Vikesh","sanjay"]
friends.insert(3,"Vikram")
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Raja","Vivek","Mahesh","Vikesh","sanjay"]
friends.remove("Raja")
print(friends)



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Raja","Vivek","Mahesh","Vikesh","sanjay"]
friends.clear()
print(friends)



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Raja","Vivek","Mahesh","Vikesh","sanjay"]
friends.pop()
print(friends)



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Raja","Vivek","Mahesh","Vikesh","sanjay"]
print(friends.index("Mahesh"))


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Raja","Vivek","Vivek","Mahesh","Vikesh","sanjay"]
print(friends.count("Vivek"))



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Raja","Vivek","Vivek","Mahesh","Vikesh","sanjay"]
friends.sort()
print(friends)


lucky_numbers = [14, 8, 5, 16, 23, 42]
friends = ["Raja","Vivek","Vivek","Mahesh","Vikesh","sanjay"]
lucky_numbers.sort()
print(lucky_numbers)


lucky_numbers = [42, 8, 15, 16, 23]
friends = ["Raja","Vivek","Vivek","Mahesh","Vikesh","sanjay"]
lucky_numbers.reverse()
print(lucky_numbers)


lucky_numbers = [42, 8, 15, 16, 23]
friends = ["Raja","Vivek","Vivek","Mahesh","Vikesh","sanjay"]
friends2 = friends.copy()
print(friends2)

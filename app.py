# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 21:30:27 2019

@author: VIVEK VISHAN
"""

print("Hello World")


print("   /|")
print("  / |")
print(" /  |")
print("/___|")


print("/___|")
print("   /|")
print("  / |")
print(" /  |")


# Variables & Data Types
character_name = "Tom"
character_age = "35"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")
character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didin't like being " + character_age + ".")

# Working with Strings
phrase = "Giraffe Acadmey"
print(phrase)
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3])
print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Elephent"))


# Working with Numbers
print(2 * (4 + 6))
print(10 % 3)

my_num = -5
print((my_num))
print(abs(my_num))
print(pow(4, 6))
print(round(3.7))

from math import* 

print(sqrt(36))


# Getting input from Users
name = input("Enter your name:")
print("Helllo " + name + "!")

name = input("Enter your name:")
age = input("Enter your age:")
print("Helllo " + name + "! You are " + age)



#Building Basic Calculator
num1 =int(input("Enter a number: "))
num2 =int(input("Enter another number: "))
result = num1 + num2
print(result)



#Building Basic Calculator
num1 =float(input("Enter a number: "))
num2 =float(input("Enter another number: "))
result = num1 + num2
print(result)


color =input("Enter a color: ")
plural_noun =input("Enter a Plural Noun: ")
celebrity =input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)


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


#Tuples
coordinates = (3, 4, 5)
print(coordinates[1])


coordinates = (3, 4, 5)
#coordinates[1] = 10
print(coordinates[1])

coordinates =[(3, 4),(6,7),(80,34)]
print(coordinates)


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



# Return Statement

def cube(num):
    num*num*num

print(cube(3))



def cube(num):
    return num*num*num

print(cube(3))

print(cube(4))

result = cube(4)
print(result)


# If Statement
is_male = True

if is_male:
    print("You are a male")
else:
    print("You are not a male")



is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")
    

is_male = True
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")
      

is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a male")
else:
    print("You are neither not male nor tall or both")


is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a male")
else:
    print("You are neither not male nor tall or both")
    
    
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")



# If Statements & Compairisions

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3 

print(max_num(3, 4, 5))   

print(max_num(30, 40, 5))


# Building a batter Calculator
num1 = float(input("Enter first number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")  
    
    
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



# While loop

i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")


#Building a Guessing Game
secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter guess : ")
print("You win!")  



secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")   
      
    


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



# Exponent Fuction
print(2**3)    


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(2,3))    

print(raise_to_power(4,3))    



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



# Build a Translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: "))) 


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
  



def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))     



# Comments
# This program is cool
# this prints out string
print("Comments are fun")

# multiple lines comment
"""
This is python beginner course

i love python 

I love coding
""" 



# Try Except
number = int(input("Enter a number: "))
print(number)



try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")




try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")       
except ValueError:
    print("Invalid Input")    
    


try:
    answer = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)       
except ValueError:
    print("Invalid Input")      
    
   
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



# Modules & pip
import useful_tools

print(useful_tools.roll_dice(10))

print(useful_tools.feet_in_mile)



import docx

docx.




# Classes & Objects
from Student import Student

student1 = Student("Vivek","Engineering",3.2, False)
print(student1.gpa)


student1 = Student("Vivek","Engineering",3.2, False)
student2 = Student("Jim","Business",3.0, True)
print(student1.gpa)
print(student2.gpa)



#Building a Multiple Choice Quiz
from Question import Question

question_prompt = [
        "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
        "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
        "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
        Question(question_prompt[0],"a"),
        Question(question_prompt[1],"c"),
        Question(question_prompt[2],"b"),
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)      



# Object Functions
from Student import Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())  



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


# Python Interpreter





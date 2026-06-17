#        ##########
#        #
#        #
#        #
###################
         #        #
         #        #
         #        #
##########        #






'''
print("")

import random
random.randint(1, 100)

int()
float()

append()

input()

.islower()
.isdigit()
.isupper()
# How to define a function
def hello():
    print("Hello, how are you?")

# call the fuction
hello()

# function with a parameter
def greet(yournameasddsa, myname):
    print(f"Hello {yournameasddsa}, how are you?")
    print(f"My name is {myname}")

greet("Peter File", "Ben Dover")
'''

### imagine a scenario

# area of 5 rectangle

# rect 1 = 65, 89
# rect 2 = 75, 12
# rect 3 = 4, 75
# rect 4 = 78, 36
# rect 5 = 14, 89

#calculate the total area of all these 5 rectangles
'''
def area_rectangle(length, breadth):
    area = length * breadth
    
    return area # return this value back

rect1 = area_rectangle(65, 89)
rect2 = area_rectangle(75, 12)
rect3 = area_rectangle(4, 75)
rect4 = area_rectangle(78, 36)
rect5 = area_rectangle(14, 89)

total = rect1 + rect2 + rect3 + rect4 + rect5
print(total)
'''




# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.


# Test the function with multiple operations.
# print(calculator(10, 5, "+"))
# print(calculator(10, 5, "-"))
# print(calculator(10, 5, "*"))
# print(calculator(10, 5, "/"))

# def calculator(num1, num2, operation):
#     if operation == "+":
#         answer = num1 + num2
#     elif operation == "-":
#         answer = num1 - num2
#     elif operation == "*":
#         answer = num1 * num2
#     elif operation == "/":
#         answer = num1 / num2
#     else:
#         answer = "Invalid operator"
#     return answer

# num1 = int(input("Input first number: "))
# num2 = int(input("Input second number: "))
# operation = input("Enter operation (+, -, *, /): ")#

# answer = calculator(num1, num2, operation)
# print(f"{num1} {operation} {num2} = {answer}")

##################################################################################################3

# define a function to say hello
# def hello():
#     print(hello)

# #call the fucntion
# hello()

# def gretting(yourname): #parameter- vairalbe used inside function
#     print(f"Hello,{yourname}")

# #call the greeting function
# gretting("Kenneth")
### return
#calc teh area of a circle)
# import math
# def area_circle(radius):
#     area = math.pi * radius**2

#     print(area)
# #################################################
# #calculate the total area ofn all the balls
# radiuslist = [3.9, 63.6, 68.4, 96.5, 44.8]
# total_area = 0

# for circle in radiuslist:
#     current = area_circle(circle)
#     total_area += current
# print(total_area)

############################################################################
users = ["Alice", "Bob", "Charlie"]


def greet_users(user_list):
    for name in user_list:
        print(f"Hello {name}")
#call
greet_users(users)





#------------------------------------------------------------
# Exercise 6: Test Grade
# A teacher wants to assign a grade based on a student's mark.
#
# Write a function get_grade(mark) that returns:
# "A" if mark is 75 or above
# "B" if mark is from 60 to 74
# "C" if mark is from 50 to 59
# "D" if mark is below 50
#
# Then call the function and print the returned grade.
#
# Example function call:
# grade = get_grade(68)
# print("Grade:", grade)
#
# Sample output:
# Grade: B
def get_grade(mark):
    if mark >= 75:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "D"


# Example call
grade = get_grade(68)
print("Grade:", grade)


#------------------------------------------------------------
# Exercise 7: Taxi Fare
# A taxi company charges:
# - a basic fare of $3.20
# - plus $0.55 for every 1 km travelled
#
# You may assume the distance can include halves, such as 4.5 km.
# This means:
# - 1 km costs $0.55
# - 0.5 km costs $0.275
#
# Write a function calculate_taxi_fare(distance) that returns
# the total fare.
#
# Then call the function and print the returned value.
#
# Example function call:
# fare = calculate_taxi_fare(4.5)
# print("Fare: $", round(fare, 3))
#
# Sample output:
# Fare: $ 5.675
def calculate_taxi_fare(distance):
    base_fare = 3.20
    cost_per_km = 0.55

    total_fare = base_fare + (distance * cost_per_km)
    return total_fare


# Example call
fare = calculate_taxi_fare(4.5)
print("Fare: $", round(fare, 3))

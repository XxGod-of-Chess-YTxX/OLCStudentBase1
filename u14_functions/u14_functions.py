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

def calculator(num1, num2, operation):
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = num1 / num2
    else:
        answer = "Invalid operator"
    return answer

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
operation = input("Enter operation (+, -, *, /): ")#

answer = calculator(num1, num2, operation)
print(f"{num1} {operation} {num2} = {answer}")






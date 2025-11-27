
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
#  # use if condition
# if num1 > num2:
#     # if the above condition is true, print this
#     print(f"{num1} > {num2}")

# elif num1 == num2:
#     print(f"{num1} = {num2}")
# else:
#     # if the above condition is false, run this:
#     print(f"{num1} < {num2}")

# PASSWORD PROGRAM
# 1

#give 3 cahances to enter the password
# password = "67mangos"   # the correct password
# attempts = 3              # number of tries allowed

# while attempts > 0:
#     guess = input("Enter the password: ")

#     if guess == password:
#         print("Access granted")
#         break
#     else:
#         attempts -= 1
#         print(f"Access Denied. You have {attempts} attempt(s) left.")

# if attempts == 0:
#     print("Womp Womp Womp Womp")
    



### RANDOM NUMBERS
# import random
# correct_answers = 0
# wrong_answers = 0


# ### TASK: MAKE A MATH QUIZ

# for i in range(10):

#     # generate 2 random numbers
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)

#     # ask the user the sum of the numbers
#     answer = int(input(f"What is {num1} + {num2}? "))
#     # check if the answer is correct
#     if answer == num1 + num2:
#         correct_answers += 1
#         print("Correct!")
#     else:
#         wrong_answers += 1
#         print(f"YOU IDIOT! The correct answer is {num1 + num2}.")
# # display the total number of correct and wrong answers
# print(f"\nYou got {correct_answers} correct answer(s) and {wrong_answers} wrong answer(s).")
# if correct_answers >= 7:
#     print("clanker detected")
# else:
#     print("marks is not defined")

# import random

# print("Guess the number from 1 to 100")
# random = random.randint(1, 100)
# attempts = 7

# guess = int(input("Guess a number: "))         

#     for i in range(1, 8):
#     if guess > random:
#         print("too high")   
#         attempts -= 1

#     elif guess < random:
#         print("too low")
#         attempts -= 1

#     else:
#         print(f"{guess} is correct")
#         # if correct, the stop the loop by breaking
#         break


# if attempts == 0:
#     print(f"the answer is {random}")


##############################################################################################################

# Recap and Warm up - DO This

# wrote a program to help cateogorize how much bus fare to pay

# ask user to input an age

# check if age is a valid number # <str>.isdigit()

#use if, elif and else
# age < 7: free
# between 7 to 12, $2.00
# between 13 to 21, $4.00
# between 22 to 60, $10.00
# 61 and above, $1.00

# print out the correct fare according to age

while True:#infinite loop
    age_input = input("How old are you?: ")
    # validasion
    if age_input.isdigit():
        age_input = int(age_input)# convert to number

        if age_input >= 61:
            print("$1.00")
        elif age_input >= 22:
            print("$10.00")
        elif age_input >= 13:
            print("$4.00")
        elif age_input >= 7:
            print("$2.00")
        else:
            print("free")
        break # complete program
    else:
        print(f"Wow, so you are {age_input} years old. Totally makes sense")#...
       




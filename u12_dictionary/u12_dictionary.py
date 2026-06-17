# ###################################################
# # Part 1: Learning Exercises


# # Practice Exercise 1: Creating a Dictionary
# # Create a dictionary to store student names and their grades.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# print("Student Grades: {}".format(students))




# #------------------------------------------------------------
# # Practice Exercise 2: Accessing Dictionary Values
# # Access Bob's grade from the dictionary.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# bob_grade = students["Bob"]  # Access using the key
# print("Bob's grade is: {}".format(bob_grade))





# #------------------------------------------------------------
# # Practice Exercise 3: Adding New Key-Value Pairs
# # Add a new student, Diana, with a grade of 92 to the dictionary.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# students["Diana"] = 92  # Add new key-value pair
# print("Updated Student Grades: {}".format(students))





# #------------------------------------------------------------
# # Practice Exercise 4: Updating Existing Values
# # Update Charlie's grade to 80 in the dictionary.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# students["Charlie"] = 80  # Update value
# print("Updated Student Grades: {}".format(students))




# #------------------------------------------------------------
# # Practice Exercise 5: Deleting Key-Value Pairs
# # Remove Alice's entry from the dictionary.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# del students["Alice"]  # Delete key-value pair
# print("Updated Student Grades: {}".format(students))





# #------------------------------------------------------------
# # Practice Exercise 6: Checking for Existence of a Key
# # Check if 'Diana' is in the student dictionary.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# if "Diana" in students:
#     print("Diana is in the dictionary.")
# else:
#     print("Diana is not in the dictionary.")




# #------------------------------------------------------------
# # Practice Exercise 7: Iterating Through a Dictionary
# # Print all student names and their grades.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# for name, grade in students.items():  # Iterate through dictionary
#     print("{}: {}".format(name, grade))




#------------------------------------------------------------








# dict1 = {"hamburger": 5, 
#          "pasta": 10, 
#          "fries": 2}

# # add / amend
# dict1["hamburger"] = 10

# # for key,value in dict1.items():
# #     print(key)
# #     print(value)

# # for key in dict1:
# #     print(key) # key
# #     print(dict1[key]) # value

# def oddoreven(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")

##################################################################################



# # How to define a dictionary
# menu = {"hamburger": "$2.00", "fries": "$1.00", "pasta": "$3.50"}  # key, value

# #retrive a value form dictionary
# priceham = menu["hamburger"]
# print(priceham)

# # change the value of a key
# menu["hamburger"] = "$20.00"
# print(menu) # to -rove change has been made

# ### add a new item to dictionary
# menu["pizza"] = "$30.00"
# print(menu) # to prove change has been made

# ## delete an item from dictionary
# del menu ["fries"]
# print(menu) # to prove change has been made

# # loop through dictionary
# for food, price in menu.items():
#     print(f"{food} : {price}")

# ### to ask customer what they want to eat?
# choice = input("Hello sir, what would you like to eat ")

# # need to check if i sell the item
# if choice in menu:
#     # means items exist
#     print(f"{choice} is {menu[choice]}")
# else:
#     print(f"Sorry I do not sell {choice}")


# ### ask for a key and value and add it to dictionary
# newfood = input("Enter name of new food: ")
# newprice = input("Enter name of new price: ")

# # add to dictionary
# menu[newfood] = newprice





'''
################ SET 1: Country and Capital ################

################ Define a dictionary ###############
# Define a dictionary named countries which will store a country and its capital city.

# 'Singapore' has capital 'Singapore'
# 'Malaysia' has capital 'Kuala Lumpur'
# 'Thailand' has capital 'Bangkok'
# 'Japan' has capital 'Tokyo'


# write and test your code here
countries = {"Singapore":"Singapore","Malaysia":"Kuala Lumpur", "Thailand":"Bangkok", "Japan":"Tokyo"}


################ Retrieve values from a dictionary ###############
# Print out the capital city of Malaysia only.
# Print out the capital city of Japan only.


# write and test your code here
print(countries["Malaysia"])
print(countries["Japan"])

########### Change the value of a dictionary key ###############
# Change the capital city of Thailand to 'Phuket'.
# Change the capital city of Singapore to 'Toa Payoh'.


# write and test your code here
newcapital = input("Enter a new capital for Thailand: ")
countries["Thailand"] = newcapital
newcapital2 = input("Enter a new capital for Singapore: ")
countries["Singapore"] = newcapital2

############ Add a new key / value to the dictionary #####################
# Add a new country => Indonesia with capital Jakarta.
# Add a new country => South Korea with capital Seoul.


# write and test your code here
countries["Indonesia"] = "Jakarta"
countries["South Korea"] = "Seoul"

############ Delete a key / value from the dictionary #####################
# Delete the country Singapore from the dictionary.


# write and test your code here
del countries["Singapore"]

########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of each country.
# Only display the keys.


# write and test your code here
for i in countries:
    print(i)

########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the capital cities.


# write and test your code here
for j in countries.values():
    print(j)

########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the country and its capital city.

# Example:
# Malaysia has capital city Kuala Lumpur
# Japan has capital city Tokyo
for k, l in countries.items():
    print(f"{k} has a capital city of {l}")
'''
#######################################################################
#######################################################################
#######################################################################

student_scores = {"mark":89, "john":34,"joseph":66}
# change a value of a key
student_scores["john"] = 74
print(student_scores)
#add a new key and its value
student_scores["mary"] = 88
print(student_scores)
#delete a key and its value
del student_scores["joseph"]
print(student_scores)
#check is a key is in a dictionary
check_student = input("WHo do you want to check?: ")
if check_student in student_scores:
    print(f"The score for {check_student} is {student_scores[check_student]}")#first is key and second is value

else:
    print(f"{check_student} is not in ur class")
#loop through dictionary keys
for name in student_scores:
    print(name)
    print(student_scores[name])
#for key, value ...............................
for name, score in student_scores.items():
    print(f"{name} got {score}")
#########################################################################################################################

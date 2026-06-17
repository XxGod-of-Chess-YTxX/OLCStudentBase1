################ SET 1: Country and Capital ################

################ Define a dictionary ###############
# Define a dictionary named countries which will store a country and its capital city.

# 'Indonesia' has capital 'Jakarta'
# 'Malaysia' has capital 'Kuala Lumpur'
# 'Thailand' has capital 'Bangkok'
# 'Japan' has capital 'Tokyo'






################ Retrieve values from a dictionary ###############
# Print out the capital city of Malaysia only.
# Print out the capital city of Japan only.


########### Change the value of a dictionary key ###############
# Change the capital city of Thailand to 'Phuket'.
# Change the capital city of Singapore to 'Toa Payoh'.




############ Add a new key / value to the dictionary #####################
# Add a new country => Indonesia with capital Jakarta.
# Add a new country => South Korea with capital Seoul.




############ Delete a key / value from the dictionary #####################
# Delete the country Singapore from the dictionary.




########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of each country.
# Only display the keys.




########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the capital cities.




########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the country and its capital city.

# Example:
# Malaysia has capital city Kuala Lumpur
# Japan has capital city Tokyo




################ SET 2: Student and Marks ################

################ Define a dictionary ###############
# Define a dictionary named marks which will store a student name and the marks they scored.

# 'Alice' scored 78
# 'Ben' scored 64
# 'Chloe' scored 89
# 'Daniel' scored 55


# # write and test your code here
# test = {"Alice":78,"Ben":64,"Chloe":89,"Daniel":55}

# ################ Retrieve values from a dictionary ###############
# # Print out the marks scored by Alice only.
# # Print out the marks scored by Daniel only.
# print(test["Alice"])
# print(test["Daniel"])

# ########### Change the value of a dictionary key ###############
# # Change Ben's marks to 70.
# # Change Daniel's marks to 60.
# test["Ben"] = 70
# test["Daniel"] = 60





# ############ Increase the value of a dictionary key ############
# # Increase Chloe's marks by 5.
# # Decrease Alice's marks by 3.
# test["Chloe"] += 5
# test["Alice"] -= 3




# ############ Add a new key / value to the dictionary #####################
# # Add a new student => Ethan who scored 82.
# # Add a new student => Fiona who scored 91.
# test["Ethan"] = 82
# test["Fiona"] = 91




# ############ Delete a key / value from the dictionary #####################
# # Delete Daniel from the dictionary.
# del test["Daniel"]



# ########### Loop through to Retrieve Keys ##################
# # Write a for loop, and only display the name of each student.
# # Only display the keys.
# for name in test:
#     print(name)




# ########### Loop through to Retrieve Values ##################
# # Write a for loop, and only print out the marks.
# for marks in test.values():
#     print(marks)



# ########### Loop through to Retrieve Key and Values ##################
# # Write a for loop, and print out the student name and marks.

# # Example:
# # Alice scored 78 marks
# # Ben scored 64 marks

# # write and test your code here
# for name, marks in test.items():
#     print(f"{name} score {marks}")
################ SET 3: Game Item and Quantity ################

################ Define a dictionary ###############
# Define a dictionary named inventory which will store a game item 
# and the quantity owned by the player.

# 'potion' quantity is 5
# 'sword' quantity is 1
# 'shield' quantity is 1
# 'arrow' quantity is 20
inv = {"potion":5,"sword":1,"shield":1,"arrow":20}


################ Retrieve values from a dictionary ###############
# Print out the quantity of potion only.
# Print out the quantity of arrow only.
print(inv["potion"])
print(inv["arrow"])


########### Change the value of a dictionary key ###############
# Change the quantity of sword to 2.
# Change the quantity of shield to 3.
inv["sword"] = 2
inv["shield"] = 3



############ Increase the value of a dictionary key ############
# Increase the quantity of potion by 10.
# Decrease the quantity of arrow by 5.

inv["potion"] += 10
inv["arrow"] -= 5


############ Add a new key / value to the dictionary #####################
# Add a new item => bow with quantity 1.
# Add a new item => apple with quantity 8.
inv["bow"] = 1
inv["apple"] = 8




############ Delete a key / value from the dictionary #####################
# Delete apple from the dictionary.

del inv["apple"]



########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of each item.

# Only display the keys.
for name in inv:
    print(name)


########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the quantities.


# # write and test your code here
for quantity in inv.values():
    print(quantity)

########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the item and quantity.

# Example:
# potion quantity: 5
# arrow quantity: 20


# write and test your code here
for item, num in inv.items():
    print(f"{item} quantity: {num}")
########################################################################

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



# How to define a dictionary
menu = {"hamburger": "$2.00", "fries": "$1.00", "pasta": "$3.50"}  # key, value

#retrive a value form dictionary
priceham = menu["hamburger"]
print(priceham)

# change the value of a key
menu["hamburger"] = "$20.00"
print(menu) # to -rove change has been made

### add a new item to dictionary
menu["pizza"] = "$30.00"
print(menu) # to prove change has been made

## delete an item from dictionary
del menu ["fries"]
print(menu) # to prove change has been made

# loop through dictionary
for food, price in menu.items():
    print(f"{food} : {price}")

### to ask customer what they want to eat?
choice = input("Hello sir, what would you like to eat ")

# need to check if i sell the item
if choice in menu:
    # means items exist
    print(f"{choice} is {menu[choice]}")
else:
    print(f"Sorry I do not sell {choice}")


### ask for a key and value and add it to dictionary
newfood = input("Enter name of new food: ")
newprice = input("Enter name of new price: ")

# add to dictionary
menu[newfood] = newprice


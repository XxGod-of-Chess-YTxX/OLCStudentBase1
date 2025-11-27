# Task 3
# The task is to edit program code so that countries and their capital 
# cities can be added to or removed from a dictionary.

# The following program has a dictionary that contains countries 
# and their capital cities. The program allows the user to:

# • input a country
# • input whether they want to remove a country and 
#    its capital city from the dictionary
# • input whether they want to add a country and its 
#    capital city to the dictionary.

'''
capital_cities = {
    'singapore': 'Singapore',
    'japan': 'Tokyo',
    'australia': 'Canberra',
    'england': 'London',
    'france': 'Paris',
    'germany': 'Berlin'
}

country = input("Please enter the name of a country: ").lower()
print(capital_cities[country])
remove = input("Would you like to remove any of the entries? (Y or N): ")
'''

# For all sub-tasks, you can assume that all user input is valid.
#  All countries input to be searched or removed are found in the dictionary.

# Task 3.1
# Edit the program so that it:
# • converts the input for country to lower case
# • searches the dictionary for the country input and outputs the capital city of that country.
# Save your program.    [3]

# 1.5 / 3
capital_cities = {
    'singapore':'Singapore',
    'japan':'Tokyo', 'australia':'Canberra',
    'england':'London',
    'france':'Paris',
    'germany':'Berlin'
}

country = input("Please enter the name of a country: ").lower()
if country in capital_cities:
    print(capital_cities[country])
add = input("Would you like to add a new entry? (Y or N): ")
remove = input("Would you like to remove any of the entries? (Y or N): ")


# Task 3.2
# Copy and paste your program from sub-task 3.1.
# Edit the program so that if the user enters the value ‘Y’ for remove, the program:
# • allows the user to input a country they want to remove from the dictionary
# • converts the country input to lower case
# • removes the country from the dictionary that is input by the user.
# 3 / 3
'''
capital_cities = {
    'singapore':'Singapore',
    'japan':'Tokyo', 'australia':'Canberra',
    'england':'London',
    'france':'Paris',
    'germany':'Berlin'
}
while True:
    country = input("Please enter the name of a country: ").lower()
    print(capital_cities[country])
    add = input("Would you like to add a new entry? (Y or N): ")
    remove = input("Would you like to remove any of the entries? (Y or N): ")

    if remove.strip().lower() == "y":
        country_to_remove = input("What country to remove? ").lower()
        if country_to_remove in capital_cities:
            del capital_cities[country_to_remove]
            print(f"{country_to_remove.title()} has been removed from the dictionary.")
        else:
            print(f"{country_to_remove.title()} not found in the dictionary.")
'''

# Save your program.   [3]

# Task 3.3
# Copy and paste your program from sub-task 3.2 .
# Edit the program so that if the user enters the value ‘Y’ for add, the program:
# • allows the user to input a country they want to add to the dictionary
# • allows the user to input the capital city for the country they want to add
# • adds the country and its capital city to the dictionary in the format country:capital
# • outputs the dictionary at the end of the program.

capital_cities = {
    'singapore':'Singapore',
    'japan':'Tokyo', 'australia':'Canberra',
    'england':'London',
    'france':'Paris',
    'germany':'Berlin'
}

country = input("Please enter the name of a country: ").lower()
    
add = input("Would you like to add a new entry? (Y or N): ")
remove = input("Would you like to remove any of the entries? (Y or N): ")

if remove.strip().lower() == "y":
    country_to_remove = input("What country to remove? ").lower()
    if country_to_remove in capital_cities:
        del capital_cities[country_to_remove]
        print(f"{country_to_remove.title()} has been removed from the dictionary.")
    else:
        print(f"{country_to_remove.title()} not found in the dictionary.")

if add.strip().lower() == "y":
    country_to_add = input("Enter the country to add: ").lower()
    capital_to_add = input(f"Enter the capital city of {country_to_add.title()}: ")
    capital_cities[country_to_add] = capital_to_add
    print(f"{country_to_add.title()} with capital {capital_to_add} has been added to the dictionary.")

print("Current dictionary:", capital_cities)
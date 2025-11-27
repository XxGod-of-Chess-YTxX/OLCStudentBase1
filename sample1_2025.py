# Task 2

# The following program allows the weights of 15 bags of rice to be input. 
# The correct weight for each bag of rice must be 
# between 4.9 kg and 5.1 kg inclusive.

bags_rice = 15
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")    
        
# 7       Edit the program so that it:
# a.       Accepts the weights for only 10 bags of rice.
# [1] ## T.David: Correct 1 mark

bags_rice = 10
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
    if bag_weight < lower_bound:
        print("The bag of rice is underweight") 

# b.       Prints out the message “The bag of rice is the correct weight” 
# when a weight entered is between 4.9kg and 5.1 kg inclusive.
# [2] ## T.David: Correct 2 mark

bags_rice = 15
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
    elif bag_weight < lower_bound:
        print("The bag of rice is underweight") 
    else:
        print("The bag of rice is the correct weight")
        

# c.       Prints out the number of bags of rice that were underweight, 
# as well as the number that were overweight, after the weights of all 
# the bags have been entered.
# [5] ## T.David: Correct 5 mark (* but note that the code should be incremental i.e. take from previous question)

overweight = 0
underweight = 0
bags_rice = 15
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
        overweight = overweight + 1
    if bag_weight < lower_bound:
        print("The bag of rice is underweight") 
        underweight = underweight + 1
print(f"There are {overweight} overweight rice bags and {underweight} underweight rice bags")

# d. Edit your program so that it works for any number of bags of rice.
# [2] ## T.David: Correct 2 mark (* but note that the code should be incremental i.e. take from previous question)
# Save your program.

bags_rice = int(input("Enter number of rice bags to weigh: "))
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")


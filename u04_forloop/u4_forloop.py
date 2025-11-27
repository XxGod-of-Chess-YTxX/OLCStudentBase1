# use the for loop and print out numbers from 0 to 5
for i in range(0, 6, 1): #start stop step
    print(i)

# use the for loop and print out numbers from 1 to 5
for i in range (1, 6, 1): #start stop step
    print(i)

# use the for loop and print out multiples of 5 from 5 to 50
for i in range (5, 51, 5):#start stop step
    print(i)

# use the for loop and print out numbers from 10 to 1
for i in range (10, 0, -1):#start stop step
    print(i)#

################################


# loop - repeates certain codes

# assume ur dumb
# print("-8===================================================D")

# repeat code number of times
# for i in range(100):
# print("I will be an idiot anymore")



# print('Mary had a')

#loop
# for i in range(3):
#    print("little lamb")
    
# print('Mary had a')

# loop
# for i in range(3):
#     print("little lamb")

# loop 1
# for j in range(2):

#     print("Mary had a")

#     #loop2
#     for i in range(3):
#         print("little lamb")

# for i in range(1, 11):
#     print(i)

# #print from 23 - 35
# for i in range(23, 36):
#     print(i)

# #print from 88 - 96
# for i in range(88, 97):
#     print(i)

# #multiplies of 4 from 4 to 48
# for i in range(4, 49, 4): #start, stop and step
#     print(i)

# #print multiples of 2 from 2 to 24
# for i in range(2, 25, 2): #start, stop and step
#     print(i)

# #print odd numbers from 3 to 27
# for i in range(3, 28, 2): #start, stop and step
#     print(i)

# # print decending numbers fomr 10 to 1
# for i in range(10, 0, -1): #start, stop and step
#     print(i)         
#


###############################################################################################

#create a times-table program

#ask the user to enter a number
number = int(input("Enter a number: "))

print(f"\nTimes Table for {number}:\n")
for i in range(1,13):
    print(f"{number} x {i} = {number * i}")


#------------------------------------------------------------
# Exercise 13: Printing a Custom Star Pattern
# Write a program to print the following pattern:
# *
# ***
# *****
# *******
# *********

# using a for loop
# print("*")
# print("*" * 3)
# print("*" * 5)
# print("*" * 7)
# print("*" * 9)


for i in range(1, 21, 2):#start, stop and step
    print("*"* i)
    
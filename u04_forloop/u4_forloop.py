

###########################################################
# Part 3. IN-CLASS Practice Exercises For loops
#
# Focus: Python for-loops (range, strings, lists, dicts, indexes)
###########################################################


#------------------------------------------------------------
# Exercise 1: Count Up with range(stop)
# Print the numbers 0 to 9 
# Use: range(10)
# Bonus Challenge: Print on one line, separated by spaces.

# Example: Output = 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print(i)




#------------------------------------------------------------
# Exercise 2: Count Down with range(start, stop, step)
# Print 10 down to 1 
# Bonus Challenge: Print on one line, separated by spaces.
# Example: Output = 10 9 8 7 6 5 4 3 2 1
for j in range (10,0,-1):
    print(j)





#------------------------------------------------------------
# Exercise 3: Evens in a Range
# Print all even numbers from 2 to 20.
# Bonus Challenge: Print on one line, separated by spaces.
# Example: Output = 2 4 6 8 10 12 14 16 18 20
even = []
for k in range(2,21,2):
    even.append(k)
print(even)




#------------------------------------------------------------
# Exercise 4: Multiples with Steps
# Print the first 6 multiples of 9.
# Use: range(start, stop, step) where step = 9
# Tip: Think about where to stop so you get 6 numbers.
# Example: Output = 9 18 27 36 45 54
for l in range(9,55,9):
    print(l)




#------------------------------------------------------------
# Exercise 5: Running Total (Accumulator)
# Compute the sum of all integers from 1 to 100 (inclusive) and print it.
# Use: range(1, 101)
# Example: Output = 5050
x = 0
for m in range(1,101):
    x = x + m
print(x)




#------------------------------------------------------------
# Exercise 6: Sum of Multiples
# Compute the sum of multiples of 3 from 3 to 30 (inclusive).
# Use: range(3, 31, 3)
# Example: Output = 165
y = 0
for n in range(3,31,3):
    y += n
print(y)




#------------------------------------------------------------
# Exercise 7: Loop Through a String (characters)
# Count the vowels in the string and print the total.
# Data:
# text = "Computhink Academy"
# Vowels: a, e, i, o, u (case-insensitive)
# Example: Output = 7'
text = "Computhink Academy"
z = 0
for a in text:
    if a.lower() in 'aeiou':
        z += 1
print(z)


#------------------------------------------------------------
# Exercise 8: Loop Through a String Using Index
# Print each character with its index in the format: index:char
# Data:
# name = "Python"
# Example: 
# 0:P
# 1:y
# 2:t
# 3:h
# 4:o
# 5:n
num = 0
name = "Python"
for c in name:
    print(f"{num}:{c}")
    num += 1



#------------------------------------------------------------
# Exercise 9: Every 2nd Character (Index Step)
# Print every 2nd character (positions 0, 2, 4, ...) of the string on one line (no spaces).
# Data:
# s = "abcdefghijkl"
# Example: Output = acegik
s = "abcdefghijkl"
result = ""
for i in range(0, len(s), 2):
    result += s[i]
print(result)





#------------------------------------------------------------
# Exercise 10: Loop Through a List (values)
# Print the squares of all numbers in the list on one line, separated by spaces.
# Data:
# nums = [3, 1, 4, 1, 5, 9]
# Example: Output = 9 1 16 1 25 81
nums = [3, 1, 4, 1, 5, 9]
square = []
for i in nums:
    square.append(i**2)
print(square)



#------------------------------------------------------------
# Exercise 11: Loop Through a List Using Index
# Replace every negative number in the list with 0, then print the updated list.
# Data:
# data = [5, -2, 7, -9, 0, 4]
# Expected final list: [5, 0, 7, 0, 0, 4]
data = [5, -2, 7, -9, 0, 4]
final = []
for i in data:
    if i > 0:
        final.append(i)
    else:
        final.append(0)
print(final)
        




#------------------------------------------------------------
# Exercise 12: Manual Max (No max())
# Find and print the largest number in the list without using max().
# Data:
# scores = [42, 67, 23, 88, 55, 88, 12]
# Example: Output = 88
scores = [42, 67, 23, 88, 55, 88, 12]
x = 0
for i in scores:
    if i > x:
        x = i

print(x)




#------------------------------------------------------------
# Exercise 13: Loop through a List (index + value)
# Print each item with a 1-based index like "1) apple", "2) banana", ...
# Data:
# fruits = ["apple", "banana", "cherry", "durian"]
no = 1
fruits = ["apple", "banana", "cherry", "durian"]
for i in fruits:
    print(f"{no}) {i}")
    no += 1
    






#------------------------------------------------------------
# Exercise 14: Pair Two Lists 
# Print "Alice: 85", "Ben: 73", etc. by pairing names with marks.
# Data:
# names = ["Alice", "Ben", "Carmen", "Dylan"]
# marks = [85, 73, 91, 66]
names = ["Alice", "Ben", "Carmen", "Dylan"]

marks = [85, 73, 91, 66]
for i in range(len(names)):
    print(f"{names[i]}: {marks[i]}")






#------------------------------------------------------------
# Exercise 15: Nested Loops – Times Table
# Print a 1–5 multiplication table with rows like:
# 1 2 3 4 5
# 2 4 6 8 10
# ...
# Use two for-loops (outer row 1..5, inner col 1..5).

for i in range(1,6):
    for j in range(i, i*10 + 1, i):
        print(j)





#------------------------------------------------------------
# Exercise 16: Pattern Printing (Right Triangle)
# For n = 5, print:
# *
# **
# ***
# ****
# *****
# Use a for-loop and string multiplication.
for n in range(1,6):
    print("*" * n)




#------------------------------------------------------------
# Exercise 17: Dictionary Iteration (keys & values)
# Print "Alice : 72" etc. for each pair in the dict.
# Data:
# grades = {"Alice":72, "Ben":65, "Chloe":88, "Dion":55}

grades = {"Alice":72, "Ben":65, "Chloe":88, "Dion":55}

for student, score in grades.items():
    print(f"{student}:{score}")



#------------------------------------------------------------
# Exercise 18: Dictionary Aggregation
# Compute and print the average value in the dictionary (to 1 decimal place).
# Data:
# temps = {"Mon":31.2, "Tue":29.8, "Wed":30.5, "Thu":32.0, "Fri":31.0}
# Example: Output = 30.9
x = 0
y = 0
temps = {"Mon":31.2, "Tue":29.8, "Wed":30.5, "Thu":32.0, "Fri":31.0}
for i in temps.values():
    x = x + i

for j in temps.keys():
    y += 1
print(x/y)

print(x/ len(temps))




#------------------------------------------------------------
# Exercise 19: Filter from a Dictionary
# Print only the students who passed (score >= 50) in "Name (score)" format.
# Data:
# results = {"Amy":49, "Bao":77, "Chin":50, "Deepa":92, "Eun":38}
# Example:
# Bao (77)
# Chin (50)
# Deepa (92)
results = {"Amy":49, "Bao":77, "Chin":50, "Deepa":92, "Eun":38}
for student, score in results.items():
    if score >= 50:
        print(f"{student} ({score})")



#------------------------------------------------------------
# Exercise 20: for-else Search
# Search for target in the list; print "Found at index i" or "Not found".
# Use for-else (else runs only if loop completes with no break).
# Data:
# items = ["id-001", "id-007", "id-010", "id-013"]
# target = "id-010"
items = ["id-001", "id-007", "id-010", "id-013"]
target = "id-010"
if target in items:
    position = items.index(target)
    print(f"Found at index {position}")





#------------------------------------------------------------
# Exercise 21: Skip and Stop (continue / break)
# Loop through the string:
#  - Skip vowels (do not print them).
#  - Stop printing entirely if you meet an exclamation mark '!' (break).
# Data:
# msg = "Code smarter, not harder!"
# Expected printed output (no vowels, stop at '!'): Cd smtr, nt hrdr
msg = "Code smarter, not harder!"
result = ""
for i in msg:
    if i in "!":
        break
    if i.lower() not in 'aeiou':
        
        result += i
print(result)
        





#------------------------------------------------------------
# Exercise 22: Character Frequency (build a dict)
# Build and print a frequency dictionary {char: count} for letters only (ignore spaces).
# Treat uppercase and lowercase as the same.
# Data:
# line = "Better code, better life"
# Example (order may vary): {'b':2, 'e':6, 't':5, 'r':3, 'c':1, 'o':1, 'd':1, 'l':1, 'i':1, 'f':1}
line = "Better code, better life"

freq = {}

for i in line.lower():
    if i == " ":
        continue
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)





#------------------------------------------------------------
# Exercise 23: Index Windows (String Slices by Loop)
# Print every 3-letter chunk of the string using indexes (i, i+3).
# Ignore the leftover if length is not a multiple of 3.
# Data:
# dna = "ATGCGATACGCTTGA"
# Example:
# ATG
# CGA
# TAC
# GCT
# TGA

dna = "ATGCGATACGCTTGA"

freq = {}

for i in dna:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)



#------------------------------------------------------------
# Exercise 24: Two-List Computation 
# Given costs and quantities, print "Item i: $TOTAL" per line and the grand total.
# Data:
# costs = [1.20, 0.80, 3.50, 2.00]
# qty   = [3,     5,    2,    1   ]
# Example lines:
# Item 1: $3.60
# Item 2: $4.00
# Item 3: $7.00
# Item 4: $2.00
# Grand Total: $16.60

costs = [1.20, 0.80, 3.50, 2.00]
qty   = [3, 5, 2, 1]

grand_total = 0

for i in range(len(costs)):
    total = costs[i] * qty[i]
    grand_total += total
    print(f"Item {i+1}: ${total:.2f}")

print(f"Grand Total: ${grand_total:.2f}")




#------------------------------------------------------------
# Exercise 25: Validate with for-loop (All Digits)
# Check if a string consists only of digits (0–9) using a for-loop.
# You cannot use .isdigit()
# Data:
# token = "A12345"
# Print True or False accordingly (no .isdigit()).
token = "A12345"
numonly = True
for i in token:
    if i < '0' or i > '9':
        numonly = False
        break
print(numonly) 



#------------------------------------------------------------
# Exercise 26: Build a New List 
# From the list, build a new list containing only the positive even numbers, then print it.
# Data:
# nums = [-3, -2, 0, 1, 2, 3, 4, 11, 12]
# Expected: [2, 4, 12]
nums = [-3, -2, 0, 1, 2, 3, 4, 11, 12]
positives = []
evenpositives = []
for i in nums:
    if i > 0:
        positives.append(i)
for j in positives:
    if j % 2 == 0:
        evenpositives.append(j)
print(evenpositives)


#------------------------------------------------------------





# # use the for loop and print out numbers from 0 to 5
# for i in range(0, 6, 1): #start stop step
#     print(i)

# # use the for loop and print out numbers from 1 to 5
# for i in range (1, 6, 1): #start stop step
#     print(i)

# # use the for loop and print out multiples of 5 from 5 to 50
# for i in range (5, 51, 5):#start stop step
#     print(i)

# # use the for loop and print out numbers from 10 to 1
# for i in range (10, 0, -1):#start stop step
#     print(i)#

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
# number = int(input("Enter a number: "))

# print(f"\nTimes Table for {number}:\n")
# for i in range(1,13):
#     print(f"{number} x {i} = {number * i}")


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


# for i in range(1, 21, 2):#start, stop and step
#     print("*"* i)
    
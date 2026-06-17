# Task 2 

# Open the file WORDLIST.ipynb 
# You will see the following program that has 
# a string of words stored in a list. 

word_list = ["apple", "window", "bend", "paper", "thought"] 

# -----------------------------------
# # Task 2.1 

# Extend the program to: 
# > ask the user to input a new word  
# > take the new word as input  
# > convert the new word to lower case  
# > store the new word at the end of the list in a new space. 

# You do not need to consider any validation for the new word. 
# Save your program. [3] 
# -----------------------------------
word_list = ["apple", "window", "bend", "paper", "thought"] 
newword = input("Enter a new word: ").lower()
word_list.append(newword)
print(word_list)



 
# -----------------------------------
# Task 2.2 
# Copy and paste your program from sub-task 2.1. 

# Extend your program to: 
# > > search the list to find words that have 5 or more letters 
# > count and output the number of words that have five or more letters, 
#       with a suitable output message. 

# Save your program. [4] 
# -----------------------------------
fiveormore = 0
word_list = ["apple", "window", "bend", "paper", "thought"] 
newword = input("Enter a new word: ").lower()
word_list.append(newword)
print(word_list)
for i in word_list:
    if len(i) >= 5:
        fiveormore += 1
print(f"Words with at least 5 characters: {fiveormore}")



# -----------------------------------
# Task 2.3 

# Copy and paste your program from sub-task 2.2. 
# Extend your program to: 
# search the list to find words that begin and end with the same letter 
# count and output the number of words that 
# begin and end with the same letter, with a suitable output message. 

# [3] 
# -----------------------------------
fiveormore = 0
firstislast = 0
word_list = ["apple", "window", "bend", "paper", "thought"] 
newword = input("Enter a new word: ").lower()
word_list.append(newword)
print(word_list)
for i in word_list:
    if len(i) >= 5:
        fiveormore += 1
print(fiveormore)
for j in word_list:
    if j[0] == j [-1]:
        firstislast += 1
print(f"Words with same first and last: {firstislast}")


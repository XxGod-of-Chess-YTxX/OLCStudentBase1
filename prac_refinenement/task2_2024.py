
# A school has a new computer network. 
# The following program allows students to create 
# a username and password to log onto the network.

# list_username = ["StudentNo1", "JaneJones", "ABC123"]
# username = input("Please enter a username: ")
# password = input("Please enter a password: ")

#======================================================
# Task 1.1
# Edit the program so that it checks to see 
# if the username entered exists in the list.
# If it does not exist in the list, it must store the username in the list.
# If it does exist in the list, the program must loop 
# until a username is entered that does not already exist in the list.
# [4]
#------------------------------------------------------
list_username = ["StudentNo1", "JaneJones", "ABC123"]
while True:
    username = input("Please enter a username: ")
    if username not in list_username:
        list_username.append(username)
        print("Username stored")
        break
    else:
        print("Username already taken")

password = input("Please enter a password: ")



# Edit your program so that it checks if the password:
# ·        contains at least one numerical character
# ·        contains at least one special character from: @ ! / ?
# ·        is at least 8 characters in length

# The program should loop until the password 
# fulfils all the three requirements.

# Use suitable input and output messages.
# [6]

#======================================================
list_username = ["StudentNo1", "JaneJones", "ABC123"]

# Task 1.1
# Username check
while True:
    username = input("Please enter a username: ")

    if username not in list_username:
        list_username.append(username)
        print("Username stored")
        break
    else:
        print("Username already taken")

# Task 1.2
# Password check
while True:
    password = input("Please enter a password: ")

    hasnum = False
    hassymbol = False

    if len(password) < 8:
        print("Password too short")
        continue

    for i in password:
        if i.isdigit():
            hasnum = True
        if i in "@!?/":
            hassymbol = True

    if hasnum and hassymbol:
        print("Password accepted")
        break
    else:
        print("Password must contain at least one number and one special character (@ ! / ?)")

### TRY THIS RECAP QUESTION ONCE YOU COME IN ###

# A student is writing a program to note down 
# the favourite sports of each of his classmates.
# the program will help check how many students like a certain sport.



# Write a program that will 
# -------------------------------------------------
# 1. ask how many students there are in the class
no_of_students = int(input("How many students are there: "))


# -------------------------------------------------
sportlist = []
# 2. for each student, ask what is their favourite sport
	# 2a. Add the sport into a list
for student in range(no_of_students):
    sport = input("favortie sport: ")
    sportlist.append(sport)


# -------------------------------------------------
# 3. After asking all the student's sport, 
	# Ask the user to enter a sport to check how many students like the sport.
check_sport = input("What sport to check: ")
counter = 0

# -------------------------------------------------
# 4. if the sport exist, print out how many people like the sport.
	# e.g. # 3 students like the sport
if check_sport in sportlist:
    for sport in sportlist:
        if check_sport == sport:
            counter = counter + 1
    print(f"{counter} students like {check_sport}")

# -------------------------------------------------
# 5. if the sport does not exist, print out an appropriate message.

# ** Assume that all inputs given are in lower case and valid.
# ** the program will work for any number of students.
else:
    print(f"No one likes {check_sport}")

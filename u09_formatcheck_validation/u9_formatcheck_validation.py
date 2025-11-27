# '''
# Question 1 (Length Check):
# Write the input entry and validation code for a program that
# needs to accept a 4-digit OTP (One-Time Password)
# The OTP must be exactly 4 digits long

# If the input is invalid, your code should keep trying
# by asking for the input to be entered again.

# #########################################

# Sample output

# Enter OTP: 12
# Invalid input. The OTP must be exactly 4 digits.

# Enter OTP: 12345

# Invalid input. The OTP must be exactly 4 digits

# Enter OTP: 1234
# OTP accepted

# '''
while True:
    otp = input("Enter a 4 digit code: ")

     #validation for length and number 6767677676776767667767676776767676767
    if not otp.isnumeric:
        print("please enter a 4 digit number")
    elif len(otp) != 4:
        print("OTP must be 4 digits")
    else:
         #means its valid
        print("Valid otp")
        break

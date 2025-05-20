# Determine full name as variable "full_name"
# Set if-elif-else command for following:
    # Input equal to 0 characters
    # Input less than 4 characters
    # Input greater than 25 characters
    # Input within numerical parameters
# Print the result once if-elif-else boolean has been fulfilled

full_name = input("Please enter your full name: ")

if len(full_name) == 0:
    print("You haven't entered anything, please enter your full name: ")
elif len(full_name) < 4:
    print("You have entered less than 4 characters, please enter your surname as well: ")
elif len(full_name) > 25:
    print("You have entered more than 25 characters, please only enter your forename and surname: ")
else:
    print(f"Hi {full_name}, thank you for entering your name!")

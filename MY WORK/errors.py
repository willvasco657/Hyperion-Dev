# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Add parenthesis around the statement (syntax)
print("\n") # Remove indent and add parenthesis (syntax)

# Variables declaring the user's age, casting the str to an int, and printing the result
# Remove indent for the below statements (syntax)
# Remove first line entirely (logical)
age = 24 # Create the variable for age as an integer (syntax)
print(f"I'm {age} years old.") # use 'f' to format the sentence and {} to print the correct variable (syntax)

# Variables declaring additional years and printing the total years of age
# Remove indent for these statments (syntax)
years_from_now = 3 # Remove the "" to make the variable an integer not a string (syntax)
total_years = age + years_from_now

print(f"The total number of years: {total_years}") # Add parenthesis and format sentence so the 'total_years' is printed (syntax) 

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6 # Amend to 'total_years' and add '+ 6' to account for the extra 6 months (logical)
print(f"In 3 years and 6 months, I'll be {total_months} months old") # Add parenthesis and format sentence to display 'total months' calculation (syntax)

#HINT, 330 months is the correct answer
total = 0 # Make sure the count starts at 0
digits = 0

number = int(input("Please input a number, enter -1 to stop: ")) # Ask user for input to start the count with integer
while number != -1: # While loop for when input is not equal to -1 (!=)
    total += number # Adds the input to total
    digits += 1 # Increases the count for each input
    number = int(input("Please input a number: ")) # While input is not -1, ask user for another input as integer
if digits > 0: # Make sure the total is divisible and not 0
    average = total / digits # Divides the total by the number of inputs, not accounting for -1
    print(f"The average of the numbers you input is: {average}") # Print the average of input total

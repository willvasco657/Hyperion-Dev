# Request user input for each of option
num_1 = int(input("Please enter your first number: "))
num_2 = int(input("Please enter your second number: "))
num_3 = int(input("Please enter your third number: "))

# Print out the user choices
print (f"You chose: {num_1, num_2, num_3}")

# Add the three values together
total = num_1 + num_2 + num_3

# Subtract input one from input two
sub_nums = num_1 - num_2

# Multiply input three by input 1
x_nums = num_3 * num_1

# Divide the totals by input three
div_nums = (total + sub_nums + x_nums) / num_3

# Print out information using formatting
print (F"""
       The sum of all the numbers: {total}
       The first number minus the second: {sub_nums}
       The third number multiplied by the first: {x_nums}
       The sum of all three numbers divided by the third number: {div_nums}""")

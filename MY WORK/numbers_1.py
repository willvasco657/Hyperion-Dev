# Request user input 3 different integers
# Print
    # the sum of all integers
    # num_1 minus num_2
    # num_3 multiplied by num_1
# sum of all three numbers stated as num_4
# divide num_4 by num_3

num_1 = int(input("Please enter your first number: "))
num_2 = int(input("Please enter your second number: "))
num_3 = int(input("Please enter your third number: "))
print (f"You chose: {num_1, num_2, num_3}")

total = num_1 + num_2 + num_3
sub_nums = num_1 - num_2
x_nums = num_3 * num_1
div_nums = (total + sub_nums + x_nums) / num_3
print (F"""
       The sum of all the numbers: {total}
       The first number minus the second: {sub_nums}
       The third number multiplied by the first: {x_nums}
       The sum of all three numbers divided by the third number: {div_nums}""")

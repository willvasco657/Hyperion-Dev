# This program will display two compliation errors, a runtime error and a logical error

car = BMW # This is a compilation error as the statement needs to have speech marks
colour = "blue"
wheels = int(4 / 0) # This is a runtime error as the program is trying to divide by 0. 
# This is also where the logical error is as the program needs to display 4 wheels in the output

# This is another compilation error as the parenthesis needs to hold an 'f' to format the output
car_details = ("This car is a {car} and it is {colour}. It has {wheels} wheels!")
print(f"{car_details}") 

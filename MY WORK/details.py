# Request user input:
    # name
    # age
    # house number
    # street name
# print input in one sentence

name = input("Enter your name: ")
age = input("Enter your age: ")
house_number = input("Enter house number: ")
street_name = input("Enter street name: ")

f_string = (f"This is {name}! He is {age} years old and lives at {house_number}, {street_name}.")
print(f_string)

# Take inputs for name, age, hair, and eye color
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hair = input("Enter your hair color: ")
eyes = input("Enter your eye color: ")

# Create a class for adult
class Adult():
    def __init__(self, name, age, hair, eyes):
        self.name = name
        self.age = age
        self.hair = hair
        self.eyes = eyes

    # Method to check if the person can drive
    def can_drive(self):
        print(f"{self.name} is old enough to drive.")

# Create a class for child
class Child(Adult):
    def __init__(self, name, age, hair, eyes):
        super().__init__(name, age, hair, eyes)

    # Method to check if the person can drive
    def can_drive(self):
        print(f"{self.name} is too young to drive.")

# Create an instance of the appropriate class based on age
if age >= 18:
    human = Adult(name, age, hair, eyes)
else:
    human = Child(name, age, hair, eyes)

# Call the method to check if the person can drive
human.can_drive()
#  Researched and found that this was the best way to
#  ensure the program can find the correct path
#  to the file if it doesn't exist yet, creating 
#  the file if needed

import os

# Function to calculate the equation
def calculate():
    try:
        num1 = float(input("Number: "))  #  Use float to allow for decimal numbers
        sign = input("Function(+, -, *, /): ")
        num2 = float(input("Number: "))
        
        if sign == '+':
            output = num1 + num2
        elif sign == '-':
            output = num1 - num2
        elif sign == '*':
            output = num1 * num2
        elif sign == '/':
            if num2 == 0: #  Prevent division by zero
                print("This is not possible, enter a different number")
                return
            output = num1 / num2
        else:  #  If the user enters an invalid sign
            print("Error! Please enter a correct sign!")
            return
        
        #  Output the answer and write it to the file
        answer = f"{num1} {sign} {num2} = {output}"
        print(f"Answer: {output}")
        
        with open("equations.txt", "a") as file:
            file.write(answer + "\n")
    except ValueError:  #  If the user enters a non-number
        print("Invalid input! Please enter a valid number.")

#  Function to display the list of equations        
def equations():
    if not os.path.exists("equations.txt"):
        print("No previous equations have been entered.")
        return  #  If the file doesn't exist, return to the menu
    
    #  Open the file and read the lines
    with open("equations.txt", "r") as file:
        equation_list = file.readlines()
        if not equation_list:
            print("No previous equations have been entered.")
        else:
            print("List of equations: ")
            for equation in equation_list:
                print(equation.strip())  #  Strip so only the equation is displayed

#  Function to display the menu
def menu():
    while True:
        print("\nCALCULATOR APP")
        print("\n1. Calculate")
        print("2. Equation list")
        print("3. Exit")
        
        option = input("What would you like to do? ")
        
        if option == '1':
            calculate()
        elif option == '2':
            equations()
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Please select a valid option (1, 2, or 3)")  #  If the user enters an invalid option

#  Run the menu function
if __name__ == "__main__": 
    menu()

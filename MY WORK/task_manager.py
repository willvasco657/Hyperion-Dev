#====Login Section====
def load_user():  # Function to load the user from the user.txt file
    user = {}
    with open('user.txt', 'r') as file:  # Opening the user.txt file in read mode
        for line in file:
            username, password = line.strip().split(', ')  # Splitting the username and password by the comma
            user[username] = password
    return user


users = load_user()  # Calling load_user function, storing result in users variable

while True:  # Loop to check if user is in user.txt file
    login = input("Enter your username: ")  # Asking user to enter their username
    password = input("Enter your password: ")  # Asking user to enter their password

    if login in users and users[login] == password:  # Checking if the user is in the user.txt file
        print("\nYou have successfully logged in!")
        break
    else:
        print("\nInvalid login details. Please try again")  # If user is not in the user.txt file, print this message

# ====Menu Section====
print(f"\nHello, {login}, welcome to the Task Manager Program!")
print("\n====================Main Menu====================")

while True:
    # Present the menu to the user and make sure that the user input is converted to lower case.
    if login == 'admin':  # Checking if the user is the admin
        menu = input('''\nSelect one of the following options:
            r - register a user
            a - add task
            va - view all tasks
            vm - view my tasks
            s - statistics
            e - exit
            : ''').lower()
    else:  # If the user is not the admin
        menu = input('''\nSelect one of the following options:
            a - add task
            va - view all tasks
            vm - view my tasks
            e - exit
            : ''').lower()

    if menu == 'r':  # Registering a new user
        if login == 'admin':  # Checking if the user is the admin
            username = input("Enter your username: ")
            while True:  # Loop to check if the password matches
                password = input("Enter your password: ")
                confirm_password = input("Confirm your password: ")

                if password == confirm_password:
                    print(f"\nYou have successfully registered, hello {username}!")
                    with open('user.txt', 'a') as register:
                        register.write(username + ', ' + password + '\n')  # Writing the username and password to the user.txt file
                    break
                else:
                    print("Password does not match, please try again")  # If the password does not match, print this message
        else:
            print("Only the admin user can register new users.")  # If the user is not the admin, print this message

    elif menu == 'a':  # Adding a task
        username = input("Enter the username of the person the task is assigned to: ")
        title = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task: ")
        date_assigned = input("Enter the date the task was assigned: ")
        complete = input("Is the task complete? (Yes/No): ")
        with open('tasks.txt', 'a') as task:
            task.write(username + ', ' + title + ', ' + description + ', ' +
                       due_date + ', ' + date_assigned + ', ' + complete + '\n')  # Writing the task details to the tasks.txt file
        print("Task has been successfully added")

    elif menu == 'va':  # Viewing all tasks
        with open('tasks.txt', 'r') as open_file:  # Opening the tasks.txt file in read mode
            read_file = open_file.readlines()
            for line in read_file:
                task_details = line.strip().split(', ')  # Splitting the task details by the comma
                print("________________________________________________________________________")
                print(f"\nUsername:           {task_details[0]}")
                print(f"Task:               {task_details[1]}")
                print(f"Description:        {task_details[2]}")
                print(f"Date Assigned:      {task_details[4]}")  # Printing the task details in user-friendly format
                print(f"Date Due:           {task_details[3]}")
                print(f"Complete:           {task_details[5]}")
                print("________________________________________________________________________")

    elif menu == 'vm':  # Viewing my tasks
        with open('tasks.txt', 'r') as open_file:  # Opening the tasks.txt file in read mode
            read_file = open_file.readlines()
            for line in read_file:
                task_details = line.strip().split(', ')  # Splitting the task details by the comma
                if task_details[0] == login:  # Checking if the username in the task details matches the login username
                    print("________________________________________________________________________")
                    print(f"\nUsername:           {task_details[0]}")
                    print(f"Task:               {task_details[1]}")
                    print(f"Description:        {task_details[2]}")
                    print(f"Date Assigned:      {task_details[4]}")  # Printing the task details in user-friendly format
                    print(f"Date Due:           {task_details[3]}")
                    print(f"Complete:           {task_details[5]}")
                    print("________________________________________________________________________")

    elif menu == 's':  # Viewing the statistics
        with open('tasks.txt', 'r') as open_file:
            read_file = open_file.readlines()
            total_tasks = len(read_file)  # Getting the total number of tasks
        with open('user.txt', 'r') as open_file:
            read_file = open_file.readlines()
            total_users = len(read_file)  # Getting the total number of users
        print("_________________________________________________________")
        print(f"\nTotal number of tasks: {total_tasks}")
        print(f"Total number of users: {total_users}")  # Printing the total tasks and users in user-friendly format
        print("_________________________________________________________")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
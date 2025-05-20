# Create email class
class Email:
    def __init__(self, email_address, subject_line, email_content):
        # Initialise the email object with the following attributes
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        # Set the default values for the email status attributes
        self.has_been_read = False
        self.mark_as_read = True

# Initialise an empty list to store the email objects
inbox = []

# Create a function to populate the inbox with some email objects
def populate_inbox():
    email_one = Email("spurs@football.com", "Tickets!", "Your ticket is ready to be used, please follow the instructions to access your pass.")
    email_two = Email("work@carfinance.com", "Holiday request", "Your holiday request has been declined, please contact your manager for more information.")
    email_three = Email("sunny@holiday.co.uk", "5 days to go!", "The countdown is on! 5 more days until your holiday to sunnny Portugal!")

    # Add the email objects to the inbox list
    inbox.append(email_one)
    inbox.append(email_two)
    inbox.append(email_three)    

# Create a function to list all emails in the inbox
def list_emails():
    if not inbox:
        print("Your inbox is empty.")
        return
    
    # Print the list of emails in the inbox
    for index, email in enumerate(inbox):
        print(f"{index + 1}. {email.subject_line} - {'Read' if email.has_been_read else 'Unread'}")

# Create a function to read an email
def read_email(index):
    if index < 0 or index >= len(inbox):
        print("Invalid email selection.")
        return

    # Get the email object at the specified index
    email = inbox[index]

    # Print the email details
    print(f"From: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content: {email.email_content}")

    # Mark the email as read
    email.has_been_read = True

# Populate the inbox with some email objects
populate_inbox()

# Create a menu for the user to interact with the email application
print("\nWelcome to your email application!")
menu = True

# Loop until the user chooses to quit the application
while menu:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    # Check the user's choice and perform the corresponding action   
    if user_choice == 1:
        list_emails()
        try:
            email_index = int(input("Enter the number of the email you want to read: ")) - 1
            read_email(email_index)
            print(f"\nEmail from {inbox[email_index].email_address} has been read.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Check for unread emails
    elif user_choice == 2:
        print("\nUnread Emails:")
        unread_emails = [email for email in inbox if not email.has_been_read]
        if not unread_emails:
            print("no unread emails.")
        else:
            # Print the list of unread emails
            for index, email in enumerate(unread_emails):
                print(f"{index + 1}. {email.subject_line}")
        print()

    # If the user chooses to quit the application        
    elif user_choice == 3:
        print("\nExiting the application. Goodbye!")
        menu = False

    # If the user enters an invalid choice
    else:
        print("Oops - incorrect input, please try again.")


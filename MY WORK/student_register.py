students = int(input("How many students are registering? ")) # Ask user to input number of students

with open ('reg_form.txt', 'w') as f: # Open/create txt file to write inputs
    for i in range(students): # For loop to ask for each student ID
        st_id = int(input(f"Please input student ID {i + 1}: ")) # Add each ID to list until total reached
        f.write(f"{st_id}\n") # Write the id in the txt file
        f.write("***************\n") # Create a line between each user input
    print("Thank you for registering for the exam. Good luck!")
f.close() # Close the file
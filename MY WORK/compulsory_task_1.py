# Create a class for course details
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    # Initialise the course object with the following attributes
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Create a method to get office location
    def head_office_location(self):
        print("Our head office is located in Cape Town")

# Create subclass for description and trainer details
class OOPCourse(Course):
    # Input default values for description and trainer in the constructor
    def __init__(self, description="OOP Fundamentals", trainer="MR Anon A. Mouse"):
        self.description = description
        self.trainer = trainer

    # Create a function to print details and tainer info
    def trainer_details(self):
        print(f"This course is about: {self.description}")
        print(f"Your trainer is: {self.trainer}")

    # Create a function to print course ID
    def show_course_id(self):
        print("The course ID is: #12345")

# Create object of subclass OOPCourse
course_1 = OOPCourse()

# Call the methods to display course details
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
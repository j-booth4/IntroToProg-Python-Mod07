# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Jocelyne, 8/17/2024, Editing Starter code

# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# Create a Person Class
class Person:
    '''
    A collection of functions that organize information about a person's first name and last name.
    Changelog: Jocelyne, 8/17/24, created the Person class.
    '''

    # Add first_name and last_name properties to the constructor (Done)
    def __init__(self, first_name:str = "", last_name:str = ""):
        '''
        This function initializes the person object.
        :param first_name: The first name property of the person.
        :param last_name: The last name property of the person.
        '''
        # Set the private variables of first_name and last_name using the parameters.
        self._first_name = first_name
        self._last_name = last_name

    # getter of the first_name property
    @property
    def first_name(self):
        '''
        This function gets the first_name property of the Person
        :return: First name property of the Person
        '''
        return self._first_name  # returns the private variable _first_name

    @first_name.setter
    def first_name(self, name:str):
        '''
        This string sets the first name of the person.
        :param name: the string to be used for the Person's first_name property
        '''
        # sets the first name if it's alphabetical characters only.
        if name.isalpha() or name == "":
            self._first_name = name
        else:  # if numbers are present, will display an error
            raise ValueError("First name must be alphabet characters only.")

    # getter for the last_name property (Done)
    @property
    def last_name(self):
        '''
        This function gets the last name of the Person
        :return: the last_name propertu of the Person
        '''
        return self._last_name

    # setter for the last_name property
    @last_name.setter
    def last_name(self, name:str):
        '''
        This function sets the last_name of a Person.
        :param name: the string used as the Person's last name
        '''
        if name.isalpha() or name == "":
            self._last_name = name
        # If the user enters non-alphabetical characters, error will occur
        else:
            raise ValueError("Last name must be alphabet characters only.")

    # Override the __str__() method to return Person data (Done)
    def __str__(self):
        '''
        This function overrides the __str__ method of the Person class to output comma-separated data
        :return: Person properties output as comma-separated data
        '''
        return f"{self._first_name},{self._last_name}"


# Create a Student class the inherits from the Person class (Done)
class Student(Person):
    '''
    A collection of functions inherited from Person. There are additional functions to account
    for the course_name property.

    Changelog: Jocelyne, 8/17/2024, created Student class
    '''

    # call to the Person constructor and pass it the first_name and last_name data (Done)
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        '''
        This initialization function creates a Student object, inheriting the Person class initializer.
        ::param first_name: student's first name
        ::param last_name:  student's last name
        ::param course_name: student's course name'
        '''
        # Use the inherited initializer since Student inherits Person's functions
        super().__init__(first_name, last_name)
        # add a assignment to the course_name property using the course_name parameter (Done)
        self._course_name = course_name

    # add the getter for course_name (Done)
    @property
    def course_name(self):
        '''
        This function returns the course_name property.
        :return: course_name string
        '''
        return self._course_name

    # add the setter for course_name (Done)
    @course_name.setter
    def course_name(self, name:str = ""):
        '''
        This function sets the course_name property.
        ::param name: the string used to set the course_name property
        '''
        self._course_name = name

# Override the __str__() method to return the Student data (Done)
    def __str__(self):
        '''
        This function prints out the Student object as a string in comma-separated variable format.
        :return: Student object properties formatted as a string
        '''
        return f"{self._first_name},{self._last_name},{self._course_name}"



# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list[Student]):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Jocelyne, 8/17/24, edit to import data as a list of Student objects

        :param file_name: string data with name of file to read from
        :param student_data: list of Students to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")
            # Import the data into a temporary list of dict entries
            temp_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        # Make student_data be a list of Students
        for entry in temp_data:
            # Create each student as a Student using the Student creation function
            student = Student(entry["FirstName"], entry["LastName"], entry["CourseName"])
            student_data.append(student)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Jocelyne, 8/17/24, Save list of Student objects as a list of Dictionaries w/ correct keys

        :param file_name: string data with name of file to write to
        :param student_data: list of Students to be writen to the file

        :return: None
        """

        try:
            file = open(file_name, "w")
            list_of_students: list = []
            # Convert the list of Students to a list of dict entries
            for student in student_data:
                entry: dict = {"FirstName": student.first_name, "LastName": student.last_name, "CourseName": student.course_name}
                list_of_students.append(entry)
            # write the list of JSON-formatted entries into the JSON file
            json.dump(list_of_students, file)
            print('Finished writing data to file. New data:')
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list[Student]):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Jocelyne, 8/17/24, edited to read properties of each Student

        :param student_data: list of Students to be displayed

        :return: None
        """
        print("-" * 50)
        for student in student_data:
            # Print the student using the new Student string printing function.
            print(student)
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Jocelyne, 8/17/24, edited to create each student as a Student using inputs as parameters

        :param student_data: list of Students to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            # Modified the creation of each student to be of the Student class
            student = Student(student_first_name, student_last_name,course_name)
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the incorrect type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

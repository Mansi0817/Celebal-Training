class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)

    def is_passed(self):
        return self.marks >= 40


# Creating an object
s1 = Student("Mansi", 101, 85)

# Calling methods
s1.display_info()

if s1.is_passed():
    print("Result: Passed")
else:
    print("Result: Failed")
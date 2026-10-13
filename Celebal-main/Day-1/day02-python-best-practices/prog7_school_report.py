# Program 7: School Report App
# Collects three students' marks, prints individual reports, and class averages.

SCHOOL_NAME = "New School Of Learning"
CLASS_NAME = "XI"
SUBJECTS = ("Physics", "Chemistry", "Mathematics")
MAX_MARKS_PER_SUBJECT = 50
NUMBER_OF_STUDENTS = 3
TOTAL_POSSIBLE_MARKS = len(SUBJECTS) * MAX_MARKS_PER_SUBJECT

students = []

for student_number in range(1, NUMBER_OF_STUDENTS + 1):
    print(f"\nEnter details for student {student_number}")
    student_name = input(f"Enter name of student {student_number}: ").strip()

    marks = {}
    for subject in SUBJECTS:
        while True:
            try:
                mark = float(
                    input(
                        f"Enter {subject} marks out of {MAX_MARKS_PER_SUBJECT} "
                        f"for student {student_number}: "
                    )
                )
                if 0 <= mark <= MAX_MARKS_PER_SUBJECT:
                    marks[subject] = mark
                    break
                print(f"Marks must be between 0 and {MAX_MARKS_PER_SUBJECT}.")
            except ValueError:
                print("Please enter a valid number.")

    students.append({"name": student_name, "marks": marks})

    total_obtained = sum(marks.values())
    total_percentage = total_obtained / TOTAL_POSSIBLE_MARKS * 100
    line = "-" * 74

    print(f"\n{SCHOOL_NAME} - Class {CLASS_NAME} - {student_name}")
    print(line)
    print(
        f"| {'Subject':^16} | {'Total Marks':^13} | "
        f"{'Marks Obtained':^14} | {'Percentage':^13} |"
    )
    print(line)

    for subject in SUBJECTS:
        mark = marks[subject]
        percentage = mark / MAX_MARKS_PER_SUBJECT * 100
        print(
            f"| {subject:^16} | {MAX_MARKS_PER_SUBJECT:^13} | "
            f"{mark:^14.0f} | {percentage:^13.2f} |"
        )

    print(line)
    print(
        f"| {'Total':^16} | {TOTAL_POSSIBLE_MARKS:^13} | "
        f"{total_obtained:^14.0f} | {total_percentage:^13.2f} |"
    )
    print(line)

print("\nClass Average And Percentage for Each Subject:")
all_marks = [sum(student["marks"].values()) for student in students]
for subject in SUBJECTS:
    subject_total = sum(student["marks"][subject] for student in students)
    subject_average = subject_total / NUMBER_OF_STUDENTS
    subject_percentage = subject_average / MAX_MARKS_PER_SUBJECT * 100
    print(
        f"{subject} Average is {subject_average:.2f} "
        f"and Percentage is {subject_percentage:.2f}%"
    )

overall_obtained = sum(all_marks)
overall_possible = NUMBER_OF_STUDENTS * TOTAL_POSSIBLE_MARKS
overall_percentage = overall_obtained / overall_possible * 100
print(f"Overall Percentage: {overall_percentage:.2f}%")

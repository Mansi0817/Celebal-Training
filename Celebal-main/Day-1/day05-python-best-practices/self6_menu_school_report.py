# Self Practice 6: Menu-Based School Report (Percentage / Grade)

SCHOOL_NAME = "New School Of Learning"
CLASS_NAME = "XI"
SUBJECTS = ("Physics", "Chemistry", "Mathematics")


def percentage_to_grade(percentage: float) -> str:
    """Convert a percentage to a grade using a simple grade scale."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def publish_student_report(
    student_name: str,
    marks: dict[str, float],
    max_marks: float = 100,
    computation_type: str = "p",
) -> None:
    """Print one student's report as percentages or grades."""
    if max_marks <= 0:
        raise ValueError("Maximum marks must be greater than zero.")

    total_obtained = sum(marks.values())
    total_possible = max_marks * len(SUBJECTS)
    overall_percentage = total_obtained / total_possible * 100

    print(f"\\n{SCHOOL_NAME} - Class {CLASS_NAME} - {student_name}")
    line = "-" * 73

    if computation_type.lower() == "g":
        print("-" * 34)
        print(f"| {'Subject':^16} | {'Grade':^10} |")
        print("-" * 34)
        for subject in SUBJECTS:
            subject_percentage = marks[subject] / max_marks * 100
            print(f"| {subject:^16} | {percentage_to_grade(subject_percentage):^10} |")
        print("-" * 34)
        print(f"| {'Total':^16} | {percentage_to_grade(overall_percentage):^10} |")
        print("-" * 34)
    elif computation_type.lower() == "p":
        print(line)
        print(
            f"| {'Subject':^16} | {'Total Marks':^13} | "
            f"{'Marks Obtained':^14} | {'Percentage':^13} |"
        )
        print(line)
        for subject in SUBJECTS:
            subject_percentage = marks[subject] / max_marks * 100
            print(
                f"| {subject:^16} | {max_marks:^13.0f} | "
                f"{marks[subject]:^14.0f} | {subject_percentage:^12.2f}% |"
            )
        print(line)
        print(
            f"| {'Total':^16} | {total_possible:^13.0f} | "
            f"{total_obtained:^14.0f} | {overall_percentage:^12.2f}% |"
        )
        print(line)
    else:
        raise ValueError("Computation type must be 'p' or 'g'.")


try:
    student_name = input("Enter student's name: ").strip()
    max_marks = float(input("Enter max marks per subject: "))
    student_marks = {}
    for subject in SUBJECTS:
        student_marks[subject] = float(input(f"Enter {subject.lower()} marks: "))
    computation_type = input(
        "Enter computation type (g for grades, p for percentage): "
    ).strip().lower() or "p"

    if any(mark < 0 or mark > max_marks for mark in student_marks.values()):
        raise ValueError("Each subject mark must be between 0 and the maximum marks.")

    publish_student_report(student_name, student_marks, max_marks, computation_type)
except ValueError as error:
    print(f"Invalid input: {error}")

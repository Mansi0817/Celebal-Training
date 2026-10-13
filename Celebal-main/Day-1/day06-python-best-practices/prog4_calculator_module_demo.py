# Day 04 - Program 4: Use the custom my_calculator module
import my_calculator

try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    print(f"Sum: {my_calculator.add(first_number, second_number):g}")
    print(f"Difference: {my_calculator.subtract(first_number, second_number):g}")
    print(f"Product: {my_calculator.multiply(first_number, second_number):g}")
    print(f"Quotient: {my_calculator.divide(first_number, second_number)}")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError as error:
    print(f"Error: {error}")

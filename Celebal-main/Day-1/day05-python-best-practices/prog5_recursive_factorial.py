# Program 5: Recursive Factorial Function

def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer using recursion."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


try:
    number = int(input("Enter the number to find the factorial : "))
    print(f"Factorial of {number} is: {factorial(number)}")
except ValueError as error:
    print(f"Invalid input: {error}")

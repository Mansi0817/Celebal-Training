# Program 3: Define and reuse a function

def add_numbers(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


result = add_numbers(10, 20)
print(f"Sum: {result}")

another_result = add_numbers(50, 60)
print(f"Another sum: {another_result}")
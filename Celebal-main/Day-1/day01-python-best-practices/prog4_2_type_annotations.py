# Program 4.2: Function parameter type annotations

def calculate_average(first_number: float, second_number: float) -> float:
    """Return the average of two numbers."""
    return (first_number + second_number) / 2


average = calculate_average(10.0, 20.0)
print(f"Average: {average:.2f}")
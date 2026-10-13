# Program 3: Compute Average

def calculate_average(numbers: list[float]) -> float:
    """Return the average of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("The list must contain at least one number.")
    return sum(numbers) / len(numbers)


number_list = [10, 20, 30, 40, 50]
print(f"Original List : {number_list}")
print(f"\nAverage of the List is {calculate_average(number_list)}")

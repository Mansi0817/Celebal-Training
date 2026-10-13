# Program 4: Return Multiple Values

def find_min_max(numbers: list[float]) -> tuple[float, float]:
    """Return the minimum and maximum values in a non-empty list."""
    if not numbers:
        raise ValueError("The list must contain at least one number.")
    return min(numbers), max(numbers)


number_list = [10, 5, 20, 15, 30]
minimum_number, maximum_number = find_min_max(number_list)

print(f"Original List : {number_list}")
print(f"Minimum number in a List is  {minimum_number}")
print(f"Maximum number in a List is  {maximum_number}")

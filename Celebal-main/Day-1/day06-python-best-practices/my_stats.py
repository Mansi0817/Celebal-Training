"""Custom statistics module without importing a statistics library."""
import math

def mean(numbers: list[float]) -> float:
    """Calculate the arithmetic mean."""
    if not numbers:
        raise ValueError("Cannot calculate the mean of an empty list.")
    return sum(numbers) / len(numbers)

def variance(numbers: list[float]) -> float:
    """Calculate population variance."""
    average = mean(numbers)
    return sum((number - average) ** 2 for number in numbers) / len(numbers)

def standard_deviation(numbers: list[float]) -> float:
    """Calculate population standard deviation."""
    return math.sqrt(variance(numbers))

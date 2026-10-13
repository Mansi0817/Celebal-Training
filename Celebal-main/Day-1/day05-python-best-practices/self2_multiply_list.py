# Self Practice 2: Multiply Elements in a List

def multiply_all(numbers: list[float]) -> float:
    """Return the product of all numbers in a list."""
    product = 1
    for number in numbers:
        product *= number
    return product


number_list = [10, 2, 3]
print(f"Original List : {number_list}")
print(f"\nResult After Multiplying Elements In The List : {multiply_all(number_list)}")

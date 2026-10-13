# Self Practice 5: Count Down Using Recursion

def count_down(number: int) -> None:
    """Print number down to zero using recursion."""
    print(number)
    if number > 0:
        count_down(number - 1)


try:
    starting_number = int(input("Enter the number to print the count down: "))
    if starting_number < 0:
        print("Please enter a non-negative integer.")
    else:
        count_down(starting_number)
except ValueError:
    print("Please enter a valid integer.")

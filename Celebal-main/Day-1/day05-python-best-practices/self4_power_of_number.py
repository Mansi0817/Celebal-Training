# Self Practice 4: Power of Number

def calculate_power(base_number: float, exponent_number: int) -> float:
    """Return base_number raised to exponent_number."""
    return base_number ** exponent_number


try:
    base_number = float(input("Enter the Base Number: "))
    exponent_number = int(input("Enter the Exponent Number: "))
    print(
        f"{base_number:g} raised to the power of {exponent_number} "
        f"is: {calculate_power(base_number, exponent_number):g}"
    )
except ValueError:
    print("Please enter a valid number and an integer exponent.")

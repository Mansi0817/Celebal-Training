# Self Practice 1: Calculator App

def calculate(first_number: float, operator: str, second_number: float) -> float:
    """Calculate a result using +, -, *, or /."""
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    else:
        raise ValueError("Unsupported operator. Use +, -, *, or /.")


try:
    operator = input("Enter the symbol for the computation (+, -, *, /): ").strip()
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    print(f"Result: {calculate(first_number, operator, second_number)}")
except (ValueError, ZeroDivisionError) as error:
    print(f"Error: {error}")

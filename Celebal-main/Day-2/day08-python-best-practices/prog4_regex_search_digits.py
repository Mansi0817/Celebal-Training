# Program 4: Search Digits Using Regular Expressions

import re


def find_digits(input_string):
    """Find all digits present in a string using regex."""
    digits = re.findall(r"\d", input_string)

    if digits:
        print("Digits found:", digits)
    else:
        print("No digits found.")


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    find_digits(input_string)
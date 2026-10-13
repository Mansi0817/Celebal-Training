# Program 5: Email Validation Using Regular Expressions

import re


def validate_email(email):
    """Check whether an email address has a valid basic format."""
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.fullmatch(pattern, email):
        print(f"{email} is a Valid Email Address.")
    else:
        print(f"{email} is an Invalid Email Address.")


if __name__ == "__main__":
    email = input("Enter an email address: ")
    validate_email(email)
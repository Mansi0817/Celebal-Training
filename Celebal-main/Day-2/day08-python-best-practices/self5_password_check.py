# Self Practice Program 5: Password Check

import re


def check_password(password):
    """Validate a password using the given password policy."""

    pattern = (
        r"^(?=.*[A-Z])"
        r"(?=.*[a-z])"
        r"(?=.*\d)"
        r"(?=.*[@#$%^&*])"
        r"[A-Za-z][A-Za-z0-9@#$%^&*]{7,}$"
    )

    if re.fullmatch(pattern, password):
        print("Password is valid.")
    else:
        print("Password is invalid.")


if __name__ == "__main__":
    password = input("Enter your password: ")
    check_password(password)
# Program 3.1: Counting Letters, Digits, and Special Symbols
# Using Explicit Loops

def count_characters(input_string):
    """Count letters, digits, and special symbols in a string."""

    letter_count = 0
    digit_count = 0
    special_count = 0

    for character in input_string:
        if character.isalpha():
            letter_count += 1
        elif character.isdigit():
            digit_count += 1
        else:
            special_count += 1

    print(f"Number of letters: {letter_count}")
    print(f"Number of digits: {digit_count}")
    print(f"Number of special symbols: {special_count}")


if __name__ == "__main__":
    input_string = input("Input String: ")
    count_characters(input_string)
# Program 3.2: Counting Letters, Digits, and Special Symbols
# Using List Comprehension

def count_characters(input_string):
    """Count letters, digits, and special symbols using comprehensions."""

    letters = [
        character for character in input_string
        if character.isalpha()
    ]

    digits = [
        character for character in input_string
        if character.isdigit()
    ]

    special_symbols = [
        character for character in input_string
        if not character.isalpha() and not character.isdigit()
    ]

    print(f"Number of letters: {len(letters)}")
    print(f"Number of digits: {len(digits)}")
    print(f"Number of special symbols: {len(special_symbols)}")


if __name__ == "__main__":
    input_string = input("Input String: ")
    count_characters(input_string)
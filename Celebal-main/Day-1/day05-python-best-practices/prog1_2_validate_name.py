# Program 1.2: Validate user input

def is_valid_name(friend_name: str) -> bool:
    """Return True if the name contains alphabetic characters only."""
    return bool(friend_name) and friend_name.isalpha()


friend_name = input("Enter your friend's name: ").strip()

if is_valid_name(friend_name):
    print(f"Hello, {friend_name}! How are you today?")
else:
    print("Please enter a valid name with alphabetic characters only.")

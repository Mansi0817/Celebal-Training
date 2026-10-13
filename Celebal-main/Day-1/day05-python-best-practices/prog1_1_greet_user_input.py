# Program 1.1: Take the user's input

def greet_friend(friend_name: str) -> None:
    """Print a greeting for a friend's name."""
    print(f"Hello, {friend_name}! How are you today?")


friend_name = input("Enter your friend's name: ").strip()
if friend_name:
    greet_friend(friend_name)
else:
    print("Please enter a name.")

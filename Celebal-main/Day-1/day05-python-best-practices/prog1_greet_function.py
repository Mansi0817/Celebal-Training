# Day 03 - Program 1: Greet Function

def greet_friend(friend_name: str, greeting: str = "Hello") -> None:
    """Print a friendly greeting for the given person."""
    print(f"{greeting}, {friend_name}! How are you today?")


greet_friend("Alice", "Hi")
greet_friend("Bob")
greet_friend("Charlie", "Namaskar")

# Self Practice 4: Number Guessing Game
import random

def play_guessing_game() -> None:
    """Give the player ten chances to guess a number from 1 to 100."""
    secret_number = random.randint(1, 100)
    chances = 10
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. You have 10 chances to guess it.")

    while chances > 0:
        guess_text = input("\nEnter your guess (between 1 and 100): ").strip()
        if not guess_text.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess_text)
        if not 1 <= guess <= 100:
            print("Please enter a number from 1 to 100.")
            continue

        chances -= 1
        if guess == secret_number:
            print(f"Congratulations! You guessed the number correctly: {secret_number}")
            return
        if guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        if chances:
            print(f"Chances left: {chances}")

    print(f"You are out of chances. The number was {secret_number}.")

play_guessing_game()

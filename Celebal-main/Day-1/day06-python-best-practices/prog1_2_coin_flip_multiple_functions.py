# Day 04 - Program 1.2: Random Module, multiple functions
import random

def flip_coin() -> str:
    """Randomly return Head or Tail."""
    return random.choice(["Head", "Tail"])

def count_heads(number_of_flips: int) -> int:
    """Return the number of heads in the requested number of flips."""
    return sum(flip_coin() == "Head" for _ in range(number_of_flips))

def run_flip_a_coin(number_of_flips: int) -> None:
    """Print the percentage of heads from repeated coin flips."""
    if number_of_flips <= 0:
        raise ValueError("Number of flips must be greater than zero.")
    heads_count = count_heads(number_of_flips)
    heads_percentage = heads_count / number_of_flips * 100
    print(
        f"After flipping the coin {number_of_flips} times, "
        f"the percentage of times head has come is: {heads_percentage:.2f}%"
    )

try:
    flips = int(input("Enter the number of times to flip the coin : "))
    run_flip_a_coin(flips)
except ValueError as error:
    print(f"Invalid input: {error}")

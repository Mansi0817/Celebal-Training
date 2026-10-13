# Day 04 - Program 1.1: Random Module, single function
import random

def flip_coin() -> str:
    """Return either Head or Tail."""
    return random.choice(["Head", "Tail"])

def run_flip_a_coin(number_of_flips: int) -> None:
    """Flip a coin repeatedly and print the percentage of heads."""
    if number_of_flips <= 0:
        raise ValueError("Number of flips must be greater than zero.")
    heads_count = sum(flip_coin() == "Head" for _ in range(number_of_flips))
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

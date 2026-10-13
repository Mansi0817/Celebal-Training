# Self Practice 3: Check Prime

def is_prime(number: int) -> bool:
    """Return whether a number is prime."""
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


print("Prime numbers between 1 and 100:")
print(*(number for number in range(1, 101) if is_prime(number)))

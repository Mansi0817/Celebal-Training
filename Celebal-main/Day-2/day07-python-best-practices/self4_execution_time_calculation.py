# Self Practice 4: Execution Time Calculation

import random
import time


def is_prime(number):
    """Check whether a number is prime."""
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def generate_random_numbers(size):
    """Generate random integers between 1 and 100."""
    return [random.randint(1, 100) for _ in range(size)]


def remove_primes(numbers):
    """Remove prime numbers by checking each number."""
    return [number for number in numbers if not is_prime(number)]


def remove_primes_optimized(numbers, prime_numbers):
    """Remove prime numbers using a precomputed set."""
    return [number for number in numbers if number not in prime_numbers]


def calculate_execution_time(size):
    """Measure execution time for both approaches."""

    print(f"\nComputing execution time for list size: {size}")

    # Generate random numbers
    start_time = time.perf_counter()
    numbers = generate_random_numbers(size)
    generation_time = time.perf_counter() - start_time

    # Original approach
    start_time = time.perf_counter()
    result_original = remove_primes(numbers)
    original_time = time.perf_counter() - start_time

    # Precompute prime numbers between 1 and 100
    prime_numbers = {
        number for number in range(1, 101)
        if is_prime(number)
    }

    # Optimized approach
    start_time = time.perf_counter()
    result_optimized = remove_primes_optimized(
        numbers, prime_numbers
    )
    optimized_time = time.perf_counter() - start_time

    # Verify both methods give the same result
    print(f"Results match: {result_original == result_optimized}")

    print(
        f"Time taken to generate random numbers: "
        f"{generation_time:.6f} seconds"
    )
    print(
        f"Time to remove primes (original): "
        f"{original_time:.6f} seconds"
    )
    print(
        f"Time to remove primes (optimized): "
        f"{optimized_time:.6f} seconds"
    )
    print(
        f"Time saved: {original_time - optimized_time:.6f} seconds"
    )


# Test all three list sizes
for list_size in [100, 10_000, 100_000]:
    calculate_execution_time(list_size)
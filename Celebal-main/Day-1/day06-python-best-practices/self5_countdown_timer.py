# Self Practice 5: Countdown Timer
import time

def countdown_timer(total_seconds: int) -> None:
    """Display a countdown in MM:SS format."""
    if total_seconds < 0:
        raise ValueError("Timer duration cannot be negative.")
    for remaining_seconds in range(total_seconds, 0, -1):
        minutes, seconds = divmod(remaining_seconds, 60)
        print(f"Time Remaining: {minutes:02d}:{seconds:02d}", end="\\r", flush=True)
        time.sleep(1)
    print("Time Remaining: 00:00")
    print("Time's up!")

try:
    duration = int(input("Enter the timer in seconds : "))
    countdown_timer(duration)
except ValueError as error:
    print(f"Invalid input: {error}")

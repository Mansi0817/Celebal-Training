# Program 5: Convert seconds to HH:MM:SS

total_seconds = int(input("Enter the time duration in seconds: "))

if total_seconds < 0:
    print("Please enter a non-negative number of seconds.")
else:
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(
        f"Time duration of {total_seconds} seconds in HH:MM:SS format "
        f"is {hours:02d}:{minutes:02d}:{seconds:02d}"
    )

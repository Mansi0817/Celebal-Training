# Self Practice 6: Calendar Module
import calendar

def print_month_calendar(month: int, year: int) -> None:
    """Print the calendar for a given month and year."""
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12.")
    print(f"\n{calendar.month_name[month]} {year}")
    print("Mo Tu We Th Fr Sa Su")
    for week in calendar.monthcalendar(year, month):
        print(" ".join(f"{day:2d}" if day else "  " for day in week).rstrip())

try:
    month = int(input("Enter the month (1-12) : "))
    year = int(input("Enter the year (Ex. 2024) : "))
    print_month_calendar(month, year)
except ValueError as error:
    print(f"Invalid input: {error}")

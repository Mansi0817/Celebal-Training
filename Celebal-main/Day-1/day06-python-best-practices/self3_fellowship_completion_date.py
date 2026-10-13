# Self Practice 3: Fellowship Completion Date
from datetime import date, timedelta

today = date.today()
days_until_monday = (0 - today.weekday()) % 7
if days_until_monday == 0:
    days_until_monday = 7
start_date = today + timedelta(days=days_until_monday)
completion_date = start_date + timedelta(weeks=12)

print(f"Fellowship start date: {start_date}")
print(f"Fellowship completion date: {completion_date}")

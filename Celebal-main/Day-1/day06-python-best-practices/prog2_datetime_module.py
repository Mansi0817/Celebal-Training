# Day 04 - Program 2: DateTime Module
from datetime import datetime

current_datetime = datetime.now()
print(f"Current Date and Time: {current_datetime}")
print("Formatted Date and Time:")
print(f"Month (as full name): {current_datetime.strftime('%B')}")
print(f"Weekday (as full name): {current_datetime.strftime('%A')}")
print(f"Year (as four digits): {current_datetime.strftime('%Y')}")
print(f"Month (as abbreviated name): {current_datetime.strftime('%b')}")
print(f"Weekday (as abbreviated name): {current_datetime.strftime('%a')}")
print(f"Year (as two digits): {current_datetime.strftime('%y')}")
print(f"Day of the month (01-31): {current_datetime.strftime('%d')}")
print(f"Hour (24-hour clock): {current_datetime.strftime('%H')}")
print(f"Hour (12-hour clock): {current_datetime.strftime('%I')}")
print(f"Minute (00-59): {current_datetime.strftime('%M')}")
print(f"Second (00-59): {current_datetime.strftime('%S')}")
print(f"AM/PM indicator: {current_datetime.strftime('%p')}")

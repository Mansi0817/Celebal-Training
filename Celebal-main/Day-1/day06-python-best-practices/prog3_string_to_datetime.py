# Day 04 - Program 3: Convert String Into Date Object
from datetime import datetime

date_string = "22 Jun 2024"
date_object = datetime.strptime(date_string, "%d %b %Y")

print(f"Date as Date String: {date_string}")
print(type(date_string))
print(f"\nDate as DateTime object: {date_object}")
print(type(date_object))

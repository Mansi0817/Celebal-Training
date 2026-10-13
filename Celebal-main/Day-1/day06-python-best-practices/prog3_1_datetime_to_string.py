# Day 04 - Program 3.1: Convert Date Object Into String
from datetime import datetime

date_string = "22 Jun 2024"
date_object = datetime.strptime(date_string, "%d %b %Y")
converted_string = date_object.strftime("%d %b %Y")

print(f"Date as Date String: {date_string}")
print(type(date_string))
print(f"\nDate as DateTime object: {date_object}")
print(type(date_object))
print(f"\nDate back to as Date String: {converted_string}")
print(type(converted_string))

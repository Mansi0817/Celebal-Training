# Program 2: Places to Visit
# Demonstrates input(), f-strings, and print() formatting.

user_name = input("Enter the user name: ").strip()
first_place = input("Enter the first place you would like to visit: ").strip()
second_place = input("Enter the second place you would like to visit: ").strip()
third_place = input("Enter the third place you would like to visit: ").strip()
visit_year = input("Enter the year to visit: ").strip()

print(f"Hello {user_name} and places to visit are ", end="")
print(first_place, second_place, third_place, sep=", ", end="")
print(f" in the year {visit_year}")

# Program 4: Find Generation

birth_year = int(input("Enter Birth Year: "))

is_baby_boomer = 1946 <= birth_year <= 1964
is_gen_x = 1965 <= birth_year <= 1980
is_millennial = 1981 <= birth_year <= 1996
is_gen_z = 1997 <= birth_year <= 2012
is_gen_alpha = 2013 <= birth_year <= 2025

print(f"\nBirth Year is {birth_year}")
print(f"Is Baby Boomer: {is_baby_boomer}")
print(f"Is Gen X: {is_gen_x}")
print(f"Is Millennial: {is_millennial}")
print(f"Is Gen Z: {is_gen_z}")
print(f"Is Gen Alpha: {is_gen_alpha}")

if not 1946 <= birth_year <= 2025:
    print("Note: The supplied notes do not define a generation for this year.")

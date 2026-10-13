# Self Practice 5: Compute Square Root

number = float(input("Enter a number: "))

if number < 0:
    print("Please enter a non-negative number.")
else:
    square_root = number ** 0.5
    print(f"The square root of {number:.2f} is {square_root:.2f}")

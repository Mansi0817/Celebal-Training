# Self Practice 7: Perimeter and Area of a Rectangle
# Inputs are centimeters; outputs are inches and square inches.

CM_PER_INCH = 2.54

length_cm = float(input("Enter length in centimeters: "))
breadth_cm = float(input("Enter breadth in centimeters: "))

if length_cm < 0 or breadth_cm < 0:
    print("Length and breadth must be non-negative.")
else:
    perimeter_cm = 2 * (length_cm + breadth_cm)
    area_sq_cm = length_cm * breadth_cm

    perimeter_inches = perimeter_cm / CM_PER_INCH
    area_sq_inches = area_sq_cm / (CM_PER_INCH ** 2)

    print(f"Perimeter of the rectangle is {perimeter_inches:.2f} inches")
    print(f"Area of the rectangle is {area_sq_inches:.2f} square inches")

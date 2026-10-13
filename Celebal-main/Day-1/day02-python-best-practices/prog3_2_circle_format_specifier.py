# Program 3.2: Circle calculations with formatted output

PI = 22 / 7
CM_PER_INCH = 2.54

radius_inches = float(input("Enter the radius of the circle in inches: "))
radius_cm = radius_inches * CM_PER_INCH

circumference_cm = 2 * PI * radius_cm
area_sq_cm = PI * (radius_cm ** 2)

print(
    f"Circumference of the Circle is {circumference_cm:.2f} cm "
    f"and Area of the Circle is {area_sq_cm:.2f} sqcm"
)

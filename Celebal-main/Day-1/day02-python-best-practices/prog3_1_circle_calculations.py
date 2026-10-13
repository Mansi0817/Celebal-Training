# Program 3.1: Circumference and Area of a Circle
# The radius is entered in inches; results are converted to centimeters.

PI = 22 / 7
CM_PER_INCH = 2.54

radius_inches = float(input("Enter the radius of the circle in inches: "))
radius_cm = radius_inches * CM_PER_INCH

circumference_cm = 2 * PI * radius_cm
area_sq_cm = PI * (radius_cm ** 2)

print(f"Circumference of the Circle is {circumference_cm} cm and")
print(f"Area of the Circle is {area_sq_cm} sqcm")

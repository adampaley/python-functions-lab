# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.

def calculate_area_triangle(base, height):
    try:
        base = float(base)
        height = float(height)
        return base * height / 2
    except TypeError:
        print("TypeError: Must enter numeric inputs.")

print('Exercise 1:', calculate_area_triangle(10, 5))
print('Exercise 1:', calculate_area_triangle(7, 3))

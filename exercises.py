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
        if base <= 0 or height <= 0:
            return print("Invalid Input: Must enter positive numeric inputs.")
        return f'{base * height / 2} units^2'
    except ValueError:
        print("ValueError: Must enter numeric inputs.")

print('Exercise 1:', calculate_area_triangle(10, 5))
print('Exercise 1:', calculate_area_triangle(7, 3))

# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.

def simple_interest (principal, rate, time):
    try:
        principal = float(principal)
        rate = float(rate)
        time = int(time)
        if principal < 0 or rate < 0 or time < 0:
            return print("Invalid Input: Must enter non-negative numeric inputs.")
        interest = principal * rate * time / 100
        return f'{int(interest)} units/year' if interest.is_integer() else f'{interest} units/year'

    except TypeError:
        print("TypeError: Must enter numeric inputs.")

print('Exercise 2:', simple_interest(1000, 5, 2))
print('Exercise 2:', simple_interest(1500, 3.5, 5))

# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.

def apply_discount (price, discount):
    try:
        price = float(price)
        discount = float(discount)/100
        if price <= 0 or discount <= 0:
            return print("Invalid Input: Must enter positive numeric inputs.")
        elif discount > 100:
            return print("Invalid Input: Price cannot be discounted beyond free.")
        new_price = (price - (price*discount))
        return f'${int(new_price)}' if new_price.is_integer() else f'${new_price}'
    except ValueError:
        print("ValueError: Must enter numeric inputs.")

print('Exercise 3:', apply_discount(100, 25))
print('Exercise 3:', apply_discount(80, 10))
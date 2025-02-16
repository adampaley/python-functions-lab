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
        return

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
        return

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
        return

print('Exercise 3:', apply_discount(100, 25))
print('Exercise 3:', apply_discount(80, 10))

# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.
def convert_temperature (temperature, original_unit, converted_unit):
    TEMPERATURE_UNITS = ('C', 'F', 'K')
    FULL_TEMPERATURE_UNITS = ("Celsius", "Fahrenheit", "Kelvin")
    try:
        temperature = float(temperature)
        if original_unit.strip().upper() and converted_unit.strip().upper() in TEMPERATURE_UNITS:
            original_unit = original_unit.strip().upper()
            converted_unit = converted_unit.strip().upper()
        elif original_unit.capitalize() or converted_unit.capitalize() in FULL_TEMPERATURE_UNITS:
            original_unit = original_unit.strip()[0:1].upper()
            converted_unit = converted_unit.strip()[0:1].upper()


        if original_unit not in TEMPERATURE_UNITS:
            print("Invalid Input: Temperature must be given in units of Celsius (C) or Fahrenheit (F).")
            return

        if (temperature < -273.15 and original_unit == "C") or (temperature < -459.67 and original_unit == "F") or (temperature < 0 and original_unit == "K"):
            print("Invalid Input: Temperature cannot be below absolute zero.")
            return
        
        if (original_unit == "C" and converted_unit == "F"):
            converted_value = f'{(temperature * 9/5) + 32}°F'
        elif (original_unit == "F" and converted_unit == "C"):
            converted_value = f'{(temperature - 32) * 5/9}°C'
        elif (original_unit == "C" and converted_unit == "K"):
            converted_value = f'{temperature + 273.15}K'
        elif (original_unit == "K" and converted_unit == "C"):
            converted_value = f'{temperature - -273.15}°C'
        elif (original_unit == "F" and converted_unit == "K"):
            converted_value = f'{(temperature - 32) * 5/9 + 273.15}K'
        else:
            converted_value = f'{((temperature - 273.15) * 9/5) + 32}°F'
        return converted_value
    except ValueError:
        print("ValueError: Temperature must be given as a numeric value, and unit must be given as 'C' or 'F'.")
        return

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(-0, 'C', 'F'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F', 'C'))
print('Exercise 4: Convert -200°C to Kelvin:', convert_temperature(-200, 'C', 'K'))
print('Exercise 4: Convert 100K to Celsius:', convert_temperature(100, 'K', 'C'))
print('Exercise 4: Convert -320°F to Kelvin', convert_temperature(-350, 'F', 'K'))
print('Exercise 4: Convert 300K to Fahrenheit', convert_temperature(300, 'K', 'F'))
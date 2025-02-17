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
        return None

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
        interest = round(principal * rate * time / 100, 2)
        return f'{int(interest)} units/year' if interest.is_integer() else f'{interest} units/year'

    except ValueError:
        print("ValueError: Must enter numeric inputs.")
        return None

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
        new_price = round((price - (price*discount)), 2)
        return f'${int(new_price)}' if new_price.is_integer() else f'${new_price}'
    except ValueError:
        print("ValueError: Must enter numeric inputs.")
        return None

print('Exercise 3:', apply_discount(100, 25))
print('Exercise 3:', apply_discount(80, 11))

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
        return None

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(-0, 'C', 'F'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F', 'C'))
print('Exercise 4: Convert -200°C to Kelvin:', convert_temperature(-200, 'C', 'K'))
print('Exercise 4: Convert 100K to Celsius:', convert_temperature(100, 'K', 'C'))
print('Exercise 4: Convert -320°F to Kelvin', convert_temperature(-350, 'F', 'K'))
print('Exercise 4: Convert 300K to Fahrenheit', convert_temperature(300, 'K', 'F'))

# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.

def sum_to (integer):
    try:
        integer = int(integer)
        if (integer < 1):
            nums = list(range(1, integer-1, -1))
        elif (integer > 1):
            nums = list(range(integer+1))
        else:
            return 1
        
        sum = 0
        for num in nums:
            sum += num
        return sum

    except ValueError:
        print("ValueError: Temperature must be given as an integer value.")
        return None

print('Exercise 5:', sum_to(6)) 
print('Exercise 5:', sum_to(10))
print('Exercise 5:', sum_to(-4)) # expect -9 because inclusive of positive one
print('Exercise 5:', sum_to(1))
print('Exercise 5:', sum_to(0)) # expect 1 because inclusive of one

# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.
def largest(int1, int2, int3):
    try:
        if any(isinstance(ints, float) for ints in [int1, int2, int3]):
            print("Floating value rounded down to closest interger and converted to integer class.")
        int1 = int(int1)
        int2 = int(int2)
        int3 = int(int3)

        return max(int1, int2, int3)
    except ValueError:
        print("ValueError: Values must be given as integer values.")
        return None


print('Exercise 6:', largest(1, 2, 3))
print('Exercise 6:', largest(10, 4, 2))

# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.

def calculate_tip(bill_amount, tip_percentage):
    try:

        bill_amount = float(bill_amount)
        tip_percentage = float(tip_percentage)/100

        if bill_amount < 0:
            return print("Invalid Input: Must enter positive numeric inputs.")
        elif bill_amount == 0:
            print("Programmer's Note: If you are getting a free service, pick a non-zero amount to tip.")
        elif tip_percentage < 0:
            return print("Invalid Input: Tip cannot be a negative percentage.")
        elif tip_percentage < 0.15:
            print("Programmer's Note: If you cannot pay a reasonable tip, consider not using the service.")

        tip_amount = round(bill_amount*tip_percentage, 2)

        return f'${int(tip_amount)}' if tip_amount.is_integer() else f'${tip_amount}'
    except ValueError:
        print("ValueError: Values must be given as integer values.")
        return None


print('Exercise 7:', calculate_tip(50, 20))

# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.

def product (*args):
    try:
        if 0 in args:
            return 0

        product = 1

        for arg in args:
            arg = float(arg)
            product *= arg

        return product    
    except ValueError:
        print("ValueError: Values must be given as numeric values.")
        return None 
        

print('Exercise 8:', product(2, 5, 5))
print('Exercise 8:', product(-1, 4))

# Exercise 9: Basic Calculator
#
# Create a function named `basic_calculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basic_calculator(10, 5, 'subtract') should return 5.
# basic_calculator(10, 5, 'add') should return 15.
# basic_calculator(10, 5, 'multiply') should return 50.
# basic_calculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.

OPERATIONS = ["Add", "Subtract", "Multiply", "Divide"]

def basic_calculator (num1, num2, operator):
    try:
        if operator.capitalize() not in OPERATIONS:
            return print("Invalid Input: Operation must be 'Add', 'Subtract', 'Multiply', or 'Divide'")
        else:
            operator = operator.capitalize()

        num1 = float(num1)
        num2 = float(num2)

        if operator == "Add":
            return num1 + num2
        elif operator == "Subtract":
            return num1 - num2
        elif operator == "Multiply":
            return num1 * num2
        else:
            if (num2 == 0):
                print("Does Not Exist: Cannot divide by 0.")
                return None
            return num1 / num2
    except ValueError:        
        print("ValueError: Values must be given as numeric values.")
        return None 
print('Exercise 9 Result:', basic_calculator(10, 5, "add"))
print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
print('Exercise 9 Result:', basic_calculator(10, 5, "multiply"))
print('Exercise 9 Result:', basic_calculator(10, 5, "divide"))


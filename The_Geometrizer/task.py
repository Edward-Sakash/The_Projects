import math


def calc_circumference(radius):
    # Calculate the circumference based on the radius
    circumference = 2 * math.pi * radius
    print(f"The circumference is {circumference}.")


def calc_area(radius):
    # Calculate the area based on the radius
    area = math.pi * radius**2
    print(f"The area is {area}.")


# Calling the functions with different values

# Calculate the circumference for a circle with radius 5
calc_circumference(5)

# Calculate the circumference for a circle with radius 7.5
calc_circumference(7.5)

# Calculate the circumference for a circle with radius 10
calc_circumference(10)

# Calculate the area for a circle with radius 5
calc_area(5)

# Calculate the area for a circle with radius 7.5
calc_area(7.5)

# Calculate the area for a circle with radius 10
calc_area(10)

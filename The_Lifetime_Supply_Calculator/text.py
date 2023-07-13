def calculate_supply(age, amount_per_day):
    max_age = 120  # Maximum age assumed as 120 years
    days_remaining = (max_age - age) * 365  # Calculating the remaining days
    supply_needed = round(
        amount_per_day * days_remaining
    )  # Rounding to nearest whole number
    print(
        f"""You will need {supply_needed}
        to last you until the ripe old age of {max_age}."""
    )


# Calling the function with different values
calculate_supply(30, 2.0)  # Age 30, consuming 2.0 units per day
calculate_supply(45, 1.5)  # Age 45, consuming 1.5 units per day
calculate_supply(50, 3.25)  # Age 50, consuming 3.25 units per day

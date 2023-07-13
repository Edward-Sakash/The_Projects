def calculate_dog_age(puppy_age, conversion_rate=7):
    dog_age = puppy_age * conversion_rate
    print(f"Your doggie is {dog_age} years old in dog years!")


# Calling the function with different values
calculate_dog_age(2)  # Using the default conversion rate of 7
calculate_dog_age(4, 5)  # Using a custom conversion rate of 5
calculate_dog_age(3, 10)  # Using a custom conversion rate of 10

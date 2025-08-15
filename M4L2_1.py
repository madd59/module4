"""
M4L2_1.py

This Python script introduces **basic object-oriented programming (OOP)** concepts by modeling real-world objects—restaurants and users—using Python classes.

What this file demonstrates:
----------------------------
1. **Restaurant Class**:
   - Represents a restaurant with two main attributes: `restaurant_name` and `cuisine_type`.
   - Includes methods:
       - `describe_restaurant()`: Displays the restaurant's name and cuisine type.
       - `open_restaurant()`: Announces that the restaurant is open.
   - Shows:
       - How to create an instance (object) of the class.
       - How to access attributes directly.
       - How to call methods.
       - How to create multiple restaurant instances and describe them.

2. **User Class**:
   - Represents a user with personal details: first name, last name, age, email, and location.
   - Includes methods:
       - `describe_user()`: Displays the full profile of the user.
       - `greet_user()`: Prints a personalized greeting.
   - Demonstrates:
       - Creating an object from the class.
       - Using methods to interact with that object.

Goal:
-----
This file helps beginners understand:
- How to **define classes**.
- How to **create objects (instances)** from those classes.
- How to **access attributes and call methods** to perform actions.

Use Case:
---------
If you want to create digital models of real-world entities and give them functionality, classes and objects are the foundation in Python.

"""

# Define the Restaurant class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create one instance
restaurant = Restaurant("La Fiesta", "Mexican")

# Print attributes individually
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n--- Creating multiple restaurants ---")

# Create three different instances
restaurant1 = Restaurant("Pizza", "Italian")
restaurant2 = Restaurant("Sakura", "Japanese")
restaurant3 = Restaurant("Burger Blast", "American")

# Call describe_restaurant for each
restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()

print("\n--- User Class Example ---")

# Define the User class
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

# Create a user instance
user1 = User("Hector", "Delatorre", 38, "hector@example.com", "Brownwood, TX")

# Call the methods
user1.describe_user()
user1.greet_user()
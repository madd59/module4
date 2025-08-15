"""
M4L2_2.py

This Python script expands on previous class examples by introducing practical features 
for tracking and managing data in a restaurant setting and user profiles.

Key Highlights:
----------------
1. Restaurant Class with Customer Tracking:
   - Adds an attribute 'number_served' to monitor the number of customers served.
   - Demonstrates three ways to modify this value:
       a) Direct attribute assignment.
       b) Using a method to set a new value safely.
       c) Using another method to increment the value by a positive number.
   - Includes error handling to prevent invalid (negative) values.

2. User Class with Login Attempts:
   - Adds an attribute 'login_attempts' to track failed or successful login attempts.
   - Provides methods to:
       a) Increment the number of attempts (simulate repeated logins).
       b) Reset the attempts back to zero (simulate successful login or reset).
   - Shows how these methods work with practical examples.

Purpose:
--------
This file demonstrates how to manage dynamic attributes using methods, 
ensuring data integrity and providing reusable functionality for real-world applications.
"""

# ---------------------------
# Restaurant Class Definition
# ---------------------------
# This class represents a restaurant. It includes:
# - Basic details (name and cuisine type).
# - A system to track the number of customers served.
# - Methods to safely update and increase that count.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value to start from zero

    def describe_restaurant(self):
        # Displays the name and cuisine type of the restaurant
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        # Simulates opening the restaurant
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        # Safely sets the number of customers served
        # Prevents assigning a negative number
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, number):
        # Increases the count of customers served by a given positive number
        if number > 0:
            self.number_served += number
        else:
            print("Increment must be positive.")


# Example usage of Restaurant class
restaurant = Restaurant("Spicy Corner", "Indian")

# Demonstrate default and updated number_served values
print(f"Customers served: {restaurant.number_served}")
restaurant.number_served = 25  # Direct change
print(f"Customers served after direct change: {restaurant.number_served}")
restaurant.set_number_served(50)  # Safe method update
print(f"Customers served after using set_number_served(): {restaurant.number_served}")
restaurant.increment_number_served(30)  # Increment method
print(f"Customers served after using increment_number_served(): {restaurant.number_served}")

print("\n--- User Class with Login Attempts ---")

# ------------------------
# User Class Definition
# ------------------------
# This class models a user profile with:
# - Personal details (name, age, email, location).
# - A feature to track login attempts.
# - Methods to increase attempts and reset them.

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # Start with zero attempts

    def describe_user(self):
        # Displays full details of the user profile
        print(f"User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        # Prints a friendly greeting to the user
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

    def increment_login_attempts(self):
        # Adds 1 to the login attempt count
        self.login_attempts += 1

    def reset_login_attempts(self):
        # Resets the login attempts to zero
        self.login_attempts = 0


# Example usage of User class
user = User("Hector", "Delatorre", 38, "hector@example.com", "Brownwood, TX")

# Simulate multiple login attempts and then reset them
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts after increments: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")

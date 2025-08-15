"""
M4L2_2.py

This Python file demonstrates object-oriented programming by enhancing two core classes: Restaurant and User.

Key Features:
-------------
1. **Restaurant Class Enhancements**:
   - Adds an attribute `number_served` to track the number of customers served.
   - Includes methods to:
     * Set `number_served` safely (prevent negative values).
     * Increment `number_served` by a positive number.
   - Example: Shows a specialized subclass `IceCreamStand` that inherits from `Restaurant` and introduces an extra feature: flavors list.

2. **User Class Enhancements**:
   - Adds an attribute `login_attempts` to track user login attempts.
   - Includes methods to:
     * Increment the login attempts.
     * Reset the login attempts back to zero.
   - Demonstrates encapsulation and safe attribute modification.

3. **Admin Class and Privileges**:
   - Creates an `Admin` class that inherits from `User` and includes a `Privileges` class to manage admin-specific permissions.
   - Demonstrates how composition works by assigning a `Privileges` object inside the `Admin` class.

Purpose:
--------
This file helps beginners understand:
- How to design classes with attributes that change over time.
- How to use methods for updating those attributes safely.
- How inheritance and composition work in Python.
"""

# ------------------------------------
# Restaurant Class
# ------------------------------------
# Represents a generic restaurant with name, cuisine type, and customer tracking.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Tracks how many customers have been served

    # Prints basic restaurant details
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    # Displays that the restaurant is open
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    # Safely sets the number of customers served (cannot be negative)
    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number

    # Increments the number served by a positive value
    def increment_number_served(self, number):
        if number > 0:
            self.number_served += number


# ------------------------------------
# IceCreamStand Class (Subclass of Restaurant)
# ------------------------------------
# Represents a specialized restaurant (ice cream stand) with a predefined list of flavors.
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road", "Cookies and Cream"]

    # Displays all available ice cream flavors
    def display_flavors(self):
        print(f"{self.restaurant_name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Example usage of IceCreamStand
ice_cream_stand = IceCreamStand("Cool Cones")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()


print("\n--- User and Admin Classes ---")

# ------------------------------------
# User Class
# ------------------------------------
# Represents a system user with personal details and login tracking.
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # Tracks the number of login attempts

    # Displays user details
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    # Greets the user
    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    # Increments login attempts by one
    def increment_login_attempts(self):
        self.login_attempts += 1

    # Resets login attempts to zero
    def reset_login_attempts(self):
        self.login_attempts = 0


# ------------------------------------
# Privileges Class
# ------------------------------------
# Represents a list of privileges for an admin user.
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "can add post",
                "can delete post",
                "can ban user",
                "can reset passwords"
            ]
        self.privileges = privileges

    # Displays all privileges for the admin
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# ------------------------------------
# Admin Class (Subclass of User)
# ------------------------------------
# Represents an admin user with additional privileges.
class Admin(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()  # Composition: Admin has a Privileges object


# Example usage of Admin
admin_user = Admin("Hector", "Delatorre", 38, "hector@example.com", "Brownwood, TX")
admin_user.describe_user()
admin_user.privileges.show_privileges()
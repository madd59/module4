"""
M4L3_2.py

This Python file demonstrates how to randomly select items from a list to simulate a simple lottery ticket drawing.

- The code creates a list containing 10 numbers and 5 letters.
- It randomly selects 4 unique items from the list to form a winning ticket.
- The winning ticket is printed, and any ticket matching these items wins a prize.

This example helps beginners understand how to use lists and random sampling in Python.
"""

import random

# Create a list with 10 numbers and 5 letters
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'H', 'C', 'P', 'R']

# Randomly select 4 unique items from the list
winning_ticket = random.sample(items, 4)

# Print the winning ticket message
print("Any ticket matching these 4 numbers or letters wins a prize:")
print(winning_ticket)

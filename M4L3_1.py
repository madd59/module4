"""
M4L3_1.py

This Python file demonstrates how to create a simple class that simulates rolling a die.

- The Die class represents a die with a customizable number of sides (default is 6).
- The roll_die method prints a random number between 1 and the number of sides, simulating a die roll.
- The code creates a 6-sided die and rolls it 10 times, printing the result of each roll.

This example helps beginners understand how to use classes and random number generation in Python.
"""
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))

# Create a 6-sided die
my_die = Die()

# Roll the die 10 times
for _ in range(10):
    my_die.roll_die()

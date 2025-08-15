"""
Assessment 4: Visualizing Cubic Numbers with Matplotlib

This Python script demonstrates how to use **data visualization** to understand mathematical patterns.  
It uses the **matplotlib** library to plot cubic numbers (x³) as scatter plots.

1. **Plotting the first 5 cubic numbers**:
   - Creates a simple scatter plot for numbers 1 through 5.
   - Each point represents (x, x³).
   - Uses color mapping to represent the cubic value.
   - Adds a color bar for better visualization.

2. **Plotting the first 5000 cubic numbers**:
   - Generates a larger scatter plot for numbers 1 through 5000.
   - Demonstrates:
       - Handling large datasets in a plot.
       - Using a different color map (`plasma`) for variety.
       - Adjusting marker size for readability (smaller points for large sets).

This file helps beginners learn:
- How to calculate cubic numbers in Python.
- How to create scatter plots with color mapping using Matplotlib.
- How to manage small and large datasets visually.

"""

import matplotlib.pyplot as plt

# First 5 cubic numbers
x_small = list(range(1, 6))
y_small = [x**3 for x in x_small]

plt.figure(figsize=(6, 4))
plt.scatter(x_small, y_small, c=y_small, cmap='viridis', s=100)
plt.title("First 5 Cubic Numbers")
plt.xlabel("Number")
plt.ylabel("Cube")
plt.colorbar(label='Cubic Value')
plt.grid(True)
plt.tight_layout()
plt.show()

# First 5000 cubic numbers
x_large = list(range(1, 5001))
y_large = [x**3 for x in x_large]

plt.figure(figsize=(10, 6))
plt.scatter(x_large, y_large, c=y_large, cmap='plasma', s=1)
plt.title("First 5000 Cubic Numbers")
plt.xlabel("Number")
plt.ylabel("Cube")
plt.colorbar(label='Cubic Value')
plt.grid(True)
plt.tight_layout()
plt.show()

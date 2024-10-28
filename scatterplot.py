import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.random.rand(100)
y = np.random.rand(100)

# Create the scatter plot
plt.scatter(x, y)
plt.title("Random Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot
plt.show()

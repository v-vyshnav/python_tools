import numpy as np
import matplotlib.pyplot as plt

# Generate data for the sine wave
x = np.linspace(0, 2 * np.pi, 100)  # X values from 0 to 2π
y = np.sin(x)  # Sine of the X values

# Create the plot
plt.plot(x, y, label='Sine Wave', color='blue', linestyle='-', linewidth=2)
plt.title("Sine Wave with Customization")
plt.xlabel("X-axis (radians)")
plt.ylabel("Y-axis (sin(x))")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

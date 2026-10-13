# Self Practice 1.2: Mean and standard deviation with NumPy
# Install once if needed: python -m pip install numpy
import numpy as np

daily_max_temperatures = [31.2, 31.5, 30.9, 31.3, 31.7, 31.9, 32.2]
print(f"Mean temperature (numpy): {np.mean(daily_max_temperatures):.2f}")
print(f"Standard deviation (numpy): {np.std(daily_max_temperatures):.2f}")

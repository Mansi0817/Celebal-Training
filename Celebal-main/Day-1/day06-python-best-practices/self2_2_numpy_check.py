# Self Practice 2.2: Check custom statistics results with NumPy
# Install once if needed: python -m pip install numpy
import numpy as np
import my_stats

temperatures = [random_value for random_value in [31.5, 34.2, 38.1, 40.7, 36.9]]
print("Values:", temperatures)
print("Custom Module Results:")
print(f"Mean: {my_stats.mean(temperatures)}")
print(f"Variance: {my_stats.variance(temperatures)}")
print(f"Standard Deviation: {my_stats.standard_deviation(temperatures)}")
print("Numpy Module Results:")
print(f"Mean: {np.mean(temperatures)}")
print(f"Variance: {np.var(temperatures)}")
print(f"Standard Deviation: {np.std(temperatures)}")

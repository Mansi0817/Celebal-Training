# Self Practice 2.1: Custom MyStats module
import random
import my_stats

temperatures = [random.uniform(30.0, 45.0) for _ in range(5)]
print(f"Generated temperatures: {[round(value, 2) for value in temperatures]}")
print("Custom Module Results:")
print(f"Mean: {my_stats.mean(temperatures)}")
print(f"Variance: {my_stats.variance(temperatures)}")
print(f"Standard Deviation: {my_stats.standard_deviation(temperatures)}")

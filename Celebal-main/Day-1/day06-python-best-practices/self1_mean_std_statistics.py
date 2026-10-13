# Self Practice 1.1: Mean and standard deviation with statistics
import statistics

daily_max_temperatures = [31.2, 31.5, 30.9, 31.3, 31.7, 31.9, 32.2]
print(f"Mean temperature: {statistics.mean(daily_max_temperatures):.2f}")
print(f"Standard deviation: {statistics.stdev(daily_max_temperatures):.2f}")

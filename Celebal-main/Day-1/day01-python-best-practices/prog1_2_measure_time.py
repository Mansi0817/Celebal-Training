# Program 1.2: Measure execution time

import time

start_time = time.perf_counter()

first_number = 10
second_number = 20
total = first_number + second_number

end_time = time.perf_counter()

print(f"Sum: {total}")
print(f"Execution time: {end_time - start_time:.8f} seconds")
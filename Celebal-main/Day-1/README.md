# Day 1: Python Best Practices

This directory contains four lesson folders with 60 Python programs and practice exercises. The work moves from basic Python syntax to input validation, reusable functions, recursion, date/time handling, and custom and third-party modules.

## How to Approach the Lessons

1. Start with `day01-python-best-practices` and follow the numbered programs in order. They introduce output, naming, functions, types, input, and errors.
2. Continue through `day02-python-best-practices` to practice input/output formatting, calculations, validation, and small report-style applications.
3. Use `day05-python-best-practices` to work with functions, lists, return values, exceptions, and recursion.
4. Finish with `day06-python-best-practices`, where programs use Python modules, dates and times, random values, and statistics.
5. Run each script, try different valid and invalid inputs, and compare the output with the calculations in the code. The `self` files are useful for applying the same ideas with slightly different requirements.

Run a script from the workspace root with Python, for example:

```powershell
python Day-1/day01-python-best-practices/hello_world.py
```

Python 3.9 or newer is recommended. Most programs use only the Python standard library. The two NumPy exercises in Day 4 need NumPy installed (`python -m pip install numpy`).

## Day 01: Python Foundations

Folder: [`day01-python-best-practices`](day01-python-best-practices/)

These programs demonstrate core habits: clear output, descriptive names, small reusable functions, type conversion, and graceful handling of invalid input.

| Program | What it covers |
| --- | --- |
| [`hello_world.py`](day01-python-best-practices/hello_world.py) | The smallest Python program: execute a statement and print text. |
| [`prog1_add_numbers.py`](day01-python-best-practices/prog1_add_numbers.py) | Add two numbers and display the result. |
| [`prog1_1_print_format.py`](day01-python-best-practices/prog1_1_print_format.py) | Add two numbers and use an f-string to include the inputs and result in a sentence. |
| [`prog1_2_measure_time.py`](day01-python-best-practices/prog1_2_measure_time.py) | Measure a calculation's elapsed time with `time.perf_counter()`. |
| [`prog2_descriptive_names.py`](day01-python-best-practices/prog2_descriptive_names.py) | Use descriptive variable names to make student and number calculations easier to understand. |
| [`prog3_modularization.py`](day01-python-best-practices/prog3_modularization.py) | Define an addition function and reuse it with different values. |
| [`prog4_1_function_usage.py`](day01-python-best-practices/prog4_1_function_usage.py) | Separate calculating a price total from displaying it, giving each function one responsibility. |
| [`prog4_2_type_annotations.py`](day01-python-best-practices/prog4_2_type_annotations.py) | Add parameter and return type annotations to a function that calculates an average. |
| [`prog5_1_hard_coding.py`](day01-python-best-practices/prog5_1_hard_coding.py) | Show fixed, hard-coded score and bonus values and calculate a final score. |
| [`prog5_2_remove_hard_coding.py`](day01-python-best-practices/prog5_2_remove_hard_coding.py) | Replace fixed values with integer input from the user. |
| [`prog5_3_type_conversion.py`](day01-python-best-practices/prog5_3_type_conversion.py) | Convert user input to floating-point numbers and format the final score. |
| [`prog6_1_handle_user_error.py`](day01-python-best-practices/prog6_1_handle_user_error.py) | Catch invalid numeric input while reading values to add. |
| [`prog6_2_exact_error.py`](day01-python-best-practices/prog6_2_exact_error.py) | Handle invalid numbers and division by zero as separate errors. |
| [`self_practice_hello_user.py`](day01-python-best-practices/self_practice_hello_user.py) | Read and trim a name, greet the user, and handle an empty name. |

## Day 02: Input, Formatting, and Calculations

Folder: [`day02-python-best-practices`](day02-python-best-practices/)

The exercises expand basic input and output into formatted calculations and complete console reports. They practice string formatting, conditionals, loops, numeric conversion, and input validation.

| Program | What it covers |
| --- | --- |
| [`prog1_oops_banner.py`](day02-python-best-practices/prog1_oops_banner.py) | Print a multi-line OOPS banner using spaces and asterisks. |
| [`prog2_places_to_visit.py`](day02-python-best-practices/prog2_places_to_visit.py) | Collect a name, three destinations, and a year, then compose a formatted sentence with `print()` separators. |
| [`prog3_1_circle_calculations.py`](day02-python-best-practices/prog3_1_circle_calculations.py) | Convert a radius from inches to centimeters, then calculate circumference and area. |
| [`prog3_2_circle_format_specifier.py`](day02-python-best-practices/prog3_2_circle_format_specifier.py) | Repeat the circle calculations while controlling the precision and presentation of the output. |
| [`prog4_find_generation.py`](day02-python-best-practices/prog4_find_generation.py) | Use year ranges and Boolean expressions to identify a birth-year generation. |
| [`prog5_time_conversion.py`](day02-python-best-practices/prog5_time_conversion.py) | Convert a non-negative number of seconds into hours, minutes, and seconds. |
| [`prog6_fruit_bill.py`](day02-python-best-practices/prog6_fruit_bill.py) | Collect apple and orange prices and quantities, then print a formatted bill and totals. |
| [`prog7_school_report.py`](day02-python-best-practices/prog7_school_report.py) | Collect marks for three students across three subjects, validate each mark, print individual reports, and calculate class averages and percentages. |
| [`self1_print_three_names.py`](day02-python-best-practices/self1_print_three_names.py) | Read three names and print them in reverse order. |
| [`self2_favorite_places.py`](day02-python-best-practices/self2_favorite_places.py) | Collect favorite places and display the list both inline and one place at a time. |
| [`self3_name_banner.py`](day02-python-best-practices/self3_name_banner.py) | Build a text-art banner from rows of characters and customize it for a name. |
| [`self4_formatted_string.py`](day02-python-best-practices/self4_formatted_string.py) | Use an f-string to create a personalized sentence from a friend's name and place of stay. |
| [`self5_square_root.py`](day02-python-best-practices/self5_square_root.py) | Calculate and format a square root while rejecting negative input. |
| [`self6_temperature_conversion.py`](day02-python-best-practices/self6_temperature_conversion.py) | Convert Celsius to Fahrenheit and display both values to one decimal place. |
| [`self7_rectangle.py`](day02-python-best-practices/self7_rectangle.py) | Calculate a rectangle's perimeter and area from centimeter dimensions, converting the results to inches and square inches. |
| [`self8_retail_invoice.py`](day02-python-best-practices/self8_retail_invoice.py) | Create a formatted retail invoice for two product categories, including quantities, prices, and rounded totals. |

## Day 05: Functions, Collections, and Recursion

Folder: [`day05-python-best-practices`](day05-python-best-practices/)

These programs focus on writing functions that validate input, calculate values, and return results. The later exercises apply recursion and combine functions in small apps.

| Program | What it covers |
| --- | --- |
| [`prog1_greet_function.py`](day05-python-best-practices/prog1_greet_function.py) | Define a greeting function with a default greeting argument. |
| [`prog1_1_greet_user_input.py`](day05-python-best-practices/prog1_1_greet_user_input.py) | Read a friend's name, check that it is present, and pass it to a greeting function. |
| [`prog1_2_validate_name.py`](day05-python-best-practices/prog1_2_validate_name.py) | Validate that a name is non-empty and alphabetic before greeting the user. |
| [`prog2_car_loan_payment.py`](day05-python-best-practices/prog2_car_loan_payment.py) | Calculate a monthly car-loan payment from the principal, duration, and annual interest rate. |
| [`prog3_compute_average.py`](day05-python-best-practices/prog3_compute_average.py) | Calculate the average of a list of numbers using a reusable function. |
| [`prog4_return_min_max.py`](day05-python-best-practices/prog4_return_min_max.py) | Return the minimum and maximum values from a list as a pair. |
| [`prog5_recursive_factorial.py`](day05-python-best-practices/prog5_recursive_factorial.py) | Calculate a non-negative integer's factorial recursively, using a base case to stop recursion. |
| [`self1_calculator_app.py`](day05-python-best-practices/self1_calculator_app.py) | Build a basic calculator for addition, subtraction, multiplication, and division, with error handling. |
| [`self2_multiply_list.py`](day05-python-best-practices/self2_multiply_list.py) | Multiply every value in a list using an accumulator. |
| [`self3_check_prime.py`](day05-python-best-practices/self3_check_prime.py) | Write a prime-number predicate and use it to list primes between 1 and 100. |
| [`self4_power_of_number.py`](day05-python-best-practices/self4_power_of_number.py) | Raise a base number to an integer exponent after reading and converting input. |
| [`self5_recursive_countdown.py`](day05-python-best-practices/self5_recursive_countdown.py) | Print a countdown recursively, validating the starting value. |
| [`self6_menu_school_report.py`](day05-python-best-practices/self6_menu_school_report.py) | Collect a student's marks, offer a menu of report calculations, and map percentages to grades. |

## Day 06: Modules, Dates, Randomness, and Statistics

Folder: [`day06-python-best-practices`](day06-python-best-practices/)

The final set introduces standard-library modules and custom modules. Two files, `my_calculator.py` and `my_stats.py`, are modules used by other scripts in this folder rather than interactive programs on their own.

| Program | What it covers |
| --- | --- |
| [`prog1_1_coin_flip.py`](day06-python-best-practices/prog1_1_coin_flip.py) | Flip a coin a requested number of times using Python's `random` module. |
| [`prog1_2_coin_flip_multiple_functions.py`](day06-python-best-practices/prog1_2_coin_flip_multiple_functions.py) | Split coin flipping into functions and count how many flips land on heads. |
| [`prog2_datetime_module.py`](day06-python-best-practices/prog2_datetime_module.py) | Get the local current date/time and format its components with `datetime` and `strftime()`. |
| [`prog2_1_datetime_ist.py`](day06-python-best-practices/prog2_1_datetime_ist.py) | Get and format the current time in the Asia/Kolkata time zone. |
| [`prog3_string_to_datetime.py`](day06-python-best-practices/prog3_string_to_datetime.py) | Parse a date string into a `datetime` object with a specified format. |
| [`prog3_1_datetime_to_string.py`](day06-python-best-practices/prog3_1_datetime_to_string.py) | Parse a date string, then format the resulting `datetime` back into a string. |
| [`my_calculator.py`](day06-python-best-practices/my_calculator.py) | Provide reusable `add`, `subtract`, `multiply`, and `divide` functions for import by another script. |
| [`prog4_calculator_module_demo.py`](day06-python-best-practices/prog4_calculator_module_demo.py) | Import `my_calculator` and use its functions on two numbers. |
| [`self1_mean_std_statistics.py`](day06-python-best-practices/self1_mean_std_statistics.py) | Calculate the mean and sample standard deviation of temperature data with Python's `statistics` module. |
| [`self1_2_mean_std_numpy.py`](day06-python-best-practices/self1_2_mean_std_numpy.py) | Calculate the mean and standard deviation of temperature data with NumPy. |
| [`my_stats.py`](day06-python-best-practices/my_stats.py) | Implement mean, population variance, and population standard deviation in a custom module. |
| [`self2_1_custom_stats_demo.py`](day06-python-best-practices/self2_1_custom_stats_demo.py) | Generate sample temperatures and use the custom `my_stats` functions to summarize them. |
| [`self2_2_numpy_check.py`](day06-python-best-practices/self2_2_numpy_check.py) | Compare results from `my_stats` with NumPy's mean, variance, and standard deviation on the same values. |
| [`self3_fellowship_completion_date.py`](day06-python-best-practices/self3_fellowship_completion_date.py) | Calculate a fellowship completion date by adding a duration to its start date with `timedelta`. |
| [`self4_number_guessing_game.py`](day06-python-best-practices/self4_number_guessing_game.py) | Play a number guessing game with a random number, a limited number of attempts, and higher/lower hints. |
| [`self5_countdown_timer.py`](day06-python-best-practices/self5_countdown_timer.py) | Run a seconds-based countdown timer using `time.sleep()` and a live remaining-time display. |
| [`self6_calendar_module.py`](day06-python-best-practices/self6_calendar_module.py) | Print a selected month's calendar using Python's `calendar` module. |

**Statistics note:** `statistics.stdev()` calculates a sample standard deviation, while NumPy's `std()` and the custom `my_stats` module use the population definition by default. Their results can therefore differ even when they use the same values.
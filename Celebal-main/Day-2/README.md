# Day 2: Python Best Practices

This directory contains two lesson folders with nine programs and practice exercises. The topics build on the earlier Python foundations with randomized data, timing and comparing approaches, invoice generation, string analysis, and regular expressions.

## How to Approach the Lessons

1. Start with `day07-python-best-practices` to explore random shuffling, performance measurements, and a generated retail invoice.
2. Continue to `day08-python-best-practices` to classify characters, search strings with regular expressions, and process text.
3. Run each script and experiment with different inputs. For the timing exercise, rerun it and compare the results at each list size; timings vary by computer and run.

Run a script from the repository root with Python, for example:

```powershell
python Day-2/day07-python-best-practices/self3_shuffle_card.py
```

Python 3.9 or newer is recommended. All programs in this directory use the Python standard library; no additional packages are required.

## Day 07: Randomness, Performance, and Invoicing

Folder: [`day07-python-best-practices`](day07-python-best-practices/)

These exercises use `random` to create or shuffle data, `time.perf_counter()` to measure elapsed time, and formatted console output to produce an invoice.

| Program | What it covers |
| --- | --- |
| [`self3_shuffle_card.py`](day07-python-best-practices/self3_shuffle_card.py) | Build a 52-card deck from four suits and thirteen ranks, print the original deck, shuffle it, and compare the Kings' positions before and after. |
| [`self4_execution_time_calculation.py`](day07-python-best-practices/self4_execution_time_calculation.py) | Generate random lists of increasing sizes and compare removing prime numbers by testing each value with removing them using a precomputed set. It checks that both results match and reports timings. |
| [`self5_retail_invoicing_app.py`](day07-python-best-practices/self5_retail_invoicing_app.py) | Generate an invoice for three randomly selected products with random quantities, category-based GST, and a formatted final billing total. |

## Day 08: String Processing and Regular Expressions

Folder: [`day08-python-best-practices`](day08-python-best-practices/)

The programs use string methods and Python's `re` module to inspect and transform user-provided text. The character-counting examples show two ways to approach the same task: explicit loops and list comprehensions.

| Program | What it covers |
| --- | --- |
| [`prog3_1_count_letters_digits_special.py`](day08-python-best-practices/prog3_1_count_letters_digits_special.py) | Count letters, digits, and non-alphanumeric characters in an input string using an explicit loop. |
| [`prog3_2_count_letters_digits_special.py`](day08-python-best-practices/prog3_2_count_letters_digits_special.py) | Perform the same character counts using list comprehensions. |
| [`prog4_regex_search_digits.py`](day08-python-best-practices/prog4_regex_search_digits.py) | Use a regular expression to find and display each digit in an input string. |
| [`prog5_email_validation.py`](day08-python-best-practices/prog5_email_validation.py) | Check an email address against a basic regular-expression format. |
| [`self5_password_check.py`](day08-python-best-practices/self5_password_check.py) | Validate a password against rules for minimum length, starting character, uppercase and lowercase letters, a digit, and an allowed special character. |
| [`self6_news_data_processing.py`](day08-python-best-practices/self6_news_data_processing.py) | Search a news paragraph for words and digits, count words and a selected word, remove articles, then remove vowels. |

The email and password exercises demonstrate basic format checks for practice; they are not complete security or identity-validation systems.

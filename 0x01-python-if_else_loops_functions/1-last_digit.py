#!/usr/bin/python3
import random
number = random.randint(-10, 10)
last_digit = int(str(number)[-1])
if number < 0:
	last_digit = -last_digit
what_is_number = "is 0" if last_digit == 0 \
 else "greater than 5" if last_digit > 5 else "less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and is {what_is_number}")

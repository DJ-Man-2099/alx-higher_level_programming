#!/usr/bin/python3
import random
number = random.randint(-10, 10)
what_is_number = "zero" if number == 0 \
 else "positive" if number > 0 else "negative"
print(f"{number} is {what_is_number}")

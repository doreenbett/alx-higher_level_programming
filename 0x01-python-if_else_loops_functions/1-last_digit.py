#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
thedigit = abs(number) % 10
if number < 0:
    thedigit = -thedigit
print("Last digit of {} is {} and is ".format(number, thedigit), end="")
if thedigit > 5:
    print("greater than 5")
elif thedigit == 0:
    print("0")
else:
    print("less than 6 and not 0")

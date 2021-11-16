#!/usr/bin/python3
def fizzbuzz():
	for number in range(1, 101):
#For multiples of three and five, print Fizzbuzz instead of te number
		if number % 3 == 0 and number % 5 == 0:
			print("FizzBuzz ", end="")
#for multiples of three , print Fizz instead of te number
		elif number % 3 == 0:
			print("Fizz ", end="")
#For multiples of five, print Buzz instead of the number
		elif number % 5 == 0:
			print("Buzz ", end="")
		else:
			print("{} ".format(number), end="")

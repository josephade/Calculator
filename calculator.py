from art import logo
import os

def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

operation = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for sym in operation:
    print(sym)
  should_continue = True

  while should_continue:
    operation_sym = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    cal_func = operation[operation_sym]
    answer = cal_func(num1, num2)
    print("{} {} {} = {}".format(num1, operation_sym, num2, answer))

    if input("Type 'y' to continue calculating with {}, or type 'n' to start a new calculation: ".format(answer)) == 'y':
      num1 = answer
    else:
      should_continue = False
      os.system("clear")
      calculator()

calculator()
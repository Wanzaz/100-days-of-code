# Calculator

#Add
def add(n1, n2):
	return n1 + n2

#Subtract
def substract(n1, n2):
	return n1 - n2

#Multiply
def multiply(n1, n2):
	return n1 * n2

#Divide
def divide(n1, n2):
	return n1 / n2

operations = {
	"+" : add,
	"-" : substract,
	"*" : multiply,
	"/" : divide
}

def calculator():
	num1 = float(input("What's the first number?: "))
	for symbol in operations:
		print(symbol)

	should_continue = True

	while should_continue:
		operation_symbol = input("Pick an operation: ")
		num2 = float(input("What's the next number?: "))
		answer = operations[operation_symbol](num1, num2)

		print(f"{num1} {operation_symbol} {num2} = {answer}")

		question = input("Type 'y' to continue calculating with 16, or type 'n' to start a new calculation: ")
		if question == 'y':
			num1 = answer
		else:
			should_continue = False
			calculator()

calculator()


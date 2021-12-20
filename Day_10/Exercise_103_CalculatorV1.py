

#add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {}
operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide


num1 = int(input("What is the first number?: "))

for operation_symbol in operations:
    print (operation_symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What is the second number?: "))

result_1 = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {result_1}")

operation_symbol = input("Pick an operation from the line above: ")
num3 = int(input("What is the third number?: "))
result_2 = operations[operation_symbol](result_1, num3)
print(f"{result_1} {operation_symbol} {num3} = {result_2}")







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

continue_calculating = "y"

first_number = int(input("What is the first number?: "))

while continue_calculating == "y":
    for operation_symbol in operations:
        print (operation_symbol)

    operation_symbol = input("Pick an operation from the line above: ")
    next_number = int(input("What is the next number?: "))

    result = operations[operation_symbol](first_number, next_number)
    print(f"{first_number} {operation_symbol} {next_number} = {result}")
    continue_calculating = input(f"Continue calculating with {result}, or type 'n' to exit?").lower()
    if continue_calculating == "y":
        first_number = result
    if continue_calculating == "n":
        print("end")
        


import os
from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    continue_calculating = True
    print(logo)
    first_number = float(input("What's the first number?: "))
    first_run = True
    while continue_calculating:
        print("\t".join([operation for operation in operations]))
        if first_run == True:
            operation_symbol = input("Pick an operation: ")
            first_run = False
        else:
            operation_symbol = input("Pick another operation, or type 'n' to start a new calculation: ")
            if operation_symbol == "n":
                continue_calculating = False
                os.system("cls")
                calculator()

        second_number = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {answer}\n")
        first_number = answer


if __name__ == "__main__":
    calculator()       

def main():
    print("Welcome to My Simple Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    result = perform_operation(num1, num2, operation)
    print("Result:", result)


def perform_operation(num1, num2, operation):
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return divide(num1, num2)
    else:
        return "Invalid operation"


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"


if __name__ == "__main__":
    main()

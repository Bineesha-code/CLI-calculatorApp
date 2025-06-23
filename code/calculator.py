# Task-1
# Simple CLI Calculator
# Author: Bineesha K P
# Date: 23-06-2025

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Can't divide by zero!."
    return x / y

def show_menu():
    print("\n*** Simple CLI Calculator ***")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input!. Please enter a number: ")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-5): ")

        if choice == '5':
            print("Exiting...")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice!. Please select a valid option: ")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
            operator = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operator = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operator = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operator = '/'

        print(f"\nResult: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()

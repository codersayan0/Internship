
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y
def modulus(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x % y
def power(x, y):
    return x ** y
def main():
    while True:
        print("\n--- Simple Calculator made by Sayan ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")
        choice = input("Enter choice (1-7): ").strip()
        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid input. Please enter a valid choice.")
            continue
        try:
            num1 = float(input("Enter first number: ").strip())
            num2 = float(input("Enter second number: ").strip())
        except ValueError:
            print("Invalid number input. Please try again.")
            continue
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = modulus(num1, num2)
        elif choice == '6':
            result = power(num1, num2)
        print("Result:", round(result, 2) if isinstance(result, float) else result)
if __name__ == "__main__":
    main()

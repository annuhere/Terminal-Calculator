# Simple Calculator (Clean Version)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero ❌"
    return a / b


print("✨ Welcome to My Calculator ✨")

while True:
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice 😅 Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except:
        print("Invalid number input ❌")
        continue

    if choice == '1':
        result = add(num1, num2)

    elif choice == '2':
        result = subtract(num1, num2)

    elif choice == '3':
        result = multiply(num1, num2)

    elif choice == '4':
        result = divide(num1, num2)

    print("👉 Result:", result)

    again = input("\nDo you want to calculate again? (yes/no): ")
    if again.lower() != 'yes':
        print("👋 Thank you for using my calculator!")
        break